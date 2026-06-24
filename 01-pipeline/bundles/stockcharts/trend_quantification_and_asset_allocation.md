> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/trend-quantification-and-asset-allocation.md).

# Trend Quantification and Asset Allocation

Long-term trend reversals are often processes, not sudden events. Think of the long-term trend as a super tanker, which requires time to reverse direction. Speedboats, on the other hand, represent the short-term trend, which can quickly reverse. Moreover, the long-term trend can range from several months to a few years. With this in mind, chartists should consider more than one long-term timeframe when defining the long-term trend. This article will show how to use an array of [moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) to define the long-term trend and identify the trend reversals with fewer whipsaws.

## Moving Averages <a href="#moving_averages" id="moving_averages"></a>

Despite their lag, moving averages are the most popular indicator for trend identification. Chartists often look at price levels relative to a specific moving average. The trend is considered up when prices are above a particular moving average and down when below it. That's what you'd think, anyway—a shame it isn't that easy.

The chart below shows the S\&P 500 ETF (SPY) with four long-term exponential moving averages (EMAs). Chartists can define the trend by comparing the price level to the 125-day EMA, 150-day EMA, 175-day EMA, and 200-day EMA. However, the trend does not always reverse when prices move above or below these moving averages.

<figure><img src="/files/El0jW7MwuexhuGpLujwm" alt=""><figcaption><p>Applying long-term exponential moving averages to a price chart.</p></figcaption></figure>

There was a clear downtrend from the 2007 high until the March 2009 low, but SPY broke above these moving averages at the end of 2007 and again in the first half of 2008. These breakouts did not signal a trend reversal because the ETF soon peaked and continued lower. After this downtrend, there was an extended uptrend from March 2009 to April 2012. Again, the ETF broke below these moving averages in 2010 and again in 2011. These breaks did not signal a trend reversal because the ETF quickly recovered and continued higher.

## Smoothing the Closing Price <a href="#smoothing_the_closing_price" id="smoothing_the_closing_price"></a>

The chart above shows that daily price data can be volatile, meaning moving average breaks are prone to false signals. A long-term trend identification system should be able to capture the long-term trend without so many whipsaws (false signals). It is impossible to totally eliminate whipsaws, but you can reduce them by smoothing the price data and then using the long-term moving averages.

The chart below shows the Dow Industrials SPDR (DIA) as a 50-day EMA (black). Four exponential moving averages are also displayed to define the trend. Note that the actual price plot for DIA is invisible on this SharpChart. This allows you to focus on the smoothed 50-day EMA for signals.

<figure><img src="/files/wekubX7BXX2eH3QbUpYy" alt=""><figcaption><p>Smoothing the price data with exponential moving averages.</p></figcaption></figure>

Smoothing the price data with a 50-day EMA increases the lag factor but also decreases the number of whipsaws. The blue arrow shows where DIA held the moving averages and maintained the trend. The blue circle shows a whipsaw towards the end of 2011. There were fewer whipsaws on this chart compared to the SPY chart, meaning this system did a better job with trend identification.

## Using the Percentage Price Oscillator <a href="#using_the_percent_price_oscillator" id="using_the_percent_price_oscillator"></a>

Chartists can also use the [Percentage Price Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md) (PPO) to determine if the 50-day EMA is above or below a long-term EMA. For example, the PPO set at (50,200,1) measures the percentage difference between the 50-day EMA and 200-day EMA. The PPO is positive when the shorter EMA is above the longer EMA and negative when the shorter EMA is below the longer EMA. This indicator makes it easy to identify moving average crossovers.

The chart below shows four versions of the PPO comparing the 50-day EMA to longer EMAs. When all four PPOs are positive, the trend is strong and bullish. The trend slowly weakens as the PPOs turn negative, and it becomes full-blown bearish when all four are negative. Trend reversals are a process and usually take a few weeks.

<figure><img src="/files/s2JkCKveyI1YccRz9d8L" alt=""><figcaption><p>Four versions of the PPO comparing the EMA(50) to longer-term EMAs.</p></figcaption></figure>

## Fixing the Long-term EMA <a href="#fixing_the_long-term_ema" id="fixing_the_long-term_ema"></a>

The example in the above chart uses a fixed medium-term exponential moving average (50-day EMA) and variable long-term EMAs. You can also fix the long-term EMA and make the shorter EMAs variable. For example, the long-term EMA could be fixed at 150 days, and the other EMAs could scale up in equal increments. The chart below shows four Percent Price Oscillators with a fixed long-term EMA (150 days) and four variable EMAs (20, 40, 60 and 80 days).

<figure><img src="/files/nwh2pxvYbSfW38kQhbRB" alt=""><figcaption><p>PPO with fixed long-term EMA and four variable EMAs.</p></figcaption></figure>

