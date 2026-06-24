> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/relative-rotation-graphs-rrg-charts.md).

# Relative Rotation Graphs (RRG Charts)

## What Is the Relative Rotation Graph? <a href="#introduction" id="introduction"></a>

Relative Rotation Graphs, commonly referred to as RRGs, are a unique visualization tool for relative strength analysis. Chartists can use RRGs to analyze the relative strength trends of several securities against a common benchmark, and against each other.&#x20;

The real power of this tool is its ability to plot relative performance on one graph and show true rotation. We have all heard of sector and asset class rotation, but it's difficult to visualize this “rotation” sequence on linear charts. RRGs use four quadrants to define the four phases of a relative trend. True rotations can be seen as securities move from one quadrant to the other over time.

{% hint style="warning" %}
**Note:** “Relative Rotation Graphs®” and “RRG®” are registered trademarks of [RRG Research](https://www.relativerotationgraphs.com).
{% endhint %}

## Background <a href="#background" id="background"></a>

RRGs were developed in 2004–2005 by Julius de Kempenaer, who would later become the Director of RRG Research. While working as a sell-side analyst for an investment bank in Amsterdam, he was confronted with two problems while producing technical and quantitative research on European sectors. First, institutional clients were much more interested in relative performance than directional forecasts; they wanted to know where to be overweight and where to be underweight in their equity portfolios. Second, these institutional investors faced an enormous information overload; they needed a tool that would clearly separate the leaders from the laggards. Enter Relative Rotation Graphs, which solved these problems with color-coded quadrants, a ranking table and an animation feature that make it easy for investors to keep an eye on the big picture.

## Main Components of Relative Rotation Graphs

Before looking at the construction of Relative Rotation Graphs, let's look at the two main inputs: JdK RS-Ratio and JdK RS-Momentum. Note that both input indicators are “normalized,” which means these indicators are expressed in the same unit of measure and fluctuate above/below the same level (100). This normalization process means RS-Ratio values for different securities can be compared, as long as the same benchmark is used.

### JdK RS-Ratio <a href="#jdk_rs-ratio" id="jdk_rs-ratio"></a>

RS-Ratio is an indicator that measures the trend for relative performance. Similar to the price relative, RS-Ratio uses ratio analysis to compare one security against another (usually the benchmark). It is designed to define the trend in relative performance and measure the strength of that trend.

The chart below shows the Technology SPDR (XLK) in the main window, the price relative (XLK:$SPX ratio) in the middle window and the RRG indicators in the bottom window. We will focus on RS-Ratio (red) first. RS-Momentum (green) will be covered in the next section.

<figure><img src="/files/A5SNGoEF3uzKySrj3VVY" alt="Chart of S&#x26;P 500, relative performance of Technology SPDR ETF XLK against the S&#x26;P 500, and RRG components RS-Ratio from StockCharts.com "><figcaption><p>Chart of Technology Select SPDR ETF (XLK), price relative (XLK:$SPX), and RRG indicators.</p></figcaption></figure>

RS-Ratio provides a clear tool to define the trend in relative performance. This indicator reflects an uptrend in relative performance when above 100 (relative strength) and a downtrend in relative performance when below 100 (relative weakness). The further the indicator is above 100, the stronger the uptrend in relative performance. The further the indicator is below 100, the stronger the downtrend in relative performance.

As with all trend-following indicators, such as [moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md), the trend-following model that powers RS-Ratio includes a lag period. This means there will already be upward movement in the price relative before RS-Ratio crosses above 100. Conversely, there will already be downward movement in the price relative before RS-Ratio crosses below 100.&#x20;

Notice on the chart above how the price relative (XLK:$SPX ratio) peaked in early August, but RS-Ratio did not cross below 100 until mid-October. Similarly, the price relative bottomed in mid-July, but RS-Ratio did not cross above 100 until mid-September. This is typical for trend-following indicators that are designed to ignore the blips and focus on the trend.&#x20;

The chart below shows the Consumer Discretionary SPDR (XLY) with another example.

<figure><img src="/files/P3Xv4CTlNvSSM2Ddvi4i" alt="Chart displaying Consumer Discretionary Select SPDR (XLY), price relative, and RRG indicators from StockCharts.com"><figcaption><p>Chart of Consumer Discretionary Select SPDR ETF (XLY), price relative (XLY:$SPX), and RRG indicators.</p></figcaption></figure>

Keep in mind that the values for RS-Ratio can be compared when using the same benchmark security. Let's assume we are comparing relative performance for four sector SPDRs against the S\&P 500 and the RS-Ratio values are as follows: XLK=102.04, XLI=101.41, XLF=100.2, and XLV=103.66.&#x20;

First, all four have RS-Ratios above 100 and this means all four show relative strength (against the S\&P 500). Second, XLV shows the most relative strength because its RS-Ratio is the highest of the four. XLF is the weakest of the four because its RS-Ratio is the lowest.

### JdK RS-Momentum <a href="#jdk_rs-momentum" id="jdk_rs-momentum"></a>

Before looking at RS-Momentum in detail, let's review the concept behind momentum and how it relates to trend. As with price charts, keep in mind that momentum changes course before the trend reverses. Not all momentum moves, however, result in trend reversals.

Consider an example using price and a moving average. Price first moves towards the moving average and then crosses it if the move extends. Price, however, doesn't always cross the moving average to signal a trend reversal. Aggressive traders would more likely take a position as price moves towards the moving average because this means momentum is improving. Conservative investors would more likely wait for price to move above the moving average because the trend has not fully reversed.

RS-Momentum is an indicator that measures the momentum (rate-of-change) of RS-Ratio. As a momentum indicator, it leads RS-Ratio, and can be used to anticipate turns in RS-Ratio. Typically, RS-Momentum crosses above 100 when RS-Ratio is forming a trough and starting to move up. Conversely, RS-Momentum crosses below 100 when RS-Ratio is forming a peak and starting to move down.

The chart below shows the Utilities SPDR (XLU) with RS-Momentum in green and RS-Ratio in red. RS-Momentum crossed above 100 in mid-December and held mostly above 100 for four weeks. Notice how RS-Ratio bottomed as RS-Momentum moved above 100 and RS-Ratio crossed above 100 later in January.

<figure><img src="/files/oVzeHRSF5d2JJe5m8aEv" alt=""><figcaption></figcaption></figure>

Keep in mind that RS-Momentum is an indicator of an indicator (RS-Ratio). Furthermore, as a momentum indicator, it will move above/below the 100 level often. Chartists may want to focus on sustained moves above/below 100 to anticipate a similar cross in RS-Ratio.

The chart below shows the Biotech SPDR (XBI) with two examples highlighting the relationship between RS-Momentum and RS-Ratio. The gray shading shows RS-Momentum below 100 for four of six weeks in February-March. Even though the indicator popped above 100 briefly, this pop did not last long and quickly moved back below 100. This was a sign that momentum was turning negative for RS-Ratio and RS-Ratio ultimately crossed below 100 in the second half of March.

<figure><img src="/files/8WQm3W5uThMXQWtIX3Ke" alt=""><figcaption></figcaption></figure>

The blue shading shows RS-Momentum above 100 from mid-April until late May. RS-Ratio bottomed as RS-Momentum moved above 100, but did not cross above 100 until the end of May. Additionally, note that the cross above 100 in RS-Ratio came just before the early June surge in XBI.

## RRG Construction <a href="#rrg_construction" id="rrg_construction"></a>

Relative Rotation Graphs are plotted on a standard scatter-plot canvas with an x-axis (horizontal) and a y-axis (vertical). The JdK RS-Ratio indicator is the input for the horizontal axis, and the JdK RS-Momentum indicator is the input on the vertical axis. These axes cross at 100 to create four relative performance quadrants. The Relative Rotation Graph simply plots RS-Ratio and RS-Momentum values for each symbol. If the symbol universe is the nine sector SPDRs and the S\&P 500 is the benchmark, we will see nine points on the Relative Rotation Graph (RRG) and each point represents that particular sector's RS-Ratio and RS-Momentum value.

<figure><img src="/files/4Kk2T5wlFR6nFb6RgJfN" alt=""><figcaption></figcaption></figure>

The Relative Rotation Graph is shown above with four possible combinations. Let's assume we use the nine sector SPDRs as our universe and the S\&P 500 as the benchmark.

* A sector is in the leading quadrant (green) when RS-Ratio and RS-Momentum are above 100 (+/+). A positive RS-Ratio indicates an uptrend in relative performance, and positive momentum means this trend is still pushing higher.
* A sector is in the weakening quadrant (yellow) when RS-Ratio is above 100, but RS-Momentum moves below 100 (+/-). A positive RS-Ratio indicates an uptrend in relative performance, but negative momentum means this uptrend is stalling or losing power.
* A sector is in the lagging quadrant when RS-Ratio and RS-Momentum are below 100 (-/-). A negative RS-Ratio indicates a downtrend in relative performance, and negative momentum means this downtrend is still pushing lower.
* A sector is in the improving quadrant when RS-Ratio is below 100, but RS-Momentum moves above 100 (-/+). A negative RS-Ratio indicates a downtrend in relative performance, but positive momentum means this downtrend is stalling or potentially reversing.

## Rotation Sequence <a href="#rotation_sequence" id="rotation_sequence"></a>

<figure><img src="/files/QfWphOjwvQKqHeUs5xkv" alt=""><figcaption></figcaption></figure>

The arrows on the model Relative Rotation Graph above show the idealized rotation, which is clockwise. Suppose a sector is in the leading quadrant (green) and follows the idealized rotation. Remember, RS-Momentum is the leading indicator here, and it will be the first to turn. From the leading quadrant, relative momentum will start to level off, and RS-Momentum will move below 100, which will cause the sector to move into the lower right-hand quadrant (weakening). Extended weakness in relative momentum will ultimately affect the trend in relative performance, and RS-Ratio will also move below 100, which would put the sector into the lagging quadrant (red). Once in the lagging quadrant, the first sign of strength will be an improvement in relative momentum. When RS-Momentum crosses above 100, the sector will move into the improving quadrant (blue). A sector in this quadrant still has a downtrend in relative performance, but RS-Momentum is improving and this could foreshadow a move into the leading quadrant (green). Extended strength in relative momentum will ultimately affect the trend in relative performance, and RS-Ratio will move above 100. This will push the sector into the leading quadrant (green), and the cycle will start again.

## Rotation Trails <a href="#rotation_trails" id="rotation_trails"></a>

Rotation comes alive with the historical trails. The chart below shows the nine sectors with 12-week trails; each sector is rotating from one quadrant to another. Each point marks one week, and the solid point with the symbol marks the most recent point. At the top, XLF moved from improving to leading. At the bottom, XLU moved from weakening to lagging. The blue line shows XLP moving from weakening to lagging and then from lagging to improving. The improving quadrant means RS-Momentum moved above 100, but RS-Ratio remains below 100. XLY moved into the leading quadrant when RS-Ratio and RS-Momentum were above 100.

<figure><img src="/files/eyiYDREUpkCrBILUsCui" alt=""><figcaption></figcaption></figure>

Chartists can also glean information from the length of the trails and the thickness of the trail lines. All trail lines extend 12 weeks on this chart, but some are longer than others. The red XLU trail is the longest, meaning it has the biggest move and shows the most volatility. The green XLY line in the upper right is the shortest, which means it has the smallest move and is the least volatile.

The thickness of the lines depends on the distance from the benchmark, which is the crosshair on the RRG. The crosshair is also known as the origin where the x-axis (RS-Ratio) crosses the y-axis (RS-Momentum). Thicker lines will be further from the benchmark, and thinner lines will be closer to the benchmark. The further a security is from the benchmark, the bigger the move in relative performance (up or down). The closer a security is to the benchmark, the smaller the move in relative performance (up or down). In other words, the thicker lines represent bigger moves and the thinner lines represent smaller moves.

Users can change the trail length using the slider next to the Relative Rotation Graph. Chartists are encouraged to experiment with the trail length and the number of symbols on the graph. In general, chartists should shorten the trail length when there are a lot of symbols on the graph. This will help de-clutter and make the analysis easier. Longer trails are fine when just a few symbols are shown on the graph.

## Interpreting RRG Charts <a href="#interpretation" id="interpretation"></a>

Before looking at some interpretation guidelines, bear in mind that Relative Rotation Graphs are not a trading system, and there are no predefined trading rules or signals. Look at RRGs as another type of charting method open to interpretation. Different people looking at the same chart will come up with different interpretations. Here are some rules of thumb you may want to follow:

* RS-Ratio is more important than RS-Momentum. RS-Ratio is also the preferred metric for ranking a group of symbols.
* The table below each RRG ranks the symbols by quadrant according to their distance from the benchmark (crosshair on the RRG). The leading quadrant (green) is first, the improving quadrant (blue) is second, the weakening quadrant (yellow) is third, and the lagging quadrant (red) is last. As the example below shows, XLK is the furthest from the benchmark in the leading quadrant, and XLE is the furthest from the benchmark in the lagging quadrant. This often coincides with tail length because the securities with the longest tails are often the furthest from the benchmark.

<figure><img src="/files/8o28Yc3oTOelJ6uddqA1" alt=""><figcaption></figcaption></figure>

* The rotational patterns are not always perfectly circular and will not always rotate through all four quadrants in a clockwise manner. These are, after all, financial markets driven by fear and greed.
* A historical trail can remain on the right side of the RRG when there is a strong uptrend in relative performance. This means RS-Ratio is holding above 100, and RS-Momentum is fluctuating above/below 100.

<figure><img src="/files/oUIhvWbmuGUXHmtiBqbe" alt=""><figcaption></figcaption></figure>

* Conversely, a historical trail can remain on the left side of the RRG when there is a strong downtrend in relative performance. This means RS-Ratio is holding below 100, and RS-Momentum is fluctuating above/below 100.
* In general, a cross from the left half to the right half signals a new uptrend in relative performance. This means RS-Ratio has moved above 100. Conversely, a cross from the right half to the left half signals a new downtrend in relative performance. This means RS-Ratio has moved below 100.

## Weekly Versus Daily <a href="#weekly_versus_daily" id="weekly_versus_daily"></a>

As with normal bar charts, line movements on a weekly RRG can look much different than on a daily RRG. For example, the weekly RRG below shows the S\&P Telecommunications Sector ($SPTS) in the lagging quadrant, which is red. In contrast, the daily RRG shows the sector rotating from the lagging quadrant to the leading quadrant. How can this be?

<figure><img src="/files/dogLfnUXqGuvM62Fvkvo" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/blraKbhXKZb6VAmplWbs" alt=""><figcaption></figcaption></figure>

The chosen timeframe affects RRGs just like regular bar charts. In the example below, the left chart shows two months of daily data for the S\&P 500, and the two-month trend is down. The chart on the right shows one year of weekly data and the overall trend is clearly up. The yellow shaded area highlights the two months shown on the daily chart to put this decline into perspective. Clearly, this is a short-term downtrend (pullback) within a long-term uptrend.

<figure><img src="/files/FHol2t4Kt1d5theX6Abn" alt=""><figcaption></figcaption></figure>

The chosen timeframe affects RRGs the same way. A sector moving into the weakening quadrant on the weekly timeframe, like the Telecom sector above, can be in the leading quadrant on the daily timeframe as the sector is going through a short-term positive rotation. This short-term rotation, however, is not powerful enough, yet, to influence the rotation on the weekly RRG.

This can be clarified a bit more by looking at RS-Ratio and RS-Momentum on bar charts. The first chart shows weekly RS-Ratio and RS-Momentum, which correspond to the weekly RRG plot. The second chart shows daily RS-Ratio and Momentum, which correspond to the daily RRG plot. Notice how the weekly indicators show negative momentum and a long-term downtrend in relative performance. The daily indicators, on the other hand, turned up and moved above 100.

<figure><img src="/files/XtZFoLAlcFGJRkqYnSAe" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/nsmxpKBbE3czXQ55fD9V" alt=""><figcaption></figcaption></figure>

Assuming that weekly rotations are stronger than daily and that a rotation will follow its normal clockwise course, one would expect the positive rotation on the daily timeframe to be temporary in nature. In a normal rotation, the sector would move through the leading quadrant, cross into the weakening quadrant and push into the lagging quadrant, thus keeping it solidly inside the lagging quadrant on the weekly timeframe! In other words, the daily move is a short-term “hiccup” within an otherwise falling relative trend on the weekly.

As with all aspects of technical analysis, it is a very good habit to study different timeframes to get a complete picture. The Telecom sector is clearly deep inside the lagging quadrant on the weekly RRG - and moving further into the red. The decrease in negative momentum, which can be seen by the leveling of the trail slope on the weekly RRG, translates into a quick positive rotation on the daily RRG.

## Conclusion <a href="#conclusion" id="conclusion"></a>

Relative Rotation Graphs make it easy to separate the market leaders from the market laggards. In this regard, RRGs save time, and money, because they narrow the focus to parts of the market that deserve attention for further analysis. RRGs can be tailored to suit any trading or investing style because they measure both momentum and trend for relative performance. Momentum traders can focus on crosses into the improving quadrant or the weakening quadrant. Trend followers can focus on crosses into the leading quadrant or lagging quadrant. Keep in mind that these are relative performance indicators, and there is still a risk that the rotation turns back or even reverses. As with all technical tools, these relative performance indicators should be used in conjunction with other technical tools to give chartists a more complete picture.

## Accessing the Tool <a href="#accessing_the_tool" id="accessing_the_tool"></a>

Chartists can access RRG Charts by clicking on “Charts & Tools” at the top of any web page at StockCharts. Simply click the “Launch RRG Chart” button in the Relative Rotation Graphs section of the Charts & Tools page. Our [RRG Charts](https://help.stockcharts.com/charts-and-tools/other-charting-tools/rrg-charts) article in the Support Center describes how to use all the controls.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/relative-rotation-graphs-rrg-charts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
