> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/detrended-price-oscillator-dpo.md).

# Detrended Price Oscillator (DPO)

## What Is the Detrend Price Oscillator (DPO)? <a href="#introduction" id="introduction"></a>

The Detrended Price Oscillator (DPO) is an indicator designed to remove trend from price and make it easier to identify cycles. DPO does not extend to the last date because it is based on a displaced moving average. However, alignment with the most recent date is not an issue because DPO is not a momentum oscillator. Instead, DPO is used to identify cycle highs/lows and estimate cycle length.

## Calculation <a href="#calculation" id="calculation"></a>

```
Price {X/2 + 1} periods ago less the X-period simple moving average.
```

X refers to the number of periods used to calculate the Detrended Price Oscillator. A 20-day DPO would use a 20-day SMA that is displaced by 11 periods {20/2 + 1 = 11}. This displacement shifts the 20-day SMA 11 days to the left, which actually puts it in the middle of the look-back period. The value of the 20-day SMA is then subtracted from the price in the middle of this look-back period. In short, DPO(20) equals price 11 days ago less the 20-day SMA.

## Displaced Moving Average <a href="#displaced_moving_average" id="displaced_moving_average"></a>

The moving average displacement actually centers the moving average. Consider a 20-day simple [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) offset 11 days to the left. There are 10 days in front of the moving average, 1 day at the moving average and 9 days behind the moving average. In reality, this moving average is in the middle of its look-back period. Roughly half the prices used in the calculation are to the right and half are to the left. Chart 1 shows the S\&P 500 ETF (SPY) with a 20-day SMA (green dotted line) and a 20-day SMA offset 11 days (pink line). The ending values are the same (106.84), but the pink moving average ends on October 27th and the green moving average ends on November 11th, which is the last date on the chart. Also, notice how the “centered” moving average (pink) more closely follows the actual price plot.

<figure><img src="/files/YZdEhQhCUHREUviaDodu" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

## What Does DPO Measure? <a href="#what_does_dpo_measure" id="what_does_dpo_measure"></a>

The Detrended Price Oscillator (DPO) measures the difference between a past price and a moving average. Keep in mind that DPO is itself displaced to the left. The indicator oscillates above/below zero as prices move above/below the displaced moving average. Chart 2 shows the S\&P 500 ETF (SPY) with a 20-day moving average displaced -11 days. 20-day DPO is shown in the indicator window. Notice how DPO is positive when price is above the displaced moving average and negative when price is below the displaced moving average.

<figure><img src="/files/LLvx6tYT4L2Tf7WuDhk9" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

## Using DPO <a href="#using_dpo" id="using_dpo"></a>

Even though this indicator looks like a classic oscillator, it is not designed for momentum signals. The displaced moving average is set in the past, which is why the DPO is shown in the past. Even with this displacement, DPO peaks and troughs can be used to estimate cycle length. DPO filters out the longer trends to focus on shorter cycles.&#x20;

The chart below displays the DPO (20) in the indicator window. Looking at the peaks and troughs, you can see a 20-day cycle with the lows in early September, early October, early November, and early December. There are roughly 20 days between these lows. The cycle missed in early January.

<figure><img src="/files/L246IHffnyb3804xEGI6" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

## To Shift or Not to Shift <a href="#to_shift_or_not_to_shift" id="to_shift_or_not_to_shift"></a>

It is possible to displace the Detrended Price Oscillator (DPO) with a horizontal shift to the right. If DPO is set at 20, then an 11-period shift is needed to place it in line with the most recent price. This displacement number comes from the formula at the top (20/2 + 1) = 11. While shifting may seem like a good idea, it really defeats the purpose of this indicator, which is to identify cycles.

<figure><img src="/files/EGQwQo1HKEyYCiAxkocy" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

Even with a positive displacement, DPO fluctuations do not match up well with prices. In the example below, the last value for DPO (20,11) is still based on the close 11 days ago and the value of the moving average. Notice that DPO turned negative as price moved below the centered moving average 11 days ago (orange box). DPO simply does not match current price action. In contrast to DPO, price has been below the 20-day EMA the last 12 days. The Percentage Price Oscillator (PPO) is better suited to identify overbought and oversold levels. PPO(1,20,1) shows the percentage difference between current price and the normal 20-day exponential moving average. Overbought/oversold conditions occur when prices get relatively far from their 20-day EMA.

<figure><img src="/files/d4s1QTKBmSkUuQIrTBBG" alt=""><figcaption><p>Chart 5</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Detrended Price Oscillator shows the difference between a past price and a simple moving average. In contrast to other price oscillators, DPO is not a momentum indicator. Instead, it is simply designed to identify cycles with its peaks and troughs. Cycles can be estimated by counting the periods between peaks or troughs. Users can experiment with shorter and longer DPO settings to find the best fit.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Detrended Price Oscillator (DPO) can be found in the indicator list on SharpCharts. The default parameter is 20 periods, but this can be adjusted accordingly to find cycles. Users can also add another parameter separated by a comma. A comma plus a positive number shifts the indicator to the right. DPO can be positioned above, below or behind the price plot. [Click here](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&b=5\&g=0\&id=p14005429311\&listNum=30\&a=191188211) for a live example of the Detrended Price Oscillator.

<figure><img src="/files/jcpEjljQ6b1LTwzFljDC" alt=""><figcaption><p>Chart 6</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

The Detrended Price Oscillator is not well suited for scans because the indicator is based on an offset moving average. A 20-day DPO correlates to a price 11 days ago, which is not practical for scans. DPO is also based on absolute levels, making it difficult to use for comparative purposes. A $100 stock will have a much wider DPO range than a $20 stock. Google traded around $590 per share in early January with a DPO around 21. Intel traded around 20.5 in early January with a DPO around .20, which is much lower. The DPO was lower due to the fact that Intel is priced much lower than Google.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/detrended-price-oscillator-dpo.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
