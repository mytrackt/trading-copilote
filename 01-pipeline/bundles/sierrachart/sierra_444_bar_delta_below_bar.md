# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=444


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Bar Delta Below Bar


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Bar Delta Below Bar

- Description

- Inputs

- Spreadsheet


### Description

This study displays the difference between the Ask Volume and the Bid Volume for each chart bar. The value of this difference at Index \(t\) is denoted as \(V^{(ask)}_t - V^{(bid)}_t\), and it is displayed on the chart as text.

The text is displayed below each bar. Let the Offset in Ticks Input be denoted as \(k\), and let the Tick Size be denoted as \(s\). Then the location of the text containing the value of \(V^{(ask)}_t - V^{(bid)}_t\) is determined by \(L_t - k \cdot s\), where \(L_t\) is the Low Price at Index \(t\).

The coloring of the text is controlled by the Subgraph Primary and Secondary colors. For more information, refer to Studies >> Subgraphs Tab >> Color .

Depending upon the Data or Trading service you are using, you may not receive historical Ask Volume when historical data is downloaded from the service. Not all services will provide this.


#### Inputs

- Offset in Ticks : This sets the distance from the bottom of the bar for the display of the text. The distance is stated in Ticks as defined for the chart in the Tick Size setting.


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Bar_Delta_Below_Bar.444.scss

*Last modified Tuesday, 31st January, 2023.