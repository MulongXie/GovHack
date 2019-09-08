import pandas as pd


def searchPop(start,end):
    df = pd.read_json('D:\git_file\github\doing\GovHack\Back-end\GovHack\population.json')
    df = df[(df['Year']>=start) & (df['Year'] <=end)]

    result = df.to_json(orient='records')
    return result


def searchCrash(start,end):
    df = pd.read_json('D:\git_file\github\doing\GovHack\Back-end\GovHack\crash.json')
    df = df[(df['Year'] >= start) & (df['Year'] <= end)]
    df = df.sort_values(by='Year')
    result = df.to_json(orient='records')
    return result


def searchBus():
    df = pd.read_json('D:\git_file\github\doing\GovHack\Back-end\GovHack\\bus.json')
    result = df.to_json(orient='records')
    return result


def searchHousing(start,end):
    df = pd.read_json('D:\git_file\github\doing\GovHack\Back-end\GovHack\housing.json')
    df = df[(df['Year'] >= start) & (df['Year'] <= end)]
    df.sort_values(by='Year')
    result = df.to_json(orient='records')
    return result