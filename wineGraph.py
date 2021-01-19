import matplotlib.pyplot as plt 
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('testgraphredwine.csv')

# x (independent variable) = alcohol
# y (dependent variable) = quality
'''
# All column
x = df['alcohol'] 
y = df['quality']

# Dot Graph
plt.xlabel('alcohol', fontsize = 18)
plt.ylabel('quality', fontsize = 16)
plt.scatter(x, y)
'''

# x (independent variable) = quality
# y (dependent variable) = alcohol

# All column
x = df['quality'] 
y = df['alcohol']

# Dot Graph
plt.xlabel('quality', fontsize = 18)
plt.ylabel('alcohol', fontsize = 16)
plt.scatter(x, y)

# Show
plt.show()