> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-breakout-and-reversal-method.md).

# P\&F Price Objectives: Breakout and Reversal Method

StockCharts automates Point & Figure price objectives using the Breakout Method and the Reversal Method. Both are based on the vertical length (height) of a Measure Column. The longer the Measure Column, the higher or lower the price objective. The column identification depends on the method—Breakout or Reversal. We'll show you how to find the Measure Column, calculate the length of the price move, and determine the Price Objective.

{% hint style="warning" %}
**Important:** P\&F Price Objectives are upside and downside price targets that stem from a P\&F buy or sell signal. These price objectives should not be used as the sole reason for buying or selling a security; they are general guidelines on what to expect based on the strength of the initial price move. The price objective represents the extreme of the range. Some securities reach their price objective, while others reverse before doing so. A lot can change after a given signal. You should continually monitor the technical situation for signs that validate or invalidate the Price Objective.
{% endhint %}

Note that different scaling methods can affect the Price Objectives. Most of the examples below are with traditional scaling, which is a half point per box below 20, one point between 20 and 100, two points between 100 and 200, and four points between 200 and 400. Price objectives can change when using dynamic ATR scaling and percentage scaling.&#x20;

If you're looking to calculate your price objectives, you may want to try “user-defined” scaling to ensure a uniform box size. This will make calculations and objectives easier to ascertain. Also, remember these price objectives are not “hard levels”. Instead, they are “soft areas” that you can use as a broad guideline. Another point to note—the chart header shows the extreme levels of the range.

***

## Basic P\&F Signals <a href="#basic_p_f_signals" id="basic_p_f_signals"></a>

The Breakout and Reversal Methods don't take into account classic P\&F patterns, such as Triple Top Breakouts, Triple Bottom Breakdowns, and High-Pole Reversals. These patterns may be present, but they do not figure into the calculations. Instead of these patterns, the Breakout and Reversal Methods use basic P\&F buy and sell signals.

A basic P\&F buy signal is a Double Top Breakout, which occurs when an X-Column exceeds the high of the prior X-Column. Because X-Columns represent rising prices, a P\&F buy signal is essentially a higher high and higher highs are present in uptrends.

A basic P\&F sell signal is a Double Bottom Breakdown, which occurs when an O-Column exceeds the low of the prior O-Column. Because O-Columns represent falling prices, a P\&F sell signal is essentially a lower low and lower lows are present in downtrends.

The chart below shows some basic P\&F signals highlighted in green (buy) or red (sell). These are the most prolific P\&F signals, so expect to see a lot of them on any given chart. Only a few of these signals are highlighted on the BBY chart below.

<figure><img src="/files/tjf6FpljHcBRcbcgNPDb" alt="P&#x26;F chart from StockCharts.com showing some basic P&#x26;F signals"><figcaption><p>Basic P&#x26;F signals.</p></figcaption></figure>

The blue arrow highlights the current signal, which is a basic P\&F buy signal. There is always a current, or active, signal in play on a P\&F chart, which means there is either an active P\&F buy signal or an active P\&F sell signal in play. It is one or the other, not both.

## Breakout Method: Bullish <a href="#breakout_method_-_bullish" id="breakout_method_-_bullish"></a>

There are four steps to finding a Bullish Price Objective with the Breakout Method. Before starting, select **Breakout** as the Price Objective method, and ensure the active signal is a P\&F buy signal. This means a Bullish Price Objective will be visible in the chart's upper left corner.

1. Working from right to left on the chart, find the most recent P\&F sell signal (Double Bottom Breakdown). It is necessary to identify the column that reversed this P\&F sell signal with a P\&F buy signal.
2. Work to the right of this P\&F sell signal and find the next P\&F buy signal (Double Top Breakout). The column that produces this P\&F buy signal is key because it's strong enough to reverse the P\&F sell signal. It is now the Measure Column. This Measure Column might not have produced the most recent P\&F buy signal on the chart. It's the one that reversed the prior P\&F sell signal.
3. Calculate the height of the Measure Column and multiply it by the box reversal amount. There are two possible methods to calculate the height. In most cases, you subtract the low from the high of the column (65 - 60 = 5) and multiply by the box reversal amount (usually three for a 3-box reversal). This is usually best when the box sizes differ, which can occur at different price levels when using dynamic ATR scaling or Percentage scaling. If the box size is equal, it's best to use the other method—count the number of filled boxes in the Measure Column, multiply by the box size by the box reversal amount (typically three).
4. Add the value to the low of the column just before the Measure Column. Because the Measure Column forms with an X-Column that produced a P\&F buy signal, the column immediately to the left will be an O-Column.

