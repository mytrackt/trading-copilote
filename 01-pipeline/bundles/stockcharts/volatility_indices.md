> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-indicators/volatility-indices.md).

# Volatility Indices

## What Are Volatility Indices? <a href="#introduction" id="introduction"></a>

The volatility indices measure the implied volatility for a basket of put and call options related to a specific index or ETF. The most popular one is the Cboe Volatility Index ($VIX), which measures the implied volatility for a basket of out-of-the-money put and call options for the S\&P 500. Specifically, the VIX is designed to measure the expected 30-day volatility for the S\&P 500. The Chicago Board Options Exchange (Cboe) calculates volatility indices for a number of different ETFs and indices. These include the Gold SPDR, the USO Oil Fund, the Euro Currency Trust, the Dow Industrials, the S\&P 500 and the Nasdaq 100. This article will focus on using the VIX. Chartists can use the VIX and other volatility indices to measure sentiment and look for sentiment extremes that can foreshadow reversals.

## Calculation <a href="#calculation" id="calculation"></a>

The complete formula for the Cboe Volatility Index and other volatility indices is beyond the scope of this article, but we can describe the basic inputs and some history. Originally created in 1993, the VIX used S\&P 100 options and a different methodology. In particular, the “original formula” used at-the-money options to calculate volatility. This indicator is still available as the Volatility Index - Original Formula ($VXO).

<figure><img src="/files/FhX14bfEFsxKt57TQVz3" alt=""><figcaption><p>Volatility Index - Chart 1</p></figcaption></figure>

<figure><img src="/files/2SSmMKlRGKL21PE4A3ME" alt=""><figcaption><p>Volatility Index - Chart 2</p></figcaption></figure>

