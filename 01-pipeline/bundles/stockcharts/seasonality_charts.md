> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/seasonality-charts.md).

# Seasonality Charts

## What Are Seasonality Charts? <a href="#introduction" id="introduction"></a>

Seasonality is the tendency for securities to perform better during some periods and worse during others. These periods can be days of the week, months of the year, six-month stretches, or even multi-year timeframes. For example, Yale Hirsh of the *Stock Traders Almanac* discovered the six-month seasonal pattern or cycle. Since 1950, the best six-month period for the S\&P 500 extends from November to April. By extension, the worst six-month period runs from May to October, where the phrase “sell in May and go away” comes from. StockCharts offers a seasonality tool that chartists can use to identify monthly seasonal patterns. This article will explain how this tool works and show what chartists should look for when using our Seasonality Charts.

## Calculations <a href="#calculations" id="calculations"></a>

The seasonality tool calculates two numbers: the percentage of time the month is positive and the average gain/loss for the month. The calculations are pretty straightforward. Looking back over 19 years, there will be 228 months in total and 19 data points for each month. If a symbol advances nine times for one month, the seasonal bar will show 47% (9/19 = 0.47). If a symbol advances 15 times for a particular month, the bar will show 74% (15/19 = 74%).&#x20;

The example below shows the seasonality tool in histogram format for the gold futures spot price ($GOLD). The number at the top shows the percentage of times $GOLD closed higher for that month. The number at the bottom shows the average gain/loss for those 19 months.

<figure><img src="/files/phX97Ds8qcdMVQz37teH" alt="Seasonality chart of gold continuous contracts from StockCharts.com"><figcaption><p>Seasonality chart for Gold futures spot price ($GOLD).</p></figcaption></figure>

Astute chartists may have noticed that the slider at the bottom shows 20, which implies 20 years. This article was written in January 2014, which marks the beginning of the 20th year, hence the number 20 in the slider. The calculations from February to December are based on 19 years of data. The January calculation is based on 20 years of data and includes month-to-date performance for January 2014. The performance for January 2014 is subject to change until the month ends, which means the numbers in the histogram could change.

Note the current date when looking at a seasonality chart. If you are looking at a seasonal chart in mid-June, the seasonal numbers from January to May will be based on the number of years shown in the slider (i.e., 20). The seasonal numbers for June will also be based on the number of years in the slider, but these numbers are subject to change because June is still a work in progress. The numbers from July to December will be based on the number of years in the slider less one (i.e. 20 - 1 = 19).

## Interpreting Seasonality Charts <a href="#interpretation" id="interpretation"></a>

Seasonality has to do with what happened in the past. It's a historical tendency. There is no guarantee that past performance will equal future performance, but traders can look for above-average tendencies to complement other signals.&#x20;

On the face of it, a bullish bias is present when a security gains more than 50% of the time for a particular month. Conversely, a bearish bias is present when a security rises less than 50% of the time. You should look for more extreme readings than 50% since that would suggest a relatively strong tendency. For example, readings above 65% would show an above-average bullish bias, while readings below 35% would show an above-average bearish bias.

The example below shows Intel (INTC) with a strong bullish bias in April (84%) and October (79%). Also, the average gain is 6.3% in April and 6% in October.&#x20;

<figure><img src="/files/gr8xh5zQkSYkDUHTQp1U" alt="Seasonality chart for Intel Corp. (INTC) from StockCharts showing strong bullish bias in April and October."><figcaption><p>The seasonality chart for Intel Corp. (INTC) shows a strong bullish bias in April and October.</p></figcaption></figure>

On the bearish side, the stock moved higher only 32% of the time in September, which means it moved lower 68% of the time. The average loss in September is 4.5%, and traders would have been rewarded for waiting until October 1 to consider buying. Notice that the remaining eight months had no strong bias because they ranged from 42% to 58%.&#x20;

Before leaving this example, Intel was up 58% of the time in June, with an average loss of 0.3%. Even though Intel moved higher more often than it moved lower, the losses during the declines outpaced the gains during the advances.

