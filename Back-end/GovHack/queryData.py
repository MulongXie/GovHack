import pandas as pd

def search(start,end):
    df = pd.read_json('D:\git_file\github\doing\GovHack\Back-end\GovHack\ACT_Population_Projections_by_Suburb__2015_-_2020_.csv.json')
    df = df[(df['Year']>=start) & (df['Year'] <=end)]

    result = df.to_json(orient='records')
    return result

def searchCrash(start,end):
    df = pd.read_json('D:\git_file\github\doing\GovHack\Back-end\GovHack\ACT_Road_Crash_Data.csv.json')
    df = df[(df['Year'] >= start) & (df['Year'] <= end)]
    result = df.to_json(orient='records')
    return result

