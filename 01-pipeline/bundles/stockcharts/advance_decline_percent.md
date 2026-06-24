> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-percent.md).

# Advance-Decline Percent

## What Is the Advance-Decline Percent Indicator? <a href="#what_is_the_advance-decline_percent_indicator" id="what_is_the_advance-decline_percent_indicator"></a>

The Advance-Decline Percent is a breadth indicator that measures the percentage of net advances. After the market close, StockCharts.com calculates this indicator for the nine sector SPDRs and several index exchange-traded funds (ETFs). Chartists can use this versatile breadth indicator to create a breadth oscillator or AD Line. These indicators can then complement the analysis of the underlying security. For example, the AD Line based on AD Percent for the Technology SPDR (XLK) would complement the analysis of XLK. We will explain how to use AD Percent and show SharpChart examples. You can find a sample list of symbols at the end of the article.

## How Do You Calculate Advance-Decline Percent? <a href="#how_do_you_calculate_advance-decline_percent" id="how_do_you_calculate_advance-decline_percent"></a>

StockCharts.com has AD Percent data going back several years. However, these calculations are based on the list of stocks in the underlying security or index (i.e., XLK), which do change. This means the breadth data from two years ago is based on the then-current holdings, which may differ from present-day holdings. Even though the holdings for the nine sector SPDRs and major stock indexes are relatively stable, chartists should consider this if using a long-term chart.

{% code overflow="wrap" %}

```
AD Percent = (Advances Less Declines) / Total Issues
AD Percent = (70 – 7) / 77 = +63/77 = +81.81% 
AD Percent = (12 – 65) / 77 = -53/77 = -68.83%
```

{% endcode %}

In the first numerical example, the Technology SPDR has 77 stocks with 70 advances and 7 declines. AD Percent is positive (+81.81%) because there are more advances than declines. In the second example, there are 12 advances and 65 declines. AD Percent is negative (-68.83%) because there are more declines than advances.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=XLK\&p=D\&yr=0\&mn=6\&dy=0\&id=p80365221695\&a=407979386)

<figure><img src="/files/BkbGSO2ys9a1uDlifmkN" alt=""><figcaption><p>AD Percent - Chart 1</p></figcaption></figure>

As the chart above shows, AD Percent fluctuates between -100% and +100% with zero as the middle line. A +100% reading means all stocks in the group advanced, while a -100% reading means all stocks declined. Extreme readings are the exception rather than the norm.

## How Do You Interpret Advance-Decline Percent? <a href="#how_do_you_interpret_advance-decline_percent" id="how_do_you_interpret_advance-decline_percent"></a>

As a breadth indicator, AD Percent measures the degree of participation. An advance with AD Percent exceeding +70% reflects extensive strength because most stocks within the group participated in the advance. Conversely, a decline with AD Percent dipping below -70% reflects extensive weakness.

The raw data fluctuates with the up and down days, creating a rather choppy-looking chart. However, you can compare the positive and negative days which helps to assess the ongoing degree of participation. You can also create an AD Line to assess the overall trend and look for divergences. You could also apply a moving average to create a breadth oscillator.

## AD Line <a href="#ad_line" id="ad_line"></a>

The chart below shows the AD Line for the Industrials SPDR (XLI) in the main window and XLI in the smaller window at the bottom. This is a cumulative measure of AD Percent for XLI ($XLIADP). The values on the right-hand scale are not important because these values depend on the starting date. Instead, chartists should simply focus on line movements and apply basic technical analysis.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24XLIADP\&p=D\&yr=0\&mn=6\&dy=0\&id=p14450257222\&a=302852595)

<figure><img src="/files/jVGiySdbK3qZwsxaHZlf" alt=""><figcaption><p>AD Percent - Chart 2</p></figcaption></figure>

There are two “technical developments” visible on this chart. First, notice that a bullish divergence formed in October-November. XLI formed a lower low in November, but the AD Line held above its October low and formed a higher low. This higher low reflected less downside participation. The subsequent breakout in the AD Line (late November) turned this indicator bullish and foreshadowed a sizable advance in XLI.

The second development occurred in April with another bullish divergence. The AD Line formed a higher low in late April as XLI formed a lower low. A breakout followed the higher low to trigger a bullish signal in the AD Line.

## Moving Averages <a href="#moving_averages" id="moving_averages"></a>

A moving average can be applied to AD Percent to create an oscillator that fluctuates above/below the zero line. Chartists can look for this moving average to cross a particular threshold and look for divergences to trigger signals. Be careful with oscillator divergences because they occur quite often and don’t always produce good trading signals.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24XLKADP\&p=D\&yr=0\&mn=6\&dy=0\&id=p33504554596\&a=302591530)

<figure><img src="/files/lZukD6gFb6zR2MbfRnYx" alt=""><figcaption><p>AD Percent - Chart 3</p></figcaption></figure>

