# HW1_uc288

## Assignment 1 - Finish Lab
GitHub Repository: [https://github.com/unissechua/gittest_uc288](https://github.com/unissechua/gittest_uc288)

For completing the lab, I paired up with Nina Nurrahmawati (nn1221) to complete the fork and merge with a pull request.

Afterwards, Christian Moscardi (clm633) was looking for partner to complete the fork and merge portion so I did that again with him.

## Assignment 2 - Setting up the environment
For setting up the environment variable and alias, I was able to complete the steps on my own.

Screenshots:
#### .bash_profile
![.bash_profile screenshot](/screenshots/bash_profile.png)

#### Testing the alias
![Terminal screenshot](/screenshots/env_variable.png)

## Assignment 3 - Reproducible Research
### Work balance
* For the random seed, I read docs and answers to questions on StackOverflow on how it works.
* For the generation of the random numbers for ReprRand, I based it on the numpy docs and the expected shape of the solution as a guide.
* For generating the 50 additional arrays, I got the idea of using `numpy.random.randint()` from **Rachel Lim** where she added that to her arrays. I used the formula in the docs to use the same function for `sigma` and `mu`.
* To get an idea of the 'expected' plot, **Shreya, Alex and Ruben** were discussing their results in our group chat and we tried to work in getting a similar looking plot..
* **Rachel** and I were wondering which values were supposed to be on the X-axis and the Y-axis and she figured out that using `ReprRandAll[i,0]` and `ReprRandAll[i,1]` will be the X and Y axis, respectively.
* For the plot, **Rachel** initially used `'ro'` for the color and style and asked how I got different colors so I explained that the `r` stands for red and the `o` stands for circle, so she can simply use `'o'` to allow the plot to use different colors. Later on, Baiyue also had the same question.
* For the challenge, based on the existing knowledge on which data need to be manipulated, I simply created one random variable to be the mean for X and another for the mean of Y and added that to each array.

