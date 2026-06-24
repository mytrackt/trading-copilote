> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/force-index.md).

# Force Index

## What Is the Force Index? <a href="#introduction" id="introduction"></a>

The Force Index is an indicator that uses price and volume to assess the power behind a move or identify possible turning points. Developed by Alexander Elder, the Force Index was introduced in his classic book, [*Trading for a Living*](https://store.stockcharts.com/products/the-new-trading-for-a-living). According to Elder, there are three essential elements to a stock's price movement: direction, extent and volume. The Force Index combines all three as an oscillator that fluctuates in positive and negative territory as the balance of power shifts. The Force Index can be used to reinforce the overall trend, identify playable corrections or foreshadow reversals with divergences.

## Calculating the Force Index <a href="#calculation" id="calculation"></a>

```
Force Index(1) = {Close (current period)  -  Close (prior period)} x Volume
Force Index(13) = 13-period EMA of Force Index(1)
```

Calculation of the 1-period Force Index is straightforward. Simply subtract the prior close from the current close and multiply by volume. The Force Index for more than one day is simply an exponential [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) of the 1-period Force Index. For example, a 13-period Force Index is a 13-period EMA of the 1-period Force Index values for the last 13 periods.

Three factors affect Force Index values. First, the Force Index is positive when the current close is above the prior close. The Force Index is negative when the current close is below the prior close. Second, the extent of the move determines the volume multiplier. Bigger moves warrant larger multipliers that influence the Force Index accordingly. Small moves produce small multipliers that reduce the influence. Third, volume plays a key role. A big move on big volume produces high Force Index values. Small moves on low volume produce relatively low Force Index values. The table below shows the Force Index calculations for Pfizer (PFE). Line 27 marks the biggest move (+84 cents) and the biggest volume (162,619). This combination produces the biggest Force Index value on the table (136,600).

<figure><img src="/files/T1g3S4slIDydNa5SxDLv" alt=""><figcaption><p>Table 1  -  Force Index</p></figcaption></figure>

The chart above shows the Force Index in action. Notice how the 1-period Force Index fluctuates above/below the zero line and looks quite jagged. Elder recommends smoothing the indicator with a 13-period EMA to reduce the positive-negative crossovers. Chartists should experiment with different smoothing periods to determine what best suits their analytical needs.

<figure><img src="/files/2k7xWIM3BGoWn2K1Meob" alt=""><figcaption><p>Chart 1  -  Force Index</p></figcaption></figure>

## Interpreting the Force Index <a href="#interpretation" id="interpretation"></a>

As noted above, there are three elements to the Force Index. First, there is either a positive or negative price change. A positive price change signals that buyers were stronger than sellers, while a negative price change signals that sellers were stronger than buyers. Second, there is the extent of the price change, which is simply the current close less the prior close. The “extent” shows us just how far prices moved. A big advance shows strong buying pressure, while a big decline shows strong selling pressure. The third and final element is volume, which, according to Elder, measures commitment. Just how committed are the buyers and sellers? A big advance on heavy volume shows a strong commitment from buyers. Likewise, a big decline on heavy volume shows a strong commitment from sellers. The Force Index quantifies these three elements into one indicator that measures buying and selling pressure.

### Trend Identification <a href="#trend_identification" id="trend_identification"></a>

The Force Index can be used to reinforce or determine the [trend](/table-of-contents/glossary/glossary-t.md#trend). Said trend, whether short-, medium- or long-term, is dependent on the Force Index parameters. While the default Force Index parameter is 13, chartists can use higher or lower numbers for more or less smoothing, respectively. The chart below shows Home Depot with 100- and 13-day Force Indexes. Notice how the 13-day Force Index is more volatile and jagged while the 100-day Force Index is smoother and crosses the zero line fewer times. In this regard, the 100-day Force Index can be used to determine the medium- or long-term trend. Notice how a resistance breakout on the price chart corresponds to a resistance breakout on the 100-day Force Index. The 100-day Force Index moved into positive territory and broke resistance in mid-February. The indicator remained positive during the entire uptrend and turned negative in mid-May. The early June support break on the price chart was confirmed with a support break in the Force Index.

<figure><img src="/files/Zs2pk6tssVRrKXVznykA" alt=""><figcaption><p>Chart 2  -  Force Index</p></figcaption></figure>

### Divergences <a href="#divergences" id="divergences"></a>

Bullish and [bearish divergences](/table-of-contents/glossary/glossary-b.md#bearish_divergence) can alert chartists of a potential trend change. Divergences are classic signals associated with oscillators. A bullish divergence forms when the indicator moves higher as the security moves lower. The indicator is not confirming weakness in price; this can foreshadow a bullish trend reversal. A bearish divergence forms when the indicator moves lower as the security moves higher. Even though the security is moving higher, the indicator shows underlying weakness by moving lower. This discrepancy can foreshadow a bearish trend reversal.

Confirmation is an important part of bullish and bearish divergences. Even though the divergences signal something is amiss, confirmation from the indicator or price chart is needed. A bullish divergence can be confirmed with the Force Index moving into positive territory or a resistance breakout on the price chart. A bearish divergence can be confirmed with the Force Index moving into negative territory or a support break on the price chart. Chartists can also use candlesticks, moving average crosses, pattern breaks and other forms of technical analysis for confirmation.

<figure><img src="/files/M3OIN1jkpVgdueBC2yAW" alt=""><figcaption><p>Chart 3  -  Force Index</p></figcaption></figure>

The chart above shows Best Buy (BBY) with the Force Index (39) sporting a series of divergences. The green lines show bullish divergences and the red lines show bearish divergences. A bullish divergence is confirmed when the Force Index (39) crosses into positive territory (green dotted lines). A bearish divergence is confirmed when the Force Index (39) crosses into negative territory (red dotted lines). Chartists can also use trend line breaks on the price chart for confirmation.

This chart shows two versions of the Force Index. The Force Index (13) captures short-term fluctuations and is more sensitive. The Force Index (39) captures medium-term fluctuations and is smoother. The 39-day Force Index produces fewer and longer-lasting zero line crossovers and these crossovers last longer. There is no right or wrong answer for these settings; it all depends on personal trading objectives, time horizon and analytical style.

### Identifying Corrections <a href="#identifying_corrections" id="identifying_corrections"></a>

The Force Index can be used in conjunction with a trend following indicator to identify short-term corrections within that trend. A pullback from [overbought](/table-of-contents/glossary/glossary-o.md#overbought) levels represents a short-term correction within an uptrend. An oversold bounce represents a short-term correction within a downtrend. Yes, corrections can be up or down, depending on the direction of the bigger trend. Alexander Elder recommends using a 22-day EMA for trend identification and a 2-day Force Index to identify corrections. The trend is up when the 22-day EMA is moving higher, which means the 2-day Force Index would be used to identify short-term pullbacks for buying. The trend is down when the 22-day EMA is moving lower, which means the 2-day Force Index would be used to identify short-term bounces for selling. This is an aggressive strategy best suited for active traders. The timeframe can be adjusted by using a longer moving average and timeframe for the Force Index. For example, medium-term traders might experiment with a 100-day EMA and 10-day Force Index.

There are two schools of thought regarding the correction play. Traders can either act as soon as the correction is evident or act when there is evidence the correction has ended. Let's look at an example with the 22-day EMA and 2-day Force Index. Keep in mind that this is designed to identify very short corrections within a bigger trend. The chart below shows Texas Instruments (TXN) with the 22-day EMA turning up in mid-September.

<figure><img src="/files/aEOE6kBpoCdaIZjmIrna" alt=""><figcaption><p>Chart 4  -  Force Index</p></figcaption></figure>

With the 22-day EMA rising, traders are looking for very short-term pullbacks when the 2-day Force Index turns negative. Traders can act when the Force Index turns negative or wait for it to move back into positive territory. Acting when negative may improve the reward-to-risk ratio, but the correction could extend a few more days. Waiting for the Force Index to turn positive again shows some strength that could signal the correction has ended. The green dotted lines show when the 2-day Force Index turns negative.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Force Index uses both price and volume to measure buying and selling pressure. The price portion covers the trend, while the volume portion determines the intensity. At its most basic, chartists can use a long-term Force Index to confirm the underlying trend. The bulls have the edge when the 100-day Force Index is positive. The bears have the edge when the 100-day Force Index is negative. Armed with this information, traders can then look for short-term setups in harmony with the larger trend, such as bullish setups in a larger uptrend or bearish setups within a larger downtrend. As with all indicators, traders should use the Force Index in conjunction with other indicators and [analysis techniques](/table-of-contents/chart-analysis/chart-patterns.md).

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Force Index is available as an indicator for SharpCharts. Once selected, users can place the indicator above, below or behind the underlying price plot. Placing the Force Index directly on top of the price plot accentuates the movements relative to price action of the underlying security. This can make it easier to identify bullish and bearish divergences. Chartists can click “advanced options” to add a moving average, horizontal line or another indicator to the Force Index.

\ <img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of the chart.](https://stockcharts.com/sc3/ui/?s=MSFT\&p=D\&yr=1\&mn=0\&dy=0\&id=p81333023268\&listNum=30\&a=219526357)

***

<figure><img src="/files/Ifaba9a67LkDCK9KvSvg" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/zBR3QsTmEYF9ufiNeSwk" alt=""><figcaption><p>SharpCharts  -  Force Index</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Oversold in Up Trend <a href="#oversold_in_up_trend" id="oversold_in_up_trend"></a>

This scan searches for stocks where the Force Index (100) is in positive territory and the Commodity Channel Index (20) is oversold. A positive Force Index establishes an overall uptrend. An oversold CCI identifies a pullback within this uptrend. This scan is meant as a starting point. Further scrutiny and adjustment is advised.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily FORCE(100) > 0] 
AND [Daily CCI(20) < -100]
```

### Overbought in Down Trend <a href="#overbought_in_down_trend" id="overbought_in_down_trend"></a>

This scan searches for stocks where the Force Index (100) is in negative territory and the Commodity Channel Index (20) is overbought. A negative Force Index establishes an overall downtrend. An overbought CCI identifies a corrective bounce within this downtrend. This scan is meant as a starting point. Further scrutiny and adjustment is advised.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily FORCE(100) < 0] 
AND [Daily CCI(20) > 100]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Force Index scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#force_index_force) in the Support Center.
{% endhint %}

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like the Force Index, base the scan on the “Last Market Close.” Examples of other volume-based indicators include Accumulation/Distribution, On Balance Volume, and the PVO.
{% endhint %}

## Additional Resources

### Recommended Books <a href="#further_study" id="further_study"></a>

Alexander Elder's [*Come Into My Trading Room*](https://a.co/d/58KTlFz) covers trading from A to Z. In addition to technical analysis and trading systems, readers will learn trading psychology, risk control, money management and record keeping.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/force-index.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
