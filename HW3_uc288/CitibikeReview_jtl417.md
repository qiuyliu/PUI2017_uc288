## Are the Null and Alternative Hypotheses Formulated Correctly?

The question being asked here relates to how subscribers and customers use bikes based on weekend vs. weekday. In words, the alternate hypothesis is that subscribers use bikes more on the weekdays, whereas customers use bikes more on the weekends. There are a couple of complications that need to be dealt with in the formulation of the hypotheses: the fact that there are more weekdays then weekends, as well as different numbers of subscribers and customers using citibike. The formulation of the hypothesis does a good job of capturing the complicated nature of this idea. Essentially, the null hypothesis suggests that if the ratio of subscribers biking on the weekday to those biking on weekends is less than or equal to the ratio of customers biking on the weekday to those biking on the weekends, then customers are therefore more inclined to bike on weekdays than subscribers. This formulation does a good job of dealing with the fact that there are more weekdays than weekend days, but there may still be an issue of sample size influencing these ratios that might skew the result. Nonetheless, the null hypothesis does a very good job of expressing this somewhat complicated idea. Furthermore, the null hypothesis is the converse of the idea presented initially, which is the correct way of thinking about a null hypothesis. Finally, the alternative hypothesis is the converse of the null hypothesis and does not overlap in any way with the null hypothesis, which is also correct.

## Does the data support the project?

**Does the data have the right variables to answer the question?** 
The data needs to contain the four variables included in the null and alternative hypotheses: the number of subscribers riding on weekdays, the nunmber of subscribers riding on weekends, the nunmber of customers riding on weekdays and the number of customers riding on the weekends. The data is clearly separated by subscriber and customer. In code cell 11, you can clearly see the counts for customers and subscribers filtered by day of the week. And in cells 16 - 21 the ratios themselves are calculated. Therfore, all the necessary variables are there!

**Was the data properly pre-processed to extract the needed values?**
The data was very well pre-processed to extract the needed values - not only that, but it was pre-processed to extract ONLY the needed values, which makes coding and following code quite easy to follow.


## The appropriate statistical test based on H0 and question asked

This is a test of ratios, where the dependent variable is a count. We do have a priori expectation. There is one variable, one sample and two categories. Therefore, according to the flowchart in the slides, the statistical test should be a chi-squared goodness of fit test with Yate's correlation or Fischers exact test.

## Other Comments and Suggestions

The idea is a really good, interesting, and testable one, but the formulation of the hypothesis is tricky because of the fact that its hard to quantify something like "x uses citibike more than y in A time period" given the many differences in sample size. I think you did a good job dealing with that but it would be nice to hear some explanation as to why you chose the ratio (if only for myself and others who might not be as intuitive with math and inequalities/ratios.
