# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=188


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Chande Momentum Oscillator


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Chande Momentum Oscillator

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays the Chande Momentum Oscillator of the data specified by the Input Data Input, as well as three horizontal lines determined by the user.

Let \(X\) be a random variable denoting the Input Data , and let \(X_t\) be the value of the Input Data at Index \(t\). The Up Change and Down Change of the Input Data at Index \(t\) are denoted as \(U(X)\) and \(D(X)\), respectively, and we compute them for \(t > 0\) as follows.

Let the Input CMO Length be denoted as \(n_{CMO}\). Then we denote the Chande Momentum Oscillator at Index \(t\) for the given Inputs as \(CMO_t(X,n_{CMO})\), and we compute it for \(t \geq n_{CMO}\) in terms of Moving Summations as follows.

Finally, the Line 1 , Line 2 , and Line 3 Inputs determine the levels of three horizontal lines that are displayed with \(CMO_t(X,n_{CMO})\).


#### Inputs

- Input Data

- CMO Length

- Line 1

- Line 2

- Line 3


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Chande_Momentum_Oscillator.188.scss

*Last modified Friday, 24th January, 2025.