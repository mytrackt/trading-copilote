# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=221


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Bollinger Squeeze


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Bollinger Squeeze

- Description

- Inputs

- Spreadsheet


### Description

This study calculates and displays a Bollinger Squeeze of the First Type for the data specified by the Input Data Input. The calculations of this study include calculations of Bollinger Bands and Keltner Bands . See those studies for an explanation of the notation used here.

The Inputs are denoted as follows. \(X\) is the Input Data , \(n_B\) is the Bollinger Bands Length , \(v_B\) is the Bollinger Bands Multiplier , \(n_K\) is the Keltner Bands Length , \(n_{ATR}\) is the Keltner True Range MovAvg Length , and \(v_K\) is the Keltner Bands Multiplier . Note that both the Top and Bottom Keltner Bands have the same Multiplier Input, unlike in the Keltner Channel study. The moving average types for the Bollinger Bands, the Average True Range, and the Keltner Bands are all controlled via the Moving Average Type for Internal Calculation Input.

This study displays two Subgraphs for \(t \geq \max\{n_B,n_K,n_{ATR}\} - 1\): The Bands Ratio and the Squeeze Indicator.

The Bands Ratio at Index \(t\) is denoted as \(BR_t(X,n_B,v_B,n_K,n_{ATR},v_K)\), and it is computed as follows.

The Bands Ratio Subgraph is displayed as a bar graph that is colored as follows.

- \(BR_t(X,n_B,v_B,n_K,n_{ATR},v_K) \geq 0 \Rightarrow\) Green

- \(BR_t(X,n_B,v_B,n_K,n_{ATR},v_K) < 0 \Rightarrow\) Red

The Squeeze Indicator is plotted at the zero line. By default, this Subgraph is displayed as a sequence of points that are colored as follows. \(TB_t^{(B)}(X,n_B,v_B) > TB_t^{(K)}(X,n_K,n_{ATR},v_K)\) and \(BB_t^{(B)}(X,n_B,v_B) < BB_t^{(K)}(X,n_K,n_{ATR},v_K) \Rightarrow\) Green \(TB_t^{(B)}(X,n_B,v_B) \leq TB_t^{(K)}(X,n_K,n_{ATR},v_K)\) or \(BB_t^{(B)}(X,n_B,v_B) \geq BB_t^{(K)}(X,n_K,n_{ATR},v_K) \Rightarrow\) Red Inputs [ Link ] - [ Top ] Input Data Moving Average Type for Internal Calculation Keltner Bands Length Keltner True Range MovAvg Length Keltner Bands Multiplier Bollinger Bands Length Bollinger Bands Multiplier Spreadsheet [ Link ] - [ Top ] The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder . Open it through File >> Open Spreadsheet . Bollinger_Squeeze.221.scss

- \(TB_t^{(B)}(X,n_B,v_B) > TB_t^{(K)}(X,n_K,n_{ATR},v_K)\) and \(BB_t^{(B)}(X,n_B,v_B) < BB_t^{(K)}(X,n_K,n_{ATR},v_K) \Rightarrow\) Green

- \(TB_t^{(B)}(X,n_B,v_B) \leq TB_t^{(K)}(X,n_K,n_{ATR},v_K)\) or \(BB_t^{(B)}(X,n_B,v_B) \geq BB_t^{(K)}(X,n_K,n_{ATR},v_K) \Rightarrow\) Red


#### Inputs

- Input Data

- Moving Average Type for Internal Calculation

- Keltner Bands Length

- Keltner True Range MovAvg Length

- Keltner Bands Multiplier

- Bollinger Bands Length

- Bollinger Bands Multiplier


#### Spreadsheet

The spreadsheet below contains the formulas for this study in Spreadsheet format. Save this Spreadsheet to the Data Files Folder .

Open it through File >> Open Spreadsheet .

Bollinger_Squeeze.221.scss

*Last modified Tuesday, 31st January, 2023.