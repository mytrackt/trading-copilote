# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=19


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Average True Range


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Average True Range

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays a Moving Average of the True Range .

Let the Input Length be denoted as \(n\), and let \(TR\) be a random variable denoting the True Range . Then we denote the Average True Range at Index \(t\) for the given Length as \(ATR_t(n)\), and we calculate it in terms of a Simple Moving Average for \(t \geq n - 1\) as follows.

Note : Depending on the setting of the Input Moving Average Type , the Simple Moving Average in the above formula could be replaced with an Exponential Moving Average , a Linear Regression Moving Average , a Weighted Moving Average , a Wilders Moving Average , a Simple Moving Average - Skip Zeros , or a Smoothed Moving Average .

This study can be used on any chart bar timeframe. However, if the intent is to get an average of the daily true range, it does require that it is used on a Historical Daily Chart with a time period of 1 day per bar.

A Historical Daily chart can be opened with File >> Find Symbol >> [select symbol] >> Open Historical Chart .

Once you add this study to a Historical Daily chart, the study can be overlaid to an Intraday chart by using the Study/Price Overlay study.


#### Inputs

- Moving Average Length

- Moving Average Type


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Average_True_Range.19.scss

*Last modified Monday, 17th February, 2025.