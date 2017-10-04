# HW3 - uc288

## Assignment 1
Based majority of my work on the skeleton Jupyter notebook provided by Professor Federica Bianco. As suggested, Wikipedia had information about the different distributions and what the mean was for each type of distribution. I mapped the different numpy.random distribution functions with the expressions from Wikipedia and found that Normal, Poisson and Chi-square distributions all had the mean as an argument. For simplicity, I chose Laplace, which also took the mean as an argument.

For the Binomial distribution, the mean is equal to $np$, where $n$ is the number of successes and $p$ is the probability of success. To be able to get the same mean for the binomial distribution, I had to set a value for the probability of success and solve for the number of successes and pass that as an argument.

For the sizes, I chose to use `numpy.random.randint` instead of the sample provided in the skeleton notebook just for randomness.

For the Gaussian fitting (extra credit), my reference was Google and StackOverflow.
The sample code which helped me is found here: http://firsttimeprogrammer.blogspot.com/2014/07/how-to-fit-data-to-normal-distribution.html

## Assignment 2
For this CitiBike hypothesis, I was trying to find a hypothesis related to the time travelled but was not sure if it would show a proper difference. When I asked **Rachel Lim Xin Rong** what she did, she said she used the user type as a point of comparison so I created my hypothesis around that idea as well.

The idea is that the Subscribers are the commuters so they are more likely to go around during the work week and Customers are more or less tourists or people who do not frequent NYC so they tour around during the weekends. This hypothesis is similar to Professor Bianco's example - User Type instead of Gender comparison.

For the data retrieval code, I simply used Professor Bianco's function although I did create a small chunk of code which works too, but is not very reusable.

```python
PUIdata = os.getenv('PUIDATA')
zipfile = '/201612-citibike-tripdata.zip'
csvfile = '/201612-citibike-tripdata.csv'

if os.path.isfile(PUIdata + csvfile):
    print('CSV File found in ' + PUIdata)
else:
    if os.path.isfile(PUIdata + zipfile):
        print('ZIP file found in ' + PUIdata)
    else:
        print('File not found! Downloading ZIP file from CDF to ' + PUIdata + '...')
        os.system('cp /gws/open/Student/citibike' + zipfile + ' ' + PUIdata)
    print('Unzipping file ' + zipfile)
    os.system('unzip ' + PUIdata + zipfile + ' -d ' + PUIdata)

if os.path.isfile(PUIdata + csvfile):
    print('File is now present in ' + PUIdata)
```

I ended up using too much time working on the hypothesis so I no longer had time to improve on this code.

For the data modification, I also got the idea of changing the values of Subscriber and Customer to numerical values from **Rachel Lim Xin Rong**.

The graphs are similar to how Professor Bianco set up her plotting using Pandas to plot instead of matplotlib.

At the end of the graphs, I added the computation for the ratios mentioned in the hypothesis to prove/reject the Null Hypothesis. It does show that the ratio of the subscribers riding on the weekdays over the subscribers riding on weekends is **HIGHER** than the ratio of customers riding on the weekdays over the customers riding on weekends.

_Based on my understanding, doing the z-test is for next week's homework._

## Assignment 3
I worked with **Rachel Lim Xin Rong** on this lab during class and followed the solutions by Professor Federica Bianco after. Completed this notebook based on the [Lab 3 notebook](/Lab3_uc288/Lab3_Distributions.ipynb).
