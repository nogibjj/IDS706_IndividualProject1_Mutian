from lib import loadData, nanInfo, describeData, preprocessData
from lib import (
    plotLocTrend,
    plotStudentLocDistribution,
    plotStudentSalaryDistribution,
    plotLocDistribution,
)


def describe():
    path = "./World University Rankings 2023.csv"
    df = loadData(path)
    naninfo = nanInfo(df)
    print(naninfo)
    db = describeData(df)
    print(db)
    return df, naninfo, db


def plotData(data):
    preprocessData(data)
    plotLocTrend(data)
    plotLocDistribution(data)
    plotStudentLocDistribution(data)
    plotStudentSalaryDistribution(data)
    return data
