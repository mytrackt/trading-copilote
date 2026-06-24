# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=292


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Cumulative Delta Bars - Volume


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Cumulative Delta Bars - Volume

- Description

- Calculation Method

- Using Drawing Tools on Cumulative Delta Bars

- Resolving Cumulative Delta Bars Differences

- Cumulative Delta Bars Study with Volume Filtering

- Cumulative Delta Bars Study with Different Volume Filtering

- Inputs


### Description

Cumulative Delta Bars - Volume is the cumulative sum, over the data in the chart or the trading day, of the difference between the Ask Volume and the Bid Volume, displayed as High-Low CandleStick bars.

The study only works on Intraday charts.

It needs to be understood that the output of this study will likely change after the chart data is reloaded because the starting Date-Time in the chart can be different in this case and this affects all of the subsequent calculations. To avoid this problem, set the Reset at Start of Trading Day Input with this study to Yes.

Unlike other charting programs, the Cumulative Delta Bars - Volume study in Sierra Chart is 100% correctly calculated and it is based upon accurate Bid Volume and Ask Volume. For example, based on user feedback we have heard that Trading View does not provide a true Cumulative Delta Bars Volume study. Therefore, you cannot make a comparison to what Sierra Chart displays with this study to other programs.


#### Calculation Method

- The difference between the AskVolume and the BidVolume is calculated during the creation of each bar. The definition of AskVolume is the volume of trades that occurred at the best Ask price or higher. The definition of BidVolume is the volume of trades that occurred at the best Bid price or lower. If a trade occurs between the Bid and Ask, there is a special algorithm to assign the volume either to the Bid side or the Ask side. In this case, this is based upon whether the trade is an uptick or a downtick. During the creation of a bar, the volume of trades at the Ask is accumulated and the volume of trades at the Bid is accumulated. So in this step, the current difference between total AskVolume and BidVolume for a bar is calculated the time of the trade.

- The maximum and the minimum of the difference calculated in the prior step are maintained for each chart bar. This is called the DifferenceHigh and the DifferenceLow .

- CDB = Cumulative Delta Bars in the following description.

- A CDB candlestick Open is set to the prior CDB candlestick Close. If there is no prior candlestick or the study is set to reset at the start of the trading day, then this is set to 0. The Open is adjusted to be within the range of the High and Low of the Cumulative Delta chart bar at the same index if it is out of that range. So it may not always be equal to 0 in this case.

- A CDB candlestick High is set to the prior CDB candlestick Close + the DifferenceHigh for the bar.

- A CDB candlestick Low is set to the prior CDB candlestick Close + the DifferenceLow for the bar.

- A CDB candlestick Close is set to the prior CDB candlestick Close + (the AskVolume - the BidVolume for the main price bar).

- In the case where Reset at Start of Trading Day Input is set to Yes, the CDB candlestick Open, High, Low, Close bar values are reset back to 0. Each of these values also start at 0 at the beginning of the chart.

Important Note : In order for the study to provide an accurate result the Intraday Data Storage Time Unit should be 2 Seconds or less. Otherwise, the results of this study will be less accurate. For the highest accuracy use tick by tick data. For instructions, refer to Tick by Tick Data Configuration .

The coloring of these bars is performed using the standard rules for an Up or a Down bar. If the Close is greater than the Open , then the bar is considered to an Up bar and uses the color defined for an Up bar; whereas, if the Close is less than the Open , then the bar is considered to be a Down bar and uses the color defined for a Down bar. What must be considered, in this case, is that the definition of Open and Close does not involve prices, but rather involves the differences between the Ask Volume and the Bid Volume. See the definitions above for the Open and the Close to further understand how this is calculated.

This study requires historical Bid Volume and Ask Volume data from the Data or Trading service Sierra Chart is using. If it is not available, then during the times Sierra Chart is not connected to the data feed, Cumulative Delta Bars-Volume will be zero or stay the same. On the Supported Data/Trading Services page, the documentation for each service indicates whether historical Bid Volume and Ask Volume is provided.

If a Data/Trading service does not provide historical Bid Volume and Ask Volume, then stay connected to that service as much as possible so that this data can be stored in real-time by Sierra Chart from the real-time data feed.


#### Using Drawing Tools on Cumulative Delta Bars

It is possible to use any of the Drawing Tools on the Cumulative Delta Bars study. However, there is one special consideration. Since the calculations in the study are cumulative since the first Date-Time in the chart in the case where you have set Reset at Start of Trading Day to No , the bar values for a specific Date-Time in the chart when each new trading day begins and the chart is reloaded, will change.

The effect of this is you will notice that Chart Drawings appear to be moving. Rather what is happening is the Cumulative Delta Bars are moving relative to the Chart Drawings. There is no automated method to realign the Chart Drawings. You would have to adjust them manually.

