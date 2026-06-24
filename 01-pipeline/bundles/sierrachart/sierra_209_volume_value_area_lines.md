# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=209


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> Volume Value Area Lines


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# Volume Value Area Lines

- Description

- Inputs


### Description

The Volume Value Area Lines study calculates and displays the Volume Value Area High (VVAH), Volume Value Area Low (VVAL), and Volume Point of Control (VPOC) on a chart for the specified time period.

For information on how the Value Area and Point of Control are calculated, refer to the Calculations section on the TPO Profile Chart study page.

It is essential that you properly set the Tick Size for the symbol you are applying this study to. This is set in Chart >> Chart Settings . If the Tick Size is not set correctly, it can cause long chart data load times and inaccuracies with this study.

The starting time for each time period in the chart for the calculations is based upon the chart Session Times . The time period for the calculations is set through the Time Period Type and Time Period Length study Inputs.

If you want to calculate the Volume Value Area High/Low and Volume Point of Control for a time period other than the supported time periods available with this study, like a number of bars, then use the Volume by Price study and set it to display only the Volume Value Area High/Low and Volume Point of Control lines. Refer to Calculating and Displaying Developing Point of Control, Value Area High/Low, Volume Weighted Average Price Lines for instructions.


#### Inputs

- Draw Developing Value Area Lines : This specifies how the Value Area Lines are calculated. If this Input is set to No , Value Area Lines are the same across the entire specified Time Period . They simply are the Volume Value Area of the entire time period being referenced. If this Input is set to Yes , Volume Value Area Lines at each bar are the current Volume Value Area lines at that bar. These values change throughout the day and the values at the end of the day are the same as the next days Value Area Lines if Draw Developing Value Area Lines is set to No and the Input Value Area Lines of n Days Back is set to 1.

- Time Period Type : Sets the type of time period for the study lines. This Input works in conjunction with Time Period Length . For a 1 Day period, set this to Days . The timeframe of the chart bars must be evenly divisible into the time period specified by the Time Period Type and the Time Period Length Inputs. You cannot use Number of Trades, Volume, Range, Reversal, Renko, Delta Volume, Price Change, Point and Figure Bars with the Volume Value Area Lines study. The result will not be accurate and can be inconsistent.

- Time Period Length : Sets the quantity to be used with Time Period Type . For example, for a period of 1 Day, set this to 1 and set Time Period Type to Days . The timeframe of the chart bars must be evenly divisible into the time period specified by the Time Period Type and the Time Period Length Inputs. You cannot use Number of Trades, Volume, Range, Reversal, Renko, Delta Volume, Price Change, Point and Figure Bars with the Volume Value Area Lines study. The result will not be accurate and can be inconsistent.

- Automatically Correct Invalid Time Period Type/Length : When this Input is set to Yes , then when changing the Bar Period for the chart that contains this study to a Daily or higher time frame, the Time Period Type will be set to Months and the Time Period Length will be set to 1 . Otherwise, when this Input is set to No then when changing the Bar Period for the chart that contains this study to a Daily or higher time frame, the Time Period Type and the Time Period Length will not be changed.

- Volume Value Area % : This setting specifies the percentage for the Volume Value Area. The default is 70%.

- Reference n Periods Back : This setting is only valid if Draw Developing Value Area Lines is set to No. This setting specifies how many time periods back the Volume Value Area and Point of Control lines, are based upon. If this is set to 1 and the Time Period is set to 1 Day, then for each 1 Day period in the chart, the lines are based upon the prior day. Another way to understand this is they are forward projected by 1 Day. When you set this to 0, then the Value Area and Point of Control lines use data from the current period that the lines are drawn on. If the latest period is incomplete, then the lines will update as new data is added to the latest period. As the lines update for the latest period, they will update for the entire period if Draw Developing Value Area Lines is set the No. If Draw Developing Value Area Lines is set to Yes, then they will just update for the current bar. When the study is referencing prior periods when Reference n Periods Back is greater than 0, if the time period being referenced does not exist and has no data, the study internally keeps searching back until it finds a prior period which has data. However, only a maximum of 20 back iterations is used. For example, if there are days skipped in the chart due to holidays, the most recent non-holiday date will be used.

- New Period At Day Session Start When Using Evening Session : When you have specified Evening Session Times in Chart >> Chart Settings and this Input is set to Yes, the Volume Value Area and Point of Control lines for the Day session and Evening session for a 1 Day period will be calculated separately. This Input is only applies if the Time Period is 1 Day. Otherwise it is ignored. When this Input is set to Yes, the time period for chart bars must not be greater than the time span of either the main session or the evening session.

*Last modified Thursday, 18th July, 2024.