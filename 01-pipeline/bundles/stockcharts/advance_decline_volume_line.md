> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-volume-line.md).

# Advance-Decline Volume Line

## What Is the Advance-Decline Volume Line? <a href="#what_is_the_advance-decline_volume_line" id="what_is_the_advance-decline_volume_line"></a>

The Advance-Decline Volume Line (AD Volume Line) is a breadth indicator based on Net Advancing Volume, which is the volume of advancing stocks less the volume of declining stocks. Net Advancing Volume is positive when advancing volume exceeds declining volume and negative when declining volume exceeds advancing volume.

The AD Volume Line is a cumulative measure of Net Advancing Volume, rising when Net Advancing Volume is positive and falling when it is negative. Chartists plot the AD Volume Line for a specific index and compare it to the performance of that index. The AD Volume Line should confirm an advance or decline with similar movements. [Bullish](/table-of-contents/glossary/glossary-b.md#bullish_divergence) or [bearish divergences](/table-of-contents/glossary/glossary-b.md#bearish_divergence) in the AD Volume Line signal a change in buying or selling pressure that could foreshadow a reversal in the index.

## How Do You Calculate the Advance-Decline Volume Line? <a href="#how_do_you_calculate_the_advance-decline_volume_line" id="how_do_you_calculate_the_advance-decline_volume_line"></a>

{% code overflow="wrap" %}

```
AD Volume Line (previous value) + Net Advancing Volume (current value)
```

{% endcode %}

As a cumulative indicator, the AD Volume Line is a running total of each period's Net Advancing Volume. The actual value of the AD Volume Line depends on the starting point for the calculation. Since it has to start somewhere, the first calculation for the AD Volume Line is simply Net Advancing Volume for one period. The next value is the AD Volume Line value for the previous period plus Net Advancing Volume for the current period.

<figure><img src="/files/9lScYpqgHfFKiWF7QND3" alt=""><figcaption></figcaption></figure>

The example above shows the AD Volume Line calculation for 25 days beginning on January 19th, 2010. The first value is simply Net Advancing Volume for that day (+1144). Net Advancing Volume for the second day (January 20th) was negative (-1150), so the AD Volume Line fell to -6 (+1144 + -1150 = -6).

Even though the actual value of the AD Volume Line would be different if we began in January 2009, the shape of the line for this calculation period would be exactly the same. It simply rises and falls as Net Advancing Volume rises and falls. The shape and direction of the AD Volume Line are important, not the actual value. Chartists can click the link below this image to see the SharpChart settings used to create this indicator.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24NAUD\&p=D\&yr=0\&mn=6\&dy=0\&id=p31876754052\&a=203324611)

<figure><img src="/files/ddDxum1EJGkqhfOZFKTl" alt=""><figcaption></figcaption></figure>

## How Do You Read the Advance-Decline Volume Line? <a href="#how_do_you_read_the_advance-decline_volume_line" id="how_do_you_read_the_advance-decline_volume_line"></a>

Because it is based on volume, the AD Volume Line measures the buying and selling pressure behind an advance or a decline. The volume behind advancing stocks represents buying pressure, while the volume behind declining stocks represents selling pressure.

An AD Volume Line that rises and records new highs along with the underlying index shows strong buying pressure. This is bullish. An AD Volume Line that fails to keep up with the underlying index and fails to confirm new highs reflects weakness in buying pressure. Market strength is undermined when buying pressure fails to confirm an advance. Weakness in buying pressure can be identified with a bearish divergence between the AD Volume Line and the underlying index.

On the downside, the market is considered weak when the AD Volume Line moves to new lows along with the underlying index. This shows strong selling pressure. A bullish divergence forms when the AD Volume Line fails to record a lower low along with the index. This means selling pressure is waning and the decline may be nearing an end.

## Bullish Divergence <a href="#bullish_divergence" id="bullish_divergence"></a>

Chart 2 shows a bullish divergence in the Nasdaq AD Volume Line. Because the Nasdaq AD Volume Line is based on the advance-decline volume statistics from the Nasdaq, it makes sense to compare its performance to the Nasdaq Composite. A bullish divergence formed in January-February 2010 when the Nasdaq moved below its January low, but the Nasdaq AD Volume Line formed a higher low. This bullish divergence showed less selling pressure as the Nasdaq forged a lower low. Even though this bullish divergence is rather small and only encompasses a few weeks, it foreshadowed an important low in February 2010. The Nasdaq subsequently advanced over 10% from its February low to its April high.

