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

raw_data = pd.read_csv(file_path)
date_time = raw_data.pop('time')

day = 24*60*60
year = (365.2425)*day

raw_data['Day sin'] = np.sin(date_time * (2 * np.pi / day))
raw_data['Day cos'] = np.cos(date_time * (2 * np.pi / day))
raw_data['Year sin'] = np.sin(date_time * (2 * np.pi / year))
raw_data['Year cos'] = np.cos(date_time * (2 * np.pi / year))

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

plt.plot(np.array(raw_data['Day sin'])[:2500])
plt.plot(np.array(raw_data['Day cos'])[:2500])
plt.xlabel('Time [h]')
plt.title('Time of day signal')