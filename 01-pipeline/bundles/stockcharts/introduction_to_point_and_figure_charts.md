> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts.md).

# Introduction to Point & Figure Charts

Point & Figure charts consist of columns of X's and O's that represent **filtered** price movements. X-Columns represent rising prices and O-Columns represent falling prices. Each price box represents a specific value that price must reach to warrant an X or an O. Time is not a factor in P\&F charting; these charts evolve as prices move. No movement in price means no change in the P\&F chart.

The 3-box Reversal Method is the most popular P\&F charting method. In classic 3-box reversal charts, column reversals are further filtered requiring a 3-box minimum to reverse the current column. Articles in the StockCharts.com ChartSchool are based on this method.

P\&F charts provide a unique look at price action that has several advantages. P\&F charts:

* Filter insignificant price movements and noise
* Focus on important price movements
* Remove the time aspect from the analysis process
* Make support/resistance levels *much* easier to identify
* Provide automatic and subjective trend lines

## History of Point & Figure Charts <a href="#history" id="history"></a>

P\&F charting has a long history. One of the first references to Point & Figure charting came from an anonymous writer named “Hoyle”, who wrote *The Game in Wall Street and How to Successfully Play It* in 1898. Early Point & Figure Charts were drawn using numbers. Hence, they were simply referred to as “Figure Charts”. These figure charts evolved into charts with X's and a few numbers. A.W. Cohen is credited with the classic 3-Box Reversal P\&F charts with X's and O's. Cohen wrote several books on this “Three-Point Reversal Method” and became the editor of ChartCraft.

Before computers, P\&F charts were popular because it was simple to maintain a large collection of charts. Using just a pencil, a newspaper and some graph paper, P\&F chartists were able to update and analyze 50 or more charts every day in less than an hour. This classic paper and pencil-based method was largely put aside as technology made charting easier. However, StockCharts.com still offers Point & Figure charting as well as the ability to scan thousands of stocks for specific P\&F patterns.

## Creating a P\&F Chart <a href="#creating_a_p_f_chart" id="creating_a_p_f_chart"></a>

On a P\&F chart, price movements are represented with rising X-Columns and falling O-Columns. Each column represents an uptrend or a downtrend of sorts. Each X or O occupies what is called a **box** on the chart. Each chart has a setting called the **Box Size**, which defines the price range for each box.

Each chart has a second setting called the **Reversal Amount**, which determines the amount a stock needs to move in the opposite direction to warrant a **column reversal**. Whenever this reversal threshold is crossed, a new column is started right next to the previous one, but moving in the opposite direction.

<figure><img src="/files/jdGjT0k4AkUyWCeP5Zg3" alt="Example of a P&#x26;f chart from StockCharts.com"><figcaption><p>P&#x26;F chart of AMZN</p></figcaption></figure>

The “reversal distance” is the box size multiplied by the reversal amount. A box size of one and the reversal amount of three would require a three-point move to warrant a reversal (1 x 3). An X-Column extends as long as price does not move down more than the “reversal distance.” Similarly, a stock in a downtrend will cause a descending O-Column to appear. Only when the stock changes direction by more than the reversal distance will a new X-column be added to the chart.

### Box Scaling <a href="#box_scaling" id="box_scaling"></a>

The P\&F charts at StockCharts.com allow users to select traditional, percentage, dynamic (ATR), or user-defined box scaling.

