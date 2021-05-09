# defining the libraries 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas                       # colection for data

import scipy.stats

# Init Style of Graph and Insert table of data in form of columns
plt.style.use('bmh')
columns = pandas.read_csv('testgraphredwine.csv')    

# All columns
x = columns['total sulfur dioxide']         #alcohol 
#
#fixed acidity

# initial value
dataArray = 1.0 * np.array(x)
print('dataArray :', dataArray)



mean = np.mean(dataArray)
standardError = scipy.stats.sem(dataArray) 
# standardError = standard deviation / samples    1.0656771926520383/ 39.98749804626440991456385162254   # from HW 1
print('standardError(hw1) :', 1.0656771926520383  / 39.98749804626440991456385162254 )  # from HW 1
print('standardError(hw4) :', standardError, '\n')







# moreeeeeeee
randomArray = []
number = 50 # sample size
loop = 50 # random loop

standardError = []

# run only 1 time
for i in range(loop): # loop times
    temp = np.random.choice(dataArray, size=number, replace=False) # not used the one that already picked
    temp.sort()
    tempMean = np.mean(temp)
    randomArray.append(tempMean)
    standardErrorForEach = scipy.stats.sem(temp)  # around 0.15
    standardError.append(standardErrorForEach)

#print('rand Array:', randomArray)
print(len(randomArray))
#mean = np.mean(randomArray)
print('mean: ', mean)

    #print('lower-upper boundary:',mean , mean - marginError[i], mean + marginError[i])

def getMarginError(confidence):
    marginError = []
    z_score = scipy.stats.t.ppf( (1 + confidence) / 2.0, number-1 )
    for i in range(loop):
        marginError.append((standardError[i] * z_score)) # margin error
    return marginError

# moreeeeeeee
figure, al_func_CI = plt.subplots(3, 1, figsize=(8, 10))
plt.tight_layout(pad=5, h_pad=5.0)


#Confidence Interval (CI) Lv. 90% of Alcohol in Red Wine
#Confidence Interval (CI) Lv. 95% of Alcohol in Red Wine
#Confidence Interval (CI) Lv. 99% of Alcohol in Red Wine
#Alcohol (%/volume)


al_func_CI[0].set_title('Confidence Interval (CI) Lv. 90% of Sulfur Dioxide in Red Wine')
al_func_CI[0].set_xlabel("Number of Replicated (times)")
al_func_CI[0].set_ylabel("Sulfur Dioxide (g/L)")
al_func_CI[0].errorbar(np.linspace(1, loop, num=loop), randomArray, getMarginError(0.90), fmt='.k')
al_func_CI[0].plot(np.linspace(0,loop,num=loop), np.linspace(mean,mean,num=loop), color="red", label="mu" )

al_func_CI[1].set_title('Confidence Interval (CI) Lv. 95% of Sulfur Dioxide in Red Wine')
al_func_CI[1].set_xlabel("Number of Replicated (times)")
al_func_CI[1].set_ylabel("Sulfur Dioxide (g/L)")
al_func_CI[1].errorbar(np.linspace(1, loop, num=loop), randomArray, getMarginError(0.95), fmt='.k')
al_func_CI[1].plot(np.linspace(0,loop,num=loop), np.linspace(mean,mean,num=loop), color="red", label="mu")

al_func_CI[2].set_title('Confidence Interval (CI) Lv. 99% of Sulfur Dioxide in Red Wine')
al_func_CI[2].set_xlabel("Number of Replicated (times)")
al_func_CI[2].set_ylabel("Sulfur Dioxide (g/L)")
al_func_CI[2].errorbar(np.linspace(1, loop, num=loop), randomArray, getMarginError(0.99), fmt='.k')
al_func_CI[2].plot(np.linspace(0,loop,num=loop), np.linspace(mean,mean,num=loop), color="red", label="mu")







# def confidence_interval(confidence):
#     con = format(confidence, '.2f')
#     print(f'*** confidence of {con} % ***')

#     z_score = scipy.stats.t.ppf( (1 + confidence) / 2.0, number-1 )
#     print('z-score :', z_score)

#     marginError = standardError * z_score
#     # marginError = standardError * z-score 
    
#     print('margin error :', marginError,'\n')

#     print('***SUMMARY***')
#     print('mean :', mean)
#     print('lower-upper boundary:', mean - marginError, mean + marginError)

#     print('*************\n\n')
#     return mean, mean - marginError, mean + marginError

# mean1, lowerB1, upperB1 = confidence_interval(0.90)
# mean2, lowerB2, upperB2 = confidence_interval(0.95)
# mean3, lowerB3, upperB3 = confidence_interval(0.99)



# # getting data of the histogram 
# al_count, al_bins_count = np.histogram(x, bins=18) # y (quantity) and x (value)

# # finding the PDF of the histogram using count values 
# al_pdf = al_count / sum(al_count) 



# figure, al_func = plt.subplots(3, 1, figsize=(8, 10))
# plt.tight_layout(pad=5, h_pad=5.0)

# y = np.linspace(0,1)

# al_func[0].set_title('Confidence Interval (CI) Lv. 90% of Alcohol in Red Wine (PDF Graph)')
# al_func[0].set_xlabel("Alcohol (%/volume)")
# al_func[0].set_ylabel("Probability")
# al_func[0].plot(al_bins_count[1:], al_pdf, color="green", label="PDF" ) 
# x1 = np.linspace(lowerB1,lowerB1)
# x2 = np.linspace(upperB1,upperB1)
# al_func[0].plot(x1,y, label="Lower Boudary = {:.4f}".format(lowerB1))
# al_func[0].plot(x2,y, label="Upper Boudary = {:.4f}".format(upperB1))
# al_func[0].legend()
# al_func[0].axis(ymax=1)

# al_func[1].set_title('Confidence Interval (CI) Lv. 95% of Alcohol in Red Wine (PDF Graph)')
# al_func[1].set_xlabel("Alcohol (%/volume)")
# al_func[1].set_ylabel("Probability")
# al_func[1].plot(al_bins_count[1:], al_pdf, color="green", label="PDF" ) 
# x1 = np.linspace(lowerB2,lowerB2)
# x2 = np.linspace(upperB2,upperB2)
# al_func[1].plot(x1,y, label="Lower Boudary = {:.4f}".format(lowerB2))
# al_func[1].plot(x2,y, label="Upper Boudary = {:.4f}".format(upperB2))
# al_func[1].legend()
# al_func[1].axis(ymax=1)

# al_func[2].set_title('Confidence Interval (CI) Lv. 99% of Alcohol in Red Wine (PDF Graph)')
# al_func[2].set_xlabel("Alcohol (%/volume)")
# al_func[2].set_ylabel("Probability")
# al_func[2].plot(al_bins_count[1:], al_pdf, color="green", label="PDF" ) 
# x1 = np.linspace(lowerB3,lowerB3)
# x2 = np.linspace(upperB3,upperB3)
# al_func[2].plot(x1,y, label="Lower Boudary = {:.4f}".format(lowerB3),)
# al_func[2].plot(x2,y, label="Upper Boudary = {:.4f}".format(upperB3))
# al_func[2].legend()
# al_func[2].axis(ymax=1)

  
plt.show()
