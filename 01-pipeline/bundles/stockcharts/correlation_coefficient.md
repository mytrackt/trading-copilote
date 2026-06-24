> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/correlation-coefficient.md).

# Correlation Coefficient

## Introduction to Correlation Coefficient <a href="#introduction_to_correlation_coefficient" id="introduction_to_correlation_coefficient"></a>

The Correlation Coefficient is a statistical measure that reflects the correlation between two securities. In other words, this statistic tells us how closely one security is related to the other. The Correlation Coefficient is positive when both securities move in the same direction (up or down) and negative when the two securities move in opposite directions. Determining the relationship between two securities is useful for analyzing intermarket relationships, sector-stock relationships and sector-market relationships. This indicator can also help investors diversify by identifying securities with a low or negative correlation to the stock market.

## How Correlation Coefficient Is Calculated <a href="#how_correlation_coefficient_is_calculated" id="how_correlation_coefficient_is_calculated"></a>

The calculation for the Correlation Coefficient is complicated, so feel free to skip this section. We will look at the basics to see some of the methods behind the madness. This indicator is at the heart of classical statistics. The first step is to select two securities. In this example, we will use Intel (INTC) and the Nasdaq 100 ETF (QQQ). Namely, we want to see the degree of correlation between Intel and QQQ. The Excel table below lays out the groundwork.

<figure><img src="/files/i4DxXnQoln6z5Te7URRG" alt=""><figcaption><p>Correlation Coefficient  -  Excel Example</p></figcaption></figure>

* The INTC column shows stock prices over a 20-day period with an average at the bottom.
* The QQQ column shows the same for QQQ.
* The following two columns show each period's price squared with the average at the bottom.
* The last columns show INTC multiplied by QQQ for each period with an average at the bottom.

Using the bottom row, you can now compute the Variance, Covariance, and Correlation Coefficient. The Excel formula is shown alongside the long formula. As seen above, Intel showed a strong positive correlation (+0.95) with the Nasdaq 100 ETF over the 20-day period.

<figure><img src="/files/degMgp83Kay6HLBHILry" alt=""><figcaption><p>Correlation Coefficient  - Intel</p></figcaption></figure>

Click below to download the Excel spreadsheet that shows the Correlation Coefficient in action. Some numbers may differ slightly due to rounding issues.

{% file src="/files/etZzUxTLFooxkuq5wj0f" %}

## Interpreting Correlation Coefficient <a href="#interpreting_correlation_coefficient" id="interpreting_correlation_coefficient"></a>

The correlation coefficient oscillates between -1 and +1. It is not a momentum oscillator, however. Instead, it moves from periods of positive correlation to periods of negative correlation. +1 is considered perfect positive correlation, which is rare. Anything between 0 and +1 indicates that two securities move in the same direction. The degree of positive correlation is likely to vary over time. Oil stocks and oil are positively correlated most of the time. The example below shows the Energy SPDR (XLE) with Spot Light Crude ($WTIC). Unsurprisingly, the 20-day Correlation Coefficient remains largely positive with regular forays above +.75. There is clearly a positive relationship between these two securities. In general, anything above .50 shows a strong positive correlation.

<figure><img src="/files/UifzWvdRFCuhGyBh1nq2" alt=""><figcaption><p>Correlation Coefficient  -  Oil and Oil Stocks</p></figcaption></figure>

At the other end of the spectrum, -1 is considered perfect negative correlation, which is rare. Anything between 0 and -1 indicates that two securities move in opposite directions. The degree of negative correlation is likely to vary over time. Gold and the Dollar are the first two securities that come to mind for a negative correlation. The chart below shows Spot Gold Spot ($GOLD) with the US Dollar Index ($USD). Although the Correlation Coefficient spends a fair amount of time in positive territory, it is negative the majority of the time. In general, anything below -.50 shows a strong negative correlation.

<figure><img src="/files/MPOx8FC74CD88evk3MZF" alt=""><figcaption><p>Correlation Coefficient  -  Gold and Dollar</p></figcaption></figure>

## Diversification: Investing in Non-correlated Securities <a href="#diversificationinvesting_in_non-correlated_securities" id="diversificationinvesting_in_non-correlated_securities"></a>

