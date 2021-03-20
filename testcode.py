import numpy as np
import scipy.stats


import matplotlib.pyplot as plt 
import pandas                       # colection for data

  
# Init Style of Graph and Insert table of data in form of columns
plt.style.use('bmh')
columns = pandas.read_csv('testgraphredwine.csv')    

# All columns
alcoholData = columns['alcohol']         # x (independent variable) = alcohol 


# initial value
dataArray = 1.0 * np.array(alcoholData)
print('dataArray :', dataArray)
number = len(dataArray)
mean = np.mean(dataArray)
standardError = scipy.stats.sem(dataArray) 
# standardError = standard deviation / samples    1.0656771926520383/ 39.98749804626440991456385162254   # from HW 1
print('standardError(hw1) :', 1.0656771926520383  / 39.98749804626440991456385162254 )  # from HW 1
print('standardError(hw4) :', standardError, '\n')


def confidence_interval(confidence):
    con = format(confidence, '.2f')
    print(f'*** confidence of {con} % ***')

    z_score = scipy.stats.t.ppf( (1 + confidence) / 2.0, number-1 )
    print('z-score :', z_score)

    marginError = standardError * z_score
    # marginError = standardError * z-score 
    
    print('margin error :', marginError,'\n')

    print('***SUMMARY***')
    print('mean :', mean)
    print('lower-upper boundary:', mean - marginError, mean + marginError)

    print('*************\n\n')

confidence_interval(0.90)
confidence_interval(0.95)
confidence_interval(0.99)
