import numpy as np
import pandas as pd
import altair as alt


def summaryStats(data, measurements=["High", "Low", "Open", "Close"]):
    """
    Generate summary statistics for profile stock data

    Parameters
    ----------
    data: ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        input data. It should be convertable to a pandas dataframe measurements
        : str columns to be summarized on. All elements should be column names
        of data. The calculation of statistics will be based on the specified
        measurement of stock price.

    Returns
    -------
    pandas.core.frame.DataFrame a Pandas dataframe that contains summary
        statistics for the specified columns of the data. Statistics calculated
        include mean price, minimum price, maximum price, volatility and
        return.

    Example
    -------
    >>> from stock_analyzer import stock_analyzer
    >>> import pandas_datareader.data as web
    >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01',
    ... end='2020-12-17')
    >>> stock_analyzer.summaryStats(data = df, measurements=["Open",
    ... "Volume"])
      measurement          mean  ...    volatility    return
    0        Open  2.265452e+03  ...  5.835520e+02  1.950010
    1      Volume  3.710356e+09  ...  8.710935e+08  0.061166

    [2 rows x 6 columns]
    """
    try:
        data = pd.DataFrame(data)
    except ValueError:
        raise ValueError(
            "Your input data cannot be converted to a pandas dataframe."
        )
    else:
        stats = {
            "measurement": [],
            "mean": [],
            "min": [],
            "max": [],
            "volatility": [],
            "return": [],
        }
        for measurement in measurements:
            if measurement not in list(data.columns):
                raise ValueError(
                    f"Your specified measurement '{measurement}' is not a \
                    column name of the data. \
            Please double check the column names in data."
                )
            else:
                data_measurement = data[measurement]
                try:
                    data_measurement = pd.to_numeric(data_measurement)
                except ValueError:
                    raise ValueError(
                        f"Data in column '{measurement}' of your input data \
                        cannot be converted to \
            numeric format."
                    )
                else:
                    stats["measurement"].append(measurement)
                    stats["mean"].append(data_measurement.mean())
                    stats["min"].append(data_measurement.min())
                    stats["max"].append(data_measurement.max())
                    stats["volatility"].append(data_measurement.std())
                    stats["return"].append(
                        (
                            list(data_measurement)[-1]
                            - list(data_measurement)[0]
                        )
                        / list(data_measurement)[0]
                    )
        return pd.DataFrame(stats)


def movingAverage(data, window, newColumnNames):
    """
    Using moving average method to profile stock data

    Parameters
    ----------
    data : pandas.core.frame.DataFrame input Pandas dataframe window : int size
        of the sliding window to compute the moving average newColumnNames :
        str new column names after creating moving average dataframe

    Returns
    -------
    pandas.core.frame.DataFrame a Pandas dataframe contains moving average from
        the data

    Example
    -------
    >>> from stock_analyzer import stock_analyzer
    >>> import pandas_datareader.data as web
    >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01',
    ... end='2020-12-17')
    >>> stock_analyzer.movingAverage(df,100,['movingAverage'+ name for name
    ... in df.columns])
                movingAverageHigh  ...  movingAverageAdj Close
    Date                           ...
    2012-01-03        1284.619995  ...             1277.060059
    2012-01-04        1284.561095  ...             1277.062458
    2012-01-05        1284.545396  ...             1277.102458
    2012-01-06        1284.517595  ...             1277.109958
    2012-01-09        1284.491295  ...             1277.146357
    ...                       ...  ...                     ...
    2020-12-11        3459.242998  ...             3438.738198
    2020-12-14        3463.419199  ...             3442.856499
    2020-12-15        3468.099500  ...             3447.646401
    2020-12-16        3472.797900  ...             3452.264001
    2020-12-17        3477.611902  ...             3457.304402

    [2256 rows x 6 columns]

    """
    try:
        data = pd.DataFrame(data)
    except ValueError:
        raise ValueError(
            "Your input data cannot be converted to a pandas dataframe."
        )

    avgs = []

    for name in data.columns:
        try:
            values = data[name].values.astype("float")
        except TypeError:
            raise TypeError(
                "Type of Column %s isn't a string \
        or a number "
                % name
            )
        except ValueError:
            raise ValueError(
                "Column %s can't be converted to floating point" % name
            )

        _nan_locations = np.argwhere(np.isnan(values))
        if _nan_locations.shape[0] > 0:
            raise ValueError(
                (
                    "Column {} has Nan at " + "{} " * _nan_locations.shape[0]
                ).format(name, *_nan_locations)
            )

        values = np.insert(values, 0, [values[0] for i in range(window - 1)])
        avg = [
            np.average(values[(i - window + 1) : (i + 1)])
            for i in range(window - 1, len(values))
        ]
        avgs.append(avg)

    df_avgs = pd.DataFrame(
        np.array(avgs).T, index=data.index, columns=newColumnNames
    )
    return df_avgs


