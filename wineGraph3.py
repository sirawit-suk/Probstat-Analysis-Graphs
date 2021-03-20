# defining the libraries 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas                       # colection for data

import scipy.stats

# Init Style of Graph and Insert table of data in form of columns
plt.style.use('bmh')
columns = pandas.read_csv('testgraphredwine.csv')    

# All columns
x = columns['alcohol']         # x (independent variable) = alcohol 

# initial value
dataArray = 1.0 * np.array(x)
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
    return mean, mean - marginError, mean + marginError

mean1, lowerB1, upperB1 = confidence_interval(0.90)
mean2, lowerB2, upperB2 = confidence_interval(0.95)
mean3, lowerB3, upperB3 = confidence_interval(0.99)



# getting data of the histogram 
al_count, al_bins_count = np.histogram(x, bins=18) # y (quantity) and x (value)

# finding the PDF of the histogram using count values 
al_pdf = al_count / sum(al_count) 



figure, al_func = plt.subplots(3, 1, figsize=(8, 10))
plt.tight_layout(pad=5, h_pad=5.0)

y = np.linspace(0,1)

al_func[0].set_title('Confidence Interval (CI) Lv. 90% of Alcohol in Red Wine (PDF Graph)')
al_func[0].set_xlabel("Alcohol (%/volume)")
al_func[0].set_ylabel("Probability")
al_func[0].plot(al_bins_count[1:], al_pdf, color="green", label="PDF" ) 
x1 = np.linspace(lowerB1,lowerB1)
x2 = np.linspace(upperB1,upperB1)
al_func[0].plot(x1,y, label="Lower Boudary = {:.4f}".format(lowerB1))
al_func[0].plot(x2,y, label="Upper Boudary = {:.4f}".format(upperB1))
al_func[0].legend()
al_func[0].axis(ymax=1)

al_func[1].set_title('Confidence Interval (CI) Lv. 95% of Alcohol in Red Wine (PDF Graph)')
al_func[1].set_xlabel("Alcohol (%/volume)")
al_func[1].set_ylabel("Probability")
al_func[1].plot(al_bins_count[1:], al_pdf, color="green", label="PDF" ) 
x1 = np.linspace(lowerB2,lowerB2)
x2 = np.linspace(upperB2,upperB2)
al_func[1].plot(x1,y, label="Lower Boudary = {:.4f}".format(lowerB2))
al_func[1].plot(x2,y, label="Upper Boudary = {:.4f}".format(upperB2))
al_func[1].legend()
al_func[1].axis(ymax=1)

al_func[2].set_title('Confidence Interval (CI) Lv. 99% of Alcohol in Red Wine (PDF Graph)')
al_func[2].set_xlabel("Alcohol (%/volume)")
al_func[2].set_ylabel("Probability")
al_func[2].plot(al_bins_count[1:], al_pdf, color="green", label="PDF" ) 
x1 = np.linspace(lowerB3,lowerB3)
x2 = np.linspace(upperB3,upperB3)
al_func[2].plot(x1,y, label="Lower Boudary = {:.4f}".format(lowerB3))
al_func[2].plot(x2,y, label="Upper Boudary = {:.4f}".format(upperB3))
al_func[2].legend()
al_func[2].axis(ymax=1)





#plt.plot(x,y, linestyle='')  # solid


  
plt.show()
