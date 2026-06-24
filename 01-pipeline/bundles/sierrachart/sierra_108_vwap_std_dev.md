# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=108


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Volume Weighted Average Price - VWAP - with Standard Deviation Lines


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Volume Weighted Average Price (VWAP) with Standard Deviation Lines

- Description

- Displaying or Hiding Standard Deviation/Fixed Offset Band Lines

- Differences Between VWAP and Standard Deviation Lines On Different Timeframe Bars

- Differences with VWAP Between Historical Daily and Intraday Charts

- Standard Deviation Band Calculation

- Inputs

- Draw Anchored VWAP Description Tool Usage Step by Step Instructions to Configure the Draw Anchored VWAP Tool Modifying Manually Drawn Anchored VWAP Erasing Drawn Anchored VWAP Drawing Tool Configuration

- Description

- Tool Usage

- Step by Step Instructions to Configure the Draw Anchored VWAP Tool

- Modifying Manually Drawn Anchored VWAP

- Erasing Drawn Anchored VWAP

- Drawing Tool Configuration


### Description

This study calculates and displays the Volume Weighted Average Price (VWAP) over the specified period of time for the symbol of the chart. The period of time is set by the Time Period Type and Time Period Length Inputs.

This calculation gives greater weight to trade prices that have a higher volume. The calculation resets at the begining of each new period in the chart.

Let \(X\) be a random variable denoting the Input Data , let \(X_i\) be the value of the Input Data at chart bar \(i\), let \(V_i\) be the Volume at chart bar \(i\), and let \(n\) be the length of the period in chart bars for the calculation as specified by the Inputs Time Period Type and Time Period Length .

We begin by computing the Period Volume \(V_P\) for the period.

Then the Volume Weighted Average Price during the length for the given Inputs is denoted as \(VWAP(X,n)\), and is calculated as follows.

The start of the trading day is determined from the Session Times set in Chart >> Chart Settings . For example, when the Time Period Length and Time Period Type Study Inputs are set to 1 Day, then the calculations will begin at the start of each trading day according to the Session Times and end at the end of the trading day.

The study also supports calculating and displaying Fixed Offet/Standard Deviation band lines, which the calculation is explained further down on this page.


### Displaying or Hiding Standard Deviation/Fixed Offset Band Lines

Up to 4 Standard Deviation/Fixed Offset lines based upon the Volume Weighted Average Price line can be displayed. To display these standard deviation band lines, follow the steps below.

- Open the Study Settings window for the Volume Weighted Average Price study on the chart. For instructions, refer to Adding/Modifying Chart Studies .

- Select the Subgraphs tab.

- The Standard Deviation/Fixed Offset lines are labeled Top Band 1-4 and Bottom Band 1-4 . To make a line visible, set its Draw Style to Dash or another visible Draw Style. To hide it, set its Draw Style to Ignore .

Refer to the description for the Band # Std. Deviation Multiplier/Fixed Offset Input, for information about how these lines are calculated.


### Differences Between VWAP and Standard Deviation Lines On Different Timeframe Bars

The VWAP is a fairly simple calculation, but is very dependent on the data that it is calculated using. For the highest accuracy and the same values on different timeframe bars, it is necessary to set the Base on Underlying Data Input to Yes , so that the study uses the underlying data that makes up the bars.

It is also necessary to have tick by tick data in the chart data file for the highest accuracy. Refer to Tick by Tick Data Configuration .

When you compare VWAPs on different timeframe bars, the values will be the same when using Base on Underlying Data so long as the starting time for the first bar used in the calculation for the VWAP period, is the same among the different bar timeframes. If Base on Underlying Data is set to No, the values will be different and this is expected.

It is expected for the VWAP values to be different among different chart bar timeframe settings when using Number of Trades, Volume, Range, Reversal, Renko, Delta Volume, Price Change, Point and Figure Bars. This is because there is not a consistent starting time for a bar with these bar types. Enabling Chart >> Chart Settings >> New Bar at Session Start can help with this.

