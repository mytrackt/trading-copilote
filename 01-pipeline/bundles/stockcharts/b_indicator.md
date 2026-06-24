> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/b-indicator.md).

# %B Indicator

## What Is the %B Indicator? <a href="#what_is_the_b_indicator" id="what_is_the_b_indicator"></a>

The %B Indicator measures a security's price in relation to the upper and lower Bollinger Bands. You can use it to identify overbought or oversold conditions and gauge trend strength. If you use it with other indicators, like the Money Flow Index (MFI), it can help you spot entry points within a given trend. Overall, the %B is a versatile tool that can help enhance your ability to analyze and respond to markets.

There are six basic relationship levels:

* %B is below 0 when price is below the lower band
* %B equals 0 when price is at the lower band
* %B is between 0 and .50 when price is between the lower and middle band (20-day SMA)
* %B is between .50 and 1 when price is between the upper and middle band (20-day SMA)
* %B equals 1 when price is at the upper band
* %B is above 1 when price is above the upper band

## How Do You Calculate the %B Indicator? <a href="#how_do_you_calculate_the_b_indicator" id="how_do_you_calculate_the_b_indicator"></a>

```
%B = (Price - Lower Band)/(Upper Band - Lower Band)
```

The default setting for %B is based on the default setting for Bollinger Bands (20,2). The bands are set two standard deviations above and below the 20-day simple [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md), which is also the middle band. Security price is the close or the last trade.

## Signals: Overbought/Oversold <a href="#signalsoverbought_oversold" id="signalsoverbought_oversold"></a>

%B can be used to identify [overbought](/table-of-contents/glossary/glossary-o.md#overbought) and [oversold](/table-of-contents/glossary/glossary-o.md#oversold) situations. However, it is important to know when to look for overbought vs. oversold readings. As with most momentum oscillators, it is best to look for short-term oversold situations when the medium-term trend is up and short-term overbought situations when the medium-term trend is down. In other words, look for opportunities in the direction of the bigger trend, such as a pullback within a bigger uptrend. You must define the bigger trend before looking for overbought or oversold readings.

Chart 1 shows Apple (AAPL) within a strong uptrend. %B moved above 1 several times, but these “overbought” readings still failed to produce good sell signals. Pullbacks were shallow as Apple reversed well above the lower band and resumed its uptrend. John Bollinger refers to “walking the band” during strong trends. This refers to the notion that, in a strong uptrend, prices can walk up the upper band and rarely touch the lower band. Conversely, in a strong downtrend, prices can walk down the lower band and rarely touch the upper band.

<figure><img src="/files/PySGlpkUQNUtkLrtbJqx" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

After identifying a bigger uptrend, %B can be considered oversold when it moves to zero or below. Remember, %B moves to zero when price hits the lower band and below zero when price moves below the lower band. This represents a move that is 2 standard deviations below the 20-day moving average.&#x20;

Chart 2 shows the Nasdaq 100 ETF (QQQQ) within an uptrend that began in March 2009. %B moved below zero three times during this uptrend. The oversold readings in early July and early November provided good entry points to partake in the bigger uptrend (green arrows).

<figure><img src="/files/qISF9ceRJWmv78MvGOOJ" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

## Signals: Trend Identification <a href="#signalstrend_identification" id="signalstrend_identification"></a>

John Bollinger described a trend-following system using %B with the Money Flow Index (MFI). An uptrend begins when %B is above .80 and MFI(10) is above 80. MFI is bound between zero and one hundred. A move above 80 places MFI(10) in the upper 20% of its range, which is a strong reading. Downtrends are identified when %B is below 0.20 and MFI(10) is below 20.

Chart 3 shows FedEx (FDX) with %B and MFI(10). An uptrend started in late July when %B was above 0.80 and MFI was above 80. This uptrend was subsequently affirmed with two more signals in early September and mid-November. While these signals were good for trend identification, traders would likely have had issues with the risk-reward ratio after such big moves. It takes a substantial price surge to push %B above 0.80 and MFI(10) above 80 at the same time. Traders might consider using this method to identify the trend and then look for appropriate overbought or oversold levels for better entry points.

<figure><img src="/files/TbU0Qpi75owXAlTVPWFl" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

%B quantifies the relationship between price and Bollinger Bands. Readings above .80 indicate that price is near the upper band. Readings below .20 indicate that price is near the lower band. Surges towards the upper band show strength, but can sometimes be interpreted as overbought. Plunges to the lower band show weakness, but can sometimes be interpreted as oversold. A lot depends on the underlying trend and other indicators. While %B can have some value on its own, it is best when used in conjunction with other indicators or price analysis.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

%B can be found in the indicator list on SharpCharts. The default parameters (20,2) are based on the default parameters for Bollinger Bands, though these can be changed accordingly. 20 represents the periods in the simple moving average, while 2 represents the number of standard deviations for the upper and lower band. %B can be positioned above, below or behind the price plot. [Click here](https://stockcharts.com/sc3/ui/?s=$SPX\&p=D\&yr=0\&mn=6\&dy=0\&id=p62195116429\&listNum=61\&a=259167452) to see a live example of %B.

<figure><img src="/files/g2iZKWYSONfJXHy03Xec" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### %B Uptrend Scan <a href="#b_uptrend_scan" id="b_uptrend_scan"></a>

This scan filters out stocks where %B is above 0.80 and MFI just crossed above 80. According to Bollinger, these stocks could be starting new upswings. This scan is just a starting point; further refinement and analysis are required.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 5] 

AND [Daily %B(20,2.0,Daily Close) > 0.8] 
AND [Daily MFI(14) > 80] 
AND [Yesterday's Daily MFI(14) < 80]
```

### %B Downtrend Scan <a href="#b_downtrend_scan" id="b_downtrend_scan"></a>

This scan filters out stocks where %B is below 0.20 and MFI just crossed below 20. According to Bollinger, these stocks could be starting new downswings. This scan is just a starting point; further refinement and analysis are required.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 5] 

AND [Daily %B(20,2.0,Daily Close) < 0.2] 
AND [Daily MFI(14) < 20] 
AND [Yesterday's Daily MFI(14) > 20]
```

For more details on the syntax to use for %B scans, please see our [Scanning Indicator Reference](https://support.stockcharts.com/doku.php?id=scans:indicators#bollinger_s_b_indicator) in the Support Center.

## %B FAQs <a href="#b_faqs" id="b_faqs"></a>

<details>

<summary>What is %B in relation to Bollinger Bands?</summary>

%B quantifies a security's price in relation to the upper and lower Bollinger Bands.

</details>

<details>

<summary>How can you determine if a stock is genuinely overbought or oversold using %B?</summary>

It's essential to identify the larger trend first. In a bigger uptrend, %B is considered oversold when it moves to zero or below. In a strong downtrend, %B can be considered overbought when it approaches or exceeds 1.

</details>

<details>

<summary>How can I use the %B for trend identification?</summary>

An uptrend is identified when %B is above 0.80 and MFI(10) is above 80. Conversely, downtrends are spotted when %B is below 0.20 and MFI(10) is below 20.

</details>

<details>

<summary>What’s the relationship between %B and the Money Flow Index (MFI)?</summary>

John Bollinger proposed a trend-following system using %B in conjunction with the Money Flow Index. The two indicators combined can help identify significant trend directions.

</details>

<details>

<summary>Are there any limitations to solely relying on %B?</summary>

While %B can indicate when a stock is near its bands, it doesn't always mean a stock is overbought or oversold. It is best used in combination with other indicators or price analysis.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/b-indicator.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