The correlation coefficient can identify non-correlated securities, which is essential in developing a diversified portfolio. Unsurprisingly, the nine S\&P sectors are mostly positively correlated with the S\&P 500. However, some are more positively correlated than others. For example, the Technology ETF (XLK) and Consumer Discretionary SPDR (XLY) have a strong positive correlation with the S\&P 500. The correlation coefficient examples below are based on 50 days. The Consumer Discretionary sector dipped below 0.50 only once in the last three years. The Technology sector never dipped below 0.50 as tech stocks remained strongly correlated to the market. In contrast, the correlation coefficient for the Consumer Staples sector dipped below 0.50 a few times and the correlation coefficient for the Utilities sector even dipped below zero twice. This indicator shows us that Consumer Staples and Utilities are less correlated to the S\&P 500 than the Consumer Discretionary and Technology sectors.

<figure><img src="/files/wDM4bIW6cRMmTwRGVszs" alt=""><figcaption><p>Correlation Coefficient - Sectors</p></figcaption></figure>

To truly diversify from stocks, it is often necessary to look outside of the stock market. The chart below shows four exchange-traded funds (ETFs) that have many periods of negative correlation with the stock market (using SPY as a proxy). Notice how the correlation coefficients dip below zero numerous times. In this example, the 50-day correlation coefficient is used. The 20+ year Bond ETF (TLT) represents bonds, which are negatively correlated with stocks most of the time. Gold (red) moves between periods of positive and negative correlation. On the whole, it has been more positively correlated than negative. The Yen Trust (green) appears to split its time between periods of positive and negative correlation. Surprisingly, the US Dollar Fund (UUP) shows a propensity to be negatively correlated with the stock market.

<figure><img src="/files/HAyk7vuSvMAyFWMKcZMQ" alt=""><figcaption><p>Correlation Coefficient  -  Other Assets</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The correlation coefficient tells us the relationship between two securities. Over a given time period, the two securities move together when the Correlation Coefficient is positive. Conversely, the two securities move in opposite directions when the Correlation Coefficient is negative. The examples above show 20-day and 50-day Correlation Coefficients. Longer-term investors may use 150 or even 250 days (one year) for smoother lines that reflect longer-term relationships.

## Correlation Coefficient: How to Find <a href="#correlation_coefficienthow_to_find" id="correlation_coefficienthow_to_find"></a>

The correlation coefficient is available as an indicator in SharpCharts and StockChartsACP.

### Using With SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The correlation coefficient is available in SharpCharts under “indicators.” First, you'll need to create a chart with the base security.

1. Enter the symbol in the symbol box at the top of the chart (INTC).
2. Select Correlation as an indicator in the drop-down menu.
3. Enter the symbol for the other security and the timeframe in the parameters box ($SPX,10). The two are separated by a comma.

The example below shows Intel in the main window with the 10-day correlation coefficient in the indicator window. This shows how Intel correlates with the S\&P 500. Note, for comparison, the S\&P 500 price plot (red dashed) is placed behind the Intel price plot. [Click here](https://stockcharts.com/sc3/ui/?s=INTC\&p=D\&b=5\&g=0\&id=p82568512106) for a live chart with the correlation coefficient.

<figure><img src="/files/XBwLEmEhs6CMxJnNmkkK" alt=""><figcaption><p>Correlation Coefficient  -  Intel SharpCharts</p></figcaption></figure>

<figure><img src="/files/BFjDo9WQKfXbIRNKhSoy" alt=""><figcaption><p>Correlation Coefficient  -  SharpCharts</p></figcaption></figure>

### Using With StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

The correlation coefficient is included in StockChartsACP in the Standard Indicators list.

<figure><img src="/files/8aufowkfKib3J5acVShc" alt=""><figcaption></figcaption></figure>

1. Pull up a chart by entering the symbol in the symbol box.
2. Select Correlation from the indicators listed in the menu on the left
3. Select the settings icon next to the indicator name to change the parameters. The Benchmark Symbol will be the symbol you entered. Enter the symbol for comparison in the Symbol box, select the number of periods for the indicator.

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Portfolio Diversification <a href="#portfolio_diversification" id="portfolio_diversification"></a>

This scan reveals ETFs that are inversely correlated (moving in the opposite direction of) the S\&P 500 index. This can be useful for diversifying an investment portfolio. The first clause limits the scan results to ETFs, excluding ultra and inverse ETFs. The second clause looks for those ETFs that have a negative correlation with $SPX over the last 200 trading days.

```
[group is ETFNOUI] 
AND [Correlation(200,$SPX) < 0] 
RANK BY [Correlation(200,$SPX)]
```

{% hint style="info" %}
For more details on the syntax to use for Correlation scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#correlation_coefficient) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/correlation-coefficient.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
