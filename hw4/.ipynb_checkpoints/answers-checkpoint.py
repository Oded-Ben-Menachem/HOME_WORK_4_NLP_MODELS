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

# ==============בוא 
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
        embed_dim = 128, 
        num_heads = 4,      # embed_dim חייב להתחלק במספר הראשים ללא שארית
        num_layers = 3,
        hidden_dim = 256,
        window_size = 64,   # חייב להיות מספר זוגי
        droupout = 0.1,     # שים לב ששגיאת הכתיב droupout מגיעה מהקוד המקורי, השארתי אותה
        lr = 1e-4,
    )

    # TODO: Tweak the hyperparameters to train the transformer encoder.
    # ====== YOUR CODE: ======
    # No extra code needed here, the dict is updated above.
    # ========================
    return hypers



part2_q1 = r"""
**Your answer:**
Similarly to the receptive field in Convolutional Neural Networks (CNNs), stacking layers with a sliding-window attention increases the effective context size linearly. In the first layer, a token attends only to $w$ neighboring tokens. However, in the second layer, that same token attends to its $w$ neighbors, which have already aggregated information from their own $w$ neighbors in the previous layer. This expands the effective context window to $2w$. After $L$ layers, the receptive field size becomes $L \times w$, allowing the deeper layers to capture a much broader, and potentially global, context of the input sequence.
"""

part2_q2 = r"""
**Your answer:**
There are two common variations to achieve a more global context while maintaining the linear $O(n \cdot w)$ complexity:

1. **Dilated Sliding Window:** Similar to dilated convolutions, we can introduce gaps in the attention window (e.g., attending to every $d$-th token instead of strictly consecutive ones). This increases the receptive field size exponentially across layers without increasing the computational cost per token.
2. **Global Attention Tokens:** We can designate a few specific tokens (such as the `[CLS]` token) to have 'global attention'. These global tokens attend to all other tokens in the sequence, and conversely, all other tokens attend to them. Since the number of global tokens $g$ is small and constant, the added complexity is $O(g \cdot n)$, keeping the overall complexity linear while propagating global information to all tokens.
"""


# ==============
