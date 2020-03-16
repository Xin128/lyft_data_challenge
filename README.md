##                                                Lyft Data Challenge

Lyft Data Challenge 2019
Team: GirlsWhoCode Xin Hao Erin Liu
Sep 15, 2019

### Proposal for Lyft Data Challenge 2019
In this Lyft Data Challenge, we explored and analyzed the given dataset of drivers, rides and event timestamps. We’ve built our statistical models, tested given data, analyzed based on visualization and given our business recommendation.

### PART ONE: Introduction
After exploring the three given datasets, we had the following findings:
As we define a driver’s lifetime value as related to his career length, average rides and profit, we find that average distance, responding time, arrival time, standard deviation of earnings and proportions of night-time rides and weekday rides greatly contribute to a driver’s lifetime value.

### Our assumptions:
We are making the following assumptions regarding this data challenge:
1. We set the time of the most recent ride in the dataset we’re given (2016-06-26 23:57:45) as the “current time”.
2. Any Lyft driver who hasn’t finished a ride within the 10 days from now is considered inactive. We know a 10-day break may be possible and even common for drivers, but considering the limited data we have and our need for training data to predict drivers’ lifetime with Lyft, we’re making this somehow bold assumption.
3. We don’t know how much profit a ride provides to Lyft . So we are generalizing the fares of rides to represent both the profit drivers made and the profit Lyft got. We believe this assumption is fair because the actual values of drivers’ and Lyft’s earnings are proportional to drive’s fares.
4. With base fare and service fee, each ride is priced directly proportional to its distance and duration. We priced ride sections during prime time 25% higher.
Data Cleaning
We began the data challenge by regular data cleaning, ignoring rides that have missing information (eg. driver’s on-board date or drive’s accepted time) and wrong information (eg. ride accepted time is before ride requested time). We then group the three files together into a drive-centered dataset (data_all_combined.py), containing each drive’s driver id, event types information, drive distance (meter), and drive duration (second). This file contains information of 148639 drives & 837 drivers and is our essential exploring target.

### PART TWO:
Main Factors of Drivers’ Lifetime Value (Response to 2.a)
We have proposed, explored, and analyzed the following factors (main factors are colored in blue);
1) Basic Info of drivers:
  a) average speed ;
  b) average distance;
  c) Total ride durations;

2) Profit & Earnings:
  a) standard deviation of profits per day

3) Time slot of main rides:
  a) average duration per ride; 
  b) average responding time per ride;
  c) average arrival time per ride;
  d) average waiting time per ride;

4) Duration for rides: 
  a) proportions: 9 am to 5 pm rides;
  b) proportions: 10 pm to 6 am;
  c) proportions: 8 pm to 10 pm;
  d) proportions: weekdays;


1.a ​Average Speed
The average speed of drivers are distributed more sparsely than other factors, ranging from 4 m/s to 15 m/s. This leads to our assumption that Lyft drivers tend to drive in local and downtown area instead of suburban district. Yet the average speed does not affect a driver’s career length too much overall.

1.b ​Average Distance
The average distance centers at 3 to 6 miles per ride. The average distance of drivers with short career length take clusters between 2 to 5. Generally, the drivers with average distance/ride over 8 miles do not have a consistently higher lifetime value, which is consistent with the pricing of Lyft and our definition of lifetime value. Based on our visualization and analysis of data, drivers with higher lifetime value prefer to accept drives with less than 5 miles. Due to pricing with the service fee and base fare, this corresponds with the drivers’ general preferences.

1.c ​Total Ride Duration
There exists an approximately linear relationship between total ride duration and a drivers’ lifetime value, which is expected since our lifetime value is based on a driver’s career length, which is closely related with his total ride duration.

2.a. ​Standard Deviation of Profits per day
The average standard deviation of a drivers’ earning per drive is approximately 9, higher than our expectation. We found an exponential growth of a driver’s standard deviation of his earnings per day when it’s less than 10. This result lead us to conclude that a driver with higher lifetime value would ride with various distances, time span and duration. 3.a ​Average Duration per ride
The average ride duration mainly clusters between 11 mins - 18 mins. We found that the drivers whose lifetime value is higher than 6000 mainly have drive length between 12 mins and 17 mins. Overall, the drivers’ lifetime value increases linearly with the increase in their average duration per ride.
3.b ​ Average Responding time
The average responding time is the time difference between the time a passenger requests the drive and the time the driver responds. This variable indicates the responsiveness and the activitiveness of a Lyft driver. We found that the drivers with higher lifetime value tends to respond in shorter time. There exists an inverse relationship between the responding time and lifetime value. Drivers whose average responding time less than 100s have no less than 4000 lifetime value. They also tend to have longer career lengths, indicating that the longer Lyft drivers have worked, the more sophisticated they are, and the faster they will respond to nearby requests. Interestingly, drivers whose responding time is over 500s have approximately less than 4000 lifetime value.

3.c ​Average arrival time per ride
The average arrival time is the time that a driver takes to arrive at appointed location after accepting the request. It’s highly correlated to the quality of a Lyft driver. Similar to responding time, there’s an inverse linear relationship between a driver’s lifetime value and its arrival time. Based on our calculation, drivers with arrival time less than 150s have an average lifetime value higher than 7500 and career length longer than 40 days. This proves that shortening drivers’ arrival time can potentially increase their lifetime value.

