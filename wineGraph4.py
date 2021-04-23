import matplotlib.pyplot as plt     # plot graphs   
import pandas                       # colection for data
from scipy import stats
import math
import statistics as stc


# Init Style of Graph and Insert table of data in form of columns
plt.style.use('bmh')
columns = pandas.read_csv('testgraphredwine.csv')    

# All columns
x = columns['alcohol']         # x (independent variable) = alcohol 
y = columns['quality']          # y (dependent variable) = quality

'''
    #Graphs
    1. Histogram
    2. Box Plot
    3. Stem and Leave
    4. XY (Scatter) Plot (suitable variable)(describe more) 

    Detail
    1. Name of Graph
    2. Name of Axis
    3. Suitable variable 
    4. Identify Outlier  

'''
'''
    y = mx + c

    m = SSxy/SSxx

    SSxy = sum(x*y) + sum(x)*sum(y)/n 
    SSxx = sum(x*x) + sum(x)*sum(x)/n
    SSyy = sum(y*y) + sum(y)*sum(y)/n

    r = SSxy / sqrt(SSxx*SSyy) 

'''
#y = m*x + c

n = len(x)
y_bar = stc.mean(y)
x_bar = stc.mean(x)

# method 1 (easy to calculate)
SSxy = sum(x*y) - sum(x)*sum(y)/n 
SSxx = sum(x*x) - sum(x)*sum(x)/n
SSyy = sum(y*y) - sum(y)*sum(y)/n

# method 2 (easy to understand)
SSxy_mean = sum(( x - x_bar) * (y - y_bar))
SSxx_mean = sum(( x - x_bar) ** 2)
SSyy_mean = sum(( y - y_bar) ** 2)

# find slope (m)
m = SSxy / SSxx
# find intercept (c)
c = y_bar - m * x_bar 
# find correlation coefficient (r)
r = SSxy / math.sqrt(SSxx*SSyy) 

y_estimate = m * x + c
SSerror = sum((y-y_estimate) ** 2)  # ( actual value - estimate value ) ^ 2  # graph -> ('/.) # value is + or - change to ^2
Rsquare = 1 - SSerror / SSyy
SSerrorInvert = sum((y_estimate-y_bar) ** 2) # ( estimate value -  mean value )  ^ 2  # graph -> (-/-) # sum is = 0 if not ^2
RsquareV2 =  SSerrorInvert / SSyy

# conclude: SSerrorInvert = (m * SSxy) = sum((y_estimate-y_bar) ** 2)
# conclude: SSerror = SSyy - (m * SSxy) =  sum((y-y_estimate) ** 2)

RsquareV3 = (m * SSxy) / SSyy

stdERR = math.sqrt(SSerror / (n-2))
stdERRV2 = math.sqrt((SSyy - (m*SSxy)) / (n-2))


print('------------ My Own Calculation --------------')

print("slope (m) = {:.2f}".format(m))
print("intercept (c) = {:.2f}\n".format(c))
print("n = {:.2f}".format(n))
print("y_bar = {:.2f}".format(y_bar))
print("x_bar = {:.2f}\n".format(x_bar))
print("SSxy_calc = {:.4f}".format(SSxy))
print("SSxy_mean = {:.4f}".format(SSxy_mean))
print("SSxx_calc = {:.4f}".format(SSxx))
print("SSxx_mean = {:.4f}".format(SSxx_mean))
print("SSyy_calc = {:.4f}".format(SSyy))
print("SSyy_mean = {:.4f}\n".format(SSyy_mean))
print("r_value (r) = {:.4f}".format(r))
print("r_value^2 (r^2) = {:.4f}".format(r ** 2))
#print(f"y_estimate = {y_estimate}\n")
print("SSerror = {:.4f}".format(SSerror))
print("SSerrorInvert = {:.4f}".format(SSerrorInvert))
print("Rsquare = {:.4f}".format(Rsquare))
print("RsquareV2 = {:.4f}".format(RsquareV2))
print("RsquareV3 = {:.4f}\n".format(RsquareV3))
print("stdERR = {:.4f}".format(stdERR))
print("stdERRV2 = {:.4f}\n".format(stdERRV2))

print('--------------- Use Library Function ------------------')

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("slope (m) = {:.2f}".format(slope))
print("intercept (c) = {:.2f}\n".format(intercept))
print("r_value (r) = {:.4f}".format(r_value))
print("r_value^2 (r^2) = {:.4f}\n".format(r_value ** 2))
print("p_value (p) = {:.4f} # Not use ".format(p_value))
print("std_err = {:.4f} # this is wrong, Don't use this one, IDK why ? use 0.7104 instead\n".format(std_err)) 
print(r"{} = {:.2f}x + {:.2f}, r^2 = {:.4f}, p = {:.4f}".format("y", slope, intercept, r_value **2, p_value))

# for title text
lineEquation = r"${} = {:.2f}x + {:.2f}, r^2 = {:.4f}, p = {:.4f}$".format("\^{y}", slope, intercept, r_value **2, p_value)

# plot graph
xMin_xMax = [min(x),max(x)]
yMin_yMax = [slope*min(x) + intercept, slope*max(x) + intercept]  # y = mx + c  

# Scatter Plot
figure, scat = plt.subplots(figsize=(12, 8))
plt.tight_layout(pad=4)
scat.set_title('The Relation between Alcohol and Quality in Red Wine (Scatter plot)\n' +lineEquation)
scat.set_xlabel('Alcohol (%/volume)') #indepentdent
scat.set_ylabel('Quality (lv.1-10)') #dependent
scat.scatter(x, y)
scat.plot(xMin_xMax, yMin_yMax, alpha=.5, color="green")

# Show
plt.show()