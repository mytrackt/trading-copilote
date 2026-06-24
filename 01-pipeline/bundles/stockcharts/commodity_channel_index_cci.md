> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/commodity-channel-index-cci.md).

# Commodity Channel Index (CCI)

## What Is the Commodity Channel Index? <a href="#introduction" id="introduction"></a>

Developed by Donald Lambert and featured in *Commodities* magazine in 1980, the Commodity Channel Index (CCI) is a versatile indicator that can identify a new trend or warn of extreme conditions.&#x20;

In general, CCI measures the current price level relative to an average price level over a given period. CCI is relatively high when prices are far above their average, but is relatively low when prices are far below their average. In this manner, CCI can be used to identify overbought and oversold levels.

<figure><img src="/files/EGU7yalt5t0KtaBTdAgu" alt=""><figcaption></figcaption></figure>

While Lambert originally developed CCI to identify cyclical turns in commodities, the indicator can be successfully applied to indices, ETFs, stocks, and other securities.

## Calculating CCI <a href="#calculation" id="calculation"></a>

The example below is based on a 20-period Commodity Channel Index (CCI) calculation. The number of CCI periods is also used for the calculations of the simple moving average and Mean Deviation.

```
CCI = (Typical Price  -  20-period SMA of TP) / (.015 x Mean Deviation)

Typical Price (TP) = (High + Low + Close)/3

Constant = .015

There are four steps to calculating the Mean Deviation: 
1. Subtract the most recent 20-period average of the typical price 
   from each period's typical price. 
2. Take the absolute values of these numbers. 
3. Sum the absolute values. 
4. Divide by the total number of periods (20). 
```

Lambert set the constant at .015 to ensure that approximately 70 to 80 percent of CCI values would fall between -100 and +100. This percentage also depends on the look-back period. A shorter CCI (10 periods) will be [more volatile](/table-of-contents/technical-indicators-and-overlays/technical-indicators/standard-deviation-volatility.md) with a smaller percentage of values between +100 and -100. Conversely, a longer CCI (40 periods) will have a higher percentage of values between +100 and -100.

<figure><img src="/files/cRuGW88mRSKUdt3PstkO" alt=""><figcaption><p>CCI calculation example</p></figcaption></figure>

Click below to download this spreadsheet example.

{% file src="/files/9oFadmKsRwctuSSRtGWC" %}

<figure><img src="/files/MpKupZt7JbnCbf5dQUEI" alt=""><figcaption><p>Chart showing CCI values calculated in the spreadsheet example</p></figcaption></figure>

## Interpreting CCI <a href="#interpretation" id="interpretation"></a>

CCI measures the difference between a security's price change and its average price change. High positive readings indicate that prices are well above their average—a show of strength. Low negative readings indicate that prices are well below their average—a show of weakness.

The CCI can be used as a coincident or leading indicator.&#x20;

