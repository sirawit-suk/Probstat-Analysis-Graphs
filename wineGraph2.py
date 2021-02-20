# defining the libraries 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas                       # colection for data

  
# Init Style of Graph and Insert table of data in form of columns
plt.style.use('bmh')
columns = pandas.read_csv('testgraphredwine.csv')    

# All columns
x = columns['alcohol']         # x (independent variable) = alcohol 
y = columns['quality']          # y (dependent variable) = quality

  
# getting data of the histogram 
al_count, al_bins_count = np.histogram(x, bins=18) 
qu_count, qu_bins_count = np.histogram(y, bins=1000) #6
  
# finding the PDF of the histogram using count values 
al_pdf = al_count / sum(al_count) 
al_cdf = np.cumsum(al_pdf) 

qu_pdf = qu_count / sum(qu_count) 
qu_cdf = np.cumsum(qu_pdf) 


figure, al_func = plt.subplots(1, 2, figsize=(14, 5))
plt.tight_layout(pad=4, w_pad=3, h_pad=1.0)

al_func[0].set_title('Alcohol in Red Wine (Probability Density Function (PDF))')
al_func[0].set_xlabel("Alcohol (%/volume)")
al_func[0].set_ylabel("Probability")
al_func[0].plot(al_bins_count[1:], al_pdf, color="green", label="PDF", ) 
al_func[0].legend()
al_func[0].axis(ymax=1)

al_func[1].set_title('Alcohol in Red Wine (Cumulative Distribution Function (CDF))')
al_func[1].set_xlabel("Alcohol (%/volume)")
al_func[1].set_ylabel("Cumulative Probability")
al_func[1].plot(al_bins_count[1:], al_cdf, color="red", label="CDF") 
al_func[1].legend()


figure, qu_func = plt.subplots(1, 2, figsize=(14, 5))
plt.tight_layout(pad=4, w_pad=3, h_pad=1.0)

qu_func[0].set_title('Quality of Red Wine (Probability Mass Function (PMF))')
qu_func[0].set_xlabel("Quality (lv.1-10)")
qu_func[0].set_ylabel("Probability")
qu_func[0].plot(qu_bins_count[1:], qu_pdf, color="green", label="PDF", ) 
qu_func[0].legend()
qu_func[0].axis(ymax=1)

qu_func[1].set_title('Quality of Red Wine (Cumulative Distribution Function (CDF))')
qu_func[1].set_xlabel("Quality (lv.1-10)")
qu_func[1].set_ylabel("Cumulative Probability")
qu_func[1].plot(qu_bins_count[1:], qu_cdf, color="red", label="CDF") 
qu_func[1].legend()


figure, total = plt.subplots(1, 2, figsize=(14, 5))
plt.tight_layout(pad=4, w_pad=3, h_pad=1.0)

total[0].set_title('Alcohol in Red Wine (PDF and CDF)')
total[0].set_xlabel("Alcohol (%/volume)")
qu_func[1].set_ylabel("Probability")
total[0].plot(al_bins_count[1:], al_pdf, color="green", label="PDF") 
total[0].plot(al_bins_count[1:], al_cdf, color="red", label="CDF") 
total[0].legend()

total[1].set_title('Quality of Red Wine Summary Graph (PMF and CDF)')
total[1].set_xlabel("Quality (lv.1-10)")
qu_func[1].set_ylabel("Probability")
total[1].plot(qu_bins_count[1:], qu_pdf, color="green", label="PDF") 
total[1].plot(qu_bins_count[1:], qu_cdf, color="red", label="CDF") 
total[1].legend()



  
plt.show()
