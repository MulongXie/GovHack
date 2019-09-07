import pandas as pd
import numpy as np
import json


def generate(Filename):
    df = pd.read_csv(Filename)
    df['Year'] = pd.to_datetime(df['Year']).dt.year
    df['Female'] = df.loc[:, df.columns[2:88]].sum(axis=1)
    df['Male'] = df.loc[:, df.columns[88:-1]].sum(axis=1)
    df['Population'] = df.loc[:, ['Female', 'Male']].sum(axis=1)

    df2 = df[['Year', 'Suburb', 'Female', 'Male', 'Population']]
    df2['Suburb'] = df2['Suburb'].str.replace(" ", "")

    df2.to_json(Filename+'.json')


generate('ACT_Population_Projections_by_Suburb__2015_-_2020_.csv')