The Standard Deviation Lines for the Volume Weighted Average Price on different timeframe bars can be different. This is because the Standard Deviation is calculated in part using the chart bar values, and the chart bar values can be significantly different between chart bar timeframes. For example, there is only every fifth value on a 5 minute bar chart versus a 1 minute bar chart.

Also refer to Resolving Differences of Chart Bars Between Charts .


### Differences with VWAP Between Historical Daily and Intraday Charts

The data in a Historical Daily data chart is different than the data in an Intraday chart. When the Base on Underlying Data Input is set the Yes, there will definitely be differences in the Volume Weighted Average Price calculation between Intraday and Historical Daily data charts. For more information, refer to

There will also be differences even when the Base on Underlying Data Input is set to No because Historical Daily charts have a higher volume per bar .

Another reason for a difference between Historical Daily charts and Intraday charts with the Volume Weighted Average Price calculation is that the closing price for each bar is different. Historical Daily charts use the official settlement as compared to the last trade price at the end of the day on Intraday data charts which are set to a 1 Day period.


### Standard Deviation Band Calculation

The following explanation of the standard deviation band calculation is when the Standard Deviation Band Calculation Method is set to VWAP Variance or Standard Deviation .

The Variance during one period for the given Inputs is denoted as \(Var(X,n)\), and is calculated as follows. \(V_P\) is documented above.

The Standard Deviation during the period for the given Inputs is denoted as \(SD(X,n)\), and is calculated as follows.

Next, the Offset during the period for the given Inputs is denoted as \(Off(X,n)\), and is calculated as follows for the given Standard Deviation Band Calculation Method .

- VWAP Variance : \(Off(X,n) = Var(X,n)\)

- Standard Deviation : \(Off(X,n) = SD(X,n)\) The Standard Deviation Bands are computed using a Multiplier \(b\). Let \(TB_j\) and \(BB_j\) be Top Band and Bottom Band number \(j\), respectively \((j=1,2,3,4)\). We compute the Bands for each Period as follows. \(TB_1 = VWAP + b\cdot Off(X,n)\) \(BB_1 = VWAP - b\cdot Off(X,n)\) \(TB_2 = VWAP + 2b\cdot Off(X,n)\) \(BB_2 = VWAP - 2b\cdot Off(X,n)\) \(TB_3 = VWAP + 3b\cdot Off(X,n)\) \(BB_3 = VWAP - 3b\cdot Off(X,n)\) \(TB_4 = VWAP + 4b\cdot Off(X,n)\) \(BB_4 = VWAP - 4b\cdot Off(X,n)\)

The Standard Deviation Bands are computed using a Multiplier \(b\). Let \(TB_j\) and \(BB_j\) be Top Band and Bottom Band number \(j\), respectively \((j=1,2,3,4)\). We compute the Bands for each Period as follows.


### Inputs

- Input Data

- Volume Type to Use : Sets the data type to be used for the calculation. The following options are available: Total Volume Bid Volume Ask Volume When using either Bid Volume or Ask Volume the option for Base on Underlying Data must be set to Yes or the calculation will be based on the Total Volume.

- Total Volume

- Bid Volume

- Ask Volume

- Base on Underlying Data : This Input setting only applies to Intraday charts and not to Historical charts. When this Input is set to No , which is the default, then the price and volume data for the calculations are based on the bars in the chart. The last trade price of the bar is used, which is the default, and the total volume of the chart bar is used. To base the calculations on the underlying price and volume data which is more detailed than the chart bars, set this Input to Yes . When this Input is set to Yes , the chart may be automatically reloaded to load in the more detailed Volume at Price data. It is recommended when using this setting that since Intraday charts are required, select Chart >> Chart Settings and select Chart Data Type >> Intraday Chart Only to always ensure the chart is set to use Intraday data. To ensure there is the most detailed data for the calculations, a Tick by Tick Data Configuration is recommended.

- Time Period Type : Sets the type of time period for the calculation. This Input works in conjunction with Time Period Length . For a 1 Day period, set this to Days . The number of Days specified always refers to calendar days and not trading days.

- Time Period Length : Sets the quantity to be used with Time Period Type . For example, for a period of 1 Day, set this to 1 and set Time Period Type to Days .