3.d ​Average waiting time
The average waiting time indicates how long it takes a Lyft driver to pick up his passenger after his arrival. As expected, this value depends a lot on the passager’s performance. The average waiting time varies from 3 min to 9 min. After careful analysis, we don’t think that this is a useful indication of the main factors that affect a driver’s lifetime value.

4.a ​Proportion of 9 pm to 5pm rides
This is the proportions of the number of a driver’s rides between 9AM to 5 PM to his all rides, which is their daytime rides. We first found that the average of this proportion clusters at 25% to 50%, which is less than our initial expectation. There does not exist an obvious contribution between the driver’s work time slot and their lifetime value. And we are trying to narrow down the time range in the future.

4.b ​Proportion of 10 pm to 6 am rides
This is the proportion of the number of a driver’s rides between 10PM to 6 PM among all his rides. Expectedly, most drivers’ night time rides are less than 20%. However, drivers with over 20% night time rides have higher lifetime value and others. We believe this is related to the variable prime time, as the demand of night-time rides are generally higher than the supply.
4.c ​Proportions of rides on weekdays
This denotes the proportion of a driver’s rides on weekdays. Over 80% of Lyft drivers have over 75% of rides on weekdays, many of whom also have high lifetime value. The graph also indicates that having more rides on weekends won’t enhance a driver’s lifetime value; and only a small fraction of Lyft drivers mainly work during
weekends.
            
Driver’s Lifetime Prediction (Response to 2.b) Find Inactive Drivers & Build Predicting Models
Under our assumption, we found in total 287 drivers that have already left Lyft. Their average working length at Lyft is ~28 days. We first investigated the relationship between their working length with the following factors by calculating their pearson coefficient: the average number of rides they finish per day; the average profit they earn per ride; their average response time to a ride request; their average arrival time to an accepted request; their average waiting time for the passengers (pick-up time minus arrival time); their average speed during all rides; the proportion of their rides from 10:00pm to 6:00am & 9:00am to 5:00pm & 20:00pm to 22:00pm & on weekend. To start off, we tried multivariate linear regression as it’s in general a good place to start. We used 80% of these drivers’ information regarding the factors in interest to build the model and the remaining 20% to validate and tune the hyperparameters. The result looks only decent, so we then proceeded in trying logistic regression, the random forest model, and finally the decision tree model. Results are summarized as follows:
As shown from the results, the simple linear regression models remains the best. Even though the error is still significant, we decided it’s the best fit for our limited given dataset.
Predict All Drivers’ Career Length with Lyft
After we’ve trained the model, we fed the information of all 837 drivers into the model and got their projected career length with Lyft.

### PART THREE: Driver’s Lifetime Value (Response to 1 & 2.a & 2.c)
Here we propose a formula to calculate a driver’s lifetime value to Lyft:
Lifetime Value = Average Rides / Day * Average Profit / Ride * Projected Career Length
This is essentially calculating the total amount of revenue a driver can make for Lyft throughout his/her entire driving time with Lyft.
With the definition, we easily calculated the lifetime value of all the 837 drivers as well as their pearson coefficient with several factors we thought might be influential.
Except for the three values we used in lifetime value calculation, we also identified responding time, arrival time, profits, proportions of night-time and weekday rides as important factors that influence drivers’ lifetime value due to their strong correlation. To more vividly demonstrate the relationship between these factors, we once again resorted to the table above.

### PART FOUR: Business Side Analysis (Response to 2.d)
Based on our analysis of factors above, we summarize our business proposal as following:
1. Improve responding time & Arrival time
As discussed in Part 2, we found that drivers with smaller responding time and arrival time will generally produce greater lifetime value. We recommend Lyft to improve their responding time with some tips and trainings provided by Lyft. For business proposal, responding time and arrival time is also critical to the passenger’s experience and feelings.
2. Increase the number of drivers for night rides
Since most of the drivers prefer to work during the daytime, night-time drivers generally have higher profits and earnings. We propose that for Lyft, it is more user friendly to explore more night-time drivers, which will increase overall lifetime value for the drivers.
3. Focus on the improvement of short-time rides and local rides
Based on drivers’ average riding duration and distance, we conclude that short-time, low-speed rides and rides in local and downtown area are the major rides for Lyft drivers. For Lyft, it is significant to improve the drivers’ driving experiences for short-time drives, in order for a higher lifetime value, longer career length for drivers, and a better riding experiences for passengers.

### PART FIVE: Summary
We have listed all our essential findings above after exploring the limited given dataset. We believe in the thoroughness of our analysis as we’ve explored a great variety of factors that may affect Lyft drivers’ career length and lifetime value. We’ve also found a good way to demonstrate their correlation by multiple scatter plots and grid of pearson coefficients. Admittedly, our machine learning predictive accuracy isn’t very good, yet it still gave us usable prediction results. If given a bigger dataset covering more information regarding drivers’ background, our model will certainly yield higher precision.
    
