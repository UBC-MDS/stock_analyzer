from stock_analyzer import __version__
from stock_analyzer import stock_analyzer
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_SummaryStats():

    # Wrong type of input
    data_1 = "wrong input"

    source = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["1", "2", "3", "4", "5"],
    )
    df_movingAverage = stock_analyzer.movingAverage(
        source, 3, ["movingAverage" + name for name in source.columns]
    )

    assert type(df_movingAverage) == type(pd.DataFrame())
    assert len(df_movingAverage) == len(source)
    assert df_movingAverage.columns.to_list()[0] == "movingAverage1"
    assert list(df_movingAverage["movingAverage1"].values) == [1, 1, 1, 1, 1, 1, 1, 1]


def testMovingAverage():
    source = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["1", "2", "3", "4", "5"],
    )
    df_movingAverage = stock_analyzer.movingAverage(
        source, 3, ["movingAverage" + name for name in source.columns]
    )

    assert type(df_movingAverage) == type(pd.DataFrame())
    assert len(df_movingAverage) == len(source)
    assert df_movingAverage.columns.to_list()[0] == "movingAverage1"
    assert list(df_movingAverage["movingAverage1"].values) == [1, 1, 1, 1, 1, 1, 1, 1]


testMovingAverage()