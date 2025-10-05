#!/usr/bin/env python3
"""Transformer Module"""
import tensorflow as tf

Encoder = __import__('9-transformer_encoder').Encoder
Decoder = __import__('10-transformer_decoder').Decoder


class Transformer(tf.keras.layers.Layer):
    """Transformer Network"""

    def __init__(self, N, dm, h, hidden, input_vocab, target_vocab,
                 max_seq_input, max_seq_target, drop_rate=0.1):
        """
        Initialize Transformer

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

        inputs: input tensor
        target: target tensor
        training: boolean for training mode
        encoder_mask: padding mask for encoder
        look_ahead_mask: look ahead mask for decoder
        decoder_mask: padding mask for decoder

        Returns: final output (batch, target_seq_len, target_vocab)
        """
        enc_output = self.encoder(inputs, training, encoder_mask)
        dec_output = self.decoder(target, enc_output, training,
                                  look_ahead_mask, decoder_mask)
        final_output = self.linear(dec_output)
        return final_output
