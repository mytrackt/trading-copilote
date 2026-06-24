> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/price-channels.md).

# Price Channels

## What Are Price Channels?

Price Channels are lines set above and below the price of a security. The upper channel is set at the x-period high and the lower channel is set at the x-period low. For a 20-day Price Channel, the upper channel would equal the 20-day high and the lower channel would equal the 20-day low. The dotted centerline is the midpoint between the two channel lines. Price Channels can be used to identify upward thrusts that signal the start of an uptrend or downward plunges that signal the start of a downtrend. Price Channels can also be used to identify overbought or oversold levels within a bigger downtrend or uptrend.

{% hint style="warning" %}
**Note:** This indicator, developed by Richard Donchian, is sometimes referred to as Donchian Channels.
{% endhint %}

***

## Calculating Price Channels <a href="#calculation" id="calculation"></a>

{% code overflow="wrap" %}

```
Upper Channel Line: 20-day high
Lower Channel Line: 20-day low
Centerline: (20-day high + 20-day low)/2 
```

{% endcode %}

The formula above is based on a daily chart and a 20-period Price Channel, which is the default setting in SharpCharts. Price Channels can be used on intraday, daily, weekly, or monthly charts. The look-back period (20) can be shorter or longer. Shorter look-back periods, such as 10 days, produce tighter channel lines. Longer look-back periods produce wider channels.

<figure><img src="/files/nAqxIAFU2S2hGtK3U4zL" alt="Chart from StockCharts.com displaying the Price Channels overlay."><figcaption><p>An example of the Price Channels overlay in SharpCharts.</p></figcaption></figure>

The Price Channel formula doesn't include the most recent period. Price Channels are based on prices prior to the current period. A 20-day Price Channel for October 21 would be based on the 20-day high and 20-day low ending the day before, October 20. A channel break would not be possible if the most recent period was used.&#x20;

In the chart below, notice how price broke above the upper price channel because it was based on the next-to-the-last bar, not the current bar.

<figure><img src="/files/V53rvAqQgIsN8l2fElhm" alt="Chart showing how price channels are based on the previous price bar"><figcaption><p>Price breaks out above upper channel because the high was based on the previous bar.</p></figcaption></figure>

***

## Interpreting Price Channels <a href="#interpretation" id="interpretation"></a>

