> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels.md).

# Keltner Channels

## What Are Keltner Channels? <a href="#introduction" id="introduction"></a>

Keltner Channels are volatility-based envelopes set above and below an exponential moving average. This indicator is similar to Bollinger Bands, which use the standard deviation to set the bands. Instead of using the standard deviation, Keltner Channels use the Average True Range (ATR) to set channel distance. The channels are typically set two Average True Range values above and below the 20-day EMA. The exponential moving average dictates direction and the Average True Range sets channel width. **Keltner Channels are a trend following indicator used to identify reversals with channel breakouts and channel direction.** Channels can also be used to identify overbought and oversold levels when the trend is flat.

<figure><img src="/files/s0ATjWqkoDYSxjrnJiFZ" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=XLP\&p=D\&b=5\&g=0\&id=p95754873344)

In his 1960 book, How to Make Money in Commodities, Chester Keltner introduced the “Ten-Day Moving Average Trading Rule,” which is credited as the original version of Keltner Channels. This original version started with a 10-day SMA of the typical price {(H+L+C)/3)} as the centerline. The 10-day SMA of the High-Low range was added and subtracted to set the upper and lower channel lines. Linda Bradford Raschke introduced the newer version of Keltner Channels in the 1980s. Like Bollinger Bands, this new version used a volatility based indicator, Average True Range (ATR), to set channel width. StockCharts.com uses this newer version of Keltner Channels.

{% hint style="info" %}
**Learn More:** [Average True Range (ATR)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md)
{% endhint %}

## Keltner Channels Calculation <a href="#keltner_channels_calculation" id="keltner_channels_calculation"></a>

There are three steps to calculating Keltner Channels. First, select the length for the exponential moving average. Second, choose the time periods for the Average True Range (ATR). Third, choose the multiplier for the Average True Range.

{% code overflow="wrap" %}

```
Middle Line: 20-day exponential moving average
Upper Channel Line: 20-day EMA + (2 x ATR(10))
Lower Channel Line: 20-day EMA - (2 x ATR(10))
```

{% endcode %}

The example above is based on the default settings for SharpCharts. Because moving averages lag price, a longer moving average will have more lag and a shorter moving average will have less lag. ATR is the basic volatility setting. Short timeframes, such as 10, produce a more volatile ATR that fluctuates as 10-period volatility ebbs and flows. Longer timeframes, such as 100, smooth these fluctuations to produce a more constant ATR reading. The multiplier has the most effect on the channel width. Simply changing from 2 to 1 will cut channel width in half. Increasing from 2 to 3 will increase channel width by 50%.

Here's a chart showing three Keltner Channels set at 1, 2, and 3 ATRs away from the central moving average. This particular technique has been advocated by Kerry Lovvorn of [SpikeTrade.com](http://spiketrade.com/) for years.

<figure><img src="/files/BDDe1OnfaD0a3Z2aLyrH" alt=""><figcaption><p>Keltner Channels - Calculation Example</p></figcaption></figure>

The chart above shows the default Keltner Channels in red, a wider channel in blue and a narrower channel in green. The blue channels were set three Average True Range values above and below (3 x ATR). The green channels used one ATR value. All three share the 20-day EMA, which is the dotted line in the middle. The indicator windows show differences in the Average True Range (ATR) for 10 periods, 50 periods and 100 periods. Notice how the short ATR (10) is more volatile and has the widest range. In contrast, 100-period ATR is much smoother with a less volatile range.

## Interpreting Keltner Channels <a href="#interpreting_keltner_channels" id="interpreting_keltner_channels"></a>

Indicators based on channels, bands and envelopes are designed to encompass most price action. Therefore, moves above or below the channel lines warrant attention because they are relatively rare. Trends often start with strong moves in one direction or another. A surge above the upper channel line shows extraordinary strength, while a plunge below the lower channel line shows extraordinary weakness. Such strong moves can signal the end of one trend and the beginning of another.

With an exponential moving average as its foundation, Keltner Channels are a trend following indicator. As with moving averages and other trend-following indicators, Keltner Channels lag price action. The direction of the moving average dictates the direction of the channel. In general, a downtrend is present when the channel moves lower, while an uptrend exists when the channel moves higher. The trend is flat when the channel moves sideways.

A channel upturn and break above the upper trend line can signal the start of an uptrend. A channel downturn and break below the lower trend line can signal the start a downtrend. Sometimes a strong trend does not take hold after a channel breakout and prices oscillate between the channel lines. Such trading ranges are marked by a relatively flat moving average. The channel boundaries can then be used to identify overbought and oversold levels for trading purposes.

