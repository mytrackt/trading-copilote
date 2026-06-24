# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=180


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Stochastic RSI


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Stochastic RSI

- Description

- Inputs


### Description

This staudy calculates and displays the Stochastic RSI for Close (Last) Price data. The RSI is used in the calculation.

Let \(C\) be a random variable denoting the Close Price, and let \(C_t\) be the value of the Close Price at Index \(t\). Then the RSI of \(C\) with RSI Length \(n_{RSI}\) at Index \(t\) is denoted as \(RSI_t(C,n_{RSI})\), and it is calculated in terms of a Simple Moving Average for \(t \geq n_{RSI} - 1\).

Note : Depending on the setting of the Input Average Type , the Simple Moving Averages in the calculations of \(RS_t\left(X,n_{RSI}\right)\) and \(\overline{RSI}_t(RSI(X,n_{RSI}),n)\) could be replaced with Exponential Moving Averages , Linear Regression Moving Averages , Weighted Moving Averages , Wilders Moving Averages , Simple Moving Averages - Skip Zeros , or Smoothed Moving Averages . The types of all three Moving Averages in the calculation are determined by this one Input.

Let the RSI HighestLowest Length Input be denoted as \(n_{HL}\). We denote the Stochastic RSI for the given Inputs at Index \(t\) as \(RSI^{(Stoch)}_t\left(n_{RSI},n_{HL}\right)\), and we compute it for \(t \geq n_{RSI} + n_{HL} - 1\) in terms of the Moving Maximum and the Moving Minimum of \(RSI_t(C,n_{RSI})\) over the last \(n_{HL}\) bars as follows.


#### Inputs

- RSI Length

- RSI Average Type

- RSI HighestLowest Length

*Last modified Friday, 24th January, 2025.