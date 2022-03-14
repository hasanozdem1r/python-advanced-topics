"""
This script is created to teach fundamental of Pandas library.
Hasan Özdemir 01/08/2022
"""

# import library
import pandas as pd

# creating data -> There are two core objects in pandas: the DataFrame and the Series.
"""
A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. 
Each entry corresponds to a row (or record) and a column.
"""
df_obj = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
print(df_obj)

df_obj2 = pd.DataFrame(
    {"Bob": ["I liked it.", "It was awful."], "Sue": ["Pretty good.", "Bland."]}
)
print(df_obj2)

indexed_df = pd.DataFrame(
    {"Bob": ["I liked it.", "It was awful."], "Sue": ["Pretty good.", "Bland."]},
    index=["Product A", "Product B"],
)
print(indexed_df)

"""
A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. 
And in fact you can create one with nothing more than a list
"""
ser_obj = pd.Series([1, 2, 3, 4, 5])
print(ser_obj)

indexed_ser = pd.Series(
    [30, 35, 40], index=["2015 Sales", "2016 Sales", "2017 Sales"], name="Product A"
)
print(indexed_ser)

# Reading data files
df_farmers = pd.read_csv("datasets/farmers_markets_from_usda.csv")
# print(df_farmers)

# We can use the shape attribute to check how large the resulting DataFrame is
print(df_farmers.shape)

# to observe data from top we can use df.head()
print(df_farmers.head())  # -> df.tail() from bottom
