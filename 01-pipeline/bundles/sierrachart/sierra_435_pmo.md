# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=435


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Price Momentum Oscillator


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Price Momentum Oscillator

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays a Price Momentum Oscillator and its Moving Average for the data specified by the Input Data Input.

Let \(X\) be a random variable denoting the Input Data , and let \(X_t\) denote the value of \(X\) at Index \(t\). The first step is to calculate the Rate of Change for \(t \geq 1\) as follows.

Next we define a Custom Smoothing Function \(CSF_t(X,n)\) as follows.

Let the PMO Line Length 1 , PMO Line Length 2 , and PMO Signal Line Length Inputs be denoted as \(n_1\), \(n_2\), and \(n_{Sig}\), respectively. We denote the Smoothed ROC at Index \(t\) as \(\overline{ROC}_t(X,1,100,n_1)\), and we compute it for \(t \geq 1\) as follows.

We denote the Price Momentum Oscillator Line at Index \(t\) as \(PMO_t(X,n_1,n_2)\), and we compute it for \(t \geq 1\) as follows.

We denote the Price Momentum Oscillator Signal Line as \(\overline{PMO}_t(X,n_1,n_1,n_{Sig})\), and we calculate it for \(t \geq 1\) in terms of an Exponential Moving Average as follows.

Note : Depending on the setting of the Input PMO Signal Line Moving Average Type , the Exponential Moving Average in the above formula could be replaced with a Linear Regression Moving Average , a Simple Moving Average , a Weighted Moving Average , a Wilders Moving Average , a Simple Moving Average - Skip Zeros , or a Smoothed Moving Average .


#### Inputs

- Input Data

- PMO Line Length 1

- PMO Line Length 2

- PMO Signal Line Length

- PMO Signal Line Moving Average Type


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Price_Momentum_Oscillator.435.scss

*Last modified Friday, 24th January, 2025.