There are two possible solutions to this. You could set the Reset at Start of Trading Day Input to Yes , to have the Cumulative Delta Bars reset every day. This will eliminate the problem.

The other possibility is for each new day that occurs, increase Chart >> Chart Settings >> Days to Load by 1. Or select Use Date Range , set the From date to a specific date, and leave the To date at 0. For complete details, refer to Use Date Range From/To .


#### Resolving Cumulative Delta Bars Differences

You may notice a difference with Cumulative Delta Bars values compared to another chart within your own copy of Sierra Chart or compared to another user running Sierra Chart.

Cumulative Delta Bars can also change when a chart is reloaded which will happen when you open a Chartbook containing the chart which contains the study, you manually reload the chart, or when historical data is re-downloaded, either partially or fully, for the symbol of the chart.

This section does not provide help comparing Cumulative Delta Bars to other charting and trading programs, since there are too many variables involved to get an exact match. Although the information here may give you a clue as to what the issue can be.

Confirm the following are the same between the two charts or copies of Sierra Chart used in the comparison.

- Check that the chart has the same Cumulative Delta Bars study. There are 3 different versions of these.

- The same market data feed needs to be used between the two copies of Sierra Chart you are comparing. A data feed that provides consistent market data needs to be used. Most, but not all, Data/Trading services Sierra Chart supports provide a consistent market data feed. All of the Sierra Chart provided Data services do provide a consistent market data feed.

- Sierra Chart needs to be set to store Tick by Tick Data in Intraday chart data files.

- The Time Zone in Global Settings >> Data/Trade Service Settings needs to be the same if you are comparing between two different copies of Sierra Chart.

- The Session Times in Chart >> Chart Settings need to be 100% identical. On the Session Times tab of the Chart Settings window, the New Bar At Session Start and Load Weekend Data options need to be set the same. It is strongly recommended that New Bar At Session Start be set to Yes. If it is set to No, then this means when the chart data is reloaded with Chart >> Reload and Recalculate or the chart is reloaded for some other reason, then the Cumulative Delta Bars will likely change after a chart reload since the starting Date-Time in the chart can likely change.

- The Days to Load or the Date Range From Date Chart Settings must be the same. This only applies if Reset at Start of Trading Day Input with the Cumulative Delta Bars study is set to No . Otherwise, these settings are not going to be relevant. If the Reset at Start of Trading Day Input is set to No , then it is 100% critical that there is Tick by Tick data for all of the data in the chart data file that is loaded into the chart. With a service like IQ Feed that provides a limited amount of historical Tick data during market hours, there is a good probability this will not be the case.

- If the Reset at Start of Trading Day Input is set to No , then select Chart >> Reload and Recalculate to make sure the chart is only loading the amount of data specified in the Chart >> Chart Settings >> Data Limiting tab and not more.

- To ensure the data is consistent between two different copies of Sierra Chart, re-download the data in the Intraday chart by selecting Edit >> Delete All Data and Download .


#### Cumulative Delta Bars Study with Volume Filtering

To add volume filtering to the result of the Cumulative Delta Bars study, use the Volume Filtering settings in Chart >> Chart Settings . It is supported to filter volume both above and below specific volume/quantity values.


#### Cumulative Delta Bars Study with Different Volume Filtering

Follow the instructions below to add another Cumulative Delta Bars study to the chart that uses different Volume Filtering compared to the Volume Filtering already set on the current chart.

- Go to the chart and select Chart >> Duplicate Chart to create an identical chart.

- On this duplicated chart select Chart >> Chart Settings .

- Set the Volume Filtering in Chart >> Chart settings as you require.

- Add the Cumulative Delta Bars - Volume / Trades / Up/Down Tick Volume study to this chart. For instructions, refer to Adding Studies .

- Go to the original chart, not the duplicated one, and add the Study/Price Overlay study to overlay the Cumulative Delta Bars study on the duplicated chart. For complete instructions, refer to Study / Price Overlay Study .


#### Inputs

- Reset at Start of Trading Day : When this Input is set to Yes , then the cumulative sum calculation is reset at the start of the trading day. The start of the trading day is determined from the Session Times in Chart >> Chart Settings . This will be the Start Time or if the Evening Session is enabled, then it will be the Evening Start Time . When it is reset at the start of the trading day, the opening value which will be equal to the Ask Volume and Bid Volume difference at the first trade or Intraday data record, will not be at zero. This is normal and expected.

- Reset at Both Session Start Times : When this Input is set to Yes , then the Input Reset at Start of Trading Day is implied to always be on and the description for that Input applies. Additionally, there is another reset which occurs at the Evening Start Time if the Evening Session is enabled for the chart.

*Last modified Friday, 24th January, 2025.