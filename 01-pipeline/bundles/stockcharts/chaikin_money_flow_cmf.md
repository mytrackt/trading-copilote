> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-money-flow-cmf.md).

# Chaikin Money Flow (CMF)

## What Is Chaikin Money Flow? <a href="#what_is_the_chaikin_money_flow" id="what_is_the_chaikin_money_flow"></a>

Developed by Marc Chaikin, Chaikin Money Flow measures the amount of money flowing into an asset over a specific period. Money Flow Volume forms the basis for the cumulative indicator Accumulation Distribution Line. Chaikin Money Flow sums Money Flow Volume for a specific look-back period, typically 20 or 21 days, instead of using a cumulative total. The resulting indicator fluctuates above/below the zero line just like an oscillator.&#x20;

<figure><img src="/files/uydRlGOfsrdQUCAyHSRC" alt=""><figcaption><p>Chart with 20-day and 60-day CMF indicators, to assess money flow in multiple timeframes</p></figcaption></figure>

Chartists weigh the balance of buying or selling pressure with the absolute level of Chaikin Money Flow. Additionally, chartists can look for crosses above or below the zero line to identify changes in money flow.

{% hint style="info" %}
**Learn More:** Marc Chaikin also developed the [Accumulation Distribution Line](/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md) and the [Chaikin Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-oscillator.md).
{% endhint %}

## Calculating Chaikin Money Flow <a href="#how_is_the_chaikin_money_flow_calculated" id="how_is_the_chaikin_money_flow_calculated"></a>

There are four steps to calculating Chaikin Money Flow (CMF). The example below is based on 20 periods. First, calculate the Money Flow Multiplier for each period. Second, multiply this value by the period's volume to find Money Flow Volume. Third, sum Money Flow Volume for the 20 periods and divide by the 20-period sum of volume.

```
               
  1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 

  2. Money Flow Volume = Money Flow Multiplier x Volume for the Period

  3. 20-period CMF = 20-period Sum of Money Flow Volume / 20 period Sum of Volume 
		
```

Each period's Money Flow Volume depends on the Money Flow Multiplier. This multiplier is positive when the close is in the upper half of the period's high-low range and negative when the close is in the lower half. The multiplier equals 1 when the close equals the high and -1 when the close equals the low. In this way, the multiplier adjusts the amount of volume that ends up in Money Flow Volume. Volume is reduced unless the Money Flow Multiplier is at its extremes (+1 or -1).

<figure><img src="/files/pM1C05Y1vmiHAK7DvCqC" alt=""><figcaption><p>Table 1  -  Chaikin Money Flow</p></figcaption></figure>

The table above and the chart below show some examples using daily data. Notice how the multiplier was near +1 on 5-Jan when the stock closed near its high. The multiplier dipped to -0.97 on 18-Jan when the stock closed near its low. The multiplier finished near zero (-0.07) when the stock closed near the midpoint of its high-low range on 29-Dec.

<figure><img src="/files/8YugP5i2btAqg8cAf4wk" alt=""><figcaption><p>Chart showing price and CMF values for the spreadsheet example</p></figcaption></figure>

Click below to download an Excel spreadsheet that includes the calculation of the Chaikin Money Flow.

{% file src="/files/QnFsCbs03GY1Pq3cOmSO" %}

The resulting Chaikin Money Flow (CMF) indicator is an oscillator that fluctuates between -1 and +1. Rarely, if ever, will the indicator reach these extremes. It would take 20 consecutive closes on the high (low) for 20-day Chaikin Money Flow to reach +1 (-1). Typically, this oscillator fluctuates between -0.50 and +0.50, with 0 as the centerline.

## Interpreting Chaikin Money Flow <a href="#how_do_you_interpret_the_chaikin_money_flow" id="how_do_you_interpret_the_chaikin_money_flow"></a>

Chaikin Money Flow measures buying and selling pressure for a given period. A move into positive territory indicates buying pressure, while a move into negative territory indicates selling pressure. Chartists can use the absolute value of Chaikin Money Flow to confirm or question the price action of the underlying security. Positive CMF would confirm an uptrend, but negative CMF would call into question the strength behind an uptrend. The reverse holds true for downtrends.

