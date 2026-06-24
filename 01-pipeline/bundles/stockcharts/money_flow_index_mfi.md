> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/money-flow-index-mfi.md).

# Money Flow Index (MFI)

## What Is the MFI? <a href="#introduction" id="introduction"></a>

The Money Flow Index (MFI) is an oscillator that uses price and volume to measure buying and selling pressure. Created by Gene Quong and Avrum Soudack, MFI is also known as volume-weighted [Relative Strength Index (RSI)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md).&#x20;

<figure><img src="/files/AB4MIG6ROZhprMBvySVe" alt=""><figcaption></figcaption></figure>

MFI starts with the typical price for each period. Money flow is positive when the typical price rises (buying pressure) and negative when the typical price declines (selling pressure). A ratio of positive and negative money flow is then plugged into an RSI formula to create an oscillator that moves between zero and one hundred. As a momentum oscillator tied to volume, MFI is best suited to identify reversals and price extremes with several signals.&#x20;

## Calculating the MFI <a href="#calculation" id="calculation"></a>

There are several steps involved in the MFI calculation. The example below is based on a 14-period MFI, which is the default setting in SharpCharts and the setting recommended by the creators.

```
Typical Price = (High + Low + Close)/3

Raw Money Flow = Typical Price x Volume
Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)

Money Flow Index = 100 - 100/(1 + Money Flow Ratio)
```

First, notice that Raw Money Flow is essentially dollar volume because the formula is volume multiplied by the typical price. Raw Money Flow is positive when the typical price advances from one period to the next and negative when the typical price declines. The Raw Money Flow values are not used when the typical price is unchanged. The Money Flow Ratio in step 3 forms the basis for the Money Flow Index.&#x20;

Positive and Negative Money Flow are summed for the look-back period (14) and the Positive Money Flow sum is divided by the Negative Money Flow sum to create the ratio. The RSI formula is then applied to create a volume-weighted indicator. The table below shows a calculation example taken from an Excel spreadsheet.

<figure><img src="/files/b3NGystRrynkbDIvfjkv" alt=""><figcaption><p>Money Flow Index - Spreadsheet</p></figcaption></figure>

Click below to download the spreadsheet example.&#x20;

{% file src="/files/prLhrB383OzyzODLcikr" %}

## Interpreting the MFI <a href="#interpretation" id="interpretation"></a>

As a volume-weighted version of RSI, the Money Flow Index (MFI) can be interpreted similarly to RSI. The big difference is, of course, volume. Because volume is added to the mix, the Money Flow Index will act differently than RSI. Theories suggest that volume leads price. RSI is a momentum oscillator that already leads prices. Incorporating volume can increase this lead time.

Quong and Soudack identified three basic signals using the MFI. They are:

1. Overbought or oversold levels can warn of unsustainable price extremes.&#x20;
2. Bullish and bearish divergences can be used to anticipate trend reversals.&#x20;
3. Failure swings at 80 or 20 can also be used to identify potential price reversals.&#x20;

In this article, the divergences and failure swings are combined to create one signal group and increase robustness.

### Overbought/Oversold Levels <a href="#overbought_oversold" id="overbought_oversold"></a>

