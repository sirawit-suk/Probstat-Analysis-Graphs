import matplotlib.pyplot as plt 
import pandas as pd
import statistics as stc

plt.style.use('bmh')
df = pd.read_csv('testgraphredwine.csv')

# x (independent variable) = alcohol
# y (dependent variable) = quality

# All column
x = df['alcohol'] 
y = df['quality']

""" use this one
# Dot Graph
plt.xlabel('alcohol', fontsize = 18)
plt.ylabel('quality', fontsize = 16)
plt.scatter(x, y)
"""


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
'''
alcoholMean = stc.mean(x)
qualityMean = stc.mean(y)
print("alcohol Mean :", alcoholMean)
print("quality Mean :", qualityMean)

alcoholMed = stc.median(x)
qualityMed = stc.median(y)
print("alcohol Med :", alcoholMed)
print("quality Med :", qualityMed)

alcoholMode = stc.mode(x)
qualityMode = stc.mode(y)
print("alcohol Mode :", alcoholMode)
print("quality Mode :", qualityMode)

alcoholSampleStandardDeviation = stc.stdev(x)
qualitySampleStandardDeviation = stc.stdev(y)
print("alcohol Sample Standard Deviation :", alcoholSampleStandardDeviation)
print("quality Sample Standard Deviation :", qualitySampleStandardDeviation)

alcoholSampleVariance = stc.variance(x)
qualitySampleVariance = stc.variance(y)
print("alcohol Sample Variance :", alcoholSampleVariance)
print("quality Sample Variance :", qualitySampleVariance)

# don't forget !!! the UNIT !!!!!

plt.boxplot(x);
plt.boxplot(y);

# Show
plt.show()