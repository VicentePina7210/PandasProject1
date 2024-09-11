import pandas as pd
import math

df = pd.read_csv('Worldhits.csv')

df.shape

# first check the version of pandas
print(pd.__version__)
# We are on version 2.2.2

#First I want to see if the data frame is working properly
print(df.head())

#I want to see all the column names
print(f"these are the column names\n {df.columns}")

#lets search for and drop any outliers (songs over 5 minutes (300000 ms))
print(df["Duration"].head(9))

for x in df.index:
    if df.loc[x, "Duration"] > 300000:
        df.drop(x, "Duration")

#Learn more about the types of data
print(df.info())

#drop any null values
new_df = df.dropna()
print(new_df.info())



#simple observations
# avg_length = new_df["Duration"].mean()
# avg_mins = math.floor((avg_length/ 1000 /60))
# avg_sec = ((avg_length/1000) % 60).round(2)
# print(f"The average length of each song is {avg_mins} min {avg_sec} sec long")
# avg_length = avg_mins + avg_sec


