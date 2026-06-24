> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/cvr3-vix-market-timing.md).

# CVR3 VIX Market Timing

The CVR3 is a short-term trading strategy using the Cboe Volatility Index ($VIX) to time the S\&P 500. Developed by Larry Connors and Dave Landry, this strategy looks for overextended VIX readings to signal excessive fear or greed in the stock market. Excessive fear is used to generate buy signals in this mean-reversion strategy, while excessive greed generates sell signals.

## VIX Defined <a href="#vix_defined" id="vix_defined"></a>

The Cboe Volatility Index ($VIX) measures the implied volatility for a basket of put and call options for the S\&P 500. Specifically, the VIX measures the expected 30-day volatility for the S\&P 500. Volatility is a measure of risk. Relatively high volatility reflects higher risk in the stock market. Relatively low volatility suggests low risk.

<figure><img src="/files/sP8LfBTDoPymPNv4c3FW" alt=""><figcaption><p>Chart 1  -  CVR3 VIX Market Timing</p></figcaption></figure>

The VIX is also known as the fear index. Volatility and the VIX spike when fear hits the stock market. This causes a surge in implied volatility for put options, which means put prices also surge. Complacency is the opposite of fear. The VIX moves lower as fear subsides and traders are deemed complacent when the VIX reaches excessively low levels.

***

## Buy Signal <a href="#buy_signal" id="buy_signal"></a>

There are three rules for buy signals, all of which pertain directly to the CBOE Volatility Index ($VIX).

**1. The daily low is above its 10-day moving average.** This means the entire bar or candlestick must be above the 10-day moving average.

**2. The daily close is at least 10% above its 10-day moving average.** In SharpCharts, the Percent Price Oscillator (PPO) can be used to define rule two, but this means using a 10-day exponential moving average. PPO(1,10,1) shows the percentage difference between the 1-day EMA (close) and the 10-day EMA. A PPO equal to 10 or greater indicates that the close is at least 10% above the 10-day EMA.

**3. The close is below the open.** It simply means that the candlestick must be black or filled. A filled candlestick indicates that the close is below the open. A white or hollow candlestick indicates the close is above the open.

## Buy Example <a href="#buy_example" id="buy_example"></a>

The example above shows the CBOE Volatility Index ($VIX) the main window, the Percent Price Oscillator (1,10,1) in the middle window and the S\&P 500 in the lower window. Getting all three rules to align on the same day doesn't happen as often as one would think. The green arrows highlight four buy signals from late July to late September 2011. Chartists might consider rule “windows” by looking for all three rules to trigger within a three-day timeframe. This would increase the number of signals.

<figure><img src="/files/2KnPSMuUDwi7DLEinZij" alt=""><figcaption><p>Chart 2  -  CVR3 VIX Market Timing</p></figcaption></figure>

***

## Sell Signal <a href="#sell_signal" id="sell_signal"></a>

There are three rules for sell signals, all of which pertain directly to the CBOE Volatility Index ($VIX).

**1.** The high of the VIX is below the 10-day moving average. This means the entire bar or candlestick must be below the 10-day moving average.

**2.** The daily close is at least 10% below the 10-day moving average. Again, chartists can use the Percent Price Oscillator (1,10,1) to measure this. A value of -10 means the close is 10% below the 10-day EMA.

**3.** The close is above the open. This means that the candlestick must be white or hollow.

## Sell Example <a href="#sell_example" id="sell_example"></a>

The example below shows one sell signal in the second half of 2011. The PPO (1,10,1) moved below -10 several times and there were a few white candlesticks below the 10-day moving average, but the three rules only aligned once. Again, relaxing these rules by creating a rule window (3 days) would increase signal frequency.

<figure><img src="/files/VOSoZtVr5nIOEOCeQa3x" alt=""><figcaption><p>Chart 3  -  CVR3 VIX Market Timing</p></figcaption></figure>

***

## Stop-Losses <a href="#stop-losses" id="stop-losses"></a>

Connors and Landry suggested relatively tight stop-losses. On long positions, a stop-loss would be triggered when the VIX moves below the prior day's 10-day moving average (on an intraday basis). Short positions would be closed when the VIX moves above the prior day's 10-day moving average. Alternatively, Connors and Landry suggest that traders could exit within two to four days. This makes the system quite short-term oriented. Chartists can also consider applying a stop-loss directly to the S\&P 500 by using the Parabolic SAR.

## Adjusting <a href="#adjusting" id="adjusting"></a>

This article is not designed to promote a single trading strategy right out of the box. Instead, it is designed to show a trading strategy developed by a professional. Larry Connors and Dave Landry designed this strategy to suit their trading preferences, which might not fit yours. Chartists should learn from this methodology, apply some tweaks and develop a strategy that suits their trading style. The CVR3 strategy uses the VIX exclusively, which means it is an excellent means to complement other strategies for trading the major indices. For example, chartists could lengthen the look-back periods for moving averages and the Percent Price Oscillator (PPO) to make this a more medium-term oriented strategy. Chartists could also look at alternatives using weekly charts.

<figure><img src="/files/8DRKGZTPAMib6QGDLiOM" alt=""><figcaption><p>Chart 4  -  CVR3 VIX Market Timing</p></figcaption></figure>

Also, note that the Chicago Board Options Exchange (CBOE) calculates volatility indices for a number of different ETFs and indices. These include the Gold SPDR, the US Oil Fund, the Euro Currency Trust, the Dow Industrials and the Nasdaq 100. Chartists can use these indices to develop trading strategies for the Dow, Nasdaq 100, oil, gold and the Euro.

<figure><img src="/files/icqXZagxhjU1FNqCGcR2" alt=""><figcaption><p>Chart 5  -  CVR3 VIX Market Timing</p></figcaption></figure>

***

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The CVR3 strategy is a classic mean-reversion strategy that takes advantage of overextended conditions. The VIX is used to measure excessive fear and complacency. Once overextended, a reversion to the mean is expected as prices settle back down. Because the VIX is the only indicator used, chartists should also analyze price action and indicators for the S\&P 500, which is, after all, the underlying security. CVR3 buy signals should be matched with bullish indications on the S\&P 500 chart. Similarly, CVR3 sell signals should be matched with bearish indications on the price chart. Keep in mind that this article is designed as a starting point for trading system development. Use these ideas to augment your trading style, risk-reward preferences and personal judgments. [Click here](https://stockcharts.com/h-sc/ui?s=$VIX\&p=D\&yr=0\&mn=6\&dy=0\&id=p05210078837\&a=266619497) for a chart of the VIX with the PPO(1,10,1) and the S\&P 500.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/cvr3-vix-market-timing.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
