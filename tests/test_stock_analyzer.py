from stock_analyzer import __version__
from stock_analyzer import stock_analyzer
from pytest import raises
import pandas as pd
import numpy as np
import altair as alt


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

    # Non-numeric data
    data_3 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            ["p", 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(ValueError) as execinfo_3:
        stock_analyzer.summaryStats(data_3, measurements=["e", "2", "3"])
    assert (
        str(execinfo_3.value)
        == "Data in column 'e' of your input data cannot be converted to numeric format."
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

    # normal test
    source = pd.DataFrame(
        data=[
            ['1', 2, 3, 4, 5],
            [1, '2.222222', 3, 4, 5],
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

    # single string test
    data_0 = 'this is a string'
    with raises(ValueError) as execinfo_0:
        stock_analyzer.movingAverage(data_0,3, ["movingAverage"])
    assert (
        str(execinfo_0.value)
        == "Your input data cannot be converted to a pandas dataframe."
    )

    # panda NA test
    data_1 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [pd.NA, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(TypeError) as execinfo_1:
        stock_analyzer.movingAverage(data_1,3, ["movingAverage" + name for name in data_1.columns])
    assert (
        str(execinfo_1.value)
        == "Type of Column e isn't a string or a number "
    )

    # numpy NaN test
    data_2 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [np.NaN, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [np.NaN, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [np.NaN, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(ValueError) as execinfo_2:
        stock_analyzer.movingAverage(data_2,3, ["movingAverage" + name for name in source.columns])
    assert (
        str(execinfo_2.value)
        == "Column e has Nan at [1] [3] [5] "
    )

    # String test
    data_3 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            ["p", 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(ValueError) as execinfo_3:
        stock_analyzer.movingAverage(data_3,3, ["movingAverage" + name for name in source.columns])
    assert (
        str(execinfo_3.value)
        == "Column e can't be converted to floating point"
    )



def test_exponentialSmoothing():
    source = pd.DataFrame(
        data=[
            [1,	2	,3],
            [2,	4	,6],
            [3,	6	,9],
            [4,	8	,12],
            [5,	10,	15]
        ],
        columns=["1", "2", "3" ],
    )
    df_exponentialSmoothing = stock_analyzer.exponentialSmoothing(source,  ["expSmoothing" + name for name in source.columns])
    assert type(df_exponentialSmoothing) == type(pd.DataFrame()),'type_error'
    assert len(df_exponentialSmoothing) == len(source),'shape_error'
    assert df_exponentialSmoothing.columns.to_list()[0] == "expSmoothing1",'naming_error'
    last_row = np.array(df_exponentialSmoothing.iloc[-1])   
    true_value = np.array([3.2269, 6.4538, 9.6807])   
    assert  (abs(last_row - true_value )  < 1e-6).all()  , 'calculation_error'








test_SummaryStats()
test_movingAverage()
test_exponentialSmoothing
test_movingAverage
test_exponentialSmoothing