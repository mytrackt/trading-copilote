# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=352


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Volume Weighted Average Price - VWAP - Rolling with Standard Deviation Lines


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Volume Weighted Average Price (VWAP) - Rolling with Standard Deviation Lines

- Description

- Displaying or Hiding Standard Deviation/Fixed Offset Band Lines

- Differences Between VWAP and Standard Deviation Lines On Different Timeframe Bars

- Standard Deviation Band Calculation

- Inputs


### Description

The Volume Weighted Average Price (VWAP) - Rolling with Standard Deviation Lines study calculates and displays the volume weighted average price over the specified period of time for the symbol of the chart.

This calculation gives greater weight to trade prices that have a higher volume.

This study uses the same calculation method as the standard Volume Weighted Average Price (VWAP) study does, except that for every bar in the chart it calculates volume weighted average price over the specified period of time starting at the bar going back by that specified period of time. So the calculation period is continuously rolling.

This differs from the standard Volume Weighted Average Price study which segments the overall time in the chart by the specified period of time and incrementally calculates the volume weighted average price at each bar within that period of time and resets itself when a new time segment is encountered. For example, for a 1 Day period, the segment will start at the beginning of the trading day and end at the end of the trading day according to the Session Times for the chart. At each time segment there is a set starting point.

The study also supports calculating and displaying Standard Deviation/Fixed Offset band lines. In the case of the Standard Deviation calculation, this is based on the volume weighted difference of the selected Input Data , like the closing price of the chart bars, and the VWAP value.


#### Displaying or Hiding Standard Deviation/Fixed Offset Band Lines

Up to 4 Standard Deviation/Fixed Offset lines based upon the Volume Weighted Average Price line can be displayed. To display these standard deviation band lines, follow the steps below.

- Open the Study Settings window for the Volume Weighted Average Price - Rolling study.

- Select the Subgraphs tab.

- The Standard Deviation/Fixed Offset lines are labeled Top Band 1-4 and Bottom Band 1-4 . To make a line visible, set its Draw Style to Dash . To hide it, set its Draw Style to Ignore .

Refer to the description for Band # Std. Deviation Multiplier/Fixed Offset , for information about how these lines are calculated.


#### Differences Between VWAP and Standard Deviation Lines On Different Timeframe Bars

Refer to Differences Between VWAP and Standard Deviation Lines On Different Timeframe Bars for the standard Volume Weighted Average Price study.

Values calculated by this study will be different from the non-rolling Volume Weighted Average Price because a rolling period of time is used and there is no resetting at the beginning of a new time segment.


#### Standard Deviation Band Calculation

Refer to Standard Deviation Band Calculation .


#### Inputs

- Input Data : For this particular study, the only valid Input types would be Open, High, Low, Last/Close. Only prices. It cannot be a volume.

- Volume Type to Use : Sets the data type to be used for the calculation. The following options are available: Total Volume Bid Volume Ask Volume When using either Bid Volume or Ask Volume the option for Base on Underlying Data must be set to Yes or the calculation will be based on the Total Volume.

- Total Volume

- Bid Volume

- Ask Volume

- Base on Underlying Data : This Input setting only applies to Intraday charts and not to Historical charts. When this Input is set to No , which is the default, then the price and volume data for the calculations are based on the bars in the chart. The last trade price of the bar is used, which is the default, and the total volume of the chart bar is used. To base the calculations on the underlying price and volume data which is more detailed than the chart bars, set this Input to Yes . When this Input is set to Yes , the chart may be automatically reloaded to load in the more detailed Volume at Price data. It is recommended when using this setting that since Intraday charts are required, select Chart >> Chart Settings and select Chart Data Type >> Intraday Chart Only to always ensure the chart is set to use Intraday data. To ensure there is the most detailed data for the calculations, a Tick by Tick Data Configuration is recommended.

