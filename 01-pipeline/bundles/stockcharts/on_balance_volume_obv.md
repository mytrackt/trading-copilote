> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/on-balance-volume-obv.md).

# On Balance Volume (OBV)

## What Is On Balance Volume (OBV)? <a href="#what_is_on_balance_volume_obv" id="what_is_on_balance_volume_obv"></a>

The On Balance Volume (OBV) is an indicator that assesses a security's buying and selling pressure by analyzing cumulative volume. It adds volume on days when the price rises and subtracts it on days when the price declines.

<figure><img src="/files/tiRsP77WLnYVcDAI0HEn" alt=""><figcaption><p>On Balance Volume smoothed with a 20-day EMA</p></figcaption></figure>

OBV was originally developed by Joe Granville, and he first explained it in his 1963 book *Granville's New Key to Stock Market Profits*. The OBV is noteworthy because it was among the earliest metrics to track the inflow and outflow of volume. By comparing the OBV with price action, analysts can detect divergences that may forecast future price shifts, or they can use the OBV to confirm existing price trends.

## Calculating OBV <a href="#how_is_obv_calculated" id="how_is_obv_calculated"></a>

The On Balance Volume (OBV) line is simply a running total of positive and negative volume. A period's volume is positive when the close is above the prior close and is negative when the close is below the prior close.

```
               
If the closing price is above the prior close price then: 
Current OBV = Previous OBV + Current Volume

If the closing price is below the prior close price then: 
Current OBV = Previous OBV  -  Current Volume

If the closing prices equals the prior close price then:
Current OBV = Previous OBV (no change)
```

<figure><img src="/files/SbN1KPEjsHnowXLAMXgc" alt=""><figcaption><p>On Balance Volume calculation example</p></figcaption></figure>

In the table above, volume figures were rounded off and are shown in 1000's. In other words, 8,200 really equals 8,200,000 or 8.2 million shares. First, we must determine if the stock closed up (+1) or down (-1). This number is now used as the volume multiplier to compute positive or negative volume. The last column (OBV) forms the running total for positive/negative volume. Because OBV has to start somewhere, the first value (8200) is simply equal to the first period's positive/negative volume. The chart below shows the stock price with volume and OBV.

<figure><img src="/files/UJYqx2UrkLAUTNDDn9HS" alt=""><figcaption><p>On Balance Volume rises on up days and drops on down days</p></figcaption></figure>

{% hint style="warning" %}
**Note:** The scale of OBV is not relevant, and is not even shown on SharpCharts. Instead, chartists look at whether the OBV line is up or down compared to previous trading periods.
{% endhint %}

## Interpreting OBV <a href="#how_do_you_interpret_obv" id="how_do_you_interpret_obv"></a>

Granville theorized that volume precedes price. OBV rises when volume on up days outpaces volume on down days. OBV falls when volume on down days is stronger. A rising OBV reflects positive volume pressure that can lead to higher prices. Conversely, falling OBV reflects negative volume pressure that can foreshadow lower prices. Granville noted in his research that OBV would often move before price. Expect prices to move higher if OBV is rising while prices are either flat or moving down. Expect prices to move lower if OBV is falling while prices are either flat or moving up.

The absolute value of OBV is not important. Chartists should instead focus on the characteristics of the OBV line. First, define the trend for OBV. Second, determine if the current trend matches the trend for the underlying security. Third, look for potential support or resistance levels. Once broken, the trend for OBV will change and these breaks can be used to generate signals. Also, notice that OBV is based on closing prices. Therefore, closing prices should be considered when looking for divergences or support/resistance breaks. Finally, volume spikes can sometimes throw off the indicator by causing a sharp move that will require a settling period.

### Divergences <a href="#how_do_you_read_obv_divergences" id="how_do_you_read_obv_divergences"></a>

