# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=296


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Cumulative Delta Bars - Trades


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Cumulative Delta Bars - Trades

- Description

- Calculation Method

- Inputs


### Description

Cumulative Delta Bars - Trades is the cumulative sum, over the data in the chart or the trading day, of the difference between the number of trades at the Ask price and the number of trades at the Bid price, displayed as High-Low CandleStick bars.


#### Calculation Method

- The difference between the number of trades at the Ask price or higher and the number of trades at the Bid price or lower is calculated during the creation of each bar.

- The maximum and the minimum of the difference of the number of trades at the Ask price or higher and the number of trades at the Bid price or lower calculated in the prior step are maintained for each chart bar. This is called the DifferenceHigh and the DifferenceLow .

- CDB = Cumulative Delta Bars in the following description.

- A CDB candlestick Open is set to the prior CDB candlestick Close. If there is no prior candlestick or the study is set to reset at the start of the trading day, then this is set to 0. The Open is adjusted to be within the range of the High and Low of the Cumulative Delta chart bar at the same index if it is out of that range. So it may not always be equal to 0 in this case.

- A CDB candlestick High is set to the prior CDB candlestick Close + the DifferenceHigh for the bar.

- A CDB candlestick Low is set to the prior CDB candlestick Close + the DifferenceLow for the bar.

- A CDB candlestick Close is set to the prior CDB candlestick Close + (the AskVolume - the BidVolume for the main price bar).

- In the case where Reset at Start of Trading Day Input is set to Yes, the CDB candlestick Open, High, Low, Close bar values are reset back to 0. Each of these values also start at 0 at the beginning of the chart.

You are able to view the number of trades at the ask price or higher by adding the study Number of Trades-Ask to the chart. You are able to view the number of trades at the bid price or lower by adding the study Number of Trades-Bid to the chart.

Important Note : In order for the study to provide an accurate result there must be tick by tick data in the Intraday chart data file. Otherwise, the results of this study will not be accurate. To be certain Sierra Chart is maintaining tick by tick data in the Intraday chart data files, refer to Tick by Tick Data Configuration .

Using Drawing Tools on Cumulative Delta Bars .

Resolving Cumulative Delta Bars Differences .

Cumulative Delta Bars Study with Volume Filtering .

Cumulative Delta Bars Study with Different Volume Filtering .


#### Inputs

- Reset at Start of Trading Day : When this Input is set to Yes , then the cumulative sum calculation is reset at the start of the trading day. The start of the trading day is determined from the Session Times in Chart >> Chart Settings . This will be the Start Time or if the Evening Session is enabled, then it will be the Evening Start Time . When it is reset at the start of the trading day, the opening value which will be equal to the Ask Volume and Bid Volume difference at the first trade or Intraday data record, will not be at zero. This is normal and expected.

- Reset at Both Session Start Times : When this Input is set to Yes , then the Input Reset at Start of Trading Day is implied to always be on and the description for that Input applies. Additionally, there is another reset which occurs at the Evening Start Time if the Evening Session is enabled for the chart.

*Last modified Friday, 24th January, 2025.