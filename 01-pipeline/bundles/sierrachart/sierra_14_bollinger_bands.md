# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=14


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Bollinger Bands


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Bollinger Bands

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays Bollinger Bands for the data specified by the Input Data Input, as well as a Moving Average of the Input Data .

Let \(X\) be a random variable denoting the Input Data , and let \(X_i\) be the value of the Input Data at Index \(i\). Let the Inputs Length and Standard Deviations be denoted as \(n\) and \(v\), respectively. Then we denote the Bollinger Bands at Index \(t\) for the given Inputs as \(TB^{(B)}_t(X,n,v)\) (Top Band), \(MB^{(B)}_t(X,n,v)\) (Middle Band), and \(BB^{(B)}_t(X,n,v)\) (Bottom Band), and we compute them for \(t \geq n - 1\) in terms of a Simple Moving Average and a Standard Deviation as follows.

Top Band: \(TB^{(B)}_t(X,n,v) = SMA_t(X,n) + v \cdot \sigma_t(X,n)\)

Middle Band: \(MB^{(B)}_t(X,n,v) = SMA_t(X,n)\)

Bottom Band: \(BB^{(B)}_t(X,n,v) = SMA_t(X,n) - v \cdot \sigma_t(X,n)\)

Note : Depending on the setting of the Input Moving Average Type , the Simple Moving Average in each of the above formulas could be replaced with an Exponential Moving Average , a Linear Regression Moving Average , a Weighted Moving Average , a Wilders Moving Average , a Simple Moving Average - Skip Zeros , or a Smoothed Moving Average .


#### Inputs

- Input Data

- Length

- Standard Deviations

- Moving Average Type


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Bollinger_Bands.14.scss

*Last modified Wednesday, 05th July, 2023.