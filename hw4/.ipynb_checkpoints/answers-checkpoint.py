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
        batch_size=128,
        seq_len=64,
        h_dim=256,
        n_layers=2,
        dropout=0.2,
        learn_rate=0.001,
        lr_sched_factor=0.5,
        lr_sched_patience=2,
    )
    # TODO: Set the hyperparameters to train the model.
    # ====== YOUR CODE: ======
    
    
    # ========================
    return hypers


def part1_generation_params():
    start_seq = ""
    temperature = 0.0001
    # TODO: Tweak the parameters to generate a literary masterpiece.
    # ====== YOUR CODE: ======
    start_seq = "ACT I. SCENE I."
    temperature = 0.55
    # ========================
    return start_seq, temperature


part1_q1 = r"""
We do it form three main reasons.

1. Memory limitations. Runing on the entire corpus at once would cause to mamory error. 
2. Gradient size problams. If the tarin will be on all the corpus, the gradient go back in not good way.
3. Afficinsy computition. Split to batch gave the option the do parallel compotition.

"""

part1_q2 = r"""
This is possible because we do not reset the hidden state of the GRU between consecutive batches. Thanks to the SequenceBatchSampler, consecutive batches process continuous text, and the hidden state carries over the long-term context (after being detached). Therefore, while the gradient memory is limited to seq_len=64, the actual hidden state representation maintains memory for much longer sequences.


"""

part1_q3 = r"""
Because we want to maintain the sequential continuity of the text across batches. 

"""

part1_q4 = r"""
1. We lower it to make the model more focused. It boosts the chances of the most likely characters, making the text cleaner, more coherent, and with fewer mistakes.
2. When temperature is very high, the probability distribution becomes flat and uniform. Because of this, the choices become completely random, and the text breaks down into gibberish.
3. When temperature is very low, the model always picks the single highest probability character . This makes the model lose all creativity, and it easily gets stuck in infinite loops of repeating the same words.


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
