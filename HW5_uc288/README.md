# HW5_uc288

## Assignment 1: Test the z-test
I was initially working on the assignment on my own but noticed really weird p-values for my KS and AD tests for both distributions. I know based on the discussions in class, we were supposed to get high p-values because the distribution of the z-statistics of a high mean Poisson and Binomial distribution is quite similar to a Gaussian.

I shared my answers with **Andrew Guobing Chen** and he reminded me that the standard deviation of the Poisson distribution is the square root of the mean.

So I readjusted the values I had and recomputed for the z-statistics for both the Poisson and Binomial distributions and got a higher p-value for both tests.

## Assignment 2: Compare Tests for Goodness of fit


## Assignment 3: Investigate linear relationships between fire arm possession, homicides by fire arms, and mass shootings for different countries, considering also the country GDP
A bunch of different data needs to be downloaded and it needs to be reproducible so I tried doing a direct download instead of downloading the files in the code and save it in the file system.
1. World firearms murders and ownership
    * Direct download to pandas using **@fedhere**'s GitHub RAW download link
2. The number of gun owned vs. the number of mass shootings 
    * Google search on how to handle `data:application` links gave me [this reference on StackOverflow](https://stackoverflow.com/questions/41919181/python-download-file-with-pandas-urllib) and I used the idea to use urllib to download like before with the MTA API and use pandas read_csv.
3. 