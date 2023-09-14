from script import *
import pandas as pd


def test_describe():
    df, naninfo, db = describe()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2341, 13)

    assert naninfo.shape[0] == 13

    for sta in ["count", "mean", "std", "max", "50%", "min"]:
        assert sta in db.columns


def test_plot():
    path = "./World University Rankings 2023.csv"
    df = loadData(path)
    df = plotData(df)
    assert df.isna().sum()["International Student"] == 1
    assert sum(df.isna().sum()) == 1


test_describe()
test_plot()
