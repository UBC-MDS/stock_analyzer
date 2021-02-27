import pandas_datareader as web
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import warnings

def summaryStats(data, windows=["10d", "1m", "1y"], measurement="Close"):
    """[Using Autoregressive Integrated Moving Average (ARIMA) method to profile stock data]

    Args:
        data ([pandas.core.frame.DataFrame]): [Input Pandas dataframe. It should have a DatetimeIndex]
        windows ([list(str)]): [a list of strings indicating the lengths of time windows to calculate summary statistics. Each element should be a numeric value followed by one of ["d", "m", "y"]. If the length of a specified time window exceeds the timespan of the whole dataset, the whole dataset will be used instead.]
        measurement ([str]): [One of ["High", "Low", "Open", "Close", "Volume", "Adj Close"]. The calculation of statistics will be based on the specified measurement of stock price.]

    Returns:
        [pandas.core.frame.DataFrame]: [A Pandas dataframe that contains summary statistics for specified lengths, up till the current time (latest time in input data). Statistics calculated include mean price, minimum price, maximum price, volatility and return]

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

        >>> df_summarystats = summaryStats(data = df, measurement="Open")
        >>> df_summarystats
      	    start_date	end_date	mean	min	max	volatility	return
        0	2020-12-07	2020-12-17	3683.394423	3656.080078	3713.649902	20.641892	0.005121
        1	2020-11-17	2020-12-17	3646.368641	3559.409912	3713.649902	44.058352	0.028624
        2	2020-11-17	2020-12-17	3646.368641	3559.409912	3713.649902	44.058352	0.028624
    """
    pass
    # TODO 

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
    pass
    # TODO


def exponentialSmoothing(data, newColumnNames, alpha=0.3):

    """[Using exponential smoothing method to profile stock data]

    Args:
        data ([pandas.core.frame.DataFrame]): [Input Pandas dataframe]
        alpha ([float]): [The smoothing parameter that defines the weighting. It should be between 0 and 1]
        newColumnNames ([str]): [new column names after creating moving average dataframe]
    Returns:
        [pandas.core.frame.DataFrame]: [A Pandas dataframe contains exponential smoothing fits of the data]

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

        >>> df_exponentialSmoothing = exponentialSmoothing(df,['exponentialSmoothing'+ name for name in df.columns])
        >>> df_exponentialSmoothing

	    exponentialSmoothingHigh	exponentialSmoothingLow	exponentialSmoothingOpen	exponentialSmoothingClose	exponentialSmoothingVolume	exponentialSmoothingAdj Close
        Date						
        2012-01-03	1284.619995	1258.859985	1258.859985	1277.060059	3.943710e+09	1277.060059
        2012-01-04	1282.852991	1261.631982	1264.310999	1277.132056	3.838371e+09	1277.132056
        2012-01-05	1282.912108	1262.720391	1268.207714	1278.310457	3.981645e+09	1278.310457
        2012-01-06	1282.590465	1265.906263	1272.024416	1278.160337	3.884200e+09	1278.160337
        2012-01-09	1282.410323	1268.499399	1273.766078	1278.922221	3.730420e+09	1278.922221
        ...	...	...	...	...	...	...
        2020-12-11	3683.080578	3649.520587	3668.977441	3671.981068	4.714086e+09	3671.981068
        2020-12-14	3687.439437	3648.416438	3670.865215	3664.633745	4.678337e+09	3664.633745
        2020-12-15	3689.794617	3651.777541	3669.528624	3673.629656	4.582920e+09	3673.629656
        2020-12-16	3696.237238	3662.815300	3677.545037	3681.891736	4.425129e+09	3681.891736
        2020-12-17	3704.902102	3677.231745	3688.376496	3694.068209	4.353069e+09	3694.068209
    
    """
    pass
    # TODO


def visMovingAverage(data, name, window):
    """[Visualizing trends of stock by using moving average]
    Args:
        data ([pandas.core.frame.DataFrame]): [Input pandas dataframe of stock of interest]
        name ([str]): [Column to be used in moving average calcuation (such as Close, Adj Close)]
        window ([int]): [Size of the window (number of days) used in moving average calculation]
        
    Returns:
        [matplotlib.pyplot.plot]: [a graph containing the plot of original movement and the moving average of the stock of interest]
    Examples:
        df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01', end='2020-12-17')
        visualizeMovingAverage(df,'Close', 50)
    """
    pass
    # TODO

def visExpSmoothing(data, name, alpha):
    """[Visualizing trends of stock by using exponential smoothing]
    Args:
        data ([pandas.core.frame.DataFrame]): [Input pandas dataframe of stock of interest]
        name ([str]): [Column to be used in exponential smoothing calculation (such as Close, Adj Close)]
        alpha ([float]): [The smoothing parameter that defines the weighting. It should be between 0 and 1]
        
    Returns:
        [matplotlib.pyplot.plot]: [a graph containing the plot of original movement and the exponential smoothing of the stock of interest]
    Examples:
        df = web.DataReader('^GSPC', data_source='yahoo', start='2012-01-01', end='2020-12-17')
        visExpSmoothing(df,'Close', 50)
    """
    pass
    # TODO
