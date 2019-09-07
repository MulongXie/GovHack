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

def generateCrash(Filename):
    df = pd.read_csv('ACT_Road_Crash_Data.csv')
    df = df[['CRASH_DATE', 'LONGITUDE', 'LATITUDE', 'CRASH_SEVERITY']]
    df['Year'] = pd.to_datetime(df['CRASH_DATE']).dt.year
    df.to_json(Filename+'.json')


generateCrash('/Users/shi/PycharmProjects/GovHack/ACT_Road_Crash_Data.csv')

