> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/standard-deviation-volatility.md).

# Standard Deviation (Volatility)

## What Is Standard Deviation (Volatility)? <a href="#introduction" id="introduction"></a>

Standard deviation is a statistical term that measures the amount of variability or dispersion around an average. Standard deviation is also a measure of volatility. Generally speaking, dispersion is the difference between the actual value and the average value. The larger this dispersion or variability is, the higher the standard deviation. The smaller this dispersion or variability is, the lower the standard deviation. Chartists can use the standard deviation to measure expected risk and determine the significance of certain price movements.

***

## Calculating Standard Deviation <a href="#calculation" id="calculation"></a>

StockCharts.com calculates the standard deviation for a population, which assumes that the periods involved represent the whole data set, not a sample from a bigger data set. The calculation steps are as follows:

1. Calculate the average (mean) price for the number of periods or observations.
2. Determine each period's deviation (close less average price).
3. Square each period's deviation.
4. Sum the squared deviations.
5. Divide this sum by the number of observations.
6. The standard deviation is then equal to the square root of that number.

<figure><img src="/files/OpZTQrU30eF1iLPtctSk" alt=""><figcaption><p>Standard Deviation Excel Spreadsheet</p></figcaption></figure>

The spreadsheet above shows an example for a 10-period standard deviation using QQQQ data. Notice that the 10-period average is calculated after the 10th period and this average is applied to all 10 periods. Building a running standard deviation with this formula would be quite intensive. Excel has an easier way with the STDEVP formula. The table below shows the 10-period standard deviation using this formula.&#x20;

Click below to download an Excel spreadsheet that shows standard deviation calculations.&#x20;

{% file src="/files/OiCkF1DFcLpoDr1Ytxt7" %}

<figure><img src="/files/z56SgKkOZG73ynSSdAed" alt=""><figcaption><p>Standard Deviation Chart 1</p></figcaption></figure>

***

## Standard Deviation Values <a href="#standard_deviation_values" id="standard_deviation_values"></a>

Standard deviation values are dependent on the price of the underlying security. Securities with high prices, such as Google (±550), will have higher standard deviation values than securities with low prices, such as Intel (±22). These higher values are not a reflection of higher volatility, but rather a reflection of the actual price. Standard deviation values are shown in terms that relate directly to the price of the underlying security. Historical standard deviation values will also be affected if a security experiences a large price change over a period of time. A security that moves from 10 to 50 will most likely have a higher standard deviation at 50 than at 10.

<figure><img src="/files/FLUlcCxY1qRzgwYGK8Hr" alt=""><figcaption><p>Standard Deviation Chart 2</p></figcaption></figure>

On the chart above, the left scale relates to the standard deviation. Google's standard deviation scale extends from 2.5 to 35, while the Intel range runs from .10 to .75. Average price changes (deviations) in Google range from $2.5 to $35, while average price changes (deviations) in Intel range from 10 cents to 75 cents.

Despite the range differences, chartists can visually assess volatility changes for each security. Volatility in Intel picked up from April to June as the standard deviation moved above .70 numerous times. Google experienced a surge in volatility in October as the standard deviation shot above 30. One would have to divide the standard deviation by the closing price to directly compare volatility for the two securities.

***

## Measuring Expectations <a href="#measuring_expectations" id="measuring_expectations"></a>

The current value of the standard deviation can be used to estimate the importance of a move or set expectations. This assumes that price changes are normally distributed with a classic bell curve. Even though price changes for securities are not always normally distributed, chartists can still use normal distribution guidelines to gauge the significance of a price movement. In a normal distribution, 68% of the observations fall within one standard deviation, while 95% fall within two and 99.7% fall within three. Using these guidelines, traders can estimate the significance of a price movement. A move greater than one standard deviation would show above average strength or weakness, depending on the direction of the move.

<figure><img src="/files/bAc3GyPKNhIaxwQi533K" alt=""><figcaption><p>Standard Deviation Chart 3</p></figcaption></figure>

The chart above shows Microsoft (MSFT) with a 21-day standard deviation in the indicator window. There are around 21 trading days in a month and the monthly standard deviation was .88 on the last day. In a normal distribution, 68% of the 21 observations should show a price change less than 88 cents. 95% of the 21 observations should show a price change of less than 1.76 cents (2 x .88 or two standard deviations). 99.7% of the observations should show a price change of less than 2.64 (3 x .88 or three standard deviations. Price movements that were 1,2 or 3 standard deviations would be deemed noteworthy.

<figure><img src="/files/ry3kTBZdcMp9QmATtBcw" alt=""><figcaption><p>Standard Deviation Chart 5</p></figcaption></figure>

The 21-day standard deviation is still quite variable as it fluctuated between .32 and .88 from mid-August until mid-December. A 250-day moving average can be applied to smooth the indicator and find an average, which is around 68 cents. Price moves larger than 68 cents were greater than the 250-day SMA of the 21-day standard deviation. These above-average price movements indicate heightened interest that could foreshadow a trend change or mark a breakout.

***

## Conclusion <a href="#conclusion" id="conclusion"></a>

The standard deviation is a statistical measure of volatility. These values provide chartists with an estimate for expected price movements. Price moves greater than the Standard deviation show above average strength or weakness. The standard deviation is also used with other indicators, such as [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md). These bands are set 2 standard deviations above and below a moving average. Moves that exceed the bands are deemed significant enough to warrant attention. As with all indicators, the standard deviation should be used in conjunction with other analysis tools, such as [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) or [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md).

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The standard deviation is available as an indicator in SharpCharts with a default parameter of 10. This parameter can be changed according to analysis needs. Roughly speaking, 21 days equals one month, 63 days equals one quarter and 250 days equals one year. The standard deviation can also be used on weekly or monthly charts. Indicators can be applied to the standard deviation by clicking advanced options and then adding an overlay. [Click here](https://stockcharts.com/sc3/ui/?s=QQQ\&p=D\&yr=0\&mn=6\&dy=0\&id=p80789045093\&listNum=30\&a=217969334) for a live chart with the standard deviation.

<figure><img src="/files/nqNy4siteBQ5KgGqtwDf" alt=""><figcaption><p>Standard Deviation Chart 6</p></figcaption></figure>

<figure><img src="/files/E6hOrhfC8mA8cZkpxBh6" alt=""><figcaption><p>Standard Deviation SharpCharts</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Weeding Out High Volatility <a href="#weeding_out_high_volatility" id="weeding_out_high_volatility"></a>

The Standard Deviation indicator is often used in scans to weed out securities with extremely high volatility. This simple scan searches for S\&P 600 stocks that are in an uptrend. The final scan clause excludes high volatility stocks from the results. Note that the standard deviation is converted to a percentage of sorts so that the standard deviation of different stocks can be compared on the same scale.

```
[group is SP600]
AND [Daily EMA(50,close) > Daily EMA(200,close)]

AND [Std Deviation(250) / SMA(20,Close) * 100 < 20]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Standard Deviation scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#standard_deviation_std_deviation) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/standard-deviation-volatility.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
