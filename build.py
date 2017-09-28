import pandas as pd
import numpy as np


def load_data():
    df = pd.read_csv("~olympics.csv",  skiprows=[1])

    df= df.rename(columns = {'0':'country', '1':'# Summer', '2':'Sum_Gold', '3':'Sum_Silver',
                             '4':'Sum_Bronze', '5': 'Totals', '6':'# Winter', '7':'Win_Gold',
                             '8':'Win_Silver', '9':'Win_Bronze','10': 'Totals',
                             '11':'# Combined', '12':'Com_Gold', '13':'Com_Silver',
                             '14':'Com_Bronze', '15': 'Totals'})

    value = df['country'].str.split('(', expand=True)[0]#Split country name and country code and add
    #country name as data frame index

    df = df.set_index(value)
    df = df.drop('country', axis=1)
    df = df.drop('Totals', axis=1)#Drop the Column Totals
    df = df.drop('Totals')#Drop the row Totals

    return df


def first_country(df):
    df = load_data()
    df = df.head(1)
    return df


def gold_medal(df):
    df = load_data()

    return df.Sum_Gold.argmax().replace(u'\xa0', u' ')


def biggest_difference_in_gold_medal(df):
    df = load_data()
    return (df.Sum_Gold - df.Win_Gold).abs().argmax().replace(u'\xa0', u' ')
#biggest_difference_in_gold_medal to get name of country
#who has biggest difference between their summer and winter gold medal counts.


def get_points(df):
    df = load_data()
    points = np.zeros(len(df))
    points += df.Com_Gold * 3
    points += df.Com_Silver * 2
    points += df.Com_Bronze
    return pd.Series(points, index=df.index).apply(int) #.appy(int) Series from float to integer


df = load_data()
print(first_country(df)["# Summer"])
print(gold_medal(df))
print(biggest_difference_in_gold_medal(df))
print(get_points(df))
