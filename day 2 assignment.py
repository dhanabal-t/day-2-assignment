import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['a','b','c','d'])

df = df.cumsum()

plt.figure()

df.plot()