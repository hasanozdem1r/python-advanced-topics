"""
This script is created to teach fundamental of Pandas library.
Hasan Özdemir 01/14/2022
"""
import pandas as pd

draw_star = lambda: print(50 * "*")

# Reading data files
chase_bank = pd.read_csv("datasets/chase_bank.csv")
dataset_cols = list(chase_bank.columns)

# groupwise analysis
#  We can replicate what value_counts() does by doing the following:
print(chase_bank.groupby("2014 Deposits")["2014 Deposits"].count())
draw_star()

# Another groupby() method worth mentioning is agg(),
# which lets you run a bunch of different functions on your DataFrame simultaneously.
print(chase_bank.groupby(["City"])["2014 Deposits"].agg([len, min, max]))
draw_star()

# Sorting
# chase_bank.sort_values('len')
# chase_bank.sort_index('len')
