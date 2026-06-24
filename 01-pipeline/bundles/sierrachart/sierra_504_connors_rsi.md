# SOURCE: https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=504


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


#### Home >> (Table of Contents) Studies and Indicators >> Technical Studies Reference >> RSI - Connors


# Technical Studies Reference

- Technical Studies Reference

- Common Study Inputs (Opens a new page)

- Using Studies (Opens a new page)


# RSI - Connors

- Description

- Inputs


### Description

This study calculates and displays the Connors RSI, as developed by Connors Research .

Let \(X\) be a random variable denoting the Input Data Input. Let the Inputs RSI Length and Rate of Change Length be denoted as \(n_{RSI}\) and \(n_{ROC}\), respectvely.

We begin by computing the standard RSI using the Wilders Moving Average by default. This can be changed by appropriately setting the RSI Average Type Input.

We then define the Up-Down Length, denoted as \(UDL_t(X)\). This is a backward-looking calculation of the number of consecutive bars (starting with the current two bars) that the value of \(X\) has been either higher or lower than than the previous bar. Let \(N\) denote this number. We then compute \(UDL_t(X)\) as follows.

We then compute \(RSI_t(UDL(X),2)\).

Next we define the Rate of Change, denoted as \(ROC_t(X,n_{ROC})\) This is the percentage of the previous \(n_{ROC}\) bars for which the price change from one bar to the next is less than the current price change. Denote the current price change as \(Delta X_t = X_t - X_{t - 1}\), and denote the price change \(i\) bars ago as \(\Delta X_{t - i} = X_{t - i} - X_{t - i - 1}\). Define \(n_i\) as follows.

We then compute \(ROC_t(X,n_{ROC})\) as follows.

Finally, we denote the Connors RSI as \(RSI^{(C)}_t(X,n_{RSI},n_{ROC})\) and compute it as follows.

In addition to displaying the Subgraph for \(RSI^{(C)}_t(X,n_{RSI},n_{ROC})\), it also displays horizontal lines at levels determined by the Line 1 Value and Line 2 Value Inputs.


#### Inputs

- Input Data

- RSI Length

- RSI Average Type

- Rate of Change Length

- Line 1 Value

- Line 2 Value

*Last modified Monday, 27th February, 2023.