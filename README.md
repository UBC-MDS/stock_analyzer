# stock_analyzer

![](https://github.com/UBC-MDS/stock_analyzer/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/stock_analyzer/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/stock_analyzer) ![Release](https://github.com/UBC-MDS/stock_analyzer/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/stock_analyzer/badge/?version=latest)](https://stock_analyzer.readthedocs.io/en/latest/?badge=latest)

This is a Python package that provides basic time series modelling functionalities to analyze historical stock prices. Investment in the stock market requires not only knowledge about the listed companies, but also basic summary statistics and modellings of individual stock prices. Given time-series stock price data, this package provides key summary statistics, applies moving average and exponential smoothing models to the data, and visualizes in-sample moving average as well as exponential smoothing fits. A convenient use case for this package is to combine it with the `pandas_datareader` package, which can provide well-formated stock price data from Yahoo Finance dataset with customized date range setting.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ stock_analyzer
```

## Features

The package contains the following five functions:

- `summaryStats`

This function calculates summary statistics including mean price, minimum price, maximum price, volatility and return rate based on daily historical stock prices.
Users can specify lengths of time spans to calculate summary statistics on, and what kind of stock price measurement to use.

- `movingAverage`

This function applies the moving average model to all measurements of stock price and returns a pandas dataframe containing in-sample fitted values. Users can specify the length of moving average windows (unit: days).

- `exponentialSmoothing`

This function performs exponential smoothing on historical stock price time series data. Users can specify the `alpha` parameter (which defines the weighting, ranging between 0 and 1) for smoothing.

- `visMovingAverage`

This function creates a line chart showing the raw historical data and fitted data using the moving average method. Users are able to specify the dataframe used, the column of choice (such as 'Close', 'Adj Close') for moving average calculation, and the length of moving average window (unit: days).

- `visExpSmoothing`

This function creates a line chart showing the raw historical data and fitted data using the exponential smoothing method. Users are able to specify the dataframe used, the column of choice (such as 'Close', 'Adj Close') for exponential smoothing calculation, and the `alpha` parameter (which defines the weighting, ranging between 0 and 1) for smoothing.

## Python Ecosystem

In the Python ecosystem, there are multiple packages with functionalities of time series modelling and analyses. In particular, `pandas` and `statsmodels` packages both provide functionalities to calculate summary statistics for time series data and basic time series modelling. In terms of time series visualization, packages including `matplotlib`, `seaborn` and `altair` all have good functionalities. However, users would need to use them separately to conduct the functionalities that this package does.

There are also multiple python packages dedicated to financial analyses. Examples include [`QuantPy`](https://github.com/jsmidt/QuantPy), [`ffn`](https://github.com/pmorissette/ffn) and [`PyNance`](http://pynance.net/). There packages have similar funcitonalities to this pakcage.

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://stock_analyzer.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/stock_analyzer/graphs/contributors).

- Kangyu (Mark) Wang 
- Sicheng (Marc) Sun
- William Xu 
- Tingyu Zhang

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