The chart below shows Citrix (CTXS) with a Bullish Price Objective of 74 (green ovals in the upper left and the right scale). That you see a Bullish Price Objective tells you that the active signal is a P\&F buy. Now, you can look for the most recent sell signal (red arrow in January).

<figure><img src="/files/UixMf12LrXXoNj7EvJA8" alt="P&#x26;F chart from StockCharts showing how to calculate bullish price objective"><figcaption><p>Calculating Bullish Price Objective.</p></figcaption></figure>

Working to the right of this sell signal, the next buy signal was triggered in February (red 2 on the breakout column). This column reversed the P\&F sell signal and became the Measure Column. For height, the Measure Column is five boxes (X's) and each box is 1 (5 x 1 = 5). Alternatively, the high of the column is at 65, and the low is at 60 (65 - 60 = 5). The height is multiplied by the reversal (5 x 3 = 15) and this value is added to the low of the prior O-Column for a Bullish Price Objective (59 + 15 = 74).

The Citrix example shows a fixed Measure Column because there was a three-box reversal to lock in column height. Despite two falling O-Columns and small declines, the buy signal and Bullish Price Objective remain in force until countered with a P\&F sell signal.

The Bullish Price Objective is tentative when the Measure Column is not yet fixed and subject to change. The chart below shows General Motors (GM) with a “tentative” Bullish Price Objective of 48 (upper left), which is the extreme of the range. (Note: this Price Objective is not shown in the chart below because it is off the scale.)

The Bullish Price Objective is tentative because the Measure Column is not yet fixed and is subject to change if prices extend higher. A move above 39 would warrant another X and increase column height, which would, in turn, increase the Bullish Price Objective. This column will not be fixed until a three-box reversal with an O-Column fills three boxes to the downside. Such a move would not, however, negate the P\&F buy signal and the Bullish Price Objective remains valid until a P\&F sell signal.

<figure><img src="/files/tHIpHxiduEoQbJuAgAnJ" alt="P&#x26;F chart from StockCharts.com showing a tentative bullish price objective"><figcaption><p>A tentative Bullish Price Objective.</p></figcaption></figure>

## Breakout Method: Bearish <a href="#breakout_method_-_bearish" id="breakout_method_-_bearish"></a>

There are four steps to finding a Bearish Price Objective with the Breakout Method. Before starting, ensure that **Breakout** is selected as the Price Objective method and the active signal is a P\&F sell signal. This means there will be a Bearish Price Objective visible in the upper left corner of the chart.

1. Working from right to left, find the most recent P\&F buy signal. This allows you to find the column that reversed the P\&F buy signal with a P\&F sell signal.
2. Work to the right of this P\&F buy signal and find the next P\&F sell signal. The column that produces this P\&F sell signal is important because it is strong enough to reverse the P\&F buy signal. It is now the Measure Column. Keep in mind that this Measure Column might not be the one that produced the most recent P\&F sell signal. It is simply the one that reversed the last P\&F buy signal.
3. Calculate the height of the Measure Column and multiply it by 2/3 of the box reversal amount. There are two methods to calculate column height. First, you can subtract the column high from the column low. Second, you can count the filled boxes and multiply by the box size. Then multiply the column height by 2/3 of the box reversal amount, typically 3 (3-box reversal). Using 2/3 for bearish counts is advocated by A.W. Cohen, a pioneer in P\&F charting, and Tom Dorsey, author of [*Point & Figure Charting*](https://store.stockcharts.com/products/point-figure-charting-the-essential-application-for-forecasting-and-tracking-market-prices-3rd-edition).
4. Subtract this total from the high of the column just before the Measure Column. Because the Measure Column forms with an O-Column that produced a P\&F sell signal, the column immediately to the left will be an X-Column.

The chart below shows an active P\&F sell signal and a Bearish Price Objective. The most recent P\&F buy signal occurred in December 2014 (red C) and a P\&F sell signal followed with the long O-Column in January 2015. This O-Column became fixed after the counter-trend bounce with the subsequent X-Column (red 2). This means the height of the Measure Column remains fixed, and the Bearish Price Objective will not change until a P\&F buy signal negates it. The column extends 10 boxes, each box is 1, and the box reversal amount is 3 (10 x 1 x 3 = 30). You can also subtract the high from the low (91 - 81 = 10) and multiply by three. Take 2/3 of the total and subtract this from the high of the X-Column just before the Measure Column (30 x 2/3 = 20 and 91 - 20 = 71).

<figure><img src="/files/hb5m0yF8ynkw8DfAWMqo" alt="P&#x26;F chart from StockCharts.com showing how to calculate a bearish price objective"><figcaption><p>Example of how to calculate a Bearish Price Objective.</p></figcaption></figure>

The chart below shows Garmin (GRMN) with an active P\&F sell signal and a tentative Bearish Price Objective because the height of the Measure Column is not yet fixed. In other words, the measuring column could still extend lower and this would affect the Bearish Price Objective. The Measure Column will become fixed when there is a 3-box reversal and rising X-Column that fills three boxes. Even with this counter-trend move, the Bearish Price Objective will remain valid until there is a P\&F buy signal.

<figure><img src="/files/9xIbI1YCxo1OkvmizOaW" alt="P&#x26;F chart from StockCharts.com showing a tentative bearish price objective"><figcaption><p>Example of a tentative Bearish Price Objective in a P&#x26;F chart.</p></figcaption></figure>

## Reversal Method: Bullish <a href="#reversal_method_-_bullish" id="reversal_method_-_bullish"></a>

There are three steps to finding a Bullish Price Objective with the Reversal Method. Before starting, make sure **Reversal** is selected as the Price Objective method and the active signal is a P\&F buy signal, which means there will be a Bullish Price Objective visible in the upper left corner of the chart.

1. Working from right to left on the chart, find the most recent P\&F sell signal. The X-Column next to the sell signal column represents the first bounce after the sell signal; this column then becomes the Measure Column.
2. Calculate the height of the Measure Column and multiply it by the box reversal amount.
3. Add this value to the low of the column just before the Measure Column, which will be the column that produced the most recent P\&F sell signal.

The chart below shows Mosaic (MOS) with a Bullish Price Objective at 64 using the Reversal Method. This means the active signal is a P\&F buy signal. To calculate this Price Objective, find the sell signal before this buy signal. The column next to the sell signal column becomes the Measure Column, and its height is eight. Multiply this number by the box reversal amount (8 x 3 = 24) and add the value to the low of the column before the Measure Column. The Bullish Price Objective is 64 (40 = 24 = 64).

<figure><img src="/files/gvA3cndhtv8s84WWo1vY" alt="P&#x26;F chart showing how to calculate the price objective of a bullish reversal"><figcaption><p>Bullish Reversal method for calculating Price Objectives in a P&#x26;F chart.</p></figcaption></figure>

The Reversal Method is also subject to “tentative” Bullish Price Objectives when the Measure Column is not yet fixed. This occurs when the X-column to the right of the sell signal triggers a P\&F buy signal.

The chart above shows LyondellBasell Industries (LYB) triggering a P\&F sell signal with an O-column in March, reversing with an X-column, and triggering a P\&F buy signal in April (red 4). This column extends to 94; should prices move higher, another X will be drawn, which would affect the Bullish Price Objective. The Measure Column will not become fixed until there is a three-box reversal and a decline with an O-Column. Such a reversal would not negate the P\&F buy signal, but it would fix the height of the Measure Column, and the Bullish Price Objective would remain valid until countered with a P\&F sell signal.

<figure><img src="/files/lffcNzJKOKiB9JDTSlf7" alt="P&#x26;F chart from StockCharts.com showing a tentative bullish reversal price objective"><figcaption><p>Example of a tentative Bullish Reversal price objective.</p></figcaption></figure>

## Reversal Method: Bearish <a href="#reversal_method_-_bearish" id="reversal_method_-_bearish"></a>

There are three steps to finding a Bearish Price Objective with the Reversal Method. Before starting, ensure the active signal is a P\&F sell signal, and a Bearish Price Objective is visible in the upper left corner of the chart.

1. Working from right to left on the chart, find the most recent P\&F buy signal. The O-Column next to this buy signal represents the first decline after the buy signal; this column then becomes the Measure Column.
2. Calculate the height of the Measure Column and multiply it by 2/3 of the box reversal amount.
3. Subtract this total from the high of the column just before the Measure Column, which will be the column that produced the most recent P\&F buy signal.

<figure><img src="/files/64UdUrcQRfwqjeF21pMV" alt=""><figcaption></figcaption></figure>

Bearish Price Objectives with the Reversal Methods are “tentative” if the height of the Measure Column is subject to change. This usually occurs when a P\&F sell signal immediately follows a P\&F buy signal. The O-Column generating the P\&F sell signal becomes the measure column, and its height is not fixed until there is a three-box reversal (X-Column with three boxes).

The chart below shows KLA-Tencor (KLAC) with an active P\&F sell signal and a Bearish Price Objective on the chart. Working from right to left on the chart, the first P\&F buy signal shows an X-column with a high at 70. The next O-column is the Measure Column; its height is 10, which is multiplied by the box reversal amount and 2/3 (10 x 3 x 2/3 = 20). This amount is subtracted from the high of the buy signal column for a downside Price Objective (70 - 20 = 50).

The chart below shows Hewlett Packard (HPQ) with a buy signal in November as the X-column moved above the prior X-column. This buy signal was immediately reversed with the next O-column and a “tentative” Bearish Price Objective was set. The O-column is not yet fixed because a decline below 31 would warrant another O and an adjustment to the Bearish Price Objective.

<figure><img src="/files/cj8O2Wb8N040fBhUoETU" alt="A P&#x26;F chart from StockCharts.com showing an example of a tentative bearish price objective"><figcaption><p>An example of a tentative Bearish Price Objective.</p></figcaption></figure>

## Met Price Objectives <a href="#met_price_objectives" id="met_price_objectives"></a>

Once a stock reaches its price objective, **MET!** appears next to the Price Objective in the upper left corner of the chart. After meeting this objective, a new price objective will not appear until the stock generates a new bullish or bearish setup.&#x20;

The first chart below shows Amazon with a Bullish Price Objective (tentative) of 375, which fits in the 372 box because each box is four points and this box covers 372, 373, 374 and 375. The second chart shows Amazon with Bullish Price Objective MET!.

<figure><img src="/files/T1wM9y8ie49ojZSJtBPO" alt="Example of a tentative bullish price objective in a P&#x26;F chart from StockCharts.com"><figcaption><p>Tentative Bullish Price Objective</p></figcaption></figure>

<figure><img src="/files/tK2HIq5FcQeoAzxHoDIZ" alt="A P&#x26;F chart from StockCharts.com showing that a bullish price objective was met with a display of MET!"><figcaption><p>The Bullish Price Objective was met as indicated by the MET! displayed on the chart.</p></figcaption></figure>

## The Takeaway <a href="#conclusions" id="conclusions"></a>

Price Objectives provide chartists with a general price target based on the vertical length of the Measure Column. The longer the Measure Column, the higher or lower the Price Objective. Price Objectives based on the Reversal Method, Breakout Method, or any other method should be taken with a grain of salt. Consider these targets as broad guidelines. Securities will not always reach their targets; some will even reverse course and trigger conflicting P\&F signals before reaching their target. A P\&F signal and a target are simply the starting point for analysis. Conditions can change, so chartists must regularly monitor the unfolding chart formation for evidence that would invalidate their original premise. Employing other technical analysis tools to confirm or refute a premise is also important. For example, chartists can apply basic trend analysis on a bar chart or use bar chart-based indicators to confirm the findings on the P\&F chart.

## Activating Price Objectives <a href="#activating_price_objectives" id="activating_price_objectives"></a>

StockCharts users can access P\&F Price Objectives by selecting **Reversal** or **Breakout** in the **Price Objective** drop-down box. This can be found just below the chart on the right side. After changing the method and selecting update, the Price Objective for the selected method will appear on the chart. See our [P\&F support article](https://help.stockcharts.com/charts-and-tools/other-charting-tools/p-and-f-charts) for details on other charting options.

***

&#x20;<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live graphical P\&F chart of the S\&P 500](https://stockcharts.com/freecharts/pnf.php?c=$spx,PWTADANRBO\[P]\[D]\[F1!3!!!2!20]).

***

<figure><img src="/files/nVy44exMK9DDYwKAuGSN" alt="StockCharts.com screenshot showing how to activate P&#x26;F price objectives in SharpCharts"><figcaption><p>Activating price objectives in SharpCharts</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

P\&F Pattern signals can be found at the bottom of the [Predefined Scans Page](https://stockcharts.com/def/servlet/SC.scan), which shows signals for more than 15 P\&F patterns.

***

## Further Study <a href="#further_study" id="further_study"></a>

Thomas Dorsey's [*Point & Figure Charting*](https://a.co/d/cxyr4Pq) examines the basic ideas and key patterns of P\&F charts. Dorsey keeps his analysis straightforward; as a relative strength disciple, he devotes a complete chapter to relative strength concepts using P\&F charts. These concepts are tied in with market indicators and sector rotation tools to provide investors with all they need to construct a portfolio. Additionally, Dorsey incorporates lessons on how to use P\&F charts with ETFs.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-breakout-and-reversal-method.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