* **As a coincident indicator.** When CCI surges above +100, it reflects strong price action that can signal the start of an uptrend. When CCI plunges below -100, it reflects weak price action that can signal the start of a downtrend.
* **As a** [**leading indicator**](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#leading_indicators)**.** Use the CCI to identify overbought or oversold conditions that may foreshadow a mean reversion. Bullish and bearish divergences can be used to detect early momentum shifts and anticipate trend reversals.

### Identifying New Trends Emerging <a href="#new_trend_emerging" id="new_trend_emerging"></a>

As noted above, most CCI movement occurs between -100 and +100. A move that exceeds this range shows unusual strength or weakness that can foreshadow an extended move. Think of these levels as bullish or bearish filters. Technically, CCI favors the bulls when positive and the bears when negative. However, using simple zero-line crossovers can result in many whipsaws. Although entry points will lag more, requiring a move above +100 for a bullish signal and a move below -100 for a bearish signal reduces whipsaws.

The chart below shows Caterpillar (CAT) with 20-day CCI. There were four trend signals within a seven-month period. Obviously, a 20-day CCI is not suited for long-term signals; chartists should use weekly or monthly charts for those. The stock peaked on Jan 11, 2010 and turned down. CCI moved below -100 on January 22 (eight days later) to signal the start of an extended move. The stock bottomed on February 8 and CCI moved above +100 on February 17 (six days later) to signal the start of an extended advance. CCI doesn't catch the exact top or bottom, but it can help filter out insignificant moves and focus on the larger trend.

<figure><img src="/files/blsB5w7nocm3qDICvVkk" alt=""><figcaption><p>Extreme CCI values can signal a change in trend</p></figcaption></figure>

CCI triggered a bullish signal when CAT surged above 60 in June. Some traders may have considered the stock overbought and the reward-to-risk ratio unfavorable at these levels. With the bullish signal in force, the focus would have been on bullish setups with a good reward-to-risk ratio. Notice that the stock retraced around 62% of the prior advance and formed a falling flag by the end of June. The subsequent surge above the flag trend line provided another bullish signal with CCI still in bull mode.

### Overbought/Oversold Conditions <a href="#overbought_oversold" id="overbought_oversold"></a>

Identifying overbought and oversold levels can be tricky with the Commodity Channel Index (CCI), or any other momentum oscillator for that matter. First, CCI is an unbound oscillator. Theoretically, there are no upside or downside limits. This makes an overbought or oversold assessment subjective. Second, securities can continue moving higher after an indicator becomes overbought. Likewise, securities can continue moving lower after an indicator becomes oversold.

The definition of overbought or oversold varies for the Commodity Channel Index (CCI). ±100 may work in a trading range, but more extreme levels are needed for other situations. ±200 is a much harder level to reach and more representative of a true extreme. Selection of overbought/oversold levels also depends on the volatility of the underlying security. The CCI range for an index ETF, such as SPY, will usually be smaller than for most stocks, such as Google.

The chart below shows Google (GOOG) with CCI(20). Horizontal lines at ±200 were added using the advanced indicators options. From early February to early October (2010), Google exceeded ±200 at least five times. The red dotted lines show when CCI moved back below +200 and the green dotted lines show when CCI moved back above -200. It is important to wait for these crosses to reduce whipsaws should the trend extend. Such a system is not foolproof, however. Notice how Google kept on moving higher even after CCI became overbought in mid-September and moved below 200.

<figure><img src="/files/hzwI3TJLKYIi0Wh4osdz" alt=""><figcaption><p>CCI moves outside of more extreme levels (+/-200) when a stock is overbought or oversold.</p></figcaption></figure>

### Identifying Bullish/Bearish Divergences <a href="#bullish_bearish_divergences" id="bullish_bearish_divergences"></a>

Divergences signal a potential reversal point because directional momentum does not confirm price. A bullish divergence occurs when the underlying security makes a lower low and CCI forms a higher low, which shows less downside momentum. A bearish divergence forms when the security records a higher high and CCI forms a lower high, which shows less upside momentum. Before getting too excited about divergences as great reversal indicators, note that divergences can be misleading in a strong trend. A strong uptrend can show numerous bearish divergences before a top actually materializes. Conversely, bullish divergences often appear in extended downtrends.

Confirmation holds the key to divergences. While divergences reflect a change in momentum that can foreshadow a trend reversal, chartists should set a confirmation point for CCI or the price chart. A bearish divergence can be confirmed with a break below zero in CCI or a support break on the price chart. Conversely, a bullish divergence can be confirmed with a break above zero in CCI or a resistance break on the price chart.

The chart below shows United Parcel Service (UPS) with 40-day CCI. A longer timeframe, 40 versus 20, was used to reduce volatility. There are three sizable divergences over a seven-month period, which is relatively few for seven months.&#x20;

<figure><img src="/files/OFEj7fPekZsu9W2ZdK2B" alt=""><figcaption><p>Divergences with CCI, confirmed by a zero-line crossover, can indicate a trend reversal.</p></figcaption></figure>

First, UPS raced to new highs in early May, but CCI failed to exceed its March high and formed a bearish divergence. A support break on the price chart and CCI move into negative territory confirm this divergence a few days later.&#x20;

Second, a bullish divergence formed in early July as the stock moved to a lower low, but CCI formed a higher low. This divergence was confirmed with a CCI break into positive territory. Also notice that UPS filled the late June gap with a surge in early July.&#x20;

Third, a bearish divergence formed in early September and was confirmed when CCI dipped into negative territory. Despite a CCI confirmation, price never broke support and the divergence did not result in a trend reversal. Not all divergences produce good signals.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

CCI is a versatile momentum oscillator that can be used to identify overbought/oversold levels or trend reversals. The indicator becomes overbought or oversold when it reaches a relative extreme. That extreme depends on the characteristics of the underlying security and the historical range for CCI. Volatile securities are likely to require greater extremes than docile securities. Trend changes can be identified when CCI crosses a specific threshold between zero and 100. Regardless of how CCI is used, chartists should use CCI in conjunction with other indicators or price analysis. Another momentum oscillator would be redundant, but [On Balance Volume (OBV)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/on-balance-volume-obv.md) or the [Accumulation Distribution Line](/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md) can add value to CCI signals.

## Charting with CCI <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

CCI is available as a SharpCharts indicator that can be placed above, below or behind the price plot of the underlying security. Placing CCI directly behind the price makes it easy to compare indicator movements with price movements. The default setting is 20 periods, but this can be adjusted to suit analysis needs. A shorter timeframe makes the indicator more sensitive, while a longer timeframe makes it less sensitive. Members can add horizontal lines to mark overbought or oversold levels. Two lines can be added by separating the numbers with a comma (200,-200).

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line"> [Click here for a live version of this chart](https://stockcharts.com/sc3/ui/?s=SPY\&a=2268545894\&p=D\&b=5\&g=0\&id=p40979175714).

<figure><img src="/files/OwWP279coU0nZLFS3DzJ" alt=""><figcaption><p>Using CCI on a SharpChart</p></figcaption></figure>

<figure><img src="/files/WOLfLy65ajHAwSLZcJGY" alt=""><figcaption><p>CCI settings on the SharpCharts Workbench</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure CCI indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#commodity_channel_index_cci) in the Support Center.
{% endhint %}

### Using with StockChartsACP

The CCI indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/gTfl1SSFS5ytoEGyorty" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/RnivDntk)

By default, this indicator is calculated using 20 periods. This parameter can be adjusted to meet your technical analysis needs. Reference lines are automatically added at -100, 0, and +100. Additional reference lines can be added by overlaying the Horizontal Line overlay on the indicator panel.

## Scanning for CCI <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on CCI values. Below are some example scans that can be used for CCI-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a CCI-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### CCI Oversold in Uptrend <a href="#cci_oversold_in_uptrend" id="cci_oversold_in_uptrend"></a>

This scan reveals stocks that are in an uptrend with oversold CCI turning up. First, stocks must be above their 200-day moving average to be in an overall uptrend. Second, CCI must cross above -200 to show the indicator rising from oversold levels.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close > Daily SMA(200,Daily Close)] 
AND [Daily CCI(20) crosses -200]
```

### CCI Overbought in Downtrend <a href="#cci_overbought_in_downtrend" id="cci_overbought_in_downtrend"></a>

This scan reveals stocks that are in a downtrend with overbought CCI turning down. First, stocks must be below their 200-day moving average to be in an overall downtrend. Second, CCI must cross below +200 to show the indicator falling from overbought levels.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close < Daily SMA(200,Daily Close)] 
AND [200 crosses Daily CCI(20)]
```

{% hint style="info" %}
For more details on the syntax to use for CCI scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#commodity_channel_index_cci) in the Support Center.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/2g3jchk) has a chapter devoted to momentum oscillators and their various uses. Murphy covers the pros and cons as well as some examples specific to the Commodity Channel Index.

Martin Pring's [*Technical Analysis Explained*](https://a.co/d/ahkphoZ) presents the basics of momentum indicators by covering divergences, crossovers, and other signals.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/commodity-channel-index-cci.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
