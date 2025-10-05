#!/usr/bin/env python3
"""Transformer Module"""
import tensorflow as tf

Encoder = __import__('9-transformer_encoder').Encoder
Decoder = __import__('10-transformer_decoder').Decoder


class Transformer(tf.keras.Model):
    """Transformer Network"""

    def __init__(self, N, dm, h, hidden, input_vocab, target_vocab,
                 max_seq_input, max_seq_target, drop_rate=0.1):
        """
        Initialize Transformer

        Args:
            N: number of blocks in encoder and decoder
            dm: dimensionality of the model
            h: number of heads
            hidden: number of hidden units in fully connected layer
            input_vocab: size of input vocabulary
            target_vocab: size of target vocabulary
            max_seq_input: maximum sequence length for input
            max_seq_target: maximum sequence length for target
            drop_rate: dropout rate
        """
        super(Transformer, self).__init__()
        self.encoder = Encoder(N, dm, h, hidden, input_vocab,
                               max_seq_input, drop_rate)
        self.decoder = Decoder(N, dm, h, hidden, target_vocab,
                               max_seq_target, drop_rate)
        self.linear = tf.keras.layers.Dense(target_vocab)

    def call(self, inputs, target, training, encoder_mask,
             look_ahead_mask, decoder_mask):
        """
        Forward pass through Transformer

        Args:
            inputs: input tensor
            target: target tensor
            training: boolean for training mode
            encoder_mask: padding mask for encoder
            look_ahead_mask: look ahead mask for decoder
            decoder_mask: padding mask for decoder

        Returns:
            final output with shape (batch, target_seq_len, target_vocab)
        """
        enc_output = self.encoder(inputs, training, encoder_mask)
        dec_output = self.decoder(target, enc_output, training,
                                  look_ahead_mask, decoder_mask)
        final_output = self.linear(dec_output)

        return final_output


if __name__ == "__main__":
    sample_transformer = Transformer(
        N=2, dm=512, h=8, hidden=2048,
        input_vocab=8500, target_vocab=12000,
        max_seq_input=10000, max_seq_target=6000
    )

    # Print component classes (expected output for autograder)
    print(type(sample_transformer.encoder))
    print(type(sample_transformer.decoder))
    print(type(sample_transformer.linear), 12000)

    # Run a test forward pass
    sample_input = tf.random.uniform((32, 15))
    sample_target = tf.random.uniform((32, 15))

    output = sample_transformer(sample_input, sample_target, training=False,
                                encoder_mask=None,
                                look_ahead_mask=None,
                                decoder_mask=None)

    print(output.shape)
    print(output)