{% hint style="info" %}
**Learn More:** [Moving Averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md)
{% endhint %}

### Identifying the Start of an Uptrend <a href="#uptrend" id="uptrend"></a>

The chart below shows Archer Daniels Midland (ADM) starting an uptrend as the Keltner Channels turn up and the stock surges above the upper channel line. ADM was in a clear downtrend in April-May as prices continued to pierce the lower channel. With a strong thrust up in June, prices exceeded the upper channel and the channel turned up to start a new uptrend. Notice that prices held above the lower channel on dips in early and late July.

<figure><img src="/files/hVwetvDiPfQldwVcSunG" alt=""><figcaption><p>Keltner Channels - Uptrend Example</p></figcaption></figure>

Even with a new uptrend established, it is often prudent to wait for a pullback or better entry point to improve the reward-to-risk ratio. Momentum oscillators or other indicators can then be employed to define oversold readings. This chart shows [StochRSI](/table-of-contents/glossary/glossary-s.md#stochrsi), one of the more sensitive momentum oscillators, dipping below .20 to become oversold at least three times during the uptrend. The subsequent crosses back above .20 signaled a resumption of the uptrend.

### Identifying the Start of a Downtrend <a href="#downtrend" id="downtrend"></a>

The chart below shows Nvidia (NVDA) starting a downtrend with a sharp decline below the lower channel line. After this initial break, the stock met resistance near the 20-day EMA (middle line) from mid-May until early August. The inability to even come close to the upper channel line showed strong downside pressure.

<figure><img src="/files/Vs5XqlS7j5atpaUlveab" alt=""><figcaption><p>Keltner Channels - Downtrend Example</p></figcaption></figure>

A 10-period [Commodity Channel Index (CCI)](/table-of-contents/glossary/glossary-c.md#commodity_channel_index_cci) is shown as the momentum oscillator to identify short-term overbought conditions. A move above 100 is considered overbought. A subsequent move back below 100 signals a resumption of the downtrend. This signal worked well until September. These failed signals indicated a possible trend change that was subsequently confirmed with a break above the upper channel line.

### Identifying Breakouts from a Trading Range <a href="#flat_trend" id="flat_trend"></a>

Once a trading range or flat trading environment has been identified, traders can use the Keltner Channels to identify overbought and oversold levels. A trading range can be identified with a flat moving average and the Average Directional Index (ADX). The chart below shows IBM fluctuating between support in the 120-122 area and resistance in the 130-132 area from February to late September. The 20-day EMA (middle line) lagged price action, but flattened out from April to September.

The indicator window shows ADX (black line) confirming a weak trend. Low and falling ADX shows a weak trend. High and rising ADX shows a strong trend. ADX was below 40 the entire time and below 30 most of the time. This reflects the absence of a trend. Also, notice that ADX peaked in early June and fell until late August.

<figure><img src="/files/pr9nOhj7ooS0tMAqUl5D" alt=""><figcaption><p>Keltner Channels - Breakout from a Trading Range</p></figcaption></figure>

Armed with the prospects of a weak trend and trading range, traders can use Keltner Channels to anticipate reversals. In addition, notice that the channel lines often coincide with chart support and resistance. IBM dipped below the lower channel line three times from late May until late August. These dips provided low-risk entry points. The stock did not manage to reach the upper channel line, but did get close as it reversed in the resistance zone. The Disney chart shows a similar situation.

<figure><img src="/files/4FzvDdV2nMQWXygga9Z5" alt=""><figcaption><p>Keltner Channels - Trading Range Example</p></figcaption></figure>

### Keltner Channels vs Bollinger Bands <a href="#versus_bollinger_bands" id="versus_bollinger_bands"></a>

There are two differences between Keltner Channels and Bollinger Bands. First, Keltner Channels are smoother than Bollinger Bands because the width of the Bollinger Bands is based on the standard deviation, which is more volatile than the Average True Range (ATR). Many consider this a plus because it creates a more constant width. This makes Keltner Channels well suited for trend following and trend identification. Second, Keltner Channels also use an exponential moving average, which is more sensitive than the simple moving average used in Bollinger Bands. The chart below shows Keltner Channels (blue), Bollinger Bands (pink), Average True Range (10), Standard Deviation (10) and Standard Deviation (20) for comparison. Notice how the Keltner Channels are smoother than the Bollinger Bands. Also, notice how the Standard Deviation covers a larger range than the Average True Range (ATR).

<figure><img src="/files/A8opO1FyuwYrzWlaoPUZ" alt=""><figcaption><p>Keltner Channels vs Bollinger Bands</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md)
{% endhint %}

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

**Keltner Channels are a trend following indicator designed to identify the underlying trend.** Trend identification is more than half the battle. The trend can be up, down or flat. Using the methods described above, traders and investors can identify the trend to establish a trading preference. Bullish trades are favored in an uptrend and bearish trades are favored in a downtrend. A flat trend requires a more nimble approach because prices often peak at the upper channel line and trough at the lower channel line. As with all analysis techniques, Keltner Channels should be used in conjunction with other indicators and analysis. Momentum indicators offer a good complement to the trend-following Keltner Channels.

{% hint style="info" %}
**Learn More:** [Momentum Indicators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators)
{% endhint %}

***

## Charting with Keltner Channels <a href="#charting_with_keltner_channels" id="charting_with_keltner_channels"></a>

The Keltner Channels overlay can be added to SharpCharts and ACP Charts.

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Keltner Channels can be found in SharpCharts as a price overlay. As with a moving average, Keltner Channels should be shown on top of a price plot. Upon selecting the indicator from the dropdown box, the default setting will appear in the parameters window (20,2.0,10). The first number (20) sets the periods for the exponential moving average. The second number (2.0) is the ATR multiplier. The third number (10) is the number of periods for Average True Range (ATR). These default parameters set the channels 2 ATR values above/below the 20-day EMA. Users can change the parameters to suit their charting needs.

[Click here for a live version of the chart.](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&b=5\&g=0\&id=p14639241588\&a=211776022)

<figure><img src="/files/1h9b5mGLwxo5j7XOJBPw" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/Pj8novJSIeME9w9ahDcq" alt=""><figcaption><p>SharpCharts settings for the Keltner Channels overlay</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Keltner Channel overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#keltner_channels) in the Support Center.
{% endhint %}

### Using with StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

This overlay can be added from the Chart Settings panel for your StockChartsACP chart. Keltner Channels can be overlaid on the security's price plot or on an indicator panel.

<figure><img src="/files/HADVHjj2ViehR3NKrxul" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/iMUpRAaf)