In 2003, the Cboe adopted a new methodology that uses near-term and next-term put and call options to measure implied volatility for the S\&P 500. As you can see from the charts above, the difference between these two indicators is negligible to the naked eye. Near-term options have at least 1 week left until expiration. Next-term options are usually 1-2 months out. Each option price carries an implied volatility, which is also known as the [Standard Deviation](/table-of-contents/glossary/glossary-s.md#standard_deviation_volatility). Using a rather complex formula, the CBOE calculates a weighted average of implied volatility to find the expected 30-day volatility for the S\&P 500. 30 days refers to calendar days, not trading days. In a nutshell, there are four steps involved in the calculation:

{% code overflow="wrap" %}

```
  * Select the near-term and next-term put and call options.
  * Calculate the implied volatility for each option. 
  * Calculate a weighted average of implied volatility for these options.
  * Multiply this weighted average by 100. 
```

{% endcode %}

The resulting VIX provides us with the weighted 30-day standard deviation of annual movement in the S\&P 500. A reading of 20% would expect a 20% move, up or down, in the next 12 months. This annualized number can be transformed into a monthly number by dividing it by the square root of 12 (\~3.464). A daily number would be found by dividing by the square root of 252 (\~15.874), which is the number of trading days in a year. The table below shows VIX levels with the expected volatility in the S\&P 500 on a monthly or daily basis. Keep in mind that we are talking about volatility, not the expected return or change.

<figure><img src="/files/bY2LNX0XHnKQhkOI1Sf1" alt=""><figcaption><p>Volatility Index - Table 1</p></figcaption></figure>

## Interpretation <a href="#interpretation" id="interpretation"></a>

Typically, the VIX and other volatility indices have an inverse relationship to the stock market. VIX advances when stocks decline and declines when stocks advance. It seems that volatility would be immune to market direction, but the stock market has a bullish bias overall. A rising stock market is viewed as less risky, while a declining stock market carries more risk. The higher the perceived risk, the higher the implied volatility. Hence, this implied volatility is very susceptible to directional movement. A downswing or extended decline increases the demand for [put options](broken://pages/PDPdWAd7BT185Ez3TVSU#put), which in turn increases put prices and the implied volatility. Puts are bought as a hedge against long positions or as a directional bet. This is why many analysts consider the VIX a coincident indicator. It moves when stocks move, not independently of stocks. In fact, VIX can be used as a trend-confirming indicator because it often trends in the opposite direction of the stock market. Despite a tendency to trend, the VIX can also trade in ranges that mark sentiment extremes. These extremes can be identified to anticipate stock market reversals.

## Trends, Ranges and Spikes <a href="#trends_ranges_and_spikes" id="trends_ranges_and_spikes"></a>

Over a long period of time, a plot of the VIX and other volatility indices will show periods with extended trends, defined ranges and intermittent spikes. The chart below shows the VIX over a 4 1/2 year period with the 200-day moving average. Over this timeframe, the VIX has changed ranges, trended higher, trended lower and spiked periodically. The first half of the chart shows the range shifting higher. As the S\&P 500 exceeded 1400 towards the end of 2006, the Cboe Volatility Index traded in the 10 to 15 range, which is low relative to 2010 levels. The VIX edged higher in the first half of 2007, then traded in a higher range from July 2007 until October 2008. Notice how the VIX did not dip below 15 during this period and reversed soon after exceeding 30.

<figure><img src="/files/6K7cdRxw0wXobDV3FJiz" alt=""><figcaption><p>Volatility Index - Chart 3</p></figcaption></figure>

The second half of the chart shows the VIX surging with a short uptrend, then moving into an extended downtrend that was punctuated by a spike. As the market decline accelerated in September 2008, the VIX started moving sharply higher, exceeding 75 in the fourth quarter. Even though the VIX peaked in late 2008, the S\&P 500 did not bottom until early March 2009. The indicator broke its 200-day moving average in April and trended lower until a surge in May 2010. Notice how the S\&P 500 trended higher as the VIX trended lower. The downtrend in the VIX ended with a spike above 40 in early May, which coincided with the famous flash crash on May 6, 2010. The flash crash is just a blip on the S\&P 500 chart, but a huge spike on the VIX chart. Implied volatility in put options surged as buyers pushed put prices sharply higher. Such panic surges are why the CBOE Volatility Index is sometimes referred to as the “fear index”.

## Sentiment Extremes <a href="#sentiment_extremes" id="sentiment_extremes"></a>

[Sentiment](/table-of-contents/glossary/glossary-s.md#sentiment_indicators) extremes can be identified when volatility indices trade within a range or spikes. As noted in the chart above, the CBOE Volatility Index traded within a well-defined range from July 2007 until October 2008. Moves to the upper end of this range (30-32) signaled excessive bearishness that foreshadowed bullish reversals. Moves to the lower end (16-18) signaled excessive bullishness that foreshadowed bearish reversals. The green dotted lines on the chart below show moves above 30, while the red dotted lines mark moves below 18. There were four bearish extremes and two bullish extremes over a 10-month period. Although not perfect, moves to these extremes were pretty effective in anticipating reversals in the S\&P 500.

<figure><img src="/files/PD2oyYWTMvDxMw2F4QbA" alt=""><figcaption><p>Volatility Index - Chart 4</p></figcaption></figure>

Most ranges are not this well-defined and can shift over time. The chart below shows the VIX from April 2004 to September 2009. The VIX trended lower in 2004, 2005, and early 2006. Instead of a well-defined range, the range drifted lower until the VIX hit 10 in July 2005. There was a spike above 20 in June 2006, but this did not foreshadow an extended downtrend. Instead, this spike signaled excessive bearishness or panic that marked a major low. The indicator moved back down to 10 in October 2007 and traded in the 10-14 area as the market continued higher for several months. There was another spike above 18, which marked a major low in the S\&P 500.

<figure><img src="/files/Z0MeMxVsJgx9KXeTqLSJ" alt=""><figcaption><p>Volatility Index - Chart 5</p></figcaption></figure>

An unusual “coupling” of the Cboe Volatility Index occurred from April 2007 until October 2007. Instead of the normal inverse relationship, both stocks and the VIX moved higher during this timeframe. The S\&P 500 recorded its high in October 2007 as the VIX traded above 16 (well above its lows around 10). Something is not right when the VIX and S\&P 500 rise together. This abnormal coupling served as a warning sign that foreshadowed an extended decline from October 2007 until February 2009.

## Detrending with the PPO <a href="#detrending_with_the_ppo" id="detrending_with_the_ppo"></a>

As noted above, the [Cboe](/table-of-contents/glossary/glossary-c.md#cboe) Volatility Index often trends, making it difficult to identify extremes or cycles. Chartists can detrend the [VIX](/table-of-contents/glossary/glossary-v.md#volatility_index_vix) and other volatility indices by applying the Percent Price Oscillator (PPO) to the indicator. [PPO](/table-of-contents/glossary/glossary-p.md#percentage_price_oscillator_ppo) equals the 10-day EMA less the 50-day EMA divided by the 50-day EMA. PPO values represent the percentage difference between the 10-day EMA and 50-day EMA. PPO is positive when the VIX 10-day EMA is above the VIX 50-day EMA and negative when the VIX 10-day EMA is below the VIX 50-day EMA. This example shows PPO (10,50,1), but any combination of moving averages can be used. A “1” is used for the signal line moving average to merge it with the actual indicator.&#x20;

{% hint style="info" %}
**Learn More.** You can read more on the PPO in our [ChartSchool article](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md).
{% endhint %}

<figure><img src="/files/CgrdpFV2XyU8rHDb5tku" alt=""><figcaption><p>Volatility Index - Chart 6</p></figcaption></figure>

The next chart shows the Percent Price Oscillator for the VIX without the VIX. Unlike the VIX plot, the VIX PPO(10,50,1) oscillates above and below the zero line. There was a fairly well-defined range from 2006 to mid-2008 as the PPO produced some good signals for both extremes. This range expanded as volatility expanded at the end of 2008. The PPO exceeded 50 in October 2008, then plunged below -17 in January 2009. After reaching its lowest level in years, the VIX PPO remained at relatively low levels and did not exceed 10 until the surge to 40 in April-May 2010. This spike represented a bearish extreme.

<figure><img src="/files/oBcVb5V6MtEcb80EHsUO" alt=""><figcaption><p>Volatility Index - Chart 7</p></figcaption></figure>

The green dotted lines show when the VIX PPO moved back below its bearish extreme (25). As with the VIX, timing can be improved by waiting for a reversal back below 25. Notice how the VIX PPO moved above 25 in September 2008 and remained above 25 for several weeks as the market continued to fall. Turning bullish on the initial move above 25 would have been costly. The red dotted lines show periods of excessive bullishness from September 2006 until January 2009. After the market bottomed in March 2009, the VIX PPO moved below -10 quite often and these excessive bullishness signals did not work during the strong uptrend.

## Conclusions <a href="#conclusions" id="conclusions"></a>

Volatility indices are sentiment indicators that react to stock market movements. They are not really predictive indicators; instead, they identify sentiment extremes, declining during a stock market advance and advancing when stocks decline. Sharp stock market declines often produce exaggerated spikes in volatility indices as panic grips the market. Spikes above specific levels suggest excessive bearishness that can lead to a market rally. A steady stock market advance produces a steady downtrend and relatively low levels for the VIX. Excessive bullishness is often hard to define when stocks are trending higher. Like most sentiment indicators, the CBOE Volatility Index and other volatility indices should be used in conjunction with other indicators for market timing. While the odds of a reversal increase with sentiment extremes, chartists should turn to [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators), [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md), or other forms of technical analysis to confirm or time a reversal.

## SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

SharpCharts users can add the Cboe Volatility Index or other volatility indices as indicators above or below the main chart window. For example, the S\&P 500 could be shown in the main chart window with the VIX as an indicator below. Choose “price” as an indicator, enter the symbol ($VIX) as a “parameter” and then choose the “position”. Alternatively, the VIX can be shown in the main chart window with the S\&P 500 ($SPX) as the indicator.

Showing a volatility index as the Percent Price Oscillator (10,50,1) involves a few more charting tricks. SharpCharts users can click the link below this chart to see the settings and save the chart to a ChartList. Here are the steps.

1. Create a chart with the Cboe Volatility Index ($VIX) in the main window
2. Under Chart Attributes and Type, choose “Invisible”
3. Select “Price” under Indicators, enter “$SPX” in Parameters and “Behind Price” for Position
4. Select Percent Price Oscillator (PPO) under Indicators, enter “10,50” for Parameters and “Below” for Position
5. For a full view, Height can be set at “1.0”
6. Click update to see the resulting chart

[Click here for a live version of this chart.](https://stockcharts.com/h-sc/ui?s=$VIX\&p=D\&b=5\&g=0\&id=p04792130979\&listNum=30\&a=210813310)

<figure><img src="/files/i8AwQ9ChZIVpruxGRowY" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/9eiys8WQYaTeyr7gdrtk" alt=""><figcaption><p>Volatility Index  -  SharpCharts</p></figcaption></figure>

## Symbol List <a href="#symbol_list" id="symbol_list"></a>

StockCharts.com users can access [an up-to-date list of symbols](https://stockcharts.com/search/?q=volatility%20indx\&section=symbols) for all our Volatility Indices. From this list, click the “Mentions” icon to the right of a specific symbol for more details about the symbol and recent mentions in Public ChartLists, blog articles, and more.

## Additional Resources <a href="#additional_resources" id="additional_resources"></a>

#### Websites <a href="#websites" id="websites"></a>

[**VIX Volatility Products from Cboe**](https://www.cboe.com/tradable_products/vix/)**.** The Cboe provides details on the VIX and how you can trade them.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-indicators/volatility-indices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
