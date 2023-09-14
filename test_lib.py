from lib import *


def test_loadData():
    path = "./World University Rankings 2023.csv"
    df = loadData(path)
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2341, 13)
    return df


def test_nanInfo():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    basicinfo = nanInfo(data)
    print(basicinfo)
    assert basicinfo.shape[0] == 13


def test_describeData():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    db = describeData(data)
    for sta in ["count", "mean", "std", "max", "50%", "min"]:
        assert sta in db.columns


def test_processData():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    preprocessData(data)
    assert data["No of student"].dtype == int
    assert data["Male"].dtype == int
    assert data["Female"].dtype == int
    assert "Female:Male Ratio" not in data.columns


def test_plotLocTrend():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    preprocessData(data)
    plotLocTrend(data)


def test_plotLocDistribution():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    preprocessData(data)
    plotLocDistribution(data)


def test_plotStudentLocDistribution():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    preprocessData(data)
    plotStudentLocDistribution(data)


def test_plotStudentSalaryDistribution():
    path = "./World University Rankings 2023.csv"
    data = loadData(path)
    preprocessData(data)
    plotStudentSalaryDistribution(data)


data = test_loadData()

test_nanInfo()

test_describeData()

test_processData()

test_plotLocTrend()

test_plotLocDistribution()

test_plotStudentLocDistribution()

test_plotStudentSalaryDistribution()
