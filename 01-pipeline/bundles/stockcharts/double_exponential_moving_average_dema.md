> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/double-exponential-moving-average-dema.md).

# Double Exponential Moving Average (DEMA)

## What Is the Double Exponential Moving Average (DEMA) Indicator? <a href="#what_is_the_double_exponential_moving_average_dema_indicator" id="what_is_the_double_exponential_moving_average_dema_indicator"></a>

The Double Exponential Moving Average (DEMA) is a technical indicator that reduces the lag of traditional Exponential Moving Averages (EMAs), making it more responsive. It uses the lag difference between a single-smoothed EMA and a double-smoothed EMA to offset the single-smoothed EMA, producing a moving average that stays closer to the price bars than traditional EMAs.

<figure><img src="/files/khRKjCjOTaejP1RGi4c5" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/utZRdWPY)

DEMA was developed by Patrick Mulloy, and introduced in the January 1994 issue of *Technical Analysis of Stocks & Commodities* magazine.

The overlay uses the lag difference between a single-smoothed EMA and a double-smoothed EMA to offset the single-smoothed EMA. This offset produces a moving average that remains smooth, but stays closer to the price bars than either the single- or double-smoothed traditional EMA.

## Calculating DEMA <a href="#how_do_you_calculate_dema" id="how_do_you_calculate_dema"></a>

```
Single- and Double-Smoothed EMAs:
  EMA1 = EMA of price
  EMA2 = EMA of EMA1
DEMA = (2 x EMA1) - EMA2
```

The formula takes the lag difference between the somewhat lagging single-smoothed EMA1 and the even more lagging double-smoothed EMA2, then subtracts that difference from EMA1. This calculation produces a smoothed line that is much closer to the price bars than either EMA1 or EMA2.

## Interpreting DEMA <a href="#how_do_you_interpret_dema" id="how_do_you_interpret_dema"></a>

DEMA is interpreted in a similar way to traditional EMAs, but responds more quickly. Like other EMAs, it can be used to confirm a trend or spot a change in a trend.

The most commonly-used signal is the DEMA crossover. Watch for the DEMA line to cross the price bars or for a shorter-term DEMA to cross a longer-term DEMA to indicate a change in trend. For example, the 20-day DEMA crossing above the 50-day DEMA would be a bullish signal.

These DEMA crossovers (whether of price or another DEMA) typically happen much earlier than the corresponding traditional EMA crossover. In the example below, the green arrows mark DEMA crossovers, and the blue arrows mark the corresponding EMA crossovers. In both cases, the DEMA crossover happens before the EMA crossover.

<figure><img src="/files/ytzeRvCHllujZrdJuIY6" alt=""><figcaption><p>Chart with the Double Exponential Moving Average</p></figcaption></figure>

Because DEMA reacts more quickly than traditional EMAs, you may need to adjust your trading strategies for use with DEMA.

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Price crossovers and other signals generally occur sooner with DEMA than with traditional EMAs. The reduced lag and greater responsiveness of DEMA appeal to short-term investors, but long-term investors may find traditional moving averages more useful. As with all technical indicators, traders should use DEMA with other indicators and analysis techniques.

***

## Charting with DEMA <a href="#charting_with_dema" id="charting_with_dema"></a>

The DEMA overlay can be charted on StockChartsACP after installing our free Advanced Indicator Pack. Please see our [StockChartsACP Plug-Ins article](https://help.stockcharts.com/charts-and-tools/stockchartsacp/stockchartsacp-plug-ins) in the Support Center for more information on installing this plug-in.

Once the plug-in is installed, the DEMA overlay can be added from the Chart Settings panel for your StockChartsACP chart. DEMA can be overlaid on the security's price plot or on an indicator panel.

<figure><img src="/files/q0DAztnndtVweFqIQ9sc" alt=""><figcaption><p>StockChartsACP Chart showing DEMA Overlay</p></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/MIsutWCJ)

By default, the moving average is calculated with 20 periods, but the number of periods can be adjusted to meet your technical analysis needs.

## Scanning for DEMA <a href="#scanning_for_dema" id="scanning_for_dema"></a>

StockCharts members can screen for stocks based on DEMA values. Below are some example scans that can be used for DEMA-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a DEMA-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-mem/price-alert-workbench.html).

### Bullish DEMA Crossover <a href="#bullish_dema_crossover" id="bullish_dema_crossover"></a>

This scan looks for stocks with a rising 150-day simple moving average and a bullish cross of the 5-day DEMA and 35-day DEMA. The 150-day moving average is rising as long as it is trading above its level five days ago. A bullish cross occurs when the 5-day DEMA moves above the 35-day DEMA on above-average volume.

```
[type = stock] AND [country = US]
AND [SMA(20,Volume) > 40000]
AND [SMA(60,Close) > 20]

AND [SMA(150,Close) > 5 days ago SMA(150,Close)]
AND [DEMA(5,Close) > DEMA(35,Close)]
AND [Yesterday's DEMA(5,Close) < Yesterday's DEMA(35,Close)]
AND [Volume > SMA(200,Volume)]
```

### Bearish DEMA Crossover <a href="#bearish_dema_crossover" id="bearish_dema_crossover"></a>

This scan looks for stocks with a falling 150-day simple moving average and a bearish cross of the 5-day DEMA and 35-day DEMA. The 150-day moving average is falling as long as it is trading below its level five days ago. A bearish cross occurs when the 5-day DEMA moves below the 35-day DEMA on above-average volume.

```
[type = stock] AND [country = US]
AND [SMA(20,Volume) > 40000]
AND [SMA(60,Close) > 20]

AND [SMA(150,Close) < 5 days ago SMA(150,Close)]
AND [DEMA(5,Close) < DEMA(35,Close)]
AND [Yesterday's DEMA(5,Close) > Yesterday's DEMA(35,Close)]
AND [Volume > SMA(200,Volume)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for DEMA scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#double_exponential_moving_average_dema) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/double-exponential-moving-average-dema.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