The chart above shows the 21-day simple moving average for AD Percent of XLK ($XLKADP). The actual $XLKADP plot is invisible, which is a setting that can be applied under Chart Attributes/Type. See below for details or click the link beneath the chart to see a live chart with the settings. The horizontal lines are set at -5%, 0% and +5%. Notice that crosses above/below the zero line are quite susceptible to whipsaws and bad signals. Traders would be better off using bullish and bearish thresholds just above/below the zero line. In this example, a move above +5% is deemed bullish and a move below -5% is deemed bearish. These signals are highlighted with the red and green lines.

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

AD Percent is a breadth indicator that measures participation within a particular group. The underlying security price (i.e. XLK) reflects what is happening on the outside. AD Percent for XLK ($XLKADP) reflects what is happening beneath the surface. Changes sometimes occur on the inside first - using breadth indicators can help chartists anticipate these changes. The AD Line is a cumulative indicator that can be used for short-term and long-term analysis. A moving average of AD Percent is more sensitive and acts like a breadth oscillator.

***

## AD Percent Using SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=XLI\&p=D\&yr=0\&mn=6\&dy=0\&id=p37319195778\&a=413675214)

<figure><img src="/files/JOR0KjZSdz5dAz7yx13z" alt=""><figcaption><p>AD Percent - Chart 4</p></figcaption></figure>

AD Percent can be added to any SharpChart using the appropriate symbol (see list below). The example below shows SharpChart settings for the histogram, 20-day SMA and AD Line. The raw data should be shown as a “histogram” chart to best capture the ups and downs (red). AD Percent can be turned into a breadth oscillator by choosing “invisible” for chart type to hide the raw data. Next, add a moving average in the “Overlays” section. Choosing invisible in the first step will ensure that the moving average becomes the main security. Chartists can easily create an AD Line by setting the chart type to “cumulative” (black).

<figure><img src="/files/wkR6mrtbZgWO9S2aJN69" alt=""><figcaption><p>AD Percent - Chart 5</p></figcaption></figure>

## Symbol Samples <a href="#symbol_samples" id="symbol_samples"></a>

StockCharts.com users can access [an up-to-date list of symbols](https://stockcharts.com/search/?q=%22Advance-Decline%20Issues%20Percent%22\&section=symbols) for all our Advance-Decline Percent indicators. From this list, click the “Mentions” icon to the right of a specific symbol for more details about the symbol and recent mentions in Public ChartLists, blog articles, and more.

## FAQs Advance-Decline Percent <a href="#advance-decline_percent_faqs" id="advance-decline_percent_faqs"></a>

<details>

<summary>Why is AD Percent considered a versatile indicator?</summary>

AD Percent is considered versatile because it can create indicators like the AD Line and breadth oscillator, helping you analyze trends and divergences in different market sectors.

</details>

<details>

<summary>How can AD Percent complement the analysis of the underlying security?</summary>

You can use AD Percent to create breadth oscillators and an AD Line to complement analyzing an underlying security like the Technology SPDR (XLK).

</details>

<details>

<summary>How does AD Percent help anticipate changes in the market?</summary>

AD Percent reflects what is happening inside a particular group, and changes often occur on the inside first. By using AD Percent, you can anticipate these internal changes before they are externally reflected in the underlying security price.

</details>

<details>

<summary>Can AD Percent data change over time?</summary>

Yes, AD Percent data can vary due to changes in the list of stocks in the underlying security or index. This can affect breadth data. You should consider this when using long-term charts.

</details>

<details>

<summary>How can extreme readings of AD Percent be interpreted?</summary>

Extreme readings, such as +100% or -100%, are exceptional and indicate that all stocks in the group have either advanced or declined, representing extensive strength or weakness in the market sector.

</details>

<details>

<summary>What are the implications of a choppy-looking AD Percent chart?</summary>

A choppy AD Percent chart results from raw data fluctuating with up and down days, but you can still assess the degree of participation by comparing the positive and negative days and can smooth out fluctuations using moving averages.

</details>

<details>

<summary>How does AD Percent for a specific sector (e.g., XLK) relate to the underlying security's price?</summary>

AD Percent reflects the internal movements within a sector, providing insight into what is happening “on the inside,” while the price of the underlying security represents the external or visible outcomes. Therefore, analyzing AD Percent can complement the analysis of the underlying security by revealing internal strengths or weaknesses.

</details>

<details>

<summary>Can AD Percent produce false signals?</summary>

Yes, particularly when using moving averages, crosses above/below the zero line in AD Percent can be susceptible to whipsaws and may produce inaccurate or false trading signals. Generally, traders are advised to use bullish and bearish thresholds just above/below the zero line to avoid such discrepancies.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-percent.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