Bullish and [bearish divergence](/table-of-contents/glossary/glossary-b.md#bearish_divergence) signals can be used to anticipate a trend reversal. These signals are truly based on the theory that volume precedes prices. A bullish divergence forms when OBV moves higher or forms a higher low even as prices move lower or forge a lower low. A bearish divergence forms when OBV moves lower or forms a lower low even as prices move higher or forge a higher high. The divergence between OBV and price should alert chartists that a price reversal could be in the making.

The chart for Starbucks (SBUX) shows a [bullish divergence](/table-of-contents/glossary/glossary-b.md#bullish_divergence) forming in July. On the price chart, SBUX moved below its June low with a lower low in early July. OBV, on the other hand, held above its June low to form a bullish divergence. OBV went on to break resistance before SBUX broke resistance. This was a classic case of volume leading price. SBUX broke resistance a week later and continued above 20 for a 30+ percent gain. The second chart shows OBV moving higher as Texas Instruments (TXN) trades within a range. Rising OBV during a trading range indicates accumulation, which is bullish.

<figure><img src="/files/LvknUy8DYHodqhL6OQnA" alt=""><figcaption><p>Bullish divergence with OBV</p></figcaption></figure>

<figure><img src="/files/9NpDHy8xww96DMOgTndA" alt=""><figcaption><p>Rising OBV during a trading range</p></figcaption></figure>

The chart for Medtronic (MDT) shows a bearish divergence with volume leading price lower. The blue dotted lines identify the divergence period. MDT moved higher (43 to 45) as OBV moved lower. Also, notice that OBV broke support during this divergence period. The uptrend in OBV reversed with the break below the February low. MDT, on the other hand, was still moving higher. Volume ultimately won the day as MDT followed volume lower with a decline into the low 30s. The second chart shows Valero Energy (VLO) with OBV forming a bearish divergence in April and a confirming support break in May.

<figure><img src="/files/WjbRMOx4zPblexvowEli" alt=""><figcaption><p>Bearish divergence with OBV</p></figcaption></figure>

<figure><img src="/files/fKmniejTzGZ0knQw8aqp" alt=""><figcaption><p>Bearish divergence with OBV</p></figcaption></figure>

### Trend Confirmation <a href="#how_do_you_use_obv_for_trend_confirmation" id="how_do_you_use_obv_for_trend_confirmation"></a>

OBV can be used to confirm a price trend, upside breakout or downside break. The chart for Best Buy (BBY) shows three confirming signals as well as confirmation of the price trend. OBV and BBY moved lower in December-January, higher from March to April, lower from May to August and higher from September to October. The trends in OBV matched the trend in BBY.

<figure><img src="/files/cvsygBssdU4vKhG6p0x0" alt=""><figcaption><p>OBV confirming price trends</p></figcaption></figure>

OBV also confirmed trend reversals in BBY. Notice how BBY broke its downtrend line in late February and OBV confirmed with a resistance breakout in March. BBY broke its uptrend line in late April and OBV confirmed with a support break in early May. BBY broke its downtrend line in early September and OBV confirmed with a trend line break a week later. These coincident signals indicated that positive and negative volume were in harmony with price.

Sometimes OBV moves step-for-step with the underlying security. In this case, OBV is confirming the strength of the underlying trend, be it down or up. The chart for Autozone (AZO) shows prices as a black line and OBV as a pink line. Both moved steadily higher from November 2009 until October 2010. Positive volume remained strong throughout the advance.

<figure><img src="/files/FwlBOaMXrUljoSyuckHz" alt=""><figcaption><p>OBV overlaid on price helps confirm price trend</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

On Balance Volume (OBV) uses volume and price to measure buying and selling pressure. Buying pressure is evident when positive volume exceeds negative volume, and the OBV line rises. Selling pressure occurs when negative volume exceeds positive volume, and the OBV line falls. Analysts can use OBV to confirm the underlying trend or look for divergences that may foreshadow a price change. As with all indicators, it's important to use OBV in conjunction with other aspects of technical analysis. It's not a standalone indicator. OBV can be combined with basic [pattern analysis](/table-of-contents/chart-analysis/chart-patterns.md) or to confirm signals from [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators).

***

## Charting with OBV <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

On Balance Volume (OBV) is available in SharpCharts as an indicator. After selecting, OBV can be positioned above, below or behind the price plot of the underlying security. Positioning it behind the plot makes it easy to compare OBV with the underlying security. Chartists can also add a [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) or another overlay to OBV using the Overlay setting for the OBV indicator.

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=IBM\&a=2266088106\&p=D\&b=5\&g=0\&id=p73480075647)

<figure><img src="/files/wuvuORyBlCts0ZTyqrIj" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/fM8xq2qSMcpPmON0pcRi" alt=""><figcaption><p>SharpCharts Settings for On Balance Volume</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Mass Index indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#on_balance_volume_obv) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/OyfFxoZd9NgNltdEIAis" alt=""><figcaption></figcaption></figure>

[Click here for a live version of the chart.](https://schrts.co/WkuWWNyB)

The indicator does not have any parameters, but the settings panel can be used to change the line style or to add an overlay to the indicator.

## Scanning for OBV <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on OBV values. Below are some example scans that can be used for OBV-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when an OBV-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

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

{% hint style="info" %}
**Learn More.** For more details on the syntax for OBV scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#on_balance_volume_obv) in the Support Center.
{% endhint %}

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like OBV, base the scan on the “Last Market Close.” Examples of other volume-based indicators include Accumulation/Distribution, Chaikin Money Flow, and the PVO.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/1eLUbD7) covers it all with explanations that are simple and clear. Murphy covers all the major charts patterns and indicators, including OBV. A complete chapter is devoted to understanding volume and open interest.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/on-balance-volume-obv.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
