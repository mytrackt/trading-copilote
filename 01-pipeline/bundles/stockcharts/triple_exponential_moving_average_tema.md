> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/triple-exponential-moving-average-tema.md).

# Triple Exponential Moving Average (TEMA)

## What Is the Triple Exponential Moving Average?

The Triple Exponential Moving Average (TEMA) reduces the lag of traditional EMAs, making it more responsive and better-suited for short-term trading. Shortly after developing the Double Exponential Moving Average (DEMA) in 1994, Patrick Mulloy took the concept a step further and created the Triple Exponential Moving Average (TEMA).

<figure><img src="/files/grlIvnrkgwu4lCvcoV7L" alt="Chart from StockCharts.com showing two TEMA overlays" width="530"><figcaption><p>Example of a price chart with two TEMA overlays.</p></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/kJuzcNEy)

Like its predecessor, [Double Exponential Moving Average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/double-exponential-moving-average-dema.md) (DEMA), the TEMA overlay uses the lag difference between different EMAs to adjust a traditional EMA. However, TEMA's formula uses a triple-smoothed EMA in addition to the single- and double-smoothed EMAs employed in the formula for DEMA. The offset created using these three EMAs produces a moving average closer to the price bars than DEMA.

{% hint style="info" %}
**Learn More.** [Double Exponential Moving Average (DEMA)](/table-of-contents/technical-indicators-and-overlays/technical-overlays/double-exponential-moving-average-dema.md)
{% endhint %}

## Calculating TEMA <a href="#tema_calculation" id="tema_calculation"></a>

```
Single-, Double-, and Triple-Smoothed EMAs:
  EMA1 = EMA of price
  EMA2 = EMA of EMA1
  EMA3 = EMA of EMA2
TEMA = (3 x EMA1) - (3 x EMA2) + (EMA3)
```

This calculation adds a triple-smoothed EMA to DEMA's lag adjustment concept, but the formula places extra weight on the EMAs with the least lag.

## Interpreting TEMA <a href="#interpreting_tema" id="interpreting_tema"></a>

TEMA is interpreted similarly to DEMA and traditional EMAs but responds even more quickly. It can be used to confirm trends and spot changes in a trend.

The most commonly used signal is the TEMA crossover. Watch for the TEMA line to cross the price bars or for a shorter-term TEMA to cross the longer-term TEMA to indicate a change in trend. For example, a 20-day TEMA crossing above the 50-day TEMA would be a bullish signal.

These TEMA crossovers (whether of price or another TEMA) typically happen much earlier than the corresponding DEMA or traditional EMA crossovers. In the example below, the green arrows mark TEMA crossovers, and the blue arrows mark the corresponding EMA crossovers. In both cases, the TEMA crossover happens before the EMA crossover.

<figure><img src="/files/4rVzP8v17g9Z4a8FwbF9" alt="Chart from StockCharts.com showing that TEMA crossovers take place much earlier than DEMA or EMA crossovers." width="538"><figcaption><p>TEMA crossovers give earlier trading signals than DEMA or EMA crossovers.</p></figcaption></figure>

Because TEMA reacts more quickly than traditional EMAs, you may need to adjust your trading strategies for use with TEMA.

{% hint style="info" %}
**Learn more.** [How to trade TEMAs](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/using-the-5-8-13-ema-crossover-for-short-term-trades.md)
{% endhint %}

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Price crossovers and other signals generally occur sooner with TEMA than with DEMA or traditional EMAs. While the reduced lag and greater responsiveness makes TEMA appealing to short-term investors, having some lag helps to filter out noise on the chart. Longer-term investors may prefer a moving average with a little more lag and a little less noise. As with all technical indicators, traders should use TEMA in conjunction with other indicators and analysis techniques.

***

## Charting with TEMA <a href="#charting_with_tema" id="charting_with_tema"></a>

### Using with StockChartsACP

After installing the StockCharts.com free **Advanced Indicator Pack**, the TEMA overlay can be charted on StockChartsACP. For more information on installing this plug-in, please see our [StockChartsACP Plug-Ins article](https://help.stockcharts.com/charts-and-tools/stockchartsacp/stockchartsacp-plug-ins) in the Support Center.

Once you've installed the plug-in, add the TEMA overlay from the **Chart Settings** panel of your StockChartsACP chart. TEMA can be overlaid on the security's price plot or added in a panel above or below the chart.

<figure><img src="/files/WbCGCJz1h5Coc8enEI2n" alt="Overlay the TEMA in your StockChartsACP charts after installing the Advanced Indicator Pack"><figcaption><p>Add TEMA to your StockChartsACP charts after installing the Advanced Indicator Pack. </p></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/sufnuCKc)

By default, the moving average is calculated with 20 periods, but the number of periods can be adjusted to meet your technical analysis needs.

## Scanning for TEMA <a href="#scanning_for_tema" id="scanning_for_tema"></a>

StockCharts members can screen for stocks based on TEMA values. Below are some example scans that can be used for TEMA-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a TEMA-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Bullish TEMA Crossover <a href="#bullish_tema_crossover" id="bullish_tema_crossover"></a>

This scan looks for stocks with a rising 150-day simple moving average and a bullish cross of the 5-day TEMA and 35-day TEMA. The 150-day moving average is rising as long as it is trading above its level five days ago. A bullish cross occurs when the 5-day TEMA moves above the 35-day TEMA on above-average volume.

{% code overflow="wrap" %}

```
[type = stock] AND [country = US] 
AND [SMA(20,Volume) > 40000] 
AND [SMA(60,Close) > 20] 

AND [SMA(150,Close) > 5 days ago SMA(150,Close)] 
AND [TEMA(5,Close) > TEMA(35,Close)] 
AND [Yesterday's TEMA(5,Close) < Yesterday's TEMA(35,Close)] 
AND [Volume > SMA(200,Volume)]
```

{% endcode %}

### Bearish TEMA Crossover <a href="#bearish_tema_crossover" id="bearish_tema_crossover"></a>

This scan looks for stocks with a falling 150-day simple moving average and a bearish cross of the 5-day TEMA and 35-day TEMA. The 150-day moving average is falling as long as it is trading below its level five days ago. A bearish cross occurs when the 5-day TEMA moves below the 35-day TEMA on above-average volume.

```
[type = stock] AND [country = US] 
AND [SMA(20,Volume) > 40000] 
AND [SMA(60,Close) > 20] 

AND [SMA(150,Close) < 5 days ago SMA(150,Close)] 
AND [TEMA(5,Close) < TEMA(35,Close)] 
AND [Yesterday's TEMA(5,Close) > Yesterday's TEMA(35,Close)] 
AND [Volume > SMA(200,Volume)]
```

{% hint style="info" %}
**Learn More.** For details on the syntax for TEMA scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#triple_exponential_moving_average_tema) in the Support Center.
{% endhint %}

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/triple-exponential-moving-average-tema.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
