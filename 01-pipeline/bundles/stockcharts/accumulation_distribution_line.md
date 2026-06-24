> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md).

# Accumulation/Distribution Line

## What Is the Accumulation Distribution Line? <a href="#what_is_the_accumulation_distribution_line" id="what_is_the_accumulation_distribution_line"></a>

The Accumulation Distribution Line is a volume-based indicator developed by Marc Chaikin to measure the cumulative flow of money into and out of a security.

Chaikin originally called the indicator the Cumulative Money Flow Line. As with cumulative indicators, the Accumulation Distribution Line is a running total of each period's Money Flow Volume.

* First, a multiplier is calculated based on the relationship of the close to the high-low range.
* Second, the Money Flow Multiplier is multiplied by the period's volume to come up with a Money Flow Volume.

A running total of the Money Flow Volume forms the Accumulation Distribution Line. Chartists can use this indicator to affirm a security's underlying trend or anticipate reversals when the indicator diverges from the security price.

## Calculating the Accumulation Distribution Line <a href="#how_do_you_calculate_the_accumulation_distribution_line" id="how_do_you_calculate_the_accumulation_distribution_line"></a>

There are three steps to calculating the Accumulation Distribution Line (ADL). First, calculate the Money Flow Multiplier. Second, multiply this value by volume to find the Money Flow Volume. Third, create a running total of Money Flow Volume to form the Accumulation Distribution Line (ADL).

```
               
  1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 

  2. Money Flow Volume = Money Flow Multiplier x Volume for the Period

  3. ADL = Previous ADL + Current Period's Money Flow Volume
```

The Money Flow Multiplier fluctuates between +1 and -1. As such, it holds the key to the Money Flow Volume and the Accumulation Distribution Line. The multiplier is positive when the close is in the upper half of the high-low range and negative when in the lower half. This makes sense, as buying pressure is stronger than selling pressure when prices close in the upper half of the period's range (and vice versa). The Accumulation Distribution Line rises when the multiplier is positive and falls when the multiplier is negative.

<figure><img src="/files/Y1onxMFS77i2OD5zNL3M" alt=""><figcaption><p>Chart 1  -  Accumulation Distribution Line</p></figcaption></figure>

The multiplier adjusts the amount of volume that ends up in the Money Flow Volume. Volume is, in effect, reduced unless the Money Flow Multiplier is at its extremes (+1 or -1). The multiplier is +1 when the close is on the high and -1 when the close is on the low. All volume is positive when +1 and all volume is negative when -1. At 0.50, only half of the volume translates into the period's Money Flow Volume.&#x20;

The table below displays the Money Flow Multipliers, Money Flow Volume, and Accumulation Distribution Line for a stock. Notice how the multiplier is between 0.50 and 1 when the close is strong and between -0.50 and -1 when the close is weak.

<figure><img src="/files/FL7ejhQ3ZrrUJFfhV2Tk" alt=""><figcaption><p>Table 1  -  Accumulation Distribution Line</p></figcaption></figure>

Click below to download an Excel spreadsheet that calculates the Accumulation Distribution Line.

{% file src="/files/49qPGnNdWI6p5rCx8aqh" %}

## Interpreting the Accumulation Distribution Line <a href="#what_does_the_accumulation_distribution_line_tell_you" id="what_does_the_accumulation_distribution_line_tell_you"></a>

The Accumulation Distribution Line is a cumulative measure of each period's volume flow, or money flow. A high positive multiplier combined with high volume shows strong buying pressure that pushes the indicator higher. Conversely, a low negative number combined with high volume reflects strong selling pressure that pushes the indicator lower. Money Flow Volume accumulates to form a line that either confirms or contradicts the underlying price trend. In this regard, the indicator is used to either reinforce the underlying trend or cast doubts on its sustainability. An uptrend in prices with a downtrend in the Accumulation Distribution Line suggests underlying selling pressure (distribution) that could foreshadow a bearish reversal on the price chart. A downtrend in prices with an uptrend in the Accumulation Distribution Line indicates underlying buying pressure (accumulation) that could foreshadow a bullish price reversal.

### ADL versus OBV <a href="#adl_versus_obv" id="adl_versus_obv"></a>

