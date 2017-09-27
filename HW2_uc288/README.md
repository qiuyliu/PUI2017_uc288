# Homework 2 - uc288

## Assignment 1
For this assignment, I got the MTA API key through the request page and created an environmental variable on my local machine for ease-of-use. 

Once I got the API key, I went through the API documentation for the MTA Bus [VehicleMonitoring](http://bustime.mta.info/wiki/Developers/SIRIVehicleMonitoring). 

Found that the needed parameters are the following:
* key - the MTA API key
* LineRef - the Bus Line
* VehicleMonitoringDetailLevel - set this to `calls` to know the next stops

Based the JSON file reading on the sample scripts available from the lab.

To understand the JSON file, I used an online JSON formatter ([www.jsonformatter.org](http://www.jsonformatter.org)) to view the response from running the URL in a browser. Switched to the `Tree` view after formatting it.

The `VehicleActivity` contains all the buses running in that route.
In that, the `VehicleLocation` contains the longitude and the latitude which is needed to print the information.

**Additional error handling done:**
I wanted to test out how the script would work when the parameters passed were not in the right order so I added more try except statements. I also entered an invalid bus route and got another `KeyError` so I added that as well.

#### Work distribution
I worked on my code alone using lab examples and Google for Python syntax issues I encountered. I learned that when working with long strings, the concatenating symbol `+` should never be at the end of the line or it will cause a syntax error.

I got the idea of using the online JSON formatter for huge data structures from back when I was still working as a front-end developer.

I also helped **Yu Chen** with some of the syntax error she was having in Python.

## Assignment 2
Working with what was already built from the first assignment, the next stop information is available under `OnwardCalls`. It has an additional key `OnwardCall` which is an array of the next stops. `StopPointName` holds the stop name and based on the sample response, the stop status is in `PresentableDistance`.

To test the "no next stop" scenario, I saved the JSON into a file and deleted the object `OnwardCall` to see what would happen. It gave a `KeyError` so I used the try-except code block to catch it and handle the scenario. I did it this way since it would be difficult to keep running the API and wait for a case wherein a bus was at its last stop. It is an assumption and I have not fully tested it on the actual data from the API.

#### Work distribution
I worked on the code alone using lab examples on how to read and write CSV files.

For the `KeyError` idea, it was discussed in class on how to use the try-except to handle the error. My work experience also helped me in knowing how to remove an element in the JSON object to help with testing. Shared this idea to **Baiyue Cao** and also **Nina Nurrahmawati**.

## Assignment 3
To find the data to be used, I went to the [CUSP Data Catalog](https://datahub.cusp.nyu.edu/data-catalog) and chose the data from there.

For the Pandas data manipulation, based the work on the lab done in class. Plotting code is similar to the previous homework done.

#### Work distribution
**Help received:**
* Going to the CUSP Data Catalog and clicking the link in that page did not work. **Rebecca Scheidegger** suggested to go through the Quick Links and check the Urban Profiler.

**Help provided:**
* Assisted **Yu Chen** with her table dropping and syntax issues.
* Helped **Dana Chermesh** with her extra credit homework for handling the date conversion in her code.