- Start Date-Time : This Input can optionally be set to a starting Date-Time to begin the calculations at for the Volume Weighted Average Price study. It is necessary to specify both the Date and the Time. You cannot just specify the Time only. The Time Period Length and Time Period Type Inputs still apply when using a Start Date-Time. The Start Date-Time setting does not refer to the starting time of day when the Time Period Length and Time Period Type is set to set to 1 Day. The purpose of this Input is to reduce the amount of calculations performed within the chart by starting at a particular Date-Time.

- Ignore Time Period Type and Length : When this Input is set to Yes , then the Inputs for Time Period Type and Time Period Length are ignored and the Volume Weighted Average Price is calculated from the first bar in the chart, or from the entered value for the Start Date-Time , if this Input is set.

- Standard Deviation Band Calculation Method : This can be set to VWAP Variance , Fixed Offset , Standard Deviation , or Percentage . For the formulas for each, refer to Standard Deviation Band Calculation .

- Band # Std. Deviation Multiplier/Fixed Offset : When the standard deviation Top # Band and Bottom # Band Subgraphs are set to be displayed, this Input specifies how far the band lines are from the Volume Weighted Average Price line. When the Standard Deviation Band Calculation Method Input is set to VWAP Variance or Standard Deviation , then this Input specifies the value multiplied by the VWAP Variance or Standard Deviation. For example, if the Input is set to 2.0, then the band would be offset by 200% of the Standard Deviation. When the Standard Deviation Band Calculation Method Input is set to Fixed Offset , then this Input becomes a fixed offset and is used to offset the Bands from the Volume Weighted Average Price by the specified amount. Bands 1-4 are offset by the exact amounts. When the Standard Deviation Band Calculation Method Input is set to Percentage , then this Input becomes the percentage of the Volume Weighted Average Price that is used to offset the Bands from the Volume Weighted Average Price. For example, if the Input is set to 2.0, then the band would be offset by 2% of the Volume Weighted Average Price.

- Volume Type to Use : The choices for this are Total Volume, Bid Volume, Ask Volume . When this is set to Bid Volume or Ask Volume it is necessary for Base on Underlying Data to be set to Yes. Otherwise, Total Volume will be used instead.


### Draw Anchored VWAP

This section documents how to manually draw an Anchored Volume Weighted Average Price study on the chart by using the Draw Anchored VWAP tool.

This lets you interactively draw a Volume Weighted Average Price on the chart which adds a Volume Weighted Average Price study for each Volume Weighted Average Price that you draw. You are able to interactively set the Starting Date-Time and the Ending Date-Time of the Volume Weighted Average Price.

It is supported to interactively modify the Starting Date-Time drawn VWAP directly on the chart using this functionality.

You cannot use the Draw Anchored VWAP tool with TPO Profile Charts . There is no support for this.


#### Description

This drawing tool allows you to interactively insert a Volume Weighted Average Price with Standard Deviation Lines study for the highlighted time range.

In the case where you want VWAP lines to repeat on the chart and have a specific time length per VWAP, you will need to directly add the Volume Weighted Average Price with Standard Deviation Lines study to the chart through Analysis >> Studies .

When drawing the VWAP lines interactively, you are controlling the starting Date-Time for the VWAP interactively. You are not controlling the High to Low range. That is completely dependent on the chart bars contained within the time range.


#### Tool Usage

- To select this tool, select Tools >> Draw Anchored VWAP on the menu. For other methods to select this particular Drawing Tool, refer to Selecting Tools .

- Left click on the chart with your Pointer at the bar where you want the VWAP lines to begin. The Date-Time of that bar will be the starting time of the VWAP lines.

- A Volume Weighted Average Price with Standard Deviation Lines study will be inserted starting at the selected point. If the required Volume at Price data is not already loaded in the chart, the chart will be reloaded with that data.


#### Step by Step Instructions to Configure the Draw Anchored VWAP Tool

The study Input settings for the inserted Volume Weighted Average price with Standard Deviation Lines study drawn with the Draw Anchored VWAP tool, can be preconfigured. Follow these instructions:

- The very first step is to define a Study Collection which will be applied when the Draw Anchored VWAP tool is used. Select Analysis >> Studies . In the Studies to Graph list, select the Volume Weighted Average Price study. Press the Add button. Press the Settings button. On the Settings and Inputs tab set the Inputs as required. Refer to Inputs . For the purpose of the configuration, the Start Date-Time Input is overridden with the value from the drawn Anchored VWAP. So this does not need to be set. All other Input settings are taken as you have set them and will be saved in the Study Collection referenced by the Draw Anchored VWAP configuration. Select the Subgraphs tab and set the Colors and Styles as desired. Press OK . In the Save Studies As Study Collection >> Name box, type a name to give the Volume Weighted Average Price Study Collection. Press the Save Single button and confirm. Press OK .

- Select Analysis >> Studies .

- In the Studies to Graph list, select the Volume Weighted Average Price study.

- Press the Add button.

- Press the Settings button.

- On the Settings and Inputs tab set the Inputs as required. Refer to Inputs .

- For the purpose of the configuration, the Start Date-Time Input is overridden with the value from the drawn Anchored VWAP. So this does not need to be set. All other Input settings are taken as you have set them and will be saved in the Study Collection referenced by the Draw Anchored VWAP configuration.

- Select the Subgraphs tab and set the Colors and Styles as desired.

- Press OK .

- In the Save Studies As Study Collection >> Name box, type a name to give the Volume Weighted Average Price Study Collection.

- Press the Save Single button and confirm.

- Press OK .

- Select Global Settings >> Tool Configs >> Draw Anchored VWAP .

- Select one of the Load >> TC1-TC24 configurations to save the configuration being defined as that particular number.

- Select the name that you saved the Study Collection as above, in the Chart Study Collection list. If a valid Study Collection is specified, then the first Volume Weighted Average Price study found in the Study Collection is used to set the settings of the inserted Volume Weighted Average Price study.

- Press OK . The configuration is now done at this point.

- Select Tools >> Draw Anchored VWAP on the menu.

- Select Tools >> Current Tool Config >> Config 1 . The particular number you need to select will correspond to the TC1-TC24 configuration that you selected above.

- Alternatively, instead of the prior two steps, you can configure a Control Bar button to select the Draw Anchored VWAP tool and a particular Tool Configuration number in a single step. For instructions, refer to Creating Control Bar Buttons which Select Drawing Tool and Drawing Tool Configuration in One Step .

- Proceed to draw the Volume Weighted Average Price as explained in the Tool Usage section.


#### Modifying Manually Drawn Anchored VWAP

An existing drawn Anchored VWAP can be modified. The beginning Date-Time can be changed. As you modify a drawn Anchored VWAP, you will see the changes to the profile immediately displayed. Follow the below procedure to do this.

- Enable the Global Settings >> Tool Settings >> Enable Drawn Volume Profiles Selection option. Press OK .

- Select Tools >> Pointer or Chart Values .

- Left click on the marker for the drawn Anchored VWAP. This will then cause the selection enclosing outline to be drawn around that marker.

- Once you can see the selection enclosing outline around the marker, then left click on the marker and move the pointer to adjust the marker position.

- As you move the Pointer left or right, the Volume Weighted Average Price lines will adjust. Left click again to set the marker into the new location.


#### Erasing Drawn Anchored VWAP

There are multiple ways to remove the Volume Weighted Average Price study that has been inserted by using this tool.

- Select Analysis >> Studies on the menu. Select the particular Volume Weighted Average Price study in the Studies to Graph list. Press the Remove button. Press OK to save the changes.

- Right-click with your Pointer along the top Region Data Line of the chart. This is not the title bar, but rather where you see the symbol and chart values displayed at the top of the chart window. Select Remove from the displayed menu. Select a specific Volume Weighted Average Price study you want to remove from the menu list.

- Erase the Anchored VWAP Chart Drawing. Refer to Erasing Chart Drawings section. All of those methods also apply to erasing Anchored VWAP Chart Drawings.


#### Drawing Tool Configuration

To set a default configuration for the Draw Anchored VWAP tool, refer to Step by Step Instructions to Configure the Draw Anchored VWAP Tool .

*Last modified Tuesday, 31st March, 2026.