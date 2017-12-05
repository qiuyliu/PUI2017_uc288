# HW10_uc288 - Time Series Analysis of MTA

## Task 1: Event Detection
I summed up the swipes per card type and per station and assigned them to their own variables. I then took one of the two and aggregated them further to create a one-dimensional data which represents the time series for all MTA swipes for the span of 194 weeks. 

Plotting the time series showed the drop which is pretty far from the usual trend. I applied the same technique from the FDNY deaths lab that was done in class by setting a threshold 3 standard deviations away from the mean and was able to identify the week when the event occurred.

### Work Distribution
I worked on this task alone but had discussions with **Yu**, **Gaurav**, and **Isha** after completing the task.

## Task 2: Stationarity of Time Series
I plotted the 23 time series per card type in a plot to visually see if there's a trend but since the difference in counts between the card types are quite far, the resolution of the plot is not so good.

Converted the 2D numpy array into a pandas DataFrame for easier plotting and application of the rolling mean because there was a warning thrown when using the     `pd.rolling()` function on `numpy.ndarray`.

I then plotted each card type time series individually with their rolling mean in their own subplot for visual comparison. I also conducted the Augmented Dickey-Fuller unit root test for each time series for the test of stationarity.

### Work Distribution

Initially worked on this alone but had discussions with **Juan** and **Julian** regarding the ratio and how to determine the trend.

## Task 3: Periodicity of Time Series

### Work Distribution


## Extra Credit

### Work Distribution