* **Traditional box scaling** uses a predefined table of price ranges to determine what the box size should be. The table was originally created by the people at ChartCraft and later popularized by Tom Dorsey in his book [*Point & Figure Charting*](http://store.stockcharts.com/products/point-figure-charting-the-essential-application-for-forecasting-and-tracking-market-prices-3rd-edition).

<figure><img src="/files/UZ0Du6FBBU19LWslsHAb" alt="" width="180"><figcaption></figcaption></figure>

* **Percentage box scaling** uses box sizes that are a fixed percentage of the stock's price. For example, if a chart used 5% scaling and the stock's price is $100, the box size for that part of the chart will be $5.00.
* **Dynamic (ATR) scaling** bases the box size on the daily Average True Range (ATR). The default is set at 20 days. However, one should take care with this setting because it changes as the ATR changes. Prior signals may disappear as ATR changes the box size. You can read more on Average True Range in our [ChartSchool article.](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md)
* **User-defined box scaling** allows users to set the box size. A larger box size will result in more filtered price movements and fewer reversals. A smaller box size will result in less filtered price movements and more reversals.

{% hint style="info" %}
**Learn More.** Chartists should experiment with various box sizes and reversal amounts to find their best fit. For more details, see our [ChartSchool article](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/point-and-figure-scaling-and-timeframes.md) on scaling and timeframes.
{% endhint %}

### Month Markings <a href="#month_markings" id="month_markings"></a>

P\&F charts do not show time linearly. In contrast to bar charts, the spacing between price changes will not be symmetrical. The chart evolves only when there is a price change big enough to warrant a new X, a new O, or a new reversal column. Chartists can view the passage of time on a monthly basis. Numbers and letters on the chart indicate when a new month has begun. For instance, the number “2” shows where February started. The letters “A,” “B,” and “C” are used to indicate the beginning of October, November, and December.

<figure><img src="/files/UPc2OFhzHMB0EPSqAF1V" alt="Example of a P&#x26;F chart showing price action for different months from StockCharts.com"><figcaption><p>Example of a P&#x26;F chart showing action during different months.</p></figcaption></figure>

### High-Low Method <a href="#high-low_method" id="high-low_method"></a>

There are two pricing methods available: the High-Low Method and the Close Method. Each method only uses one price point. Obviously, the Close Method uses the closing price only. The High-Low Method uses the high or the low, but not both. Sometimes both are ignored. Here are the rules for the High-Low method.

When the current column is an X-Column (rising):

* Use the high when another X can be drawn and then ignore the low.
* Use the low when another X cannot be drawn and the low triggers a 3-box reversal.
* Ignore both when the high does not warrant another X and the low does not trigger a 3-box reversal.

When the current column is an O-Column (falling):

* Use the low when another O can be drawn and then ignore the high.
* Use the high when another O cannot be drawn and the high triggers a 3-box reversal.
* Ignore both when the low does not warrant another O and the high does not trigger a 3-box reversal.

<figure><img src="/files/5na7xWMA8cZKLe0tSVwe" alt="Example of a P&#x26;F chart using the high/low method from StockCharts.com"><figcaption><p>A P&#x26;F chart using the high/low method.</p></figcaption></figure>

### Varying Box Ranges <a href="#varying_box_ranges" id="varying_box_ranges"></a>

A P\&F Box does not represent a single price, but rather a price range that depends on the box scaling method chosen, as well as the direction of the current column. The range rises for a rising X-Column and falls for a falling O-Column. In the following simple example, assume the user has chosen user-defined box scaling with a box size of 1.0 for their P\&F chart. For a rising X-Column on that chart, a box marked with a 12 would range from 12 to 12.99 and a box with a 13 would range from 13 to 13.99. Prices would remain in the 12 box as long as they ranged from 12 to 12.99. A move to 13 would warrant another X in the 13 box. In fact, a price anywhere between 13 and 13.99 would warrant another X.

It works a little differently when the current column is a falling O-Column. A move to 12 would warrant an O in the 12 box. This O would remain as long as prices range from 11.01 to 12. Notice that this range is different from the range for a rising X-Column. A price of 11 would then warrant an O in the 11 box. Anything between 10.01 and 11 would warrant an O in the 11 box.

{% hint style="info" %}
**Learn More.** For more information on other box scaling methods, see our [ChartSchool article](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/point-and-figure-scaling-and-timeframes.md) on scaling and timeframes.
{% endhint %}

## P\&F Chart Construction Example <a href="#p_f_chart_construction_example" id="p_f_chart_construction_example"></a>

To fully understand P\&F chart dynamics, it is helpful to walk through the construction process with a few simple examples. The key points to remember are:

* X-Columns represent rising prices (demand)
* O-Column represent falling prices (supply)
* Columns can contain X's or O's - not both
* Change requires a move equal to or greater than the reversal distance

This example will use the High-Low Method, with user-defined scaling and a box size of 1.0. Here are the first numbers:

<div align="left"><figure><img src="/files/9BkTBg8xb9ZgSaqhwAf8" alt="" width="155"><figcaption></figcaption></figure></div>

**Day 1 High = 15.50; Low = 12.90.** The chart has to start somewhere. We will assume prices are falling and plot O's in the 15, 14, and 13 boxes.

<div align="left"><figure><img src="/files/T5RIHxLrG7Ss4bZKWlnt" alt="" width="92"><figcaption></figcaption></figure></div>

**Day 2 High = 12.20; Low = 11.70.** Using the High-Low Method, we have to choose one number. Since the current column is an O-Column, we first check the low. Is it low enough to warrant another O? Yes. Since we can draw another O, we will ignore the high.

<div align="left"><figure><img src="/files/fpoyCX9cbx44hrdiGAZ4" alt="" width="92"><figcaption></figcaption></figure></div>

**Day 3 High = 12.60; Low = 10.90.** Again, we look to see if the low moves lower by at least the box amount. It does. So we add O in the 11 box (11 - 10.01). Once we plot an O, the high is ignored even if a 3-box reversal is warranted.

<div align="left"><figure><img src="/files/cD0JAnMTh1e1w0HgZcvl" alt="" width="93"><figcaption></figcaption></figure></div>

**Day 4 High = 14.10; Low = 11.95.** The current column is an O-Column and the price is in the 11 box (10.01 to 11). Since we are still in an O-Column, we check the low first. It does not move to 10 or lower and therefore does not warrant a new O in the 10 box. We then see if the high is greater than or equal to current box value (11) plus the reversal distance (3). The high is 14.10, which is greater than the current box value plus the reversal distance (11 + 3 = 14). This means a three box reversal is warranted and we add three X's starting one above the low of the previous column.

<div align="left"><figure><img src="/files/2Q34wg4YnbKM3kEqmKL7" alt="" width="131"><figcaption></figcaption></figure></div>

**Day 5 High = 15.99; Low = 13.80.** The current column is a rising X-Column and the price is in the 14 box (14 to 14.99). Since we are in an X-Column, we check the high first. Anything between 15 and 15.99 would warrant a new X in the 15 box. The high is 15.99 and thus warrants an X in the 15 box. Because we drew a new X, the low is completely ignored - even if it is low enough to warrant a 3-box reversal.

<div align="left"><figure><img src="/files/PeJdtrVsEb9FCIEFAvBW" alt="" width="128"><figcaption></figcaption></figure></div>

**Day 6 High = 15.90; Low = 12.00.** The current column is a rising X-Column and the price is in the 15 box (15 to 15.99). Since we are in an X-Column, we check the high first. Anything between 16 and 16.99 would warrant a new X in the 16 box. The high is 15.90, and this does not warrant a new X.&#x20;

Now let's turn to the low. See if the low is less than or equal to current box value (15) less the reversal distance (3). The low is 12.00, which is less than the current box value less the reversal distance (15 - 3 = 12). This means a three-box reversal is warranted and we add three O's starting one below the high of the previous column.

<div align="left"><figure><img src="/files/Uon3TgUbbCTCBER5raFp" alt="" width="172"><figcaption></figcaption></figure></div>

Over time, our chart might look something like this:

<div align="left"><figure><img src="/files/ceIR9MGQotxjNVBixjkr" alt="" width="375"><figcaption></figcaption></figure></div>

Is it important to remember that **P\&F charts do not show time in a linear fashion**. Each column can represent one day, or many days, depending on the price movement. Because P\&F charts filter out the noise associated with more traditional charting methods, every mark on the chart is significant.

## Basic P\&F Analysis <a href="#basic_p_f_analysis" id="basic_p_f_analysis"></a>

There are four things to look for on a Point & Figure chart:

* Support levels
* Resistance levels
* Upward trend lines
* Downward trend lines

**Support** is the price level at which demand is thought to be strong enough to prevent the price from declining further. Support levels are easy to spot on P\&F charts. In particular, a sequence of O-Columns with equal lows marks a clear support level.

<figure><img src="/files/OMPWTsE77omXd9ymR5vl" alt="" width="375"><figcaption></figcaption></figure>

**Resistance** is the price level at which selling is thought to be strong enough to prevent the price from rising further. Resistance levels are also easy to spot on P\&F charts. In particular, a sequence of X-Columns with equal highs marks a clear resistance level.

<figure><img src="/files/E2L9UnnjHCOHJxV5QLje" alt="" width="375"><figcaption></figcaption></figure>

**Trend lines** are drawn automatically on the Point & Figure charts. An upward-sloping trend line is called a Bullish Support Line, while a downward-sloping trend line is called a Bearish Resistance Line. Bullish Support Lines slope up at 45 degrees and start from an important low. At a minimum, it takes a column sequence of 5-3-5-3-5-3 to produce an advance steep enough to maintain this angle. X-Columns need to be at least 5 boxes with O-Columns a maximum of 3 boxes. An X-Column greater than 5 would allow for an O-Column greater than 3.

<figure><img src="/files/g1Cu8WqaWBafoVrtaCwr" alt="" width="309"><figcaption></figcaption></figure>

Bearish Resistance Lines slope down at 135 degrees (180 - 45 = 135) and start from an important high. A similar ratio is needed to maintain the slope of a Bearish Resistance Line. A column sequence of 5-3-5-3-5-3 is needed to maintain the slope. O-Columns need to be at least 5 boxes with X-Columns a maximum of 3 boxes. An O-Column greater than 5 would allow for an X-Column greater than 3.

<figure><img src="/files/HR5xIgTWazjLSeQd8fBC" alt="" width="325"><figcaption></figcaption></figure>

## P\&F Scans <a href="#p_f_scans" id="p_f_scans"></a>

P\&F Pattern Alerts are at the end of the [Predefined Scans Page](https://stockcharts.com/def/servlet/SC.scan). These are based on daily data. StockCharts.com provides daily alerts for over 15 P\&F patterns on various exchanges, including the TSX and LSE. Some of these are shown in the image below. Note that there were over 100 NYSE stocks with Triple Top Breakouts.

<figure><img src="/files/iy7XdPFEKqd8aLVwAjgK" alt="Screenshot showing the P&#x26;F pattern scans available in StockCharts.com"><figcaption><p>P&#x26;F pattern scans available in StockCharts.com.</p></figcaption></figure>

Chartists can also scan for specific P\&F patterns using daily data and the drop-down menu for P\&F Patterns on the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI). Over 20 P\&F patterns and criteria are included in this drop-down menu. Users can combine these P\&F patterns with other non-P\&F criteria to create truly unique scans.

<figure><img src="/files/4nbcscFSZ3sUXgAj6V0z" alt="Screenshot of P&#x26;F scan component available in StockCharts.com"><figcaption><p>The P&#x26;F scan component available in StockCharts.com.</p></figcaption></figure>

## P\&F Chart Patterns <a href="#p_f_chart_patterns" id="p_f_chart_patterns"></a>

There are many specific chart patterns for 3-box Reversal charts. These are detailed in the ChartSchool articles below.

* [Bullish Breakout Patterns](/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bullish-breakouts.md)
* [Bearish Breakdown Patterns](/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bearish-breakdowns.md)
* [Bearish and Bullish Signal Reversed](/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-signal-reversed.md)
* [Bullish and Bearish Catapults](/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-catapults.md)
* [Bullish and Bearish Triangles](/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-triangles.md)
* [Bull and Bear Traps](/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bull-and-bear-traps.md)
* [P\&F Trend Lines](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/p-and-f-trend-lines.md)

## P\&F Price Objectives <a href="#p_f_price_objectives" id="p_f_price_objectives"></a>

StockCharts.com computes Price Objectives based on specific Point & Figure charts. Here is a link to an article with more details on the [P\&F Price Objectives](/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives.md) found on the charts.

Chartists may also wish to calculate Price Objectives using the Horizontal or Vertical Count. These are more involved, but there are detailed articles about them in ChartSchool:

* [Horizontal Count](/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-horizontal-counts.md)
* [Vertical Count](/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-vertical-counts.md)

## Further Study <a href="#further_study" id="further_study"></a>

*Point & Figure Charting* by Thomas Dorsey starts with the basics of P\&F charting and then proceeds to the key patterns. Dorsey keeps his P\&F analysis simple and straightforward, much like the work of P\&F pioneer A.W. Cohen. As a relative strength disciple, Dorsey devotes a complete chapter to relative strength concepts using P\&F charts. These concepts are tied in with market indicators and sector rotation tools to provide investors with all they need to construct a portfolio. There is also a section on using P\&F charts with ETFs.

| <p><a href="https://a.co/d/cSc7TXU"><strong>Point & Figure Charting</strong></a><br>Thomas Dorsey</p> |
| ----------------------------------------------------------------------------------------------------- |
| <img src="/files/eI0Bwm4fgFIiwe9fiUH1" alt="" data-size="original">                                   |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