def exponentialSmoothing(data, newColumnNames, alpha=0.3):

    """
    Using exponential smoothing method to profile stock data

    Parameters
    ----------
    data : pandas.core.frame.DataFrame input Pandas dataframe alpha : float the
        smoothing parameter that defines the weighting. It should be between 0
        and 1 newColumnNames : str new column names after creating moving
        average dataframe

    Returns
    -------
    pandas.core.frame.DataFrame a Pandas dataframe contains exponential
        smoothing fits of the data

    Example
    -------
    >>> from stock_analyzer import stock_analyzer
    >>> import pandas_datareader.data as web
    >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01',
    ... end='2020-12-17')
    >>> stock_analyzer.exponentialSmoothing(df,['exponentialSmoothing'+ name
    ... for name in df.columns])
                exponentialSmoothingHigh  ...  exponentialSmoothingAdj Close
    Date                                  ...
    2012-01-03               1284.619995  ...                    1277.060059
    2012-01-04               1282.852991  ...                    1277.132056
    2012-01-05               1282.912108  ...                    1278.310457
    2012-01-06               1282.590465  ...                    1278.160337
    2012-01-09               1282.410323  ...                    1278.922221
    ...                              ...  ...                            ...
    2020-12-11               3683.080578  ...                    3671.981068
    2020-12-14               3687.439437  ...                    3664.633745
    2020-12-15               3689.794617  ...                    3673.629656
    2020-12-16               3696.237238  ...                    3681.891736
    2020-12-17               3704.902102  ...                    3694.068209

    [2256 rows x 6 columns]
    """

    try:
        data = pd.DataFrame(data)
    except ValueError:
        raise ValueError(
            "Your input data cannot be converted to a pandas dataframe."
        )

    if alpha < 0 or alpha > 1:
        raise ValueError("The value of alpha must between 0 and 1.")

    smoothed = []
    for name in data.columns:
        try:
            values = data[name].values.astype("float")
        except TypeError:
            raise TypeError(
                "Type of Column %s isn't a string \
        or a number "
                % name
            )
        except ValueError:
            raise ValueError(
                "Column %s can't be converted to floating point" % name
            )

        _nan_locations = np.argwhere(np.isnan(values))
        if _nan_locations.shape[0] > 0:
            raise ValueError(
                (
                    "Column {} has Nan at " + "{} " * _nan_locations.shape[0]
                ).format(name, *_nan_locations)
            )

        pred = []
        values = data[name].values
        St_prev = values[0]
        for i in range(len(values)):
            yt = values[i]
            St = alpha * yt + St_prev * (1 - alpha)
            pred.append(St)
            St_prev = St
        smoothed.append(pred)
    df_smoothed = pd.DataFrame(
        np.array(smoothed).T, index=data.index, columns=newColumnNames
    )
    return df_smoothed


def visMovingAverage(data, name, window):
    """
    Visualizing trends of stock by using moving average

    Parameters
    ----------
    data : pandas.core.frame.DataFrame input pandas dataframe of stock of
        interest name : str column to be used in moving average calculation
        (such as Close, Adj Close) window : int size of the window (number of
        days) used in moving average calculation

    Returns
    -------
    altair.vegalite.v4.api.LayerChart an Altair plot object containing the plot
        of original movement and the moving average of the stock of interest

    Example
    -------
    >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01',
    >>> end='2020-12-17')
    >>> visMovingAverage(df,'Close', 50)
    """
    if name not in data.columns:
        raise ValueError(
            "Your input name does not match with the dataframe column name! \
            Please enter valid column name!"
        )

    df_avgs = movingAverage(
        data, window, [movingAverage.__name__ + name for name in data.columns]
    )

    if data.index.name is None:
        index_name = "index"
    else:
        index_name = data.index.name

    plot_a = (
        alt.Chart(
            data.reset_index(),
            title="Stock Price History with Simple Moving Average",
        )
        .mark_line()
        .encode(
            x=index_name,
            y=alt.Y(name, title="Price"),
            color=alt.value("#0abab5"),
        )
    )
    plot_b = (
        alt.Chart(df_avgs.reset_index())
        .mark_line()
        .encode(
            x=index_name,
            y=movingAverage.__name__ + name,
            color=alt.value("#00008b"),
        )
    )

    sma_plot = plot_a + plot_b
    return sma_plot


def visExpSmoothing(data, name, alpha):
    """
    Visualizing trends of stock by using exponential smoothing

    Parameters
    ----------
    data : pandas.core.frame.DataFrame input pandas dataframe of stock of
        interest name : str column to be used in exponential smoothing
        calculation (such as Close, Adj Close) alpha :float the smoothing
        parameter that defines the weighting. It should be between 0 and 1

    Returns
    -------
    altair.vegalite.v4.api.LayerChart an Altair plot object containing the plot
        of original movement and the exponential smoothing of the stock of
        interest

    Example
    -------
    >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01',
    >>> end='2020-12-17')
    >>> visExpSmoothing(df,'Close', 0.3)
    """
    if name not in data.columns:
        raise ValueError(
            "Your input name does not match with the dataframe column name! \
            Please enter valid column name!"
        )

    df_smoothed = exponentialSmoothing(
        data,
        [exponentialSmoothing.__name__ + name for name in data.columns],
        alpha,
    )

    if data.index.name is None:
        index_name = "index"
    else:
        index_name = data.index.name

    plot_c = (
        alt.Chart(
            data.reset_index(),
            title="Stock Price History with Exponential Smoothing",
        )
        .mark_line()
        .encode(
            x=index_name,
            y=alt.Y(name, title="Price"),
            color=alt.value("#0abab5"),
        )
    )
    plot_d = (
        alt.Chart(df_smoothed.reset_index())
        .mark_line()
        .encode(
            x=index_name,
            y=exponentialSmoothing.__name__ + name,
            color=alt.value("#00008b"),
        )
    )

    expsm_plot = plot_c + plot_d
    return expsm_plot
