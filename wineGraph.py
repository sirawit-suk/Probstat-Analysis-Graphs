import matplotlib.pyplot as plt     # plot graphs   
import pandas                       # colection for data
import stemgraphic as stm          # stem-leaf graphs
import statistics as stc            # statistics

# Init Style of Graph and Insert table of data in form of columns
plt.style.use('bmh')
columns = pandas.read_csv('testgraphredwine.csv')    

# All columns
x = columns['alcohol']         # x (independent variable) = alcohol 
y = columns['quality']          # y (dependent variable) = quality

'''
    #Calculations 
    1. Mean
    2. Median
    3. Mode
    4. Sample Stardard Deviation
    5. Variance

    Indepentdent
        1. Alcohol 
        2. Residual sugar
    Depentdent 
        1. Quality 
'''

print("All Statistics")
print('--------------Alcohol in Wines---------------')

# Alcohol calculations
alcoholMin = min(x)
alcoholMean = stc.mean(x)
alcoholMed = stc.median(x)
alcoholMax = max(x)
alcoholMode = stc.mode(x)
alcoholSampleSD = stc.stdev(x)
alcoholSampleV = stc.variance(x)

print("alcohol Unit: %/volume")
print("alcohol Min", alcoholMin)
print("alcohol Mean :", alcoholMean)
print("alcohol Median :", alcoholMed)
print("alcohol Max", alcoholMax)
print("alcohol Mode :", alcoholMode)
print("alcohol Sample Standard Deviation :", alcoholSampleSD)
print("alcohol Sample Variance :", alcoholSampleV)

# Alcohol Outlier 
aQt = stc.quantiles(x, method='inclusive')
print("Alcohol[Q1, Q2, Q3]= ",aQt)
al_q1 = aQt[0]
al_q3 = aQt[2]
al_iqr = al_q3 - al_q1
print("IQR = ", al_iqr)
al_mild_low_bound = al_q1 - al_iqr*1.5
al_extreme_low_bound = al_q1 - al_iqr*3
al_mild_up_bound = al_q3 + al_iqr*1.5
al_extreme_up_bound = al_q3 + al_iqr*3

print('\n-----------All Alcohol Outliers Boundaries---------------')
print("al_extreme_low_bound = ", al_extreme_low_bound)
print("al_mild_low_bound = ", al_mild_low_bound)
print("al_mild_up_bound = ", al_mild_up_bound)
print("al_extreme_up_bound = ", al_extreme_up_bound)

al_extreme_low = []
al_mild_low = []
al_mild_up = []
al_extreme_up = []

for i in x:
    if i < al_extreme_low_bound: 
        al_extreme_low.append(i)
    elif al_extreme_low_bound <= i < al_mild_low_bound:
        al_mild_low.append(i)
    elif al_mild_up_bound < i <= al_extreme_up_bound:
        al_mild_up.append(i)
    elif i >= al_extreme_up_bound:
        al_extreme_up.append(i)

print('\n---------------All Alcohol Outliers---------------------')
print("Extreme Outlier(Lower) = ", al_extreme_low)
print("Mild Outlier(Lower) = ", al_mild_low)
print("Mild Outlier(Upper) = ", al_mild_up)
print("Extreme Outlier(Upper) = ", al_extreme_up)
        




print('\n\n--------------Quality of Wines---------------')
# Quality calculations
qualityMin = min(y)
qualityMean = stc.mean(y)
qualityMed = stc.median(y)
qualityMax = max(y)
qualityMode = stc.mode(y)
qualitySampleSD = stc.stdev(y)
qualitySampleV = stc.variance(y)

print("\nquality Unit: None (lv.1-10)")
print("quality Min",qualityMin)
print("quality Mean :", qualityMean)
print("quality Median :", qualityMed)
print("quality Max",qualityMax)
print("quality Mode :", qualityMode)
print("quality Sample Standard Deviation :", qualitySampleSD)
print("quality Sample Variance :", qualitySampleV)

