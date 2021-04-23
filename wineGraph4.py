import matplotlib.pyplot as plt     # plot graphs   
import pandas                       # colection for data
from scipy import stats


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


slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("slope (m) = {:.2f}".format(slope))
print("intercept (c) = {:.2f}".format(intercept))
print("r_value (r) = {:.4f}".format(r_value))
print("r_value^2 (r^2) = {:.4f}".format(r_value ** 2))
print("p_value (p) = {:.4f}".format(p_value))
print("std_err = {:.4f}".format(std_err))
print(r"{} = {:.2f}x + {:.2f}, r^2 = {:.4f}, p = {:.4f}".format("y", slope, intercept, r_value **2, p_value))

lineEquation = r"${} = {:.2f}x + {:.2f}, r^2 = {:.4f}, p = {:.4f}$".format("\^{y}", slope, intercept, r_value **2, p_value)

l = slope * min(x) + intercept, slope * max(x) + intercept  # y = mx + c  

# Scatter Plot
figure, scat = plt.subplots(figsize=(12, 8))
plt.tight_layout(pad=4)
scat.set_title('The Relation between Alcohol and Quality in Red Wine (Scatter plot)\n' +lineEquation)
scat.set_xlabel('Alcohol (%/volume)') #indepentdent
scat.set_ylabel('Quality (lv.1-10)') #dependent
scat.scatter(x, y)
scat.plot([min(x),max(x)], l, linestyle="--", alpha=.5, color="green")


# Show
plt.show()