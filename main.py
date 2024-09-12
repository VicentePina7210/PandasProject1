import pandas as pd
import math

df = pd.read_csv('Worldhits.csv')

print(f"The size of our data set: {df.shape}")

# first check the version of pandas
print(pd.__version__)
# We are on version 2.2.2

#First I want to see if the data frame is working properly
print(df.head(1))

#I want to see all the column names
print(f"these are the column names\n {df.columns}")

#lets search for and drop any outliers (songs over 5 minutes (300000 ms))
print(df["Duration"].head())


# Drop any outliers (songs over 6 minutes(360000))
df = df[(df["Duration"] <= 360000 ) & (df["Duration"]>= 60000)]
print("outliers dropped!")
print(df["Duration"].head())


#Learn more about the types of data
df.info()

#drop any null values
new_df = df.dropna()
print("null values dropped!")
print(df.head())



#simple observations
def avg_duration():
    avg_length = new_df["Duration"].mean()
    avg_mins = math.floor((avg_length/ 1000 /60))
    avg_sec = ((avg_length/1000) % 60).round(2)
    print(f"The average length of each song is {avg_mins} min {avg_sec} sec long")
    avg_length = avg_mins + avg_sec


