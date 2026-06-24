> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-indicators/high-low-index.md).

# High-Low Index

The High-Low Index is a breadth indicator based on [Record High Percent](/table-of-contents/market-indicators/record-high-percent.md), which is based on new 52-week highs and new 52-week lows. The Record High Percent equals new highs divided by new highs plus new lows. The High-Low Index is simply a 10-day SMA of the Record High Percent, which makes it a smoothed version of the Record High Percent. This article will explain how to identify the direction of the High-Low Index and how to use the absolute level to define a trading bias.

## Calculating the High-Low Index <a href="#calculation" id="calculation"></a>

```
Record High Percent = {New Highs / (New Highs + New Lows)} x 100 

High-Low Index = 10-day SMA of Record High Percent
```

<figure><img src="/files/uK27MtI8FdAGLt2L1h1x" alt=""><figcaption><p>Spreadsheet 1</p></figcaption></figure>

The table above shows some possibilities for Record High Percent. As the formula implies, Record High Percent shows the number of new highs relative to the total (new highs plus new lows). The total is multiplied by 100 to generate round numbers that fluctuate between 0 and 100. The table above shows various possibilities based on an index with 100 stocks, such as the Nasdaq 100 or S\&P 100. Rarely, if ever, will 100% of stocks record a new high or new low. Readings below 50 indicate that there were more new lows than new highs. Readings above 50 indicate that there were more new highs than new lows. 0 indicates there were zero new highs (0% new highs). 100 indicates that there was at least 1 new high and no new lows (100% new highs). 50 indicates that new highs and new lows were equal (50% new highs).

<figure><img src="/files/uGOSmaYQHLYCBjzUDymR" alt=""><figcaption><p>High-Low Index - Chart 1</p></figcaption></figure>

The High-Low Index smooths Record High Percent with a 10-day SMA. Chart 1 above shows the Record High Percent in the first indicator window (black line) and the High-Low Index in the second indicator window (red line). Notice how the S\&P 100 Record High Percent ($OEXHILO) smooths the S\&P 100 Record High Percent ($RHOEX), especially during May-June 2010 (yellow area). Record High Percent bounced from 0 to 100 numerous times, but the High-Low Index trended lower in May and higher in June.

## Interpreting the High-Low Index <a href="#interpretation" id="interpretation"></a>

In general, a stock index is deemed strong (bullish) when the High-Low Index is above 50, which means new highs outnumber new lows. Conversely, a stock index is deemed weak (bearish) when the High-Low Index is below 50, which means new lows outnumber new highs. This indicator can move to its extremities and remain near its extremes when the underlying index is in a strong uptrend or downtrend. Readings consistently above 70 usually coincide with a strong uptrend. Readings consistently below 30 usually coincide with a strong downtrend.

## Direction Identification <a href="#direction_identification" id="direction_identification"></a>

The directional movement of The High-Low Index shows when new highs are expanding or contracting, which in turns reflects underlying strength or weakness in the index. Chartists can define direction by applying a moving average to the High-Low Index. Chart 2 shows the NY Composite with the NYSE High-Low Index ($NYHILO) and its 20-day SMA. The High-Low Index turns up when it moves above the 20-day SMA and turns down when it moves below the 20-day SMA. New highs are increasing and/or new lows are decreasing when the High-Low Index rises. New highs are decreasing and/or new lows are increasing when the High-Low Index falls.

<figure><img src="/files/OuZuqpg6FmvA0KwXzn45" alt=""><figcaption><p>High-Low Index - Chart 2</p></figcaption></figure>

The green dotted lines show the High-Low Index turning up and moving above its 20-day SMA, which is positive for the NY Composite. The red dotted lines show the High-Low Index moving below its 20-day SMA, which is negative for the NY Composite. Because the bigger trend was down from October 2007 to March 2009, the bearish signals worked much better than the bullish signals.

## Bull-Bear Bias <a href="#bull-bear_bias" id="bull-bear_bias"></a>

The absolute level of the High-Low Index can also be used to ascertain strength or weakness in new highs, which in turn reflects underlying strength or weakness in the index. Sometimes the High-Low Index can be rather volatile, but still remain consistently above or below its midpoint (50). Remember, new highs outnumber new lows when above 50 and new lows outnumber new highs when below 50. This level provides a clear bullish or bearish bias for the underlying index.