[Click here for a live version of this chart.](https://stockcharts.com/h-sc/ui?s=%24NAUD\&p=D\&yr=0\&mn=6\&dy=0\&id=p20298583208\&a=203323167)

<figure><img src="/files/5fuHgVSK6BOaolvN8Gf9" alt=""><figcaption></figcaption></figure>

Once the Nasdaq moved below its January low and the AD Volume Line was still above its January low, the possibility of a bullish divergence surfaced. This possibility served as an alert to watch for a potential bullish reversal in the Nasdaq because the AD Volume Line showed less selling pressure. Some other form of technical analysis is then needed to confirm the higher low in the AD Volume Line and signal an upturn. Normal chart analysis can be applied to the AD Volume Line. Notice how the AD Volume Line broke [resistance](/table-of-contents/glossary/glossary-r.md#resistance) a few days ahead of the Nasdaq. This breakout signaled a trend reversal in the AD Volume Line and the Nasdaq followed a few days later.

## Bearish Divergence <a href="#bearish_divergence" id="bearish_divergence"></a>

Chart 3 shows a bearish divergence in the Nasdaq AD Volume Line in October 2007. The AD Volume Line peaked in early October, but the Nasdaq forged a higher high in late October. The lower high in the AD Volume Line showed weakness in buying pressure as the Nasdaq moved to a new high for the move. Weak buying pressure gave way to increased selling pressure that pushed the Nasdaq lower in November. Notice that the AD Volume Line broke support a day before the Nasdaq broke its corresponding [support level](/table-of-contents/glossary/glossary-s.md#support).

[Click here for a live version of this chart.](https://stockcharts.com/h-sc/ui?s=%24NAUD\&p=D\&yr=0\&mn=6\&dy=0\&id=p20298583208\&a=203323167)

<figure><img src="/files/NWDOyPYg5ry2dEI4IYPj" alt=""><figcaption></figcaption></figure>

As noted above, basic chart analysis can be applied to the AD Volume Line. A moving average can be overlaid on the indicator to identify upturns and downturns. Chartists can also use the AD Volume Line to confirm support or resistance breaks in the underlying index. The AD Volume Line and the Nasdaq bounced from late November to late December. Both moved step-for-step during this period and broke support in early January. The support break in the AD Volume Line showed a notable increase in selling pressure and confirmed the support break in the Nasdaq.

## Large-Cap Bias <a href="#large-cap_bias" id="large-cap_bias"></a>

The advance-decline volume statistics favor large-cap stocks over small-cap and mid-cap stocks. Thousands of stocks trade on the Nasdaq and NYSE daily; most are small- and mid-caps, and relatively few are large-caps. Despite fewer large caps, the largest companies account for the most volume. Large caps such as Alphabet, Inc. (GOOGL), Amazon.com, Inc. (AMZN), Apple, Inc. (AAPL), NVIDIA Corp. (NVDA), Meta Platforms, Inc. (META), and Microsoft, Inc. (MSFT) regularly appear on the most active list. Small stocks occasionally make it, but large caps still dominate volume. For example, NVIDIA averages over 50 million shares per day. On the other hand, a small-cap stock like Super Micro Computer, Inc. (SMCI) averages just over 3 million shares per day. An advance in NVIDIA adds some 50 million shares to Net Advancing Volume, while an advance in SMCI will add just 3 million shares. It takes a lot of SMCIs to make up for one Alphabet. You'll find a similar logic in the NYSE.

[Click here for a live version of this chart.](https://stockcharts.com/h-sc/ui?s=%24NAUD\&p=D\&yr=3\&mn=0\&dy=0\&id=p88261582351\&a=203329049)

<figure><img src="/files/7JNwFszf2uCMyzG6Okyy" alt=""><figcaption></figcaption></figure>

While the Nasdaq AD Line has a long-term downward bias, the AD Volume Line does not share this characteristic. Nasdaq listing requirements are not as strict as NYSE listing requirements. As a result, the Nasdaq is full of upstarts in industries ranging from biotech to technology to alternative energy. Even though more Nasdaq stocks are prone to failure, these failures are usually small-caps. The negative impact on the AD Volume Line is minimal because large caps drive the AD Volume Line. In contrast to small-caps and mid-caps, large-caps are much less likely to go out of business or fail to meet listing requirements on the Nasdaq. There will, however, be a few exceptions along the way.

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

The AD Volume Line is a breadth indicator that reflects buying and selling pressure in large-caps, which are the volume leaders on the major exchanges. A rise in the AD Volume Line shows more money flowing into advancing stocks than declining stocks. This also provides a means to quantify total volume. While an advance on relatively low volume may appear weak, looking at Net Advancing Volume and the AD Volume Line may prove otherwise. Total volume is important, but the balance of volume is more important. Net Advancing Volume shows when more money moves into stocks (buying pressure) or out of stocks (selling pressure).

***

## SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

The AD Volume Line can be created on SharpCharts for the Amex, Vancouver, Nasdaq, NYSE or Toronto stock exchanges. A list of symbols for Net Advancing Volume can be found below the chart. First, enter the symbol for Net Advancing Volume. Second, change the chart “type” to “[cumulative](/table-of-contents/glossary/glossary-c.md#cumulative)” and click “update” to create the AD Volume Line. A solid 1-day [moving average](/table-of-contents/glossary/glossary-m.md#moving_average_ma) was added to better highlight the AD Volume Line.

[Click here for a live version of this chart.](https://stockcharts.com/h-sc/ui?s=%24NAUD\&p=D\&yr=0\&mn=6\&dy=0\&id=p75530125873\&a=413672913)

<figure><img src="/files/jbsSr93DNelPB7JHpFiK" alt=""><figcaption></figcaption></figure>

SharpCharts users can also add the underlying index by selecting “price” as an indicator and entering the index symbol in the “parameters” box. Net Advancing Volume is also shown as a separate indicator in histogram format to see the daily fluctuations. [Click here](https://stockcharts.com/h-sc/ui?s=%24NAUD\&p=D\&yr=0\&mn=6\&dy=0\&id=p75530125873\&a=413672913) for a live example.

<figure><img src="/files/d4IEu2IjvTKlnuKKA14l" alt=""><figcaption></figcaption></figure>

## Symbol List <a href="#symbol_list" id="symbol_list"></a>

StockCharts.com users can access up-to-date lists of symbols for our [Advance-Decline Volume Indicators](https://stockcharts.com/search/?q=%22Advance-Decline%20Volume%22\&section=symbols) and [Advance-Decline Volume Percent Indicators](https://stockcharts.com/search/?blogAuthor=\&q=advance-decline%20volume%20percent\&section=symbols). Both indicators can be used to create AD Volume Lines. From these lists, click the “Mentions” icon to the right of a specific symbol for more details about the symbol and recent mentions in Public ChartLists, blog articles, and more.

## FAQs Advance-Decline Volume Line  <a href="#advance-decline_volume_line_faqs" id="advance-decline_volume_line_faqs"></a>

<details>

<summary>Why does the AD Volume Line favor large-cap stocks?</summary>

The AD Volume Line favors large-cap stocks as they account for the most volume in major exchanges, affecting Net Advancing Volume more significantly than small- and mid-caps.

</details>

<details>

<summary>How does AD Volume Line help in analyzing market conditions?</summary>

The AD Volume Line provides insights into the buying and selling pressure behind market advances or declines, helping you identify internal strengths or weaknesses in the market.

</details>

<details>

<summary>Can the AD Volume Line signal market reversals?</summary>

Yes, bullish or bearish divergences in the AD Volume Line can signal a change in buying or selling pressure, potentially foreshadowing a reversal in the index.

</details>

<details>

<summary>Can I apply basic chart analysis to the AD Volume Line?</summary>

Yes, basic chart analysis can be applied to the AD Volume Line, including using moving averages and identifying support or resistance breaks.

</details>

<details>

<summary>Can the AD Volume Line confirm support or resistance breaks in the underlying index?</summary>

Yes, the AD Volume Line can be used to confirm support or resistance breaks in the underlying index, enhancing the robustness of market analysis.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-volume-line.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