- Time Period Type : Sets the type of time period for the calculation. This Input works in conjunction with Time Period Length . The Time Period Type can be one of the following: Days - Trading Days : With this setting, the Time Period Length Input specifies the number of Trading days the VWAP calculation is performed over at each chart bar. When using Days - Trading Days the VWAP calculation is rolling day by day and not bar by bar. For example, if Time Period Length is set to 3, then for any given bar within a trading day, the VWAP calculation includes the data for that particular chart bar, all the chart bars for the trading day that bar is within, and the prior 2 trading days going back to the Session Start Time on that second prior day. For rolling bar by bar, set Time Period Type to Days - 24 Hour Period or Minutes and specify the number of Days or Minutes with the Time Period Length Input. A trading day is from the Session >> Start Time to the End Time settings in the chart. For complete details, refer to Session Times . With Days - Trading Days , every time a new day begins, you can and most likely will notice an obvious shift in the VWAP value because the furthest day back in time that was previously being used in the VWAP calculation is no longer included. It is not a bar to bar rollover, but a day to day rollover. If you want a bar to bar rollover, then set this Input to Days - 24 Hour Period instead. Days - 24 Hour Period : With this setting, the Time Period Length Input specifies the number of rolling 24-hour periods (days) the calculation is performed over. When using Days - 24 Hour Period the calculation is rolling bar by bar. Minutes : The Time Period Length Input specifies the number of minutes. The VWAP calculation will be rolling bar by bar. Bars : The Time Period Length Input specifes how many bars the VWAP calculation is performed over The VWAP calculation will be rolling bar by bar.

- Days - Trading Days : With this setting, the Time Period Length Input specifies the number of Trading days the VWAP calculation is performed over at each chart bar. When using Days - Trading Days the VWAP calculation is rolling day by day and not bar by bar. For example, if Time Period Length is set to 3, then for any given bar within a trading day, the VWAP calculation includes the data for that particular chart bar, all the chart bars for the trading day that bar is within, and the prior 2 trading days going back to the Session Start Time on that second prior day. For rolling bar by bar, set Time Period Type to Days - 24 Hour Period or Minutes and specify the number of Days or Minutes with the Time Period Length Input. A trading day is from the Session >> Start Time to the End Time settings in the chart. For complete details, refer to Session Times . With Days - Trading Days , every time a new day begins, you can and most likely will notice an obvious shift in the VWAP value because the furthest day back in time that was previously being used in the VWAP calculation is no longer included. It is not a bar to bar rollover, but a day to day rollover. If you want a bar to bar rollover, then set this Input to Days - 24 Hour Period instead.

- Days - 24 Hour Period : With this setting, the Time Period Length Input specifies the number of rolling 24-hour periods (days) the calculation is performed over. When using Days - 24 Hour Period the calculation is rolling bar by bar.

- Minutes : The Time Period Length Input specifies the number of minutes. The VWAP calculation will be rolling bar by bar.

- Bars : The Time Period Length Input specifes how many bars the VWAP calculation is performed over The VWAP calculation will be rolling bar by bar.

- Time Period Length : Sets the quantity to be used with Time Period Type . For example, for a period of 1 Day, set this to 1 and set Time Period Type to Days - Trading Days . In the case of a Length of 1 with Time Period Type set to Days - Trading Days the calculation will be done on the current trading day only.

- Number of Days to Calculate : This Input sets the number of days in the chart that the Volume Weighted Average Price calculations will be done over relative to the last Date in the chart. The default value is 10. It is recommended to set this as small as is needed to minimize the calculation time since the study can take a significant amount of time to do calculations across many days of data. This setting is not the same as Time Period Length . It does not control the length of the calculation for a particular chart bar. The very first bar in the chart where the calculation begins at according to the Number of Days to Calculate Input will not have any prior data reference. Therefore, the VWAP result at that chart bar is based upon just that one bar. On the next bar in the chart after that first bar, will only have two bars in the VWAP calculation. It is not until the bar in the chart that has a sufficient number of prior bars to calculate the VWAP according to the Time Period Type and Time Period Length Inputs, will then give a correct result. Until that bar, the calculation is considered a developing calculation. It is for the reason described in the prior paragraph that when you perform a full recalculation of the chart through Chart >> Recalculate after additional data has been added to the chart during real-time updating or during a replay, that you can notice a change in the VWAP values because at prior chart bars where previously there was sufficient underlying VWAP data, there may no longer be sufficient underlying VWAP data relative to the last Date in the chart based on this Input setting. It is recommended that this setting be set twice the Time Period Length Input setting to ensure there is sufficient data for the VWAP calculation at each chart bar during the length of the calculation.

