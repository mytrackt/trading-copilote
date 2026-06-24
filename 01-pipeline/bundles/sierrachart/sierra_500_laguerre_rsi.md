# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=500


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Laguerre RSI


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Laguerre RSI

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays a Laguerre RSI for the data given by the Input Data Input. This study is an ACSIL implementation of the Indicator given in Figures 14.8 and 14.9 of the book Cybernetic Analysis for Stocks and Futures by John Ehlers.

The Laguerre RSI can be loosely thought of as an RSI in which the Average Type is a Laguerre Moving Average, given by the components of the Laguerre Filter . See the documentation of that study for an explanation of the notation used here.

Let \(X\) be a random variable denoting the Input Data , and let \(X_t\) be the value of \(X\) at Index \(t\). Let the Damping Factor Input be denoted as \(\gamma\) (Greek letter gamma).

We begin by defining an Up Sum and a Down Sum, denoted as \(U_t(X,\gamma)\) and \(D_t(X,\gamma)\), respectively. We compute them as follows.

For an explanation of the Sigma (\(\Sigma\)) notation for summation, refer to our description here .

In the above sum, \(c^{(U)}_k\) is a coefficient defined for each \(k\) as follows.

In the above sum, \(c^{(D)}_k\) is a coefficient defined for each \(k\) as follows.

The Laguerre RSI at Index \(t\) is denoted as \(RSI^{(L)}_t(X,\gamma)\), and we compute it as follows.

This study also displays horizontal lines at the levels specified by the Line 1 Value and Line 2 Value Inputs.


#### Inputs

- Input Data

- Damping Factor : A custom Input that determines the weighting factor given to both current and previous values of the Input Data.

- Line 1 Value

- Line 2 Value


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Laguerre_RSI.500.scss

*Last modified Friday, 24th January, 2025.