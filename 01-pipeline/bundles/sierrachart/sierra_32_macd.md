# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=32


## Sierra Chart

Financial Markets Charting and Trading Platform

- Main Home Software Download What Is New Features Data/Trade Services User Image Gallery Additional Files About Us Other Websites

- Home

- Software Download

- What Is New

- Features

- Data/Trade Services

- User Image Gallery

- Additional Files

- About Us

- Other Websites

- Documentation Table of Contents Frequently Asked Questions Sierra Chart Setup Instructions Data/Trade Services Video Library What Is New Developing for Sierra Chart Services for Brokers

- Table of Contents

- Frequently Asked Questions

- Sierra Chart Setup Instructions

- Data/Trade Services

- Video Library

- What Is New

- Developing for Sierra Chart

- Services for Brokers

- Getting Started Sierra Chart Setup Instructions Software Download Data/Trade Services What Is Included in Free Trial Understanding Real-time Futures Data

- Sierra Chart Setup Instructions

- Software Download

- Data/Trade Services

- What Is Included in Free Trial

- Understanding Real-time Futures Data

- Account Management Create Account Account Control Panel Make a Payment Activate Services License and Purchase Info Pricing Account Password Reset

- Create Account

- Account Control Panel

- Make a Payment

- Activate Services

- License and Purchase Info

- Pricing

- Account Password Reset

- Support Contact * Support Board * Self Help/Account Support Tickets Data/Trade Services Software Download Account Control Panel Study and System Programmers Custom Studies Store/List

- Contact

- * Support Board *

- Self Help/Account Support Tickets

- Data/Trade Services

- Software Download

- Account Control Panel

- Study and System Programmers

- Custom Studies Store/List


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> MACD


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# MACD

- Description

- Inputs

- Spreadsheet


### Description

The Moving Average Convergence/Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of prices. The MACD was developed by Gerald Appel. In Sierra Chart you have a choice of the Moving Average type to use in the calculations. We describe the calculation below.

Let \(X\) be a random variable denoting the Input Data Input. Let the Inputs Fast Moving Average Length , Slow Moving Average Length , and MACD Moving Average Length be denoted as \(n_F\), \(n_S\), and \(n_M\), respectively. This study calculates and displays three indicators: the MACD, the Moving Average of the MACD, and the MACD Difference. We denote the values of these indicators for the given Inputs at Index \(t\) as \(MACD_t\left(X,n_F,n_S\right)\), \(\overline{MACD}_t\left(X,n_F,n_S,n_M\right)\), and \(\Delta MACD_t\left(X,n_F,n_S,n_M\right)\), respectively. We describe the methods of calculation of these indicators below.

The MACD is calculated for \(t \geq 0\) in terms of Exponential Moving Averages as follows.

The Moving Average of the MACD is calculated for \(t \geq \max\{n_S,n_F\} + n_M\) in terms of an Exponential Moving Average as follows.

\(\overline{MACD}_t\left(X,n_F,n_S,n_M\right) = EMA_t\left(MACD\left(X,n_F,n_S\right),n_M\right)\)

In the above formula, \(MACD\left(X,n_F,n_S\right)\) is a random variable denoting the MACD with Inputs as listed in the parentheses.

Note : Depending on the setting of the Input Moving Average Type , the Exponential Moving Averages in each of the above formulas could be replaced with Linear Regression Moving Averages , Simple Moving Averages , Weighted Moving Averages , Wilders Moving Averages , Simple Moving Averages - Skip Zeros , or Smoothed Moving Averages .

The MACD Difference is calculated for \(t \geq \max\{n_S,n_F\} + n_M\) in terms of the MACD and the Moving Average of the MACD as follows.


#### Inputs

- Input Data

- Fast Moving Average Length

- Slow Moving Average Length

- MACD Moving Average Length

- Moving Average Type


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

MACD.32.scss

*Last modified Friday, 24th January, 2025.