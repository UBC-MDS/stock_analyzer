from stock_analyzer import stock_analyzer
from pytest import raises
import pandas as pd
import numpy as np

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
        == "Your specified measurement 'High' is not a column name of the data. \
            Please double check the column names in data."
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
        == "Data in column 'e' of your input data cannot be converted to \
            numeric format."
    )

    # pandas NA test
    data_4 = pd.DataFrame(
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
        columns=["1", "2", "3", "4", "5"],
    )

    df_summaryStats_4 = stock_analyzer.summaryStats(data_4, measurements=["1", "5"])

    assert type(df_summaryStats_4) == type(pd.DataFrame())
    assert len(df_summaryStats_4) == 2
    output_4 = pd.DataFrame(
        data=[
            ["1", 1.0, 1.0, 1.0, 0.0, 0.0],
            ["5", 5.0, 5.0, 5.0, 0.0, 0.0],
        ],
        columns=["measurement", "mean", "min", "max", "volatility", "return"],
    )
    assert df_summaryStats_4.equals(output_4)

    # numpy Nan test
    data_5 = pd.DataFrame(
        data=[
            [1, np.nan, 3, 4, 5],
            [np.nan, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["1", "2", "3", "4", "5"],
    )

    df_summaryStats_5 = stock_analyzer.summaryStats(data_5, measurements=["1", "2"])

    assert type(df_summaryStats_5) == type(pd.DataFrame())
    assert len(df_summaryStats_5) == 2
    output_5 = pd.DataFrame(
        data=[
            ["1", 1.0, 1.0, 1.0, 0.0, 0.0],
            ["2", 2.0, 2.0, 2.0, 0.0, np.nan],
        ],
        columns=["measurement", "mean", "min", "max", "volatility", "return"],
    )
    assert df_summaryStats_5.equals(output_5)

    # normal test
    data_6 = pd.DataFrame(
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

    df_summaryStats = stock_analyzer.summaryStats(
        data_6, measurements=["1", "2"])

    assert isinstance(df_summaryStats, type(pd.DataFrame()))
    assert len(df_summaryStats) == 2


def test_movingAverage():

    # normal test
    source = pd.DataFrame(
        data=[
            ["1", 2, 3, 4, 5],
            [1, "2.222222", 3, 4, 5],
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

    assert isinstance(df_movingAverage, type(pd.DataFrame()))
    assert len(df_movingAverage) == len(source)
    assert df_movingAverage.columns.to_list()[0] == "movingAverage1"
    assert list(df_movingAverage["movingAverage1"].values) == [
        1, 1, 1, 1, 1, 1, 1, 1]

    # single string test
    data_0 = "this is a string"
    with raises(ValueError) as execinfo_0:
        stock_analyzer.movingAverage(data_0, 3, ["movingAverage"])
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
        stock_analyzer.movingAverage(
            data_1, 3, ["movingAverage" + name for name in data_1.columns]
        )
    assert str(execinfo_1.value) == "Type of Column e isn't a string \
        or a number "

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
        stock_analyzer.movingAverage(
            data_2, 3, ["movingAverage" + name for name in source.columns]
        )
    assert str(execinfo_2.value) == "Column e has Nan at [1] [3] [5] "

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
        stock_analyzer.movingAverage(
            data_3, 3, ["movingAverage" + name for name in source.columns]
        )
    assert str(
        execinfo_3.value) == "Column e can't be converted to floating point"


def test_exponentialSmoothing():
    source = pd.DataFrame(
        data=[[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12], [5, 10, 15]],
        columns=["1", "2", "3"],
    )
    df_exponentialSmoothing = stock_analyzer.exponentialSmoothing(
        source, ["expSmoothing" + name for name in source.columns])
    assert isinstance(
        df_exponentialSmoothing, type(
            pd.DataFrame())), "type_error"
    assert len(df_exponentialSmoothing) == len(source), "shape_error"
    assert (df_exponentialSmoothing.columns.to_list()
            [0] == "expSmoothing1"), "naming_error"

    last_row = np.array(df_exponentialSmoothing.iloc[-1])
    true_value = np.array([3.2269, 6.4538, 9.6807])
    assert (abs(last_row - true_value) < 1e-6).all(), "calculation_error"

    with raises(ValueError) as execinfo_0:
        stock_analyzer.exponentialSmoothing(
            'not a dataframe', [
                "expSmoothing" + name for name in source.columns])
    assert (str(execinfo_0.value)
            == "Your input data cannot be converted to a pandas dataframe.")


    # panda NA test
    data_1 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [pd.NA, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(TypeError) as execinfo_1:
        stock_analyzer.exponentialSmoothing(
            data_1, [name for name in data_1.columns])
    assert str(execinfo_1.value) == "Type of Column e isn't a string \
        or a number "

    # numpy NaN test
    data_2 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [np.NaN, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [np.NaN, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(ValueError) as execinfo_2:
        stock_analyzer.exponentialSmoothing(
            data_2, [name for name in source.columns])
    assert str(execinfo_2.value) == "Column e has Nan at [1] [3] "

    # String test
    data_3 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            ["p", 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        columns=["e", "2", "3", "4", "5"],
    )
    with raises(ValueError) as execinfo_3:
        stock_analyzer.exponentialSmoothing(data_3, [name for name in source.columns])
    assert str(execinfo_3.value) == "Column e can't be converted to floating point"

    # wrong alpha value tests
    with raises(ValueError) as execinfo_4:
        stock_analyzer.exponentialSmoothing(
            source, ["expSmoothing" + name for name in source.columns], alpha=-1
        )
    assert str(execinfo_4.value) == "The value of alpha must between 0 and 1."

    with raises(ValueError) as execinfo_5:
        stock_analyzer.exponentialSmoothing(
            source, ["expSmoothing" + name for name in source.columns], alpha=2
        )
    assert str(execinfo_5.value) == "The value of alpha must between 0 and 1."


def test_visMovingAverage():

    # dataframe with no index name
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
    sma_example = stock_analyzer.visMovingAverage(source, "3", 3)

    assert (
        sma_example.layer[0].encoding.x.shorthand == "index"
    ), "x_axis should be mapped to the x axis"
    assert (
        sma_example.layer[0].encoding.y.shorthand == "3"
    ), "y_axis should be mapped to the y axis"
    assert sma_example.layer[0].mark == "line", "mark should be a line"
    assert (
        sma_example.layer[1].encoding.x.shorthand == "index"
    ), "x_axis should be mapped to the x axis"
    assert (
        sma_example.layer[1].encoding.y.shorthand == "movingAverage3"
    ), "y_axis should be mapped to the y axis"
    assert sma_example.layer[1].mark == "line", "mark should be a line"

    # dataframe with index name
    source_2 = pd.DataFrame(
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
        index=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    )
    source_2.index.names = ["Year"]

    sma_example_2 = stock_analyzer.visMovingAverage(source_2, "3", 3)

    assert (
        sma_example_2.layer[0].encoding.x.shorthand == "Year"
    ), "x_axis should be mapped to the x axis"
    assert (
        sma_example_2.layer[0].encoding.y.shorthand == "3"
    ), "y_axis should be mapped to the y axis"
    assert sma_example_2.layer[0].mark == "line", "mark should be a line"
    assert (
        sma_example_2.layer[1].encoding.x.shorthand == "Year"
    ), "x_axis should be mapped to the x axis"
    assert (
        sma_example_2.layer[1].encoding.y.shorthand == "movingAverage3"
    ), "y_axis should be mapped to the y axis"
    assert sma_example_2.layer[1].mark == "line", "mark should be a line"

    # test exception handling
    with raises(ValueError) as bad_ex:
        stock_analyzer.visMovingAverage(source_2, "hello", 3)
    assert (
        str(bad_ex.value)
        == "Your input name does not match with the dataframe column name! \
            Please enter valid column name!"
    )


def test_visExpSmoothing():
    # dataframe with no index name
    source = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [1, 12, 3, 4, 5],
            [1, 22, 3, 4, 5],
            [1, 32, 3, 4, 5],
            [1, 42, 3, 4, 5],
            [1, 52, 3, 4, 5],
            [1, 62, 3, 4, 5],
            [1, 72, 3, 4, 5],
        ],
        columns=["1", "2", "3", "4", "5"],
        index=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    )
    exp_plot = stock_analyzer.visExpSmoothing(source, "2", 0.5)

    assert (
        exp_plot.layer[0].encoding.x.shorthand == "index"
    ), "index should be mapped to the x axis"
    assert (
        exp_plot.layer[1].encoding.x.shorthand == "index"
    ), "index should be mapped to the x axis"

    assert (
        exp_plot.layer[0].encoding.y.shorthand == "2"
    ), "colum '2' should be mapped to the y axis"
    assert (
        exp_plot.layer[1].encoding.y.shorthand == "exponentialSmoothing2"
    ), "colum 'exponentialSmoothing2' should be mapped to the y axis"

    assert exp_plot.layer[0].mark == "line", "mark should be a line"
    assert exp_plot.layer[1].mark == "line", "mark should be a line"

    # dataframe with index name
    source_2 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [1, 12, 3, 4, 5],
            [1, 22, 3, 4, 5],
            [1, 32, 3, 4, 5],
            [1, 42, 3, 4, 5],
            [1, 52, 3, 4, 5],
            [1, 62, 3, 4, 5],
            [1, 72, 3, 4, 5],
        ],
        columns=["1", "2", "3", "4", "5"],
        index=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    )
    source_2.index.names = ["Year"]
    exp_plot_2 = stock_analyzer.visExpSmoothing(source_2, "2", 0.5)

    assert (
        exp_plot_2.layer[0].encoding.x.shorthand == "Year"
    ), "index should be mapped to the x axis"
    assert (
        exp_plot_2.layer[1].encoding.x.shorthand == "Year"
    ), "index should be mapped to the x axis"

    assert (
        exp_plot_2.layer[0].encoding.y.shorthand == "2"
    ), "colum '2' should be mapped to the y axis"
    assert (
        exp_plot_2.layer[1].encoding.y.shorthand == "exponentialSmoothing2"
    ), "colum 'exponentialSmoothing2' should be mapped to the y axis"

    assert exp_plot_2.layer[0].mark == "line", "mark should be a line"
    assert exp_plot_2.layer[1].mark == "line", "mark should be a line"

    # test exception handling
    with raises(ValueError) as bad_ex_2:
        stock_analyzer.visExpSmoothing(source_2, "hello", 0.5)
    assert (
        str(bad_ex_2.value)
        == "Your input name does not match with the dataframe column name! \
            Please enter valid column name!"
    )