[Overbought](/table-of-contents/glossary/glossary-o.md#overbought) and oversold levels can be used to identify unsustainable price extremes. Typically, MFI above 80 is considered overbought and MFI below 20 is considered oversold. Strong trends can present a problem for these classic overbought and oversold levels. MFI can become overbought (>80) and prices can simply continue higher when the uptrend is strong. Conversely, MFI can become oversold (<20) and prices can continue lower when the downtrend is strong. Quong and Soudack recommended expanding these extremes to further qualify signals. A move above 90 is truly overbought, and a move below 10 is truly oversold. Moves above 90 and below 10 are rare occurrences that suggest a price move is unsustainable.&#x20;

Admittedly, many stocks will trade for a long time without reaching the 90/10 extremes. However, you can use the StockCharts.com scan engine to find those that do. Links to such scans are provided at the end of this article.

In the chart below, Nike (NKE) became oversold when the Money Flow Index moved below 10 in late May and late September 2023. The preceding declines were sharp enough to produce these readings, but the oversold extremes suggested that these declines were unsustainable.&#x20;

Oversold levels alone are not reason enough to turn bullish. Some sort of reversal or upturn is needed to confirm that prices have indeed turned a corner. NKE confirmed the first oversold reading with a resistance breakout on good volume. The stock confirmed the second oversold reading with a gap and trend line break on a spike in volume.

<figure><img src="/files/ML2J9ZrOx11zBeq0ZZQY" alt="Chart of a stock from StockCharts.com showing the money flow index at extreme oversold levels"><figcaption><p>Money Flow Index at extreme oversold levels. </p></figcaption></figure>

In the chart below, Philip Morris (PM) became overbought when the Money Flow Index hit 90 in early January 2022. Extremes in MFI suggested that this advance was not sustainable and a pullback was imminent.&#x20;

<figure><img src="/files/45jbSpRGjlieJnorHv5O" alt="Chart showing stock price action when the Money Flow Index is at extreme overbought level"><figcaption><p>Money Flow Index at extreme overbought levels.</p></figcaption></figure>

The first signal did not immediately lead to a decline. Instead, price tested the support level at 82.40 for a few weeks before moving upward again. During this time, MFI dropped below 80, but not very far below. The second time MFI reached 90, in mid-February 2022, PM formed lower highs until mid-March, producing two down gaps and breaking the previous support level of 82.40.

### Divergences and Failure Swings <a href="#divergences_and_failures" id="divergences_and_failures"></a>

Both failure swings and divergences can be used to identify potential price reversals.&#x20;

A **bullish divergence** forms when prices move to a lower low, but the indicator forms a higher low to show improving money flow or momentum. A **bullish failure swing** occurs when MFI becomes oversold below 20, surges above 20, holds above 20 on a pullback, and then breaks above its prior reaction high. Both are bullish signals when occuring during a downtrend, indicating a possible trend reversal.

Conversely, a **bearish divergence** forms when the stock forges a higher high and the indicator forms a lower high, which indicates deteriorating money flow or momentum. A **bearish failure swing** occurs when MFI becomes overbought above 80, plunges below 80, fails to exceed 80 on a bounce and then breaks below the prior reaction low. Both are bearish signals when occurring during an uptrend, foreshadowing a possible trend reversal.

While failure swings and divergences on their own are valid signals, when both occur at the same time, that is a much stronger signal than either one alone.&#x20;

In the chart below, CVS Health (CVS) formed a bullish divergence and failure swing in October-December 2012. First, notice how the stock price formed a lower low in mid-November while the MFI held well above its October low for a bullish divergence. Second, notice how MFI dipped below 20 in late October, held above 20 in November, and broke its prior high in early December. This signal combination so close together foreshadowed an advance in the stock's price.

<figure><img src="/files/mB24TnRbKJzhvw92Q3K4" alt=""><figcaption><p>Failure swings and divergences with the MFI. </p></figcaption></figure>

In March-April 2013, a bearish divergence occurred on the same chart, when the stock forged a higher high and the MFI indicator formed a lower high. The beginnings of a bearish failure swing started in mid-March when MFI became overbought above 80, then dropped below 80 and held there. However, the MFI took until the end of May to break decisively below the prior lows. At that point, both price and MFI values had been moving sideways for weeks, and no dramatic decline in price occurred. When only the divergence or only the failure swing occurs, the signal is not as robust as when they appear together.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Money Flow Index is a unique indicator that combines momentum and volume with an RSI formula. RSI momentum generally favors the bulls when the indicator is above 50 and the bears when below 50. Even though MFI is considered a volume-weighted RSI, using the centerline to determine a bullish or bearish bias isn't ideal. Instead, MFI is better suited to identify potential reversals with overbought/oversold levels, bullish/bearish divergences and bullish/bearish failure swings. As with all indicators, MFI should not be used by itself. A pure [momentum oscillator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators), such as RSI, or [pattern analysis](/table-of-contents/chart-analysis/chart-patterns.md) can be combined with MFI to increase signal robustness.

***

## Charting with the MFI <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Money Flow Index is available as a SharpCharts indicator that can be placed above, below or behind the price plot of the underlying security. Placing MFI directly behind the price makes it easy to compare indicator swings with price movements. The default setting is 14-periods, but this can be adjusted to suit analysis needs. A shorter timeframe makes the indicator more sensitive. A longer timeframe makes it less sensitive. Users can add horizontal lines for custom overbought and oversold levels. Two lines can be added by separating the numbers with a comma: (10,90).

\ <img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of the chart.](https://stockcharts.com/sc3/ui/?s=IBM\&p=D\&yr=0\&mn=6\&dy=0\&id=p62268879970\&listNum=30\&a=221699049)

<figure><img src="/files/9sHd9m52ytqGi9RL8l0i" alt=""><figcaption><p>Using MFI on a SharpChart</p></figcaption></figure>

<figure><img src="/files/S7NHNJLROh3tOnG6GwLn" alt=""><figcaption><p>MFI settings on the SharpCharts Workbench</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure MFI indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#money_flow_index_mfi) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/EtlixUqQOMyZIViBFVB6" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/DVpKCXJF)

By default, this indicator is calculated using 14 periods. This parameter can be adjusted to meet your technical analysis needs.

## Scanning for the MFI <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on Money Flow Index values. Below are some example scans that can be used for MFI-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a MFI-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### MFI Oversold <a href="#mfi_oversold" id="mfi_oversold"></a>

This scan searches for stocks that are above $20 per share, trade over 100,000 shares per day and have oversold Money Flow Index (<10). Consider this a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily MFI(14) < 10]
```

### MFI Overbought <a href="#mfi_overbought" id="mfi_overbought"></a>

This scan searches for stocks that are above $20 per share, trade over 100,000 shares per day and have overbought Money Flow Index (>90). Consider this a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily MFI(14) > 90]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax for Money Flow Index scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#money_flow_index_mfi) in the Support Center.
{% endhint %}

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like the MFI, base the scan on the “Last Market Close.” Examples of other volume-based indicators include Accumulation/Distribution, On Balance Volume, and the PVO.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

[**Technical Analysis for the Trading Professional**](https://a.co/d/7CFVvAn)\
Constance Brown


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/money-flow-index-mfi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
