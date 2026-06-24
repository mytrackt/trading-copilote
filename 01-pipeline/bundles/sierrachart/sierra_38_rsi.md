# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=38


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> RSI


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# RSI

- Description

- Inputs

- Spreadsheet


### Description

This study calculates the Welles Wilder Relative Strength Index (RSI) of the data specified by the Input Data Input. The study also calculates a Moving Average of the RSI. It displays graphs of both of these functions, in addition to two horiztonal lines, which are specified by the Inputs Line1 Value and Line2 Value . Both the RSI and the Moving Average of the RSI have an associated Length Input: RSI Length \(n_{RSI}\) and RSI Moving Average Length \(n\), respectively.

Let \(X\) be a random variable denoting the Input Data , and let \(X_t\) be the value of the Input Data at Index \(t\). Then we denote the Upward Change and Downward Change in \(X\) at Index \(t\) as \(U_t(X)\) and \(D_t(X)\), respectively. We compute these for \(t > 0\) as follows.

The Relative Strength Index at Index \(t\) is denoted as \(RSI_t\left(X,n_{RSI}\right)\), and it is computed in terms of a Simple Moving Average for \(t \geq n_{RSI} + n\) as follows.

In the above formula, \(U(X)\) and \(D(X)\) are random variables denoting the Upward and Downward Changes in \(X\), respectively.

Note : For the purposes of computing \(RSI_t\left(X,n_{RSI}\right)\) for \(t \geq n_{RSI} + n\), we use internal calculations for \(n_{RSI} - 1 \leq t < n_{RSI} + n\) using the last formula given above. These values are not returned as output.

The Moving Average of \(RSI_t\left(X,n_{RSI}\right)\) with Length RSI Moving Average Length \(n\) at Index \(t\) is denoted as \(\overline{RSI}_t(X,n_{RSI},n)\). This Moving Average is calculated for \(t \geq n_{RSI} + n\) as follows.

In the above formula, \(RSI(X,n_{RSI})\) is a random variable denoting the RSI of \(X\) with Length \(n\).

Note : For the purposes of computing \(\overline{RSI}_t(X,n_{RSI},n)\) for \(t \geq n_{RSI} + n\), we use internal calculations for \(n_{RSI} +n - 2 \leq t < n_{RSI} + n\) using the last formula given above. These values are not returned as output.

Note : Depending on the setting of the Input Average Type , the Simple Moving Averages in the calculations of \(RSI_t\left(X,n_{RSI}\right)\) and \(\overline{RSI}_t(RSI(X,n_{RSI}),n)\) could be replaced with Exponential Moving Averages , Linear Regression Moving Averages , Weighted Moving Averages , Wilders Moving Averages , Simple Moving Averages - Skip Zeros , or Smoothed Moving Averages . The types of all three Moving Averages in the calculation are determined by this one Input.

If the Input Use RSI - 50 is set to Yes, then 50 is subtracted from the values of the RSI, the Moving Average of the RSI, Line 1 Value , and Line 2 value .


#### Inputs

- Input Data

- RSI Length

- RSI Moving Average Length

- Use RSI - 50 : This custom Input determines whether the values of the four Subgraphs of the study are offset by -50.

- Line 1 Value

- Line 2 Value

- Average Type


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

RSI.38.scss

*Last modified Monday, 27th February, 2023.