The Accumulation Distribution Line and On Balance Volume (OBV) are cumulative volume-based indicators that sometimes move in opposite directions because their basic formulas are different. Joe Granville developed [On Balance Volume](/table-of-contents/glossary/glossary-o.md#on_balance_volume_obv) (OBV) as a cumulative measure of positive and negative volume flow. OBV adds a period's total volume when the close is up and subtracts it when the close is down. A cumulative total of this positive and negative volume flow forms the OBV line. This line can then be compared with the price chart of the underlying security to look for divergences or confirmation.

<figure><img src="/files/sytedESAjnCpmVCDMCZ6" alt=""><figcaption><p>Chart 2  -  Accumulation Distribution Line</p></figcaption></figure>

As the formula above shows, Chaikin took a different approach by completely ignoring the change from one period to the next. Instead, the Accumulation Distribution Line focuses on the level of the close relative to the high-low range for a given period (day, week, month). With this formula, a security could gap down and close significantly lower, but the Accumulation Distribution Line would rise if the close were above the midpoint of the high-low range. The chart above shows Clorox (CLX) with a big gap down and a close near the top of the day's high-low range. OBV moved sharply lower because the close was below the prior close. The Accumulation Distribution Line moved higher because the close was near the high of the day.

### Using the ADL for Trend Confirmation <a href="#using_the_adl_for_trend_confirmation" id="using_the_adl_for_trend_confirmation"></a>

Trend confirmation is a pretty straightforward concept. An uptrend in the Accumulation Distribution Line reinforces an uptrend on the price chart and vice versa. The chart below shows Freeport McMoran (FCX) and the Accumulation Distribution Line advancing in February-March, declining from April to June and advancing from July to January. The Accumulation Distribution Line confirmed each of these price trends.

<figure><img src="/files/o9sri1g2xGxHhxUJCRzB" alt=""><figcaption><p>Chart 3  -  Accumulation Distribution Line</p></figcaption></figure>

### ADL Divergences <a href="#adl_divergences" id="adl_divergences"></a>

Bullish and bearish divergences are where it starts getting interesting. A bullish divergence forms when price moves to new lows, but the Accumulation Distribution Line does not confirm these lows and moves higher. A rising Accumulation Distribution Line shows, well, accumulation. Think of this as basically stealth buying pressure. Based on the theory that volume precedes price, chartists should be on alert for a bullish reversal on the price chart.

The chart below shows Nordstrom (JWN) with the Accumulation Distribution Line. Notice how it is easy to compare price action when the indicator is placed “behind” the price plot. The indicator (pink) and the price trend moved in unison from February to June. Signs of accumulation emerged as the indicator bottomed in early July and started moving higher. JWN moved to a new low in late August. Even though the indicator showed signs of buying pressure, it was important to wait for a bullish catalyst or confirmation on the price chart. This catalyst came as the stock gapped up and surged on big volume.

<figure><img src="/files/Xwl3WBmcqhfs9UCyP5pO" alt=""><figcaption><p>Chart 4  -  Accumulation Distribution Line</p></figcaption></figure>

A bearish divergence forms when price moves to new highs, but the Accumulation Distribution Line does not confirm and moves lower. This shows distribution or underlying selling pressure that can foreshadow a bearish reversal on the price chart.

<figure><img src="/files/adcsWPU1qWGc8ZI0e5rG" alt=""><figcaption><p>Chart 5  -  Accumulation Distribution Line</p></figcaption></figure>

The chart above shows Southwest Airlines (LUV) with the Accumulation Distribution Line peaking two months ahead of prices. The indicator not only peaked, but it also moved lower in March and April, which reflected some selling pressure. LUV confirmed weakness with a support break on the price chart and RSI moved below 40 shortly afterward. RSI often trades in bull zones (40-80) and bear zones (20-60). [RSI](/table-of-contents/glossary/glossary-r.md#relative_strength_index_rsi) held in the bull zone until early May and then moved into a bear zone.

### Disconnect with Prices <a href="#disconnect_with_prices" id="disconnect_with_prices"></a>

The Accumulation Distribution Line is an indicator based on a derivative of price and volume. This makes it at least two steps removed from the actual price of the underlying security. Moreover, the Money Flow Multiplier does not take into account price changes from period to period. As such, it cannot be expected to always affirm price action or successfully predict price reversals with divergences. Sometimes there is a disconnect between prices and the indicator. Sometimes the Accumulation Distribution Line simply doesn't work. This is why it is vitally important to use the Accumulation Distribution Line, and all indicators for that matter, in conjunction with price/trend analysis and/or other indicators.

<figure><img src="/files/9nsPbgiHpR34H822ooIc" alt=""><figcaption><p>Chart 6  -  Accumulation Distribution Line</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

**The Accumulation Distribution Line can be used to gauge the general flow of volume.** An uptrend indicates that buying pressure is prevailing on a regular basis, while a downtrend indicates that selling pressure is prevailing. Bullish and bearish divergences serve as alerts for a potential reversal on the price chart. As with all indicators, it is important to use the Accumulation Distribution Line in conjunction with other aspects of technical analysis, such as [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) and [chart patterns](/table-of-contents/chart-analysis/introduction-to-chart-patterns.md). It is not a standalone indicator.

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Accumulation Distribution Line is available in SharpCharts as an indicator. After selecting, the indicator can be positioned above, below or behind the price of the underlying security. Positioning “behind price” makes it easy to compare with the underlying security. Chartists can also add a moving average to the indicator by using the advanced options. [**Click here**](https://stockcharts.com/sc3/ui/?s=IBM\&p=D\&yr=0\&mn=8\&dy=0\&id=p93414126571\&listNum=30\&a=222506084) for a live chart with the Accumulation Distribution Line.

<figure><img src="/files/o9d33ZRbPSxCjX4wiezm" alt=""><figcaption><p>Chart 7  -  Accumulation Distribution Line</p></figcaption></figure>

<figure><img src="/files/YTFSdcHRwZYwI4JX7oha" alt=""><figcaption><p>SharpCharts  -  Accumulation Distribution Line</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Bullish Divergence in OBV and ADL <a href="#bullish_divergence_in_obv_and_adl" id="bullish_divergence_in_obv_and_adl"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 daily volume over the last 60 days. Potential bullish divergences are found by looking for stocks where price is BELOW the 65-day SMA and 20-day SMA, but OBV and the Accumulation Distribution Line are ABOVE the 65-day SMA and 20-day SMA.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily Close < Daily SMA(65,Daily Close)] 
AND [Daily AccDist > Daily AccDist Signal (65)] 
AND [Daily OBV > Daily OBV Signal(65)] 
AND [Daily Close < Daily SMA(20,Daily Close)] 
AND [Daily AccDist > Daily AccDist Signal (20)] 
AND [Daily OBV > Daily OBV Signal(20)]
```

### Bearish divergence in OBV and ADL <a href="#bearish_divergence_in_obv_and_adl" id="bearish_divergence_in_obv_and_adl"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 daily volume over the last 60 days. Potential bearish divergences are found by looking for stocks where price is ABOVE the 65-day SMA and 20-day SMA, but OBV and the Accumulation Distribution Line are BELOW the 65-day SMA and 20-day SMA.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily Close > Daily SMA(65,Daily Close)] 
AND [Daily AccDist < Daily AccDist Signal (65)] 
AND [Daily OBV < Daily OBV Signal(65)] 
AND [Daily Close > Daily SMA(20,Daily Close)] 
AND [Daily AccDist < Daily AccDist Signal (20)] 
AND [Daily OBV < Daily OBV Signal(20)]
```

For more details on the syntax for Accumulation Distribution Line scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like Accumulation/Distribution, base the scan on the “Last Market Close.” Examples of other volume-based indicators include Chaikin Money Flow, On Balance Volume, and the PVO.
{% endhint %}

## FAQs <a href="#accumulation_distribution_line_faqs" id="accumulation_distribution_line_faqs"></a>

<details>

<summary>What is the general usage of the Accumulation Distribution Line?</summary>

The Accumulation Distribution Line can be used to gauge the general flow of volume, indicating whether buying or selling pressure is prevailing. It can also serve as an alert for potential reversal on the price chart when bullish and bearish divergences occur.

</details>

<details>

<summary>How does volume affect the Accumulation Distribution Line?</summary>

Volume plays a crucial role in the calculation of the Accumulation Distribution Line. The Money Flow Multiplier is multiplied by the period's volume to determine the Money Flow Volume, which subsequently affects the trend of the Accumulation Distribution Line. For instance, a high positive multiplier combined with high volume shows strong buying pressure that pushes the indicator higher, and a low negative number combined with high volume reflects strong selling pressure that pushes the indicator lower.

</details>

<details>

<summary>What is the difference between the Accumulation Distribution Line and On Balance Volume (OBV)?</summary>

The Accumulation Distribution Line and On Balance Volume are both cumulative volume-based indicators, but their calculations are different. While OBV adds a period's total volume when the close is up and subtracts it when the close is down, the Accumulation Distribution Line focuses on the level of the close relative to the high-low range for a given period.

</details>

<details>

<summary>How does the Accumulation Distribution Line confirm or contradict an underlying price trend?</summary>

The Accumulation Distribution Line measures volume flow, or money flow. A high positive multiplier combined with high volume shows strong buying pressure that pushes the indicator higher, confirming an uptrend. Conversely, a low negative number combined with high volume reflects strong selling pressure that pushes the indicator lower, contradicting an uptrend.

</details>

<details>

<summary>Can the Accumulation Distribution Line be used as a standalone indicator?</summary>

No, it is important to use the Accumulation Distribution Line in conjunction with other aspects of technical analysis, such as momentum oscillators and chart patterns, as well as price/trend analysis. It is not a standalone indicator.

</details>

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/67tLBFU) covers it all with explanations that are simple and clear. Murphy covers most of the major chart patterns and indicators. A complete chapter is devoted to understanding volume and open interest.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
