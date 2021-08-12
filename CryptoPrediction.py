import os
import datetime
import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

coin_name = 'BTC-USD'
file_path = f'raw_historic_data/{coin_name}/{coin_name}.csv'

BATCH_SIZE = 4096
INPUT_STEPS = 60
OUTPUT_STEPS = 1
SHIFT_STEPS =60
MAX_EPOCHS = 30

# for record history and plot
val_performance = {}
performance = {}
multi_val_performance = {}
multi_performance = {}

raw_data = pd.read_csv(file_path)


mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False