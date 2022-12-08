# 1 - Import the data (csv upload)
# 2 - Clean the data
# 3 - Split data. Training Set/Test Set (decide rows to learn from and which to test on)
# 4 - Create a Model
# 5 - Check the output
#6 - Improve
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


fifa = pd.read_csv("../input/fifa-20-complete-player-dataset/players_20.csv")
fifa.head()

fifa["nationality"].value_counts()[0:5]

plt.figure(figsize=(10, 5))
plt.bar(list(fifa["nationality"].value_counts()[0:5].keys()), list(
    fifa["nationality"].value_counts()[0:5]), color="#10542F")
plt.show

# COMPLETE COPY AND PASTE FROM A JUPYTER LIBRARY PROJECT