## Relative Seasonality <a href="#relative_seasonality" id="relative_seasonality"></a>

Another way to measure relative seasonality is by [comparing the performance](/table-of-contents/technical-indicators-and-overlays/technical-indicators/price-relative-relative-strength.md) of one security against another. The option to add a "compare" symbol can be found just above the chart.&#x20;

The example below shows the Russell 2000 ETF (IWM) relative to the S\&P 500 ETF (SPY) over the last 20 years, which reflects the performance of small-cap stocks relative to large-cap ones.

<figure><img src="/files/V02FmuhqvGFfWsW36TtC" alt="An example of a seasonality chart from StockCharts.com comparing the Russell 2000 and the S&#x26;P 500 index."><figcaption><p>Seasonality chart of the Russell 2000 vs. the S&#x26;P 500. </p></figcaption></figure>

Use relative seasonality to find stocks, sectors, or groups that outperform the market during certain months. As the chart above shows, the Russell 2000 shows a strong tendency to outperform the S\&P 500 in June (70% of the time). In addition, the Russell 2000 outperforms the S\&P 500 by an average of 0.92%. The worst month for relative performance is April, where the Russell 2000 ETF only outperforms the S\&P 500 ETF 30% of the time, and typically underperforms by -0.95%.

## Viewing Seasonality Charts <a href="#viewing_options" id="viewing_options"></a>

There are three different ways to view seasonality charts—line, same scale, and histogram. The examples above were shown in histogram format, which makes it easy to see aggregate performance for each month.&#x20;

You can switch between viewing options by clicking the icons in the lower left-hand corner. The example below shows a line version for Merck (MRK) relative to the S\&P 500 ($SPX). First, notice that January is still a work in progress because the red line has yet to reach the end of the month. This is because the chart was created on January 27, and the month was incomplete. Second, notice that there is no scale because we are only concerned with directional movement, i.e., whether the lines moved up or down. Notice how the lines tended to decline in May and rise in September.

<figure><img src="/files/KlBQaUupYHQrphjhs5wY" alt="A seasonality chart viewed as a line chart comparing MRK and S&#x26;P 500 from StockCharts.com"><figcaption><p>A seasonality chart comparing a stock against a benchmark is a line chart.</p></figcaption></figure>

The middle icon is to view charts with the same scale for all lines. This means all performance lines begin at zero percent, allowing you to compare monthly or yearly performance.&#x20;

The chart below shows that 2013 was the best year of the four complete years. The fifth year, 2014, is still a work in progress because this chart was created in January 2014. 2010 was the worst year, with the smallest gain, which was barely positive.&#x20;

The year icons at the chart's upper left are for hiding or showing the line for a particular year.&#x20;

<figure><img src="/files/FFOs0sumBOqFdMbc92Yz" alt="Seasonality chart from StockCharts showing which year was best for MRK and which was worst."><figcaption><p>This Seasonality chart shows that 2012 was the best year for MRK, and 2010 was the worst.</p></figcaption></figure>

## The Takeaway <a href="#conclusion" id="conclusion"></a>

Seasonality is a tool that gives chartists a historical perspective on performance tendencies. Even though past performance does not guarantee future performance, chartists can use these seasonal patterns to increase their edge. Chartists can look for bullish setups when the seasonal patterns are strongly bullish and bearish setups when seasonal patterns are strongly bearish. As with all indicators and technical analysis tools, seasonal charts should be used with other analysis techniques.

## Accessing the Tool <a href="#accessing_the_tool" id="accessing_the_tool"></a>

Access Seasonality Charts by clicking on **Charts & Tools** at the top of any web page at StockCharts. Enter a symbol in the **Seasonality** section of the **Charts & Tools** page and click **Go**. Our [Seasonality Charts article](https://help.stockcharts.com/charts-and-tools/other-charting-tools/seasonality-charts) in the Support Center describes how to use all the controls.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/seasonality-charts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
