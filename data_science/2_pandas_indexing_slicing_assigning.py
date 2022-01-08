"""
This script is created to teach fundamental of Pandas library.
Hasan Özdemir 01/08/2022
"""

import pandas as pd

draw_star = lambda: print(50 * "*")

# Reading data files
df_farmers = pd.read_csv('datasets/farmers_markets_from_usda.csv')
dataset_cols = list(df_farmers.columns)

# accessing by columns
print(df_farmers[dataset_cols[0]])  # 1st way
print(df_farmers.Facebook)  # 2nd way
draw_star()
# accessing first data of column
print(df_farmers[dataset_cols[3]][0])
draw_star()
# Index-based selection
"""Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its 
numerical position in the data. """
print(df_farmers.iloc[1])

draw_star()

"""Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, 
which is column-first, row-second. This means that it's marginally easier to retrieve rows, and marginally harder to 
get retrieve columns. To get a column with iloc, we can do the following """
print(df_farmers.iloc[:, 0])
draw_star()
# just take 3 of them
print(df_farmers.iloc[:3, 0])
draw_star()
# Label-based selection
"""
The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. In 
this paradigm, it's the data index value, not its position, which matters. 
"""
print(df_farmers.loc[0, "FMID"])
draw_star()
"""
iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the 
dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast, 
uses the information in the indices to do its work 
"""
# Manipulating the index
"""
Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. 
We can manipulate the index in any way we see fit.
"""
# The set_index() method can be used to do the job.
df_farmers.set_index("FMID")
print('Successfully index is set')
draw_star()
# Conditional Selection
print(df_farmers.FMID == 1018261)  # 1st way
draw_star()
print(df_farmers.loc[df_farmers.FMID == 1018261])  # 2nd way
draw_star()
# Conditional multiple selection with AND / OR operator
# AND operation
print(df_farmers.loc[(df_farmers.FMID == 1018261) & (df_farmers.MarketName == "Stearns Homestead Farmers' Market")])
# OR operation
print(df_farmers.loc[(df_farmers.FMID == 1018261) | (df_farmers.MarketName == "Stearns Homestead Farmers' Market")])
draw_star()
"""
The isin built-in selector is lets you select data whose value "is in" a list of values.
"""
print(df_farmers.loc[df_farmers.FMID.isin([1018261, 1004686, 1004767])])
draw_star()

"""
The second built-in is isnull (and its companion notnull). 
These methods let you highlight values which are (or are not) empty (NaN). 
"""
print(df_farmers.loc[df_farmers.FMID.notnull()])
draw_star()