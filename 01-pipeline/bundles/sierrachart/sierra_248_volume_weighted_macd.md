# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=248


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> MACD - Volume Weighted


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# MACD - Volume Weighted

- Description

- Inputs

- Spreadsheet


### Description

Let \(X\) be a random variable denoting the Input Data Input. Let the Inputs Fast Moving Average Length , Slow Moving Average Length , and MACD Moving Average Length be denoted as \(n_F\), \(n_S\), and \(n_M\), respectively. This study calculates and displays three indicators: the Volume Weighted MACD, the Moving Average of the Volume Weighted MACD, and the Volume Weighted MACD Difference. These indicators are the same as those in the MACD study, but with the Volume Weighted Moving Average used in place of the Exponential Moving Average . We describe the methods of calculation of these indicators below.

The Volume Weighted MACD is calcuated \(t \geq \max\{n_S,n_F\} + n_M\) in terms of Volume Weighted Moving Averages as follows.

Note : \(MACD_t\left(X,n_F,n_S\right)\) is calculated internally for \(n_S \leq t < \max\{n_S,n_F\} + n_M\), but these values are not displayed as output. However, the value at \(t = \max\{n_S,n_F\} + n_M - 1\) is used to calculate the Exponential Moving Average in the next step.

The Moving Average of the Volume Weighted MACD is then calculated using an Exponential Moving Average as follows.

In the above formula, \(MACD\left(X,n_F,n_S\right)\) is a random variable denoting th Volume Weighted MACD with Inputs as listed in parentheses.

Finally, the Volume Weighted Moving Average Difference is calculated as follows.


#### Inputs

- Fast Moving Average Length

- Slow Moving Average Length

- MACD Moving Average Length

- Input Data


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

MACD_-_Volume_Weighted.248.scss

*Last modified Friday, 24th January, 2025.