Chartists can use positive and negative readings to assess the trend. The PPO (20,150,1) will be the most sensitive and the first to change, while the PPO (80,150,1) will be the least sensitive and the last to change. Chartists can then quantify trend direction and strength based on the number of indicators in positive or negative territory. Again, the trend is full-blown bullish when all four PPOs are positive and full-blown bearish when all four are negative.

## Asset Allocation <a href="#asset_allocation" id="asset_allocation"></a>

Many investing strategies scale into positions as the evidence turns bullish and scale out as the evidence turns bearish. Chartists can use these four PPOs to develop a scaling system based on a strengthening or weakening trend. For example, the four PPOs could represent one-quarter of the trend and one-quarter of the portfolio allocation. When one PPO turns positive and the trend is one-quarter bullish, investors could invest 25 percent in the stock market. The second tranche could be invested when a second PPO turns positive and so forth. An investor would be 100 percent invested by the time all four are in positive territory.

<figure><img src="/files/jXCwzTKjsiC8vn6soBnj" alt=""><figcaption><p>Using the Percentage Price Oscillator indicator for asset allocation.</p></figcaption></figure>

In a similar fashion, an investor could reduce long positions by 25% when the first PPO turns negative. Market exposure would be subsequently reduced as the other PPOs turn negative; the investor would be out of the market when all four are negative.

## Indicator Tweaks <a href="#indicator_tweaks" id="indicator_tweaks"></a>

Other indicators can help define the trend and determine asset allocation. For example, the slope indicator can be used similarly, though you will most likely want to adjust the timeframe.&#x20;

The chart below shows four versions of the slope indicator (50-day, 75-day, 100-day and 125-day). The trend is up when the slope is positive and down when the slope is negative. The degree of strength depends on how many slope indicators are positive. A strong uptrend is in play when all four are positive, while a strong downtrend is present when all four are negative.

<figure><img src="/files/rVbsL7SIsOsBe8oU0krP" alt=""><figcaption><p>Chart 6  -  Trend Composite</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Trend identification is often the starting point for many trading and investing strategies. Relatively passive investors can use a long-term trend following strategy to define the trend and allocate funds accordingly. Active traders can use these trend indicators to define the long-term trend and then look for trades in the direction of that trend. This article shows examples using long-term exponential moving averages and long-term settings for the Percent Price Oscillator (PPO). These settings can, of course, be tweaked to suit your trading or investing style. Keep in mind that this article is designed as a starting point for trading system development. Use these ideas to augment your trading style, risk-reward preferences and personal judgments. [Click here](https://stockcharts.com/h-sc/ui?s=SPY\&p=D\&yr=1\&mn=6\&dy=0\&id=p23212476121) for a chart of the S\&P 500 ETF (SPY) with the four exponential moving averages and Percent Price Oscillators used above.

## Suggested Scans to Identify Trends <a href="#suggested_scans" id="suggested_scans"></a>

### Long-term Downtrend <a href="#long-term_downtrend" id="long-term_downtrend"></a>

This scan finds stocks that are in a long-term downtrend.

{% code overflow="wrap" %}

```
  [type = stock]
  and [today's sma(20,volume) > 40000]
  and [today's sma(60,close) > 20]
  and [today's ema(20,close) > today's ema(150,close) ]
  and [today's ema(40,close) > today's ema(150,close) ]
  and [today's ema(60,close) > today's ema(150,close) ]
  and [today's ema(80,close) > today's ema(150,close) ]
```

{% endcode %}

### Long-term Uptrend <a href="#long-term_uptrend" id="long-term_uptrend"></a>

This scan finds stocks that are in a long-term uptrend.

{% code overflow="wrap" %}

```
  [type = stock]
  and [today's sma(20,volume) > 40000]
  and [today's sma(60,close) > 20]
  and [today's ema(20,close) < today's ema(150,close) ]
  and [today's ema(40,close) < today's ema(150,close) ]
  and [today's ema(60,close) < today's ema(150,close) ]
  and [today's ema(80,close) < today's ema(150,close) ]
```

{% endcode %}

## Further Study <a href="#further_study" id="further_study"></a>

John Murphy's *Technical Analysis of the Financial Markets* has a chapter devoted to stock market indicators (breadth) and their various uses. Murphy also covers moving averages and other signals that can be used to augment this system.

| <p><a href="https://www.amazon.com/dp/0735200661?k=technical%20analysis%20of%20the%20financial%20markets&#x26;ref_=nb_sb_ss_w_scx-ent-pd-bk-d_l_k0_1_10&#x26;crid=SPAISH7NQBQW&#x26;sprefix=Technical%20"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/trend-quantification-and-asset-allocation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