<figure><img src="/files/7cWS6QkaHzVILBXAYFnO" alt=""><figcaption><p>High-Low Index - Chart 3</p></figcaption></figure>

Chart 3 shows the Nasdaq with the High-Low Index and its 20-day SMA. The index moved above/below its 20-day SMA many times from June to August 2007 and from November 2007 to February 2008. Playing these crossovers would have resulted in numerous whipsaws. Instead, chartists can look at the overall level of the High-Low Index. Notice how the High-Low Index moved below 50 at the end of May and remained below 50 until late August (3 months). Once moving above 50, the High-Low Index remained above 50 until early March (7 months). Not all signals will last this long, however.

Armed with a bullish or bearish bias, chartists can then turn to other aspects of technical analysis to generate corresponding signals. Chartists can focus on bullish signals when the High-Low Index is above 50 and ignore bearish signals. Oversold readings, resistance breakouts or bullish moving average crosses can be used in a bullish environment. Chartists can focus on bearish signals when the High-Low Index trades below 50 and ignore bullish signals. Overbought readings, support breaks, and bearish moving average crosses can be used in a bearish environment.

## A Lagging Indicator <a href="#a_lagging_indicator" id="a_lagging_indicator"></a>

New 52-week highs and new 52-week lows are considered lagging indicators. In other words, the market will change direction before there is a significant shift in the number of new 52-week highs or the number of new 52-week lows. Think about it. It takes at least 52 weeks to forge a new high or a new low. Therefore, an extended move is required for a stock to forge a new high or a new low. There are plenty of new highs after an extended advance, just as there are plenty of new lows after an extended decline. New highs dry up when a stock index corrects after an extended advance. Some new lows will surface during a correction, but it takes an extended decline to generate a serious increase in new lows. Similarly, new lows dry up when a stock index bounces after an extended decline. Some new highs may surface during this bounce, but it takes an extended advance to generate a serious increase in new highs.

## The Bottom Line <a href="#conclusions" id="conclusions"></a>

As with its cousin, the Record High Percent, the High-Low Index is a breadth indicator specific to an underlying index. The Nasdaq 100 High-Low Index applies to stocks in the Nasdaq 100, the NYSE High-Low Index applies to stocks in the NY Composite and so on. Like all indicators, the High-Low Index is not meant to be used as a stand-alone indicator. It should be used in conjunction with other aspects of technical analysis.

## SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

SharpCharts users can plot the High-Low Index for eight indices, including the S\&P 500, TSX Composite and Dow (see list below). It is often helpful to plot the underlying index along with the indicator for easy reference. The High-Low Index can be plotted in an indicator window or in the main chart window. It can even be plotted behind the price plot of the underlying index. In this example, the index is shown in the main window with corresponding High-Low Index plotted behind the index and in the indicator window. First, enter the index symbol in the “Symbol” box in the upper left. Second, go to “Indicators” and select “Price.” Third, enter the symbol for the Record High Percent in the “Parameters” box. Fourth, select “Above, Below or Behind” for the “Position” of the indicator plot. A moving average can be added by choosing “Advanced Options” and selecting an “Overlay.” [Click here](https://stockcharts.com/h-sc/ui?s=$SPX\&p=D\&yr=0\&mn=8\&dy=0\&id=p98263754159\&listNum=61\&a=203609792) for a live example.

<figure><img src="/files/FOMhoizzMHDUNXEUPPY4" alt=""><figcaption><p>High-Low Index - Chart 4</p></figcaption></figure>

<figure><img src="/files/uscTBiB11Jbo7B8cccQW" alt=""><figcaption><p>High-Low Index - SharpCharts</p></figcaption></figure>

## Symbol List <a href="#symbol_list" id="symbol_list"></a>

StockCharts.com users can access [an up-to-date list of symbols](https://stockcharts.com/search/?q=%22High-Low%20Index%22\&section=symbols) for all our High-Low Index indicators. From this list, click the “Mentions” icon to the right of a specific symbol for more details about the symbol, as well as recent mentions in Public ChartLists, blog articles, and more.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-indicators/high-low-index.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
