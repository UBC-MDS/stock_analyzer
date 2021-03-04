from stock_analyzer import __version__
from stock_analyzer import stock_analyzer
from pytest import raises
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_SummaryStats():

    # Wrong type of input
    data_1 = "wrong input type"
    with raises(ValueError) as execinfo_1:
        stock_analyzer.summaryStats(data_1)
    assert (
        str(execinfo_1.value)
        == "Your input data cannot be converted to a pandas dataframe."
    )

    # measurement not in column names
    data_2 = pd.DataFrame(
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
    with raises(ValueError) as execinfo_2:
        stock_analyzer.summaryStats(data_2, measurements=["High"])
    assert (
        str(execinfo_2.value)
        == "Your specified measurement 'High' is not a column name of the data. Please double check the column names in data."
    )

    # Test output
    data_3 = pd.DataFrame(
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

    df_summaryStats = stock_analyzer.summaryStats(data_3, measurements=["1", "2"])

    assert type(df_summaryStats) == type(pd.DataFrame())
    assert len(df_summaryStats) == 2


def test_movingAverage():
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


test_SummaryStats()
test_movingAverage()