Price Channels can be used to identify trend reversals or overbought/oversold levels that denote pullbacks within a bigger trend. A surge above the upper channel line shows extraordinary strength that can signal the start of an uptrend. Conversely, a plunge below the lower channel line shows serious weakness that can signal the start of a downtrend. Once an uptrend has started, chartists can move to a shorter timeframe to identify pullbacks with oversold readings. A move below the lower channel line indicates oversold conditions that can foreshadow an end to the pullback. Similarly, short-term bounces within a bigger uptrend can be identified with Price Channels. A move above the upper channel line signals [overbought](/table-of-contents/glossary/glossary-o.md#overbought) conditions that can foreshadow an end to the bounce.

***

## Identifying Trends With Price Channels <a href="#trend_identification" id="trend_identification"></a>

Price Channels can be used to identify strong moves that may result in lasting trend reversals. A move above the 20-day Price Channel signals a new 20-day high. A move above the 20-week Price Channel signals a new 20-week high. A 20-week high is more consequential than a 20-day high. The choice of timeframe depends on your trading timeframe and rationale for using Price Channels. For example, you can use weekly charts with 20-week Price Channels to determine the big trend and overall trading bias.

The chart below shows weekly prices over a 4-1/2-year period. The green arrows mark weekly highs above the upper channel line, which signaled the start of an uptrend. The red arrows mark weekly lows below the lower channel, which signaled the start of a downtrend. These channel breaks caught a few good trends, but there were two whipsaws or bad signals. Indicator signals are not perfect, and there will be whipsaws. It's part of the game.

<figure><img src="/files/SY6xSEJeTx5JqygYQTjj" alt="Example of a chart from StockCharts.com showing how Price Channels can be used in your trading although sometimes there can be unreliable signals"><figcaption><p>Here's an example of how Price Channels can be applied to your trading. A few signals ended up being whipsaws or bad signals.</p></figcaption></figure>

To filter signals further, you could use a close-only line plot. The next chart shows the same 4 1/2-year period with 20-week Price Channels and the security as a close-only line plot. This eliminates the intra-week highs and lows. Notice that the price did not close above the upper channel line in May 2008 or below the lower channel line in May 2010 (blue arrows). Using a close-only price chart reduced volatility and signals.

<figure><img src="/files/pr5j4jPVPnVrhEhRD3qz" alt="A close-only line plot chart from StockCharts.com shows that signals and volatility are reduced "><figcaption><p>Adding a close-only line plot can help filter signals and reduce volatility.</p></figcaption></figure>

***

## Price Channels Are Similar to Stochastics <a href="#similar_to_stochastics" id="similar_to_stochastics"></a>

Price Channels are similar to [the Stochastic Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md) in terms of what they measure. The Stochastic Oscillator measures the close's level relative to the high-low range over a given period of time, say 20 days. It is relatively high when the close is near the high end of its 20-day range and low when it's near the low end of this range.

Let's compare the 20-day Fast Stochastic Oscillator with 20-day Price Channels. The Stochastic Oscillator is usually above 80 when prices exceed the upper Price Channel. Similarly, the 20-day Fast Stochastic Oscillator will usually be below 20 when prices move below the lower Price Channel. There is a slight timing difference because Price Channel data ends with the prior period. On the other hand, stochastic oscillator data ends with the current period. This means the Stochastic Oscillator includes the most recent price action, but Price Channels do not. Nevertheless, the two measure pretty much the same thing.

The daily chart of the SPDR Dow Industrials (DIA) below shows 20-day Price Channels (pink) with the 20-day Fast Stochastic Oscillator displayed in the panel below chart). The red and green lines indicate when prices are overbought (near the upper channel line) and oversold (near the lower channel line), respectively. The prices move above and below the centerline as the Stochastic Oscillator moves above and below 50.

<figure><img src="/files/XvddHjRpB3rtS18iqS9L" alt="Chart from StockCharts.com comparing Price Channels and Stochastic Oscillator"><figcaption><p>Chart comparing Price Channels with the Stochastic Oscillator.</p></figcaption></figure>

{% hint style="info" %}
**Learn More.** [Stochastic Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md)
{% endhint %}

***

## Identifying Overbought/Oversold Levels <a href="#overbought_oversold" id="overbought_oversold"></a>

Measuring overbought and oversold conditions can be tricky with Price Channels. Securities can become overbought and remain overbought in a strong uptrend. Similarly, securities can become oversold and remain oversold in a strong downtrend. In a strong uptrend, prices can move above the upper channel line and continue above the upper channel line. The upper channel trend line will rise as price continues above the upper channel—a sign of strength even though it looks overbought. Similarly, the Stochastic Oscillator can move above 80—technically overbought—and continue to remain there for an extended period.