By default, the overlay uses a 20-period EMA, 10 periods for the ATR, and an ATR multiplier of 2.0. These parameters can be adjusted to meet your technical analysis needs.

## Scanning for Keltner Channels <a href="#scanning_for_keltner_channels" id="scanning_for_keltner_channels"></a>

StockCharts members can screen for stocks based on Keltner Channel values. Below are some example scans that can be used for Keltner Channel-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a Keltner Channel-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Oversold after Bullish Keltner Channel Breakout <a href="#oversold_after_bullish_keltner_channel_breakout" id="oversold_after_bullish_keltner_channel_breakout"></a>

This scan looks for stocks that broke above their upper Keltner Channel 20 days ago to affirm or establish an uptrend. The current 10-period CCI is below -100 to indicate a short-term oversold condition.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]

AND [20 days ago Daily High > 20 days ago Daily Upper Kelt Chan(20,2.0,10)]
AND [Daily CCI(10) < -100]
```

### Overbought after Bearish Keltner Channel Breakout <a href="#overbought_after_bearish_keltner_channel_breakout" id="overbought_after_bearish_keltner_channel_breakout"></a>

This scan looks for stocks that broke below their lower Keltner Channel 20 days ago to affirm or establish a downtrend. The current 10-period CCI is above +100 to indicate a short-term overbought condition.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]

AND [20 days ago Daily Low < 20 days ago Daily Lower Kelt Chan(20,2.0,10)]
AND [Daily CCI(10) > 100]
```

{% hint style="info" %}
**Learn More:** For more details on the scan syntax to use for Keltner Channel scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#keltner_channels) in the Support Center.
{% endhint %}

## Additional Resources <a href="#recommended_books" id="recommended_books"></a>

### Recommended Books <a href="#recommended_books" id="recommended_books"></a>

Even though Keltner Channels are not used specifically in Thomas Carr's [*Trend Trading for a Living*](https://a.co/d/6qP0b1P), the book shows traders how to trade in the direction of the underlying trend. Carr also shows readers how to configure a bullish and bearish watch list from which to set your entry and exit prices.

Michael Covel's [*Trend Following*](https://a.co/d/a9zSIWz) introduces the fundamental concepts and techniques for a variety of trend following systems. Covel shows why market prices contain all available information, and readers will learn how to interpret price movements and profit from trend following.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
