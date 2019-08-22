import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import uszipcode as usz

data = pd.read_csv("green_tripdata_2015-09.csv")

"""Question 1"""
print("*** Question 1 ***\n")
#(1494926, 21)
print ("This data has the dimensions of ", data.shape,'\n')
#Find which factors' columns are sparsely filled or completely empty
print ("Number of null values for each factor:")
print (pd.isnull(data).sum(),'\n')
#Find the number of trips with a trip distance of zero
stationary_trips = len(data.index) - (data[["Trip_distance"]].astype(bool).sum(axis=0))
print ("Trips of zero distance = ", int(stationary_trips),'\n') #20,592

"""Question 2"""
print("*** Question 2 ***\n")
#print (data.info())
#print (data.describe())
#Cluster starting locations of trips to find pickup hubs
kmeans = KMeans(n_clusters=4).fit(data[['Pickup_latitude','Pickup_longitude']])
centroids = kmeans.cluster_centers_
search = usz.SearchEngine()
print ("Starting location hubs based on latitude and longitude")
print (centroids,'\n')
#Convert coordinates into zip codes
point1 = search.by_coordinates(centroids[0][0],centroids[0][1], radius=1)
point2 = (search.by_coordinates(centroids[2][0],centroids[2][1], radius=1))
point3 = (search.by_coordinates(centroids[3][0],centroids[3][1], radius=1))
print(point1,'\n',point2,'\n',point3,'\n\n')
print ('Three points where many customers request taxi pickups (within a mile): New York (10035), Brooklyn (11205), and'
       ' Elmhurst (11373)\n\n')
#Trip length histogram
hist = data.hist("Trip_distance", bins=[0.001,1,2,3,4,5,6,7,8,9,10,11])
plt.title("Green Taxi September 2015 Trip Lengths (#2)")
plt.xlabel("Trip distance (miles)")
plt.ylabel("Number of trips")
plt.show()

"""Question 3"""

print("*** Question 3 ***\n")
#Group data by hour and separate continuous and discrete factors for cleaner data and graphs
data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
sub_data_continuous = data[['lpep_pickup_datetime', 'Trip_distance', 'Fare_amount', 'Tip_amount']]
hourly_data_continuous = sub_data_continuous.groupby(sub_data_continuous['lpep_pickup_datetime'].dt.hour)
sub_data_discrete = data[['lpep_pickup_datetime', 'Payment_type']]
hourly_data_discrete = sub_data_discrete.groupby(sub_data_discrete['lpep_pickup_datetime'].dt.hour)
print ("Trips grouped by hour and separated by continuous and discrete factors:\n")
print (hourly_data_continuous.mean(), '\n\n')
print (hourly_data_discrete.describe(),'\n\n')

"""Question 4"""
print("*** Question 4 ***\n")
#Sort tip averages by different factors
print ("Tip averages sorted by different factors\n")
trip_type_data = data[['Tip_amount']].groupby(data['Trip_type '])
print (trip_type_data.mean(),'\n')
payment_type_data = data[['Tip_amount']].groupby(data['Payment_type'])
print (payment_type_data.mean(),'\n')
rate_code_data = data[['Tip_amount']].groupby(data['RateCodeID'])
print (rate_code_data.mean(),'\n')

print("Street-hail taxis receive a $0.30 higher tip than Dispatch taxis on average per trip.\n")
print("Customers paying with credit cards pay a $2.63 higher tip than cash-paying customers on average per trip.\n")
print("Customers going to Newark, Nassau, or Westchester tip the best at over $5 per trip. "
      "Customers going to JFK tip next best at about $4 per trip.\n"
      "Customers with a standard rate or negotiated fare tip about $1 per trip.\n")
#Sort tip averages by a combination of these factors
discrete_data = data.groupby(['RateCodeID', 'Payment_type', 'Trip_type '])['Tip_amount'].mean()
discrete_data_dataframe = discrete_data.reset_index()
sorted_data = discrete_data_dataframe.sort_values(by='Tip_amount', ascending=False)
print ("Tip averages sorted by a combination of factors:\n")
print (sorted_data, '\n')
print ("The highest tips come from customers paying by credit card, street-hailing taxis, and going to Newark, JFK, "
       "or Nassau.\n")

"""Question 5 (Graphs)"""
print ('*** Question 5 ***')
#3D scatter plot to map starting locations and tip ranges
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = data[['Pickup_latitude']]
y = data[['Pickup_longitude']]
z = data[['Trip_distance']]
ax.scatter(x, y, z, c='r', marker='o')
ax.set_title('Trip distance based on starting location (#5)')
ax.set_xlabel('Starting Latitude')
ax.set_ylabel('Starting Longitude')
ax.set_zlabel('Trip_distance')
#ax.set_xlim3d(38, 42)
#ax.set_ylim3d(-75, -72)
ax.set_zlim3d(0.001, 100)
plt.show()

#Trend line graphs for #3
plt.plot(range(24), 'Trip_distance', data=hourly_data_continuous.mean(), marker='o', color='skyblue', linewidth=2)
plt.plot(range(24), 'Fare_amount', data=hourly_data_continuous.mean(), marker='o', color='olive', linewidth=2)
plt.plot(range(24), 'Tip_amount', data=hourly_data_continuous.mean(), marker='o', color='red', linewidth=2,)
plt.title("Averages by Hour Across All Days (#3)")
plt.xlabel("Time of Departure by Hour (AM-PM)")
plt.legend()
plt.show()

plt.plot(range(24), 'Payment_type', data=hourly_data_discrete.median(), color='purple', linewidth=2)
plt.title("Median Payment_type by Hour (#3)")
plt.xlabel("Time by Hour (AM-PM)")
plt.ylabel("Payment_type (1=credit, 2=cash)")
plt.show()

#Scatter plot to visualize one factor (rate code ID) from #4
data.plot(x='RateCodeID', y='Tip_amount', style='o')
plt.title("Tip Amounts based on rateCodeID (#4)")
plt.xlim(0,7)
plt.xlabel("Rate Code IDs")
plt.ylabel("Tip_amount")
plt.show()