### Zero Line Crosses <a href="#identifying_buying_selling_pressure" id="identifying_buying_selling_pressure"></a>

A zero line cross in Chaikin Money Flow indicates a shift in buying or selling pressure. When CMF crosses above the zero line, it suggests that buying pressure is stronger. Conversely, a cross below the zero line indicates stronger selling pressure.

While this zero line cross seems simple enough, the reality is much choppier. Chaikin Money Flow sometimes only briefly crosses the zero line with a move that turns the indicator barely positive or negative. There is no follow-through through and this zero line cross ends up becoming a whipsaw (bad signal). Chartists can filter these signals with buffers by setting the bullish threshold a little above zero (+0.05) and the bearish threshold a little below zero (-0.05). These thresholds will not eliminate bad signals but can help reduce whipsaws and filter out weaker signals.

The chart below shows Freeport McMoran (FCX) with 20-day Chaikin Money Flow in the indicator window.

<figure><img src="/files/ydCVBXi7giRvb9fUYQZB" alt=""><figcaption><p>Reducing CMF whipsaws with a buffer zone</p></figcaption></figure>

There were at least 10 crosses of the zero line between February and December 2010. Adding a small buffer reduced the number of bullish and bearish signals. A move above +0.05 was considered bullish, while a move below -0.05 was considered bearish. There were only three signals. While these signals came later, the reduction of whipsaws was worth implementing.

The chart of Harley-Davidson (HOG) below shows a few good signals and a whipsaw with the May bounce.

<figure><img src="/files/q2yrHM4dIAuxnU4nbB4C" alt=""><figcaption><p>Trading pullbacks with bullish CMF</p></figcaption></figure>

CMF moved above +0.05 for a few days, but this move failed to hold, and the indicator broke back below -0.05 in early June. Whipsaws will happen, especially during volatile periods. CMF turned bullish in July and stayed bullish the rest of the year. HOG formed a falling wedge that retraced just over 62% in August when CMF was still in bull mode. This pullback offered a second chance to partake in the CMF signal.

### Caveat: CMF in Volatile or Choppy Conditions

Chaikin Money Flow can be less reliable during volatile periods or when the trend of a security is flattening. This is because of the indicator's sensitivity to price fluctuations, which can lead to whipsaws (false signals). For this reason, CMF is not always suited to all securities, especially those with choppy price trends.

The chart below of P.F. Chang (PFCB) shows 18 crosses above +0.05 or below -0.05.

<figure><img src="/files/qDaZrDkH195DaeyrJGQ8" alt=""><figcaption><p>CMF is not effective in volatile or choppy conditions</p></figcaption></figure>

Basing CMF signals on these crosses resulted in several whipsaws. It's important to analyze the basic price trend and characteristics of an indicator with a particular security. PFCB exhibits some trend, but price action within this trend is choppy, and money flow cannot maintain a positive or negative bias. It would be better to find a different indicator for this stock.

### Caveat: CMF and Gaps <a href="#caveatwatch_out_for_cmf_s_calculation_quirk" id="caveatwatch_out_for_cmf_s_calculation_quirk"></a>

The Money Flow Multiplier in Chaikin Money Flow focuses on the level of the close relative to the high-low range for a given period (day, week, month). With this formula, a security could gap down and close significantly lower, but the Money Flow Multiplier would rise if the close were above the midpoint of the high-low range. Ignoring the change from close-to-close means that Chaikin Money Flow can sometimes disconnect with price.

The chart below shows Clorox (CLX) with a big gap down and a close near the top of the day's high-low range. Even though the stock closed sharply lower on high volume, Chaikin Money Flow rose because the Money Flow Multiplier was positive, and volume was well above average.&#x20;

<figure><img src="/files/vkp1ZaJaTDHyh2bzuRUx" alt=""><figcaption><p>CMF is misleading after a down gap</p></figcaption></figure>