# Quality Outlier 
qQt = stc.quantiles(y, method='inclusive')
print("Quality[Q1, Q2, Q3]= ",qQt)
qu_q1 = qQt[0]
qu_q3 = qQt[2]
qu_iqr = qu_q3 - qu_q1
print("IQR = ", qu_iqr)
qu_mild_low_bound = qu_q1 - qu_iqr*1.5
qu_extreme_low_bound = qu_q1 - qu_iqr*3
qu_mild_up_bound = qu_q3 + qu_iqr*1.5
qu_extreme_up_bound = qu_q3 + qu_iqr*3

print('\n-----------All Quality Outliers Boundaries---------------')
print("qu_extreme_low_bound = ", qu_extreme_low_bound)
print("qu_mild_low_bound = ", qu_mild_low_bound)
print("qu_mild_up_bound = ", qu_mild_up_bound)
print("qu_extreme_up_bound = ", qu_extreme_up_bound)

qu_extreme_low = []
qu_mild_low = []
qu_mild_up = []
qu_extreme_up = []

for i in y:
    if i < qu_extreme_low_bound: 
        qu_extreme_low.append(i)
    elif qu_extreme_low_bound <= i < qu_mild_low_bound:
        qu_mild_low.append(i)
    elif qu_mild_up_bound < i <= qu_extreme_up_bound:
        qu_mild_up.append(i)
    elif i >= qu_extreme_up_bound:
        qu_extreme_up.append(i)

print('\n---------------All Quality Outliers---------------------')
print("Extreme Outlier(Lower) = ", qu_extreme_low)
print("Mild Outlier(Lower) = ", qu_mild_low)
print("Mild Outlier(Upper) = ", qu_mild_up)
print("Extreme Outlier(Upper) = ", qu_extreme_up)



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

# Scatter Plot
figure, scat = plt.subplots(figsize=(12, 8))
plt.tight_layout(pad=4)
scat.set_title('The Relation between Alcohol and Quality in Red Wine (Scatter plot)')
scat.set_xlabel('Alcohol (%/volume)') #indepentdent
scat.set_ylabel('Quality (lv.1-10)') #dependent
scat.scatter(x, y)

# Histogram
figure, his = plt.subplots(1,2, figsize=(14, 5))
plt.tight_layout(pad=4, w_pad=6, h_pad=1.0)
his[0].set_title('Alcohol in Red Wine (Histogram)')
his[0].set_xlabel("Alcohol (%/volume)")
his[0].set_ylabel("Amount of Red Wine (Bottles)")
his[0].hist(x,range(8,16))
his[1].set_title('Quality of Red Wine (Histogram)')
his[1].set_xlabel("Quality (lv.1-10)")
his[1].set_ylabel("Amount of Red Wine (Bottles)")
his[1].hist(y,range(1,11))

# Box Plot
figure, box = plt.subplots(1, 2, figsize=(14, 5))
plt.tight_layout(pad=4, w_pad=3, h_pad=1.0)
box[0].set_title('Alcohol in Red Wine (Box Plot)')
box[0].set_xlabel("Alcohol (%/volume)")
box[0].boxplot(x, vert=False, widths=0.3)
box[1].set_title('Quality of Red Wine (Box Plot)')
box[1].set_xlabel("Quality (lv.1-10)")
box[1].boxplot(y, vert=False, widths=0.3)

# Stem and Leaf
figure, stem = stm.graphic.stem_graphic(x, scale=0.1,leaf_order=1,aggregation =False ,unit='%/volume', display=3000,compact=True)
stem.set_title("Alcohol in Red Wine Stem-And-Leaf")

figure, stem = stm.graphic.stem_graphic(y, scale=1.0,leaf_order=1,aggregation =True,display=3000)
stem.set_title("Quality of Red Wine Stem-And-Leaf")

# Show
plt.show()