- Start Date-Time : This Input can optionally be set to a starting Date-Time to begin the calculations at for the Volume Weighted Average Price study. It is necessary to specify both the Date and the Time together. To disable the Start Date-Time Input, set it to a date before the first date in the chart. This will effectively disable it.

- Exclude Weekends in Date Look Back : When this Input is set to Yes , Saturday and Sundays are skipped when determining how many days back to include in the calculation according to the Time Period Length Input. This input applies when Time Period Type is set to Days - Trading Days or Days - 24 Hour Period . This option must still be set to Yes even when weekends are excluded from the chart in Chart >> Chart Settings >> Session Times . You need to consider, as could be the case when using a far Eastern world time zone, that there can be trading on a Saturday which is considered Friday in other time zones. This happens when using Reversed Session Times , or just based upon the very fact that trading is indeed on Saturday in the time zone of the chart. In this particular case you must set the Exclude Weekends in Date Look Back Input to No to prevent skipping of this valid Saturday data when establishing the starting point of the calculations based upon the Time Period Type and Time Period Length Inputs. Or avoid using a far Eastern time zone.

- Minimum Required Time Period as Percent for Skip Days : This Input only applies when the Time Period Type is set to Days - Trading Days or Days - 24 Hour Period . This study employs special logic when looking back at the previous days, to determine if there is sufficient data. If there is insufficient data, it looks back to the period before the first period it originally referenced. This is very useful for holidays and Sunday trading. There is no need to remove data from periods where there is insufficient data. You can control the functioning of this period skipping feature with this Input. For example, if you want there to be at least 50% or more of the bars needed for 1 day period, then set this Input to 50. When this study determines the number of bars that are needed for a period, it does not consider the Session Times settings in Chart >> Chart Settings . For example, if you are just including the Day Session only in your chart, then there are going to be fewer bars available. Therefore, you need to consider this when setting this percentage. So if you have less than the full 24 hour Session of bars in the chart, then you will want to use a lower percentage to avoid skipping periods. It does not make sense to set this input to 100. This will only likely trigger unnecessary skipping when you do not intend that.

This Input only applies when the Time Period Type is set to Days - Trading Days or Days - 24 Hour Period .

This study employs special logic when looking back at the previous days, to determine if there is sufficient data. If there is insufficient data, it looks back to the period before the first period it originally referenced.

This is very useful for holidays and Sunday trading. There is no need to remove data from periods where there is insufficient data. You can control the functioning of this period skipping feature with this Input. For example, if you want there to be at least 50% or more of the bars needed for 1 day period, then set this Input to 50.

When this study determines the number of bars that are needed for a period, it does not consider the Session Times settings in Chart >> Chart Settings . For example, if you are just including the Day Session only in your chart, then there are going to be fewer bars available. Therefore, you need to consider this when setting this percentage. So if you have less than the full 24 hour Session of bars in the chart, then you will want to use a lower percentage to avoid skipping periods.

It does not make sense to set this input to 100. This will only likely trigger unnecessary skipping when you do not intend that.

- Standard Deviation Band Calculation Method : This can be set to VWAP Variance , Fixed Offset , Standard Deviation , or Percentage . For the formulas for each, refer to Standard Deviation Band Calculation .

- Band # Std. Deviation Multiplier/Fixed Offset : When the standard deviation Top # Band and Bottom # Band Subgraphs are set to be displayed, this Input specifies how far the band lines are from the Volume Weighted Average Price line. When the Standard Deviation Band Calculation Method Input is set to VWAP Variance or Standard Deviation , then this Input specifies the value multiplied by the VWAP Variance or Standard Deviation. For example, if the Input is set to 2.0, then the band would be offset by 200% of the Standard Deviation. When the Standard Deviation Band Calculation Method Input is set to Fixed Offset , then this Input becomes a fixed offset and is used to offset the Bands from the Volume Weighted Average Price by the specified amount. Bands 1-4 are offset by the exact amounts. When the Standard Deviation Band Calculation Method Input is set to Percentage , then this Input becomes the percentage of the Volume Weighted Average Price that is used to offset the Bands from the Volume Weighted Average Price. For example, if the Input is set to 2.0, then the band would be offset by 2% of the Volume Weighted Average Price.

*Last modified Thursday, 20th June, 2024.