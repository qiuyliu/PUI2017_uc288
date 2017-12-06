# HW10_uc288 - Time Series Analysis of MTA

## Task 1: Event Detection
I summed up the swipes per card type and per station and assigned them to their own variables. I then took one of the two and aggregated them further to create a one-dimensional data which represents the time series for all MTA swipes for the span of 194 weeks. 

Plotting the time series showed the drop which is pretty far from the usual trend. I applied the same technique from the FDNY deaths lab that was done in class by setting a threshold 3 standard deviations away from the mean and was able to identify the week when the event occurred.

### Work Distribution
I worked on this task alone but had discussions with **Yu**, **Gaurav**, and **Isha** after completing the task.

## Task 2: Stationarity of Time Series
I plotted the 23 time series per card type in a plot to visually see if there's a trend but since the difference in counts between the card types are quite far, the resolution of the plot is not so good.

Converted the 2D numpy array into a pandas DataFrame for easier plotting and application of the rolling mean because there was a warning thrown when using the `pd.rolling()` function on `numpy.ndarray`.

I then plotted each card type time series individually with their rolling mean in their own subplot for visual comparison. I also conducted the Augmented Dickey-Fuller unit root test for each time series for the test of stationarity. I also computed for the "flux ratio" by dividing the mean of the first 10 weeks by the mean of the last 10 weeks.

### Work Distribution
Initially worked on this alone but had discussions with **Juan** and **Julian** regarding the ratio and how to determine the trend. Also discussed which card types they chose for the increasing and decreasing trend and why they chose those.

For the plot of the two trends for comparison, I got the idea of plotting the rolling mean and the actual timeseries from **Juan**.

## Task 3: Periodicity of Time Series
I plotted the power spectrum of the number of swipes for the 194-week period for all 600 stations and from there, I zoomed in on the initial plot to get the 4 stations with the most prominent annual periodcity by limiting the x and y axis. In the for loop, I also used the y-limit to get the index of the stations which show up in the plot. Then I plotted the 4 stations and saw that they indeed have similar periodcity for every 52 weeks.

### Work Distribution
For this task, I attempted to finish it alone however I consulted **Chun Chieh (Jack) Tsai** and refered to his notebook to figure out where I was getting the Power Spectrum plot wrong. I only used the notebook as a guide to understand the concept of periodicity better.

## Extra Credit
I followed Professor Federica's code for reshaping the data for clustering and applied lessons from Applied Data Science class to get the clustering using PCA.

### Work Distribution
I worked on this task alone with the help of code from lab notebooks from Applied Data Science. I also realized I did something wrong after discussing the extra credit homework with **Rachel**.