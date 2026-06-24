# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=35


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Momentum


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Momentum

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays the Momentum of the data specified by the Input Data Input.

Let \(X\) be a random variable denoting the Input Data , and let \(X_t\) be the value of the Input Data at Index \(t\). Let the Input Length be denoted as \(n\). The Momentum at Index \(t\) for the given Inputs is denoted as \(M_t(X,n)\), and we compute it for \(t \geq n\). The method of computation depends on the setting of the Momentum Type Input, as decribed below.

If Momentum Type is set to Difference , then \(M_t(X,n)\) is calculated as follows.

If Momentum Type is set to Quotient , then \(M_t(X,n)\) is calculated as follows.


#### Inputs

- Input Data

- Length

- Momentum Type : This custom Input determines whether the Difference or Quotient version of the Momentum formula is used.


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Momentum.35.scss

*Last modified Friday, 24th January, 2025.