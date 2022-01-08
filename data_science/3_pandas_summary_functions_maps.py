"""
This script is created to teach fundamental of Pandas library.
Hasan Özdemir 01/08/2022
"""
import pandas as pd

draw_star = lambda: print(50 * "*")

# Reading data from csv
df_farmers = pd.read_csv('datasets/farmers_markets_from_usda.csv')

# Summary functions
# Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way.
"""
The describe() method generates a high-level summary of the attributes of the given column.
The output above only makes sense for numerical data
"""
print(df_farmers.describe())
draw_star()
#  to see the mean of the points allotted (e.g. how well an averagely rated wine does), we can use the mean() function
print(df_farmers.x.mean())
draw_star()

# To see a list of unique values we can use the unique() function:
print(df_farmers.x.unique())
draw_star()

# To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method
print(df_farmers.x.value_counts())
draw_star()

# MAPS
"""
A map is a term, borrowed from mathematics, for a function that takes
one set of values and "maps" them to another set of values
In data science we often have a need for creating new representations from existing data, 
or for transforming data from the format it is in now to the format that we want it to be in later.
"""
df_x_mean=df_farmers.x.mean()
print(df_farmers.x.map(lambda p:p-df_x_mean))
draw_star()
