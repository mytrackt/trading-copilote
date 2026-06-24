# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=13


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> ADX


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# ADX

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays the Welles Wilder's Average Directional Movement Index (ADX).

The ADX is based on calculations similar to those used in the Directional Movement Index . Just as in that study, the DX Length Input is denoted as \(n_{DX}\). The Directional Indicators \(DI_t^{(+)}\left(n_{DX}\right)\) and \(DI_t^{(-)}\left(n_{DX}\right)\) are calculated slightly differently here, as shown below.

The Directional Index at Index \(t\) is denoted as \(DX_t(n_{DX})\). This is initially equal to zero, and we compute it for \(t \geq 0\) as follows.

Let the DX Mov Avg Length Input be denoted as \(n_{ADX}\). We denote the ADX at Index \(t\) as \(ADX_t(n_{DX},n_{ADX})\), and we compute it in terms of a Wilders Moving Average for \(t \geq n_{DX} + n_{ADX} - 1\) as follows.

For an explanation of the Sigma (\(\Sigma\)) notation for summation, refer to our description here .


#### Inputs

- DX Length

- DX Mov Avg Length


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

ADX.13.scss

*Last modified Sunday, 29th January, 2023.