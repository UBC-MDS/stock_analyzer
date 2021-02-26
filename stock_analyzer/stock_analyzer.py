import pandas_datareader as web
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

from statsmodels.tsa.arima.model import ARIMA


def movingAverage(data, window, newColumnNames):
    """[Using moving average method to profile stock data]

    Args:
        data ([pandas.core.frame.DataFrame]): [Input Pandas dataframe]
        window ([int]): [Size of the sliding window to compute the moving average]
        newColumnNames ([str]): [new column names after creating moving average dataframe]

    Returns:
        [pandas.core.frame.DataFrame]: [A Pandas dataframe contains moving average from the data]

    Examples:
        >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01', end='2020-12-17')
        >>> df
                        High          Low         Open        Close      Volume    Adj Close
        Date
        2012-01-03  1284.619995  1258.859985  1258.859985  1277.060059  3943710000  1277.060059
        2012-01-04  1278.729980  1268.099976  1277.030029  1277.300049  3592580000  1277.300049
        2012-01-05  1283.050049  1265.260010  1277.300049  1281.060059  4315950000  1281.060059
        2012-01-06  1281.839966  1273.339966  1280.930054  1277.810059  3656830000  1277.810059
        2012-01-09  1281.989990  1274.550049  1277.829956  1280.699951  3371600000  1280.699951
        ...                 ...          ...          ...          ...         ...          ...
        2020-12-11  3665.909912  3633.399902  3656.080078  3663.459961  4367150000  3663.459961
        2020-12-14  3697.610107  3645.840088  3675.270020  3647.489990  4594920000  3647.489990
        2020-12-15  3695.290039  3659.620117  3666.409912  3694.620117  4360280000  3694.620117
        2020-12-16  3711.270020  3688.570068  3696.250000  3701.169922  4056950000  3701.169922
        2020-12-17  3725.120117  3710.870117  3713.649902  3722.479980  4184930000  3722.479980

        >>> df_movingAverage = movingAverage(df,100,['movingAverage'+ name for name in df.columns])
        >>> df_movingAverage

                    movingAverageHigh  movingAverageLow  movingAverageOpen  movingAverageClose  movingAverageVolume  movingAverageAdj Close
        Date
        2012-01-03        1284.619995       1258.859985        1258.859985         1277.060059         3.943710e+09             1277.060059
        2012-01-04        1284.561095       1258.952385        1259.041686         1277.062458         3.940199e+09             1277.062458
        2012-01-05        1284.545396       1259.016385        1259.226086         1277.102458         3.943921e+09             1277.102458
        2012-01-06        1284.517595       1259.161185        1259.446787         1277.109958         3.941052e+09             1277.109958
        2012-01-09        1284.491295       1259.318086        1259.636487         1277.146357         3.935331e+09             1277.146357
        ...                       ...               ...                ...                 ...                  ...                     ...
        2020-12-11        3459.242998       3416.176194        3438.266194         3438.738198         4.415716e+09             3438.738198
        2020-12-14        3463.419199       3420.407996        3442.302495         3442.856499         4.418761e+09             3442.856499
        2020-12-15        3468.099500       3425.003696        3446.780793         3447.646401         4.423414e+09             3447.646401
        2020-12-16        3472.797900       3429.746897        3451.544893         3452.264001         4.424345e+09             3452.264001
        2020-12-17        3477.611902       3434.693899        3456.338691         3457.304402         4.425915e+09             3457.304402
    """

    avgs = []
    for name in data.columns:
        values = data[name].values

        values = np.insert(values, 0, [values[0] for i in range(window - 1)])
        avg = [
            np.average(values[i - window + 1 : i + 1])
            for i in range(window - 1, len(values))
        ]
        avgs.append(avg)

    df_avgs = pd.DataFrame(np.array(avgs).T, index=data.index, columns=newColumnNames)
    return df_avgs