The opposite can happen when a security gaps up and closes near the low for the day. The chart below shows Travellers (TRV) gapping up and closing over 1% higher on the day. Despite this jump, the close was near the low for the day, which ensured a Money Flow Multiplier near -1. As a result, almost all of the day's volume was counted as negative money flow, and the Chaikin Money Flow fell.

<figure><img src="/files/lqM9fRZhgWMF1bhF8KnW" alt=""><figcaption><p>CMF is misleading after an up gap</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Chaikin Money Flow is an oscillator that measures buying and selling pressure over a set period of time. At its most basic, money flow favors the bulls when CMF is positive and the bears when negative. Chartists looking for quicker money flow shifts can look for bullish and bearish divergences. However, relying on CMF has risks. Selling pressure still has the edge in negative territory, even when there is a bullish divergence. This bullish divergence simply shows less selling pressure. It takes a move into positive territory to indicate actual buying pressure. As a money flow oscillator, CMF can be used in conjunction with pure price oscillators, such as [MACD](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) or [RSI](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md). As with all indicators, Chaikin Money Flow should not be used as a stand-alone indicator.&#x20;

***

## Charting with Chaikin Money Flow <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Chaikin Money Flow can be set as an indicator above or below the main price plot. Because it is shown in area format, it is not suited for placement behind the security's price plot. Once the indicator is chosen from the dropdown list, a CMF indicator is added to the chart with the default setting of 20 periods. This setting can be adjusted to increase or decrease sensitivity. Users can add horizontal lines, moving averages, or other overlays. Chartists can even plot a second and longer Chaikin Money Flow indicator on top of the other, as shown below. Periods of overlap between the two CMF indicators show when money flow is strong for two different periods.&#x20;

[Click here for a live version of this chart](https://stockcharts.com/sc3/ui/?s=CAT\&id=p81912421830).

<figure><img src="/files/SkENyAI5lK4hmKfQQ44u" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/kL7o2IyXeYX5NZ6Xpdnw" alt=""><figcaption><p>SharpCharts settings for Chaikin Money Flow</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Mass Index indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#chaikin_money_flow_cmf) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above or below the security's price plot.

<figure><img src="/files/jBKhKSVx9CeUXnhCBSLM" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/utUJbSGx)

By default, the indicator is calculated using 20 periods. This parameter can be adjusted to meet your technical analysis needs.

## Scanning for Chaikin Money Flow <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on CMF values. Below are some example scans that can be used for CMF-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a CMF-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### CMF Turns Positive and RSI Moves Above 50 <a href="#cmf_turns_positive_and_rsi_moves_above_50" id="cmf_turns_positive_and_rsi_moves_above_50"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. Accumulation and buying pressure is identified when Chaikin Money Flow moves into positive territory. Price momentum confirms when RSI moves above 50 (the centerline). This scan is meant as a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily CMF(20) crosses 0] 
AND [Daily RSI(14,Daily Close) crosses 50]
```

### CMF Turns Negative and RSI Moves Below 45 <a href="#cmf_turns_negative_and_rsi_moves_below_45" id="cmf_turns_negative_and_rsi_moves_below_45"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. Distribution and selling pressure are identified when Chaikin Money Flow moves into negative territory. Price momentum confirms when RSI moves below 50 (the centerline). This scan is meant as a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [0 crosses Daily CMF(20)] 
AND [50 crosses Daily RSI(14,Daily Close)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Chaikin Money Flow scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.
{% endhint %}

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like CMF, base the scan on the “Last Market Close.” Examples of other volume-based indicators include Accumulation/Distribution, On Balance Volume, and the PVO.
{% endhint %}

## Additional Resources <a href="#additional_resources" id="additional_resources"></a>

### Recommended Books <a href="#stocks_commodities_magazine_articles" id="stocks_commodities_magazine_articles"></a>

[*Technical Analysis of the Financial Markets*](https://a.co/d/1g4BtEl) covers it all with explanations that are simple and clear. Murphy covers most the major charts patterns and indicators. A complete chapter is devoted to understanding volume and open interest.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-money-flow-cmf.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
