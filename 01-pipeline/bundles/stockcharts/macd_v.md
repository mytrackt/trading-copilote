> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-v.md).

# MACD-V

## Introduction

The MACD-V was created by Alex Spiroglou, CFTe, DipTA (ATAA), to overcome the issues/challenges of conventional range-bound indicators such as the RSI and Stochastic Oscillator and boundless indicators such as the [Moving Average Convergence/Divergence](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) (MACD) and [Rate of Change](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md) (ROC). Spiroglou discovered the indicator in 2015 and publicized it in 2022 in the form of a research paper, which received the Founders Award for Advances in Active Investment Management from the National Association of Active Investment Managers (NAAIM) and the Charles H. Dow Award for outstanding research in technical analysis from the Chartered Market Technicians (CMT) Association.

Conventional range-bound indicators have a bounded scaling (0 – 100) and can't expand with the market. Therefore, they get “pegged” at high/low levels during strong market moves. They also get “skewed” by market trends. Because of their normalized scaling, they're comparable across markets and time.

Boundless indicators are absolute price indicators and cannot be comparable across markets and time. However, because of their unbounded nature, they can expand with the market. Boundless indicators present a truer form of momentum.

## The Solution: MACD-V <a href="#the_solutionmacd-v" id="the_solutionmacd-v"></a>

Spiroglou created a hybrid indicator that was the “best of these two worlds”—a boundless indicator with normalized scaling. He normalized the MACD by volatility, creating a momentum lifecycle model, and also addressing the following five limitations of the MACD:

* **Limitation 1.** The MACD is not comparable across time
* **Limitation 2.** The MACD is not comparable across markets
* **Limitation 3.** The MACD doesn't have a normalized momentum framework
* **Limitation 4.** The MACD Signal Line isn't accurate
* **Limitation 5.** The MACD Signal doesn't help with timing

## Calculating the MACD-V <a href="#calculating_the_macd-v" id="calculating_the_macd-v"></a>

The MACD-V is based on the Moving Average Convergence-Divergence (MACD). What's different is that it incorporates volatility into its calculations.

```
MACD-V =[(12-period EMA - 26-period EMA) / ATR (26)] * 100 
Signal line = 9-period EMA of MACD-V
Histogram = MACD-V - Signal Line

where
EMA = exponential moving average
```

## The Advantages of MACD-V <a href="#the_advantages_of_macd-v" id="the_advantages_of_macd-v"></a>

The MACD-V has the following advantages:

* **MACD-V is stable across securities.** You can apply the MACD-V to cryptocurrencies, mega-cap tech stocks, commodities, etc. The indicator retains the same readings.
* **The Indicator is boundless.** When momentum is very high, you can use the indicator to determine how strong the spike is because a reading of 100 or 0 doesn't limit the indicator.
* **MACD-V creates pattern recognition strategies.** These types of strategies aren't possible with the classic MACD.

## Range Rules for the MACD-V <a href="#range_rules_for_the_macd-v" id="range_rules_for_the_macd-v"></a>

The MACD-V can open the door to several pattern recognition strategies. The basic use is to help identify the following core seven momentum stages:

1. **Risk.** The market is considered at risk (oversold) when the MACD-V is < -150.
2. **Rebounding.** The market is rebounding and rising off a low when the MACD-V is between 50 and -150 (50 > X > -150) and above its signal line.
3. **Rallying.** The market is rallying with strong upside momentum when the MACD-V is between 150 and 50 (150 > X > 50) and above its signal line.
4. **Risk.** The market is considered at risk (overbought) when the MACD-V is > 150 and above its signal line.
5. **Retracing.** The market is retracing and falling off a high when the MACD-V is greater than (X > -50) and below its signal line.
6. **Reversing.** The market is falling with strong downside momentum when the MACD-V is between -50 and -150 (-50 > X > -150) and below its signal line.
7. **Ranging.** The market is in a short-term trading range when the MACD-V is between 50 and -50 (50 > X > -50) for more than 20–30 bars.

## Advanced Patterns in the MACD-V <a href="#advanced_patterns_in_the_macd-v" id="advanced_patterns_in_the_macd-v"></a>

You can design several setups based on the seven ranges mentioned above. Spiroglou created a more powerful version of the MACD-V that doesn't use the signal line. This makes the indicator quicker to signal momentum changes and locate highs/lows in the indicator for advanced pattern recognition strategies.

***

## Using MACD-V in StockCharts ACP <a href="#using_macd-v_in_stockcharts_acp" id="using_macd-v_in_stockcharts_acp"></a>

The MACD-V indicator is available as a standard indicator in StockCharts ACP.

<figure><img src="/files/MGekG8kmfi5xJ0LgI37t" alt=""><figcaption><p>MACD-V applied to 10-year Treasury Yields in StockChartsACP</p></figcaption></figure>

To access it:

1. Select Chart Settings
2. Scroll down the list of Standard Indicators and select MACD-V
3. Change the MACD-V parameters by selecting the settings icon next to the indicator name.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-v.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
