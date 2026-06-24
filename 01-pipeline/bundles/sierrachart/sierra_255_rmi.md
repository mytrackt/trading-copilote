# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=255


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Relative Momentum Index


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Relative Momentum Index

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays a Relative Momentum Index for the data specified by the Input Data Input.

Let \(X\) be a random variable denoting the Input Data , and let \(X_t\) be the value of the Input Data at Index \(t\). Let the Inputs RMI Length and RMI Moving Average Length be denoted as \(n\) and \(n_{MA}\), respectively. Then we denote the Upward Change and Downward Change in \(X\) over \(n\) periods at Index \(t\) as \(U_t(X,n)\) and \(D_t(X,n)\), respectively. We compute these for \(t \geq 0\) as follows.

For \(0 \leq t < n\):

For \(t \geq n\):

We denote the Relative Momentum Index at Index \(t\) for the given Inputs as \(RMI_t(X,n,n_{MA})\). At \(t = \max\{n,n_{MA}\} - 1\) we initialize the RMI to zero, and for \(t \geq \max\{n,n_{MA}\}\) we compute it in terms of Simple Moving Averages as follows.

Note : Depending on the setting of the RMI Moving Average Type Input, the Simple Moving Averages in the above formula could be replaced with Exponential Moving Averages , Linear Regression Moving Averages , Weighted Moving Averages , Wilders Moving Averages , Simple Moving Averages - Skip Zeros , or Smoothed Moving Averages .

This study also displays three horizontal lines at levels determined by the Overbought Value , Oversold Value , and Midline Value Inputs.


#### Inputs

- Input Data

- RMI Length

- RMI Moving Average Length

- RMI Moving Average Type

- Overbought Value

- Oversold Value

- Midline Value


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Relative_Momenum_Index.255.scss

*Last modified Friday, 24th January, 2025.