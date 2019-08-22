# Green-Taxi-DS-Challenge
Data analysis of New York Green Taxi trips from September 2015

This script (DataAnalysis.py) requires the pandas, matplotlib, sklearn, mpl_toolkits, and uszipcode packages to run successfully.  It takes just under 40 seconds to run.  Can be run in 20 seconds if the 3D scatterplot is commented out

Green Taxi September 2015 Data Analysis

(1) There are 1,494926 data points.  Most of the columns have values for all the data points except for trip type that is missing values for 4 data points and Ehail_fee which is a null column for all data points.

(2) I made a histogram to measure how many trips were of each length to show how many of the taxi trips are <= 2 miles (almost 50%).  I also did a standard k-means clustering on the starting latitudes and longitudes to find the hubs where taxis are most likely to pickup customers based on this data.  This gave me three zip codes: New York (10035), Brooklyn (11205), and Elmhurst (11373)

(3) Here I have 2 tables: The first has the average numbers for trip distance, fare amount, and tip amount sorted by hour across all days in the data.  It showed that people on average were consistently tipping just under 10% of the fare and the trip distance at all times is never much more than 4 miles on average.  I also made a table for median payment type by hour to see when people are more likely to pay by credit card vs paying in cash.  I added graphs to visualize these tables in question 5.

(4) I found the average tip amount based on trip type, payment type, and the destination RateCodeID.  After summarizing the tables, I created a table that ranks the tip amount based on a combination of the 3 factors above.  It showed that regardless of the destination ID, the tips were highest on average when customers paid with credit card.  The best trips for taxi drivers to get tips are ones where from customers paying by credit card, street-hailing taxis, and going to Newark, JFK, Nassau, or Westchester.  I made another graph to visualize the RateCodeID effect on the the tip amounts in question 5.


(5A) Anomalies:
There are trips where the distance is 0 miles but the fare is not $0.  If there had been only a few hundred data points with this situation, I would have ignored these data points when doing my analysis.  However, there ended up being 20,592 trips where this happened, which indicated to me that this scenario occurs with reasonable frequency.  Some possible explanations are that this is a taxi’s way of charging someone for damages.  Some of these data points have very small changes in longitude or latitude suggesting that a taxi driver just forgot to start his meter and so the mile counts did not get registered for a trip.  For trips of type 2, this could also be a cost for calling the dispatch for a taxi and then canceling it after the taxi has driven a while to pick the customers up.
All trips that were dispatched (trip_type = 2) had an improvement surcharge = 0.  Since the two columns correlate 100%, we do not necessarily need an entire column for the improvement surcharge and could condition the total cost of a trip based on the trip type instead by just adding $0.30 to any trip of type 1.

(5B) The first graph is a 3D scatterplot to illustrate the starting points for all the trips and the tip range for these starting positions.  The second 2 graphs illustrate the findings from question 3 and show the trend lines for the averages of each value over the course of any day by hour.  The first of these two graphs (3 trend lines) shows that trip distance, fare amount, and tip amount all peak on cabs called between 5-7AM and also rise again slightly around 11PMc for a couple hours.  The second one (1 trend line) shows that customers are more likely to pay with a credit card from 6-10AM and 10-12PM while cash is more likely for the rest of the day.  The final graph is a scatter plot of all the tip amounts based on the destination RateCodeID.  It showed that the range of tips for trips ending in JFK, Nassau, Westchester, and Newark were smaller, although we saw in question 4 that tips on average are highest for these destinations.  The graph also shows less data points for these destinations indicating that there are more people trying to ride at the standard rate or a negotiated fare even if they are tipping less.  Both of the trend line graphs and the histogram from #2 are directed more at the taxi drivers themselves while the 2 scatter plots are more useful for a developer and to possibly extend their analysis on this data.

All in all, my analysis shows green taxi drivers the best places and times to pick up customers and helps them know how much of a tip they will get based on factors such as the destination, the payment type, and the trip type.


P.S. One graph I was having trouble with was mapping the trip routes on an actual geographic map such as google maps using the gmplot package.  That would be one of the ways I would extend this project to have another helpful visualization for taxi drivers
