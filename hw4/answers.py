r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

import os

# ==============
# Dataset location
#
# Root directory containing the pre-prepared dataset files used by the
# notebooks (e.g. the `hw4_tests/` directory used to verify your
# implementation). Change this to point to wherever you placed the datasets
# on the course HPC.
DATASETS_DIR = os.path.expanduser("~/datasets")

# ==============
# Part 1 answers


def part1_rnn_hyperparams():
    hypers = dict(
        batch_size=0,
        seq_len=0,
        h_dim=0,
        n_layers=0,
        dropout=0,
        learn_rate=0.0,
        lr_sched_factor=0.0,
        lr_sched_patience=0,
    )
    # TODO: Set the hyperparameters to train the model.
    # ====== YOUR CODE: ======
    raise NotImplementedError()
    # ========================
    return hypers


def part1_generation_params():
    start_seq = ""
    temperature = 0.0001
    # TODO: Tweak the parameters to generate a literary masterpiece.
    # ====== YOUR CODE: ======
    raise NotImplementedError()
    # ========================
    return start_seq, temperature


part1_q1 = r"""
**Your answer:**


"""

part1_q2 = r"""
**Your answer:**


"""

part1_q3 = r"""
**Your answer:**


"""

part1_q4 = r"""
**Your answer:**


"""
# ==============


# ==============
# Part 2 answers

PART2_CUSTOM_DATA_URL = None


def part2_transformer_encoder_hyperparams():
    hypers = dict(
        embed_dim = 0, 
        num_heads = 0,
        num_layers = 0,
        hidden_dim = 0,
        window_size = 0,
        droupout = 0.0,
        lr=0.0,
    )

    # TODO: Tweak the hyperparameters to train the transformer encoder.
    # ====== YOUR CODE: ======
    raise NotImplementedError()
    # ========================
    return hypers




part2_q1 = r"""
**Your answer:**


"""

part2_q2 = r"""
**Your answer:**


"""


# ==============
