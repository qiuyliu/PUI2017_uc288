# HW6_uc288

## Building Energy Consumption Linear Regression Exercise

Help received to complete homework:
* **Rachel Lim Xin Rong** helped me understand how to use log properly in the regression. I was getting NaN for my R-squared initially due to syntax error.
* **Rachel Lim Xin Rong** also shared the hint that we can use the CSV from NYC City Planning for the PLUTO data. She got this from **Gaurav Bhardwaj**.
* Everything else was based on understanding the skeleton notebook from Professor Bianco.

Help given:
I shared my code to download the data needed to **Rachel Lim Xin Rong** and **Yu Chen**.

What I did:
1. To make the work reproducible, I tried doing `curl` commands on the terminal first to test how it would work and coded it up after.
2. When I reran the code with the `curl` commands, the LL84 data from OpenData was not downloading properly and was throwing an SSL Connect Error so I switched to using `wget` instead.
3. Initially used the API link from OpenData and noticed the data given to me was smaller than the whole file so I switched to using the download link instead.
4. Renamed columns after choosing them for easier coding after.
5. Used the same threshold as Professor Bianco for cutting the data but used boolean selectors instead of multiplying.
6. Had trouble understanding the math behind the log propagation, but following the formula's provided by Professor Bianco, I tried to explain why she used those formulas/equations.
7. Computed for the Likelihood Ratio as we did in the class/lab session.
