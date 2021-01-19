import matplotlib.pyplot as plt 
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('testgraphredwine.csv')

x = df['quality']
y = df['alcohol']

# Line Graph
plt.xlabel('quality', fontsize = 18)
plt.ylabel('alcohol', fontsize = 16)
plt.bar(x, y)