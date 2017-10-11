# HW4_uc288

## Assignment 1
Completed the CitiBike review on my own. Based the statistical test suggestion on the screenshot that was in the slides.

## Assignment 2
I worked on this assignment on my own and tried my best to understand the articles and the analysis done in the researches. To better find the independent and dependent variables, I used the table which listed what type of variables should be present for each type of test.

I shared the ANCOVA and Correlation papers I used to **Yu Chen** but we did not discuss the papers together to find the required values for the table.

## Assignment 3
I worked on this assignment on my own by following the skeleton notebook already created by Professor Bianco and simply filling up the cells that needed explaning.

For the null and alternative hypothesis formulation of the "Convicted of a felony", it was the opposite of the first sample done so necessary changes needed to be made on the signs. Doing the z-test was pretty straightforward given the skeleton and the explanantion done in class.

The chi-squared test was also straightforward based on the first example. To explain how to understand the chi-squared statistic computed and how it relates to the null hypothesis, I did further reading online about the chi-squared test and how to read and interpret the table.

## Assignment 4
For this CitiBike assignment, I mostly worked on my own while following the skeleton notebook from Professor Bianco.

Getting the hour of the day was the same as what we did back in the UCSL for the CitiBike challenge. I split day and night as such so that there would be an equal 12-hour split. After that, it was simply up to the scipy packages to run the tests.

For the Manhattan-Brooklyn ridership, I used an online reference to get the min/max longitude and latitude of the boroughs from the GeoJSON file downloaded from NYC Planning's Open Data website. Working with shapefiles and GeoJSON files from other classes allowed me to see the format of these files and also utilizing knowledge from our previous homework of reading JSON files.

---
## Assignment 2: Literature choices of statistical tests
| Statistical Analyses | IV(s) | IV type(s) | DV(s) | DV type(s) | Control Variable | Control Variable Type | Question to be answered | *H0* | alpha | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ANCOVA  | 1, type of game played (Brain Age or Tetris) | categorical | 1, the change in scores | continuous | 1, pre-training score | continuous | Does playing brain training games boost the cognitive functions of the player? | Change in *Brain Age* group <= Change in *Tetris* group | 0.05 | [Brain Training Game Boosts Executive Functions, Working Memory and Processing Speed in the Young Adults: A Randomized Controlled Trial](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0055518)
| Correlation | 1, Intra-abnominal pressure (IAP) | continuous | 1, Extracellular water content (ECW) | continuous | 0 | n/a | How strongly does IAP correlate with ECW? | Intra-abnominal pressure (IAP) is not correlated with extracellular water content (ECW) | 0.05 | [Intra-Abdominal Pressure Correlates with Extracellular Water Content](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0122193)
| Logistic Regression | 1, community size | continuous | 1, absence/presence of critical scalar stress | dichotomous | 0 | n/a | What is the probability that a group experienced critical scalar stress? | Lower probabilities of experiencing a critical level of scalar stress are associated with smaller group sizes and higher probabilities with larger group sizes | 0.05 | [Modeling Group Size and Scalar Stress by Logistic Regression from an Archaeological Perspective](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0091510)