def ARIMA(
    data,
):
    """[Using moving average method to profile stock data]

    Args:
        data ([pandas.core.frame.DataFrame]): [Input Pandas dataframe]
        window ([int]): [Size of the sliding window to compute the moving average]
        newColumnNames ([str]): [new column names after creating moving average dataframe]

    Returns:
        [pandas.core.frame.DataFrame]: [A Pandas dataframe contains moving average from the data]

    Examples:
        >>> df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01', end='2020-12-17')
        >>> df
                        High          Low         Open        Close      Volume    Adj Close
        Date
        2012-01-03  1284.619995  1258.859985  1258.859985  1277.060059  3943710000  1277.060059
        2012-01-04  1278.729980  1268.099976  1277.030029  1277.300049  3592580000  1277.300049
        2012-01-05  1283.050049  1265.260010  1277.300049  1281.060059  4315950000  1281.060059
        2012-01-06  1281.839966  1273.339966  1280.930054  1277.810059  3656830000  1277.810059
        2012-01-09  1281.989990  1274.550049  1277.829956  1280.699951  3371600000  1280.699951
        ...                 ...          ...          ...          ...         ...          ...
        2020-12-11  3665.909912  3633.399902  3656.080078  3663.459961  4367150000  3663.459961
        2020-12-14  3697.610107  3645.840088  3675.270020  3647.489990  4594920000  3647.489990
        2020-12-15  3695.290039  3659.620117  3666.409912  3694.620117  4360280000  3694.620117
        2020-12-16  3711.270020  3688.570068  3696.250000  3701.169922  4056950000  3701.169922
        2020-12-17  3725.120117  3710.870117  3713.649902  3722.479980  4184930000  3722.479980

        >>> df_movingAverage = movingAverage(df,100,['movingAverage'+ name for name in df.columns])
        >>> df_movingAverage

                    movingAverageHigh  movingAverageLow  movingAverageOpen  movingAverageClose  movingAverageVolume  movingAverageAdj Close
        Date
        2012-01-03        1284.619995       1258.859985        1258.859985         1277.060059         3.943710e+09             1277.060059
        2012-01-04        1284.561095       1258.952385        1259.041686         1277.062458         3.940199e+09             1277.062458
        2012-01-05        1284.545396       1259.016385        1259.226086         1277.102458         3.943921e+09             1277.102458
        2012-01-06        1284.517595       1259.161185        1259.446787         1277.109958         3.941052e+09             1277.109958
        2012-01-09        1284.491295       1259.318086        1259.636487         1277.146357         3.935331e+09             1277.146357
        ...                       ...               ...                ...                 ...                  ...                     ...
        2020-12-11        3459.242998       3416.176194        3438.266194         3438.738198         4.415716e+09             3438.738198
        2020-12-14        3463.419199       3420.407996        3442.302495         3442.856499         4.418761e+09             3442.856499
        2020-12-15        3468.099500       3425.003696        3446.780793         3447.646401         4.423414e+09             3447.646401
        2020-12-16        3472.797900       3429.746897        3451.544893         3452.264001         4.424345e+09             3452.264001
        2020-12-17        3477.611902       3434.693899        3456.338691         3457.304402         4.425915e+09             3457.304402
    """


def visualizeMovingAverage(data, name, window, method=movingAverage):
    """[Visualizing trends of stock by using moving average]

    Args:
        data ([pandas.core.frame.DataFrame]): [Input Pandas dataframe]
        name ([str]): [Column names with specific method (moving average) to be used]
        window ([int]): [Size of the sliding window to compute the moving average]
        method ([function]): [functions of different method to be used, default: movingAverage]

    Examples:
        df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01', end='2020-12-17')
        visualizeMovingAverage(df,'High', 300)
    """

    df_avgs = method(data, window, [method.__name__ + name for name in data.columns])
    print(df_avgs)

    plt.plot(data[name], color="blue")
    plt.plot(df_avgs[method.__name__ + name], color="red")
    plt.show()


# # Get the stock quote
# df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01', end='2020-12-17')
# # Show the data
# visualizeMovingAverage(df,'High', 300)