# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=158


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> TPO Value Area Lines


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# TPO Value Area Lines

- Description

- Basing on Specific Number of Bars

- Inputs


### Description

The TPO Value Area Lines study displays the Value Area High, Value Area Low, and Point of Control (POC) based upon the Time Price Opportunity (TPO) time blocks for each specified time period in the chart. The time length for each period is set through the study Input settings.

A TPO represents the trading at a particular price or price range for a specific period of time. This is one continuous period of time. The price or price range is specified with the Price Increment in Takes Input setting. The time length of the period of time is set with the TPO Letter Time Length in Minutes Input.

The TPO Value Area Lines study can only be used on a standard chart and not a TPO Profile Chart. If of this study is used on a TPO Profile Chart the calculations will be inaccurate .

For complete details on how the Value Areas and Point of Control are calculated, refer to the Calculations section on the TPO Profile Chart documentation page.

It is essential that the Tick Size in Chart >> Chart Settings is set correctly when using the TPO Value Area Lines study. Verify the Tick Size is set correctly. This is the smallest increment that the symbol trades in.

The time period that the TPO Point of Control and Value Area Lines span for a period is set through the Time Period Type and Time Period Length study Inputs. In the case of Intraday charts, the time period is relative to the Session Times set in Chart >> Chart Settings for the chart the study is on. The starting time for each Intraday period will be based upon the Start Time or if the Evening Session is enabled, then it will be the Evening Start Time .


#### Basing on Specific Number of Bars

To base the TPO Value Area Lines study on a specific number of bars, set the chart bars to a fixed timeframe/period per bar. For instructions, refer to Changing Period of Chart Bars .

Multiply the number of bars you want to base the TPO Value Area Lines study on by the timeframe per bar. For example if the chart bars have a timeframe of 5 Minutes each, and you want to base a study on 12 bars, then this is 12 * 5 = 60 Minutes.

In this particular case the next step is to set the Time Period Type Input to Minutes and the Time Period Length Input to 60 .


#### Inputs

- Draw Developing Value Area Lines : When this Input is set to No , the Value Area Lines are the same across the entire specified time period as defined by the Time Period Length and the Time Period Type Inputs. They are the Value Area of the entire time period being referenced. When this is set to No and Reference n Periods Back is set to 0, then as the specified time period develops during chart updating, the Value Area and Point of Control lines will change. When this Input is set to Yes , the Value Area Lines at each bar represent the Value Area from the beginning of the time period up until that bar. There is no consideration of the remaining bars within the same time period. This Input is assumed to be No if the Reference n Periods Back is set to a value other than 0.

- Price Increment In Ticks : The Price Increment In Ticks specifies the grouping of prices. The price increment can be as small 1 which represents the Tick Size for the symbol. 1 is the default. Example: If a sub period within the specified Time Period has a price range from 1110.5 to 1114, the tick size for the symbol is .25, and the Price Increment In Ticks is set to 4, this will group prices into the following price groups: 1111, 1112, 1113, 1114. The price group for 1111 will include the range from 1110.5 to 1111.25. A Price Increment In Ticks of 2 in this same example, will group prices into the following price groups, 1110.5, 1111, 1111.5, 1112, 1112.5, 1113, 1113.5, 1114. The price group for 1110.5 will include the range from 1110.25 to 1110.5.

- Time Period Type : Sets the type of time period for the TPO Point of Control and Value Area lines. This Input works in conjunction with Time Period Length . For a 1 Day period, set this to Days.

- Time Period Length : Sets the quantity to be used with Time Period Type . For example, for a period of 1 Day, set this to 1 and set Time Period Type to Days .

- Automatically Correct Invalid Time Period Type/Length : When this Input is set to Yes , then when changing the Bar Period for the chart that contains this study to a Daily or higher time frame, the Time Period Type will be set to Months and the Time Period Length will be set to 1 . Otherwise, when this Input is set to No then when changing the Bar Period for the chart that contains this study to a Daily or higher time frame, the Time Period Type and the Time Period Length will not be changed.

