import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action='ignore')


member = pd.read_csv("./credit.csv" , encoding='utf-8')



print(member)