Successful use of overbought and [oversold](/table-of-contents/glossary/glossary-o.md#oversold) levels depends on successful trend identification. Once you've identified a longer-term uptrend, look for oversold levels in the shorter-term trend. Short-term oversold levels occur after a pullback within a bigger uptrend.&#x20;

In the earlier examples, you saw how the weekly charts turned bullish when price surged above the upper channel line. When you've identified a bullish trend on the weekly chart, the next step would be to bring up the daily chart to look for oversold signals.&#x20;

Start by looking for pullbacks on the daily chart (see chart below). The green arrows show when price dipped below the 20-day Price Channel. There were two good signals in early July and early November. There were three touches from January–February. The first two signals were “early,” while the February signal was a direct hit.

<figure><img src="/files/b0mgCAZu5yiPMZbEeZ6p" alt="Chart from StockCharts.com with green arrows marking price pullbacks"><figcaption><p>The green arrows mark when price dips below the 20-day Price channel. </p></figcaption></figure>

Inverse logic can be applied in downtrends. A weekly downtrend starts with a plunge below the lower channel line. Once this downtrend is established, you can turn to the daily chart to look for overbought signals. Overbought signals occur after a bounce within a bigger downtrend. Downtrends tend to be faster than uptrends. This means overbought readings may not occur during a strong or fast downtrend. You may then need to tweak the Price Channel settings or use the centerline for signals. Prices are more likely to touch the centerline than the upper channel line.

***

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Price Channels tell us when a security reaches a high or low for a specific period. For example, 20-day Price Channels mark the 20-day high-low range, and 10-week Price Channels mark the 10-week high-low range. The channel centerline marks the midpoint.&#x20;

Price continuously exceeding the upper channel line is a sign of strength. It takes strong buying pressure to forge higher highs. Similarly, securities that continuously break the lower channel line show weakness. Strong selling pressure is evident with lower lows.&#x20;

Price Channels can help identify if buyers or sellers are the dominant force. As with all indicators, it's important to use other analysis techniques, such as chart patterns, indicators, or basic chart analysis, to confirm Price Channels.

***

## Price Channels With SharpCharts

Price Channels can be found in SharpCharts under **Overlays**. When you select Price Channels from the dropdown box, the default parameter setting is 20. This can be changed to align with your charting needs. A shorter look-back period will narrow the channels. A longer look-back period will widen the channels.&#x20;

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&yr=0\&mn=6\&dy=0\&id=p40145316764\&listNum=30\&a=212191178) for a live example.

***

{% hint style="info" %}
**Learn More.** To configure Price Channels overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#price_channels) in the Support Center.
{% endhint %}

***

## Scanning for Price Channels <a href="#scanning_for_price_channels" id="scanning_for_price_channels"></a>

StockCharts members can screen for stocks based on Price Channel values. Below are some example scans that can be used for Price Channels-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a Price Channels-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Oversold Bounce in Larger Uptrend <a href="#oversold_bounce_in_larger_uptrend" id="oversold_bounce_in_larger_uptrend"></a>

This scan starts with stocks that average $20 per share and 100,000 daily volume per day. An uptrend is present because the stock is trading above its 200-day SMA. The stock becomes oversold with a move below the Lower Price Channel and then turns up with a cross back above the Lower Price Channel.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close > Daily SMA(200,Daily Close)] 
AND [Daily Close crosses Daily Lower Price Chan(20)] 
AND [Daily Close > Yesterday's Daily Close]
```

### Overbought Decline in Larger Downtrend <a href="#overbought_decline_in_larger_downtrend" id="overbought_decline_in_larger_downtrend"></a>

This scan starts with stocks that average $20 per share and 100,000 daily volume per day. A downtrend is present because the stock is trading below its 200-day SMA. The stock becomes overbought with a move above the Upper Price Channel and then turns down with a cross back below the Upper Price Channel.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close < Daily SMA(200,Daily Close)] 
AND [Daily Upper Price Chan(20) crosses Daily Close] 
AND [Daily Close < Yesterday's Daily Close]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Price Channel scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#price_channels) in the Support Center.
{% endhint %}

***

## Additional Resources <a href="#additional_resources" id="additional_resources"></a>

### Recommended Books <a href="#recommended_books" id="recommended_books"></a>

Even though Price Channels are not used specifically in Thomas Carr's [*Trend Trading for a Living*](https://a.co/d/3FNuqiR), the book shows traders how to trade in the direction of the underlying trend. Carr also shows readers how to configure a bullish and bearish watch list from which to set your entry and exit prices.

Michael Covel's [*Trend Following*](https://a.co/d/1dpMk5k) introduces the fundamental concepts and techniques for a variety of trend following systems. Covel shows why market prices contain all available information, and readers will learn how to interpret price movements and profit from trend following.

| <p><a href="https://a.co/d/3FNuqiR"><strong>Trend Trading for a Living</strong></a><br>Thomas Carr</p> | <p><a href="https://a.co/d/1dpMk5k"><strong>Trend Following</strong></a><br>Michael Covel</p> |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/price-channels.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
