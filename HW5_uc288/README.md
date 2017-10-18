# HW5_uc288

## Assignment 1: Test the z-test
I was initially working on the assignment on my own but noticed really weird p-values for my KS and AD tests for both distributions. I know based on the discussions in class, we were supposed to get high p-values because the distribution of the z-statistics of a high mean Poisson and Binomial distribution is quite similar to a Gaussian.

I shared my answers with **Andrew Guobing Chen** and he reminded me that the standard deviation of the Poisson distribution is the square root of the mean.

So I readjusted the values I had to follow the definitions of mean and standard deviation for Poisson and Binomial distributions and recomputed the z-statistics for both the distributions and got a higher p-value for both tests.

## Assignment 2: Compare Tests for Goodness of fit
In this assignment, we tried to compare the two distributions - Poisson and Binomial - to a Gaussian distribution by increasing the mean of the distributions and normalizing it to be centered at 0.

For the first part of the assignment, I was able to follow the skeleton notebook provided and just added the null hypothesis and findings based on the results. I replicated what was done in Binomial for Poisson, changing the values for the parameters to be passed to match the distribution.

For the KL divergence, I tried to understand the values by researching more on how the values of KL divergence changes. Quotes that helped me are in the notebook, together with the links to where I found them. For passing the arguments to the KL divergence test, I simply used the code from the skeleton but I understood that numpy.histogram returns the values of the histogram and the bin edges. Setting the density to false gives the probability density function in the bin instead of the actual values which matches the values we pass in scipy.stats.norm.pdf() for the normal distribution.

For the Chi-square test, **Yu Chen** and I based it off **Yuwen Chang**'s implementation by passing the same arguments to the function as the KL divergence. It was quite confusing to get a p-value of 0.99 for all three comparisons despite the low mean so I'm not 100% sure about how this works despite trying to find an answer online. But to complete the assignment, I wrote that we cannot reject the null hypothesis of the chi-square test that the two distributions are similar because of the high p-value.

## Assignment 3: Investigate linear relationships between fire arm possession, homicides by fire arms, and mass shootings for different countries, considering also the country GDP
A bunch of different data needs to be downloaded and it needs to be reproducible so I tried doing a direct download instead of downloading the files in the code and save it in the file system.
1. World firearms murders and ownership
    * Direct download to pandas using **@fedhere**'s GitHub RAW download link
2. The number of gun owned vs. the number of mass shootings 
    * Google search on how to handle `data:application` links gave me [this reference on StackOverflow](https://stackoverflow.com/questions/41919181/python-download-file-with-pandas-urllib) and I used the idea to use urllib to download like before with the MTA API and use pandas read\_csv.
    * Shared the code to do this download to **Rachel Lim Xin Rong** and **Yu Chen**.
3. Population and GDP data from World Bank
    * I downloaded it manually and extracted the files from the ZIP file and uploaded it to my GitHub repo. I used the RAW download link to read the files in my homework.
    * I got the link of GDP data from **Rachel Lim Xin Rong**
    * I also shared to **Rachel Lim Xin Rong** that the link in my repository can be used to download the data to make her work reproducible.
    
For the data exploration plotting, I had some discussions with **Rachel Lim Xin Rong** and **Gaurav Bhardwaj** to understand which values are being plotted and how they did their plots. I adjusted mine based on the results I saw from their plots.

For the modelling part, I consulted with **Rachel Lim Xin Rong** regarding the weights she used in hers and she pointed out that 1 is the default value in the scipy function for WLS so replacing infinity with 1 made sense. I also got the polyfit from **Rachel** and how to plot it.