- TPO Letter Time Length in Minutes : This is the amount of time for each TPO time block which are used to calculate the Value Area Lines from. The default is 30 minutes. This Input only applies to Intraday charts. If the Time Period Type Input is set to Years, this Input does not apply. The TPO time block is internally set to 1 month for Years. The TPO Letter Time Length in Minutes is also known as the Sub Period time length. The timeframe/period per bar in an Intraday chart must evenly divide into this time block specified. The timeframe/period per bar must also be less than or equal to this time block specified. For more information, refer to Incorrect Value Area or Point of Control Values . For example, if TPO Letter Time Length in Minutes is set to 30, that means the chart bars cannot exceed 30 minutes per bar, and the time period of the chart bars must evenly divide into this time. So for example the chart bars can be 1 minute, 5 minutes, 10 minutes, 15 minutes or 30 minutes.

- TPO Value Area % : This percentage specifies the percentage around the Point of Control that the Value Area High and Low are calculated from. The default is 70%. Refer to Calculations for details.

- Reference n Periods Back : This Input only applies when Draw Developing Value Area Lines is set to No. This Input sets the number of periods (1 day, 1 Week,...) back that the TPO Value Area and Point of Control lines will reference. If it is set to 0, then the lines are calculated based upon the period they are drawn on. If it is set to 1, they will reference the prior period. If it is set to 2, then the Value Area and Point of Control lines will reference 2 periods back.

- One Period Only at End of Chart : When this Input is set to Yes , then there will be just one set of lines for the Value Area and Point of Control for the specified Time Period Type and Length at the end of the chart. For example, if the Time Period for the Value Area calculations is set to 1 Day, then the Value Area High, Value Area Low, and Point of Control will be displayed at the end of the chart going back 24 hours. The lines will always be for the duration of the specified Time Period Type and Length and not less. When using this option, there is not any consideration of weekend days. Therefore, if this Input is set to Yes and the Time Period Length and Type are set to 3 Days, then on a Monday at 12:00:00, the starting Date-Time will be Friday at 12:00:01.

- New Period At Day Session Start When Using Evening Session (1 Day Period Only) : When this Input is set to Yes and you have defined separate Evening Session times in Chart >> Chart Settings , then separate Value Area Lines and Point of Control will be calculated and displayed for both the Day session and the Evening session. Normally there will be one set of lines that starts at the Evening session time. When this Input is set to Yes, then at the day session Start Time a new set of Value Area Lines and Point of Control will begin.

- 30 Minute Letter/Block SubPeriod Handling : This Input specifies several options for the handling of TPO Profile subperiods when using a TPO Letter/Block time period of 30 minutes and a Session Times >> Start Time in Chart >> Chart Settings which is not evenly divisible by 30 minutes or does not start at 0:00. The choices are as follows: Standard : This is the default setting and there is no special handling. Merge Odd SubPeriod with Next : This will merge the odd sub period which arises from an odd chart Start Time, with the next subperiod creating a longer subperiod than the setting. Example: If the chart Start Time is 8:20 and the sub period time length is 30 minutes, there will be a single sub period which goes from 8:20 to 8:59:59. Start New Subperiods at Even 30 Minute Time Blocks : Any odd sub periods are handled on their own, creating a shorter sub period. Example: If the chart Start Time is 8:20, there will be a single sub period which goes from 8:20 to 8:29:59. The next sub period will begin at 8:30 and will be 30 minutes long.

- Standard : This is the default setting and there is no special handling.

- Merge Odd SubPeriod with Next : This will merge the odd sub period which arises from an odd chart Start Time, with the next subperiod creating a longer subperiod than the setting. Example: If the chart Start Time is 8:20 and the sub period time length is 30 minutes, there will be a single sub period which goes from 8:20 to 8:59:59.

- Start New Subperiods at Even 30 Minute Time Blocks : Any odd sub periods are handled on their own, creating a shorter sub period. Example: If the chart Start Time is 8:20, there will be a single sub period which goes from 8:20 to 8:29:59. The next sub period will begin at 8:30 and will be 30 minutes long.

- Count 2 Levels at a Time for Value Area : When this input is set to Yes , the calculation for the Value Area uses every other level, rather than looking at every level. Refer to How Point of Control and Value Area are Calculated for more information.

- Base on Day Session Only : When this Input is set to Yes then the TPO Value Area Lines calculation does not use the Evening Session times, therefore the calculations are only based on the Day Session times as defined in the Session Times .

*Last modified Thursday, 18th July, 2024.