> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar.md).

# Parabolic SAR

## What Is the Parabolic SAR? <a href="#what_is_the_parabolic_sar" id="what_is_the_parabolic_sar"></a>

Developed by Welles Wilder, the Parabolic SAR is a price-and-time-based trading system. Wilder called this the “Parabolic Time/Price System.” SAR stands for “stop and reverse,” which is the actual indicator used in the system. **SAR trails price as the trend extends over time.** The indicator is plotted below prices as they're rising and above prices as they're falling. In this regard, the indicator stops and reverses when the price trend reverses and breaks above or below the indicator.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=UNH\&p=D\&yr=0\&mn=5\&dy=0\&id=p78782001351\&a=1192587589)

***

<figure><img src="/files/5ksFjmUmyL7VCwmTgOBw" alt="Chart from StockCharts.com displaying the Parabolic SAR (Stop and Reverse). In an uptrend, Parabolic SAR is plotted below price bars and in a downtrend Parabolic SAR is plotted above price bars."><figcaption><p>Parabolic SAR is plotted below price bars when they're rising and is plotted above price bars when they're falling.</p></figcaption></figure>

Wilder introduced the Parabolic Time/Price System in his 1978 book *New Concepts in Technical Trading Systems*. This book also includes the Relative Strength Index (RSI), Average True Range (ATR), and the Directional Movement Concept (ADX). Despite being developed before the computer age, Wilder's indicators have stood the test of time and remain extremely popular.

## How Do You Calculate the Parabolic SAR? <a href="#how_do_you_calculate_the_parabolic_sar" id="how_do_you_calculate_the_parabolic_sar"></a>

Calculation of SAR is complex with if/then variables that make it difficult to put in a spreadsheet. These examples will provide a general idea of how SAR is calculated. Because the formulas for rising and falling SAR are different, it is easier to divide the calculation into two parts. The first calculation covers rising SAR and the second covers falling SAR.

### Rising SAR <a href="#rising_sar" id="rising_sar"></a>

This calculation method is used on prices that are rising.

{% code overflow="wrap" %}

```
Rising SAR
----------

Prior SAR: The SAR value for the previous period. 

Extreme Point (EP): The highest high of the current uptrend. 

Acceleration Factor (AF): Starting at .02, AF increases by .02 each time the extreme point makes a new high. AF can reach a maximum of .20, no matter how long the uptrend extends. 

Current SAR = Prior SAR + Prior AF(Prior EP - Prior SAR)
13-Apr-10 SAR = 48.28 = 48.13 + .14(49.20 - 48.13)

The Acceleration Factor is multiplied by the difference between the Extreme Point and the prior period's SAR. This is then added to the prior period's SAR. Note however that SAR can never be above the prior two periods' lows. Should SAR be above one of those lows, use the lowest of the two for SAR. 
```

{% endcode %}

This table shows the calculated values for rising Parabolic SAR in the example chart below.

<figure><img src="/files/DmsSRJZbJNm3MkGdvpBW" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/nIWeTCeTtmLkevEND7LR" alt=""><figcaption></figcaption></figure>

### Falling SAR <a href="#falling_sar" id="falling_sar"></a>

This calculation method is used on prices that are falling.

{% code overflow="wrap" %}

```
Falling SAR
-----------

Prior SAR: The SAR value for the previous period. 

Extreme Point (EP): The lowest low of the current downtrend. 

Acceleration Factor (AF): Starting at .02, AF increases by .02 each time the extreme point makes a new low. AF can reach a maximum of .20, no matter how long the downtrend extends. 

Current SAR = Prior SAR - Prior AF(Prior SAR - Prior EP)
9-Feb-10 SAR = 43.56 = 43.84 - .16(43.84 - 42.07)

The Acceleration Factor is multiplied by the difference between the Prior period's SAR and the Extreme Point. This is then subtracted from the prior period's SAR. Note that SAR can never be below the prior two periods' highs. Should SAR be below one of those highs, use the highest of the two for SAR. 
```

{% endcode %}

This table shows the calculated values for falling Parabolic SAR in the example chart below.

<figure><img src="/files/B9mLE6kE8B2fsGAFLo1B" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/7AOneoCAYFbRjoG9AIDG" alt=""><figcaption></figcaption></figure>

## How Do You Read the Parabolic SAR <a href="#how_do_you_read_the_parabolic_sar" id="how_do_you_read_the_parabolic_sar"></a>

SAR follows price and can be considered a trend-following indicator. Once a downtrend reverses and starts up, SAR follows prices like a trailing stop. The stop continuously rises as long as the uptrend remains in place. In other words, SAR never decreases in an uptrend and continuously protects profits as prices advance. The indicator acts as a guard against the propensity to lower a stop-loss. Once price stops rising and reverses below SAR, a downtrend starts, with SAR above the price. SAR follows prices lower like a trailing stop. The stop continuously falls as long as the downtrend extends. Because SAR never rises in a downtrend, it continuously protects profits on [short positions](/table-of-contents/glossary/glossary-s.md#short_selling).

### Adjusting the Step Increment <a href="#adjusting_the_step_increment" id="adjusting_the_step_increment"></a>

As shown in the spreadsheet example, the Step, also referred to as the Acceleration Factor (AF), is a multiplier that influences the rate-of-change in SAR. SharpCharts users can set the Step and the Maximum Step. The Step gradually increases as the trend extends until it reaches the maximum set by the user. The Step dictates the sensitivity of the SAR indicator.

**SAR sensitivity can be&#x20;*****decreased*****&#x20;by decreasing the Step**. A lower step moves SAR further from price, making a reversal less likely. Similarly, SAR sensitivity can be increased by increasing the step. A higher step moves SAR closer to the price action, making a reversal more likely. The indicator will reverse too often if the step is set too high. This will produce [whipsaws](/table-of-contents/glossary/glossary-w.md#whipsaw) and fail to capture the trend.

Chart 6 shows IBM with SAR (0.01, 0.20). The step is 0.01 and the Maximum Step is 0.20. Chart 7 shows IBM with a higher Step (0.03). SAR is more sensitive in chart 7 because there are more reversals. This is because the Step is higher in chart 7 (0.03) than chart 6 (0.01).

<figure><img src="/files/tDWm398295HkAIZMHxU4" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/3sNqjGfCEJTJ2KOBCZ9V" alt=""><figcaption></figcaption></figure>

### Adjusting the Maximum Step <a href="#adjusting_the_maximum_step" id="adjusting_the_maximum_step"></a>

The sensitivity of the indicator can also be adjusted using the Maximum Step. While the Maximum Step can influence sensitivity, the Step carries more weight because it sets the incremental rate of increase as the trend develops. Also, note that increasing the Step ensures that the Maximum Step will be hit quicker when a trend develops.&#x20;

Chart 8 shows Best Buy (BBY) with a Maximum Step (0.10), which is lower than the default setting (0.20). This lower Maximum Step decreases the sensitivity of the indicator and produces fewer reversals. Notice how this setting caught a two-month downtrend and a subsequent two-month uptrend. Chart 9 shows BBY with a higher Maximum Step (0.20). This higher reading produced extra reversals in early February and early April.

<figure><img src="/files/k6vcWMY3zOMZ515C0cW3" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/cMP4C6poFPJlLq6khXwP" alt=""><figcaption></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

According to Wilder's estimates, the Parabolic SAR works best with trending securities, which occur roughly 30% of the time. This means the indicator will be prone to whipsaws over 50% of the time or when a security is not trending. After all, SAR is designed to catch the trend and follow it like a trailing stop.&#x20;

As with most indicators, the signal quality depends on the settings and characteristics of the underlying security. The right settings combined with decent trends can produce a great trading system. The wrong settings will result in whipsaws, losses, and frustration. There is no golden rule or one-size-fits-all setting. Each security should be evaluated based on its characteristics. Parabolic SAR should also be used with other indicators and technical analysis techniques. For example, Wilder's [Average Directional Index](/table-of-contents/glossary/glossary-a.md#average_directional_index_adx) can estimate the trend's strength before considering signals.

***

## Charting with the Parabolic SAR <a href="#charting_with_the_parabolic_sar" id="charting_with_the_parabolic_sar"></a>

The Parabolic SAR overlay can be added to SharpCharts and ACP charts.

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Parabolic SAR can be found as an Overlay in SharpCharts. The default parameters are 0.02 for the Starting Step and 0.20 for the Maximum Step. If you want the increment amount to be different than the starting step value, then you can add an optional third parameter to set the increment amount. As shown above, these can be changed to suit the characteristics of an individual security. The example below shows the indicator in pink with prices in black/white and the chart grid removed. This contrast makes it easier to compare the indicator with the price action of the underlying security.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=%24SPX\&p=D\&b=5\&g=0\&id=p55388275021\&a=1192566623)

***

<figure><img src="/files/cfWR64dsxxAHPWEOykAG" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure Parabolic SAR overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#parabolic_stop_and_reverse_parabolic_sar) in the Support Center.
{% endhint %}

### Using with StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

This overlay can be added from the Chart Settings panel for your StockChartsACP chart. The Parabolic SAR can be overlaid on the security's price plot or an indicator panel.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of this chart.](https://schrts.co/INFdTYPV)

***

<figure><img src="/files/d4hQ7l4qNHT9gCLHmdM1" alt="Chart from StockChartsACP displaying the Parabolic SAR overlay on a chart of XLE"><figcaption><p>Parabolic SAR applied to StockChartsACP.</p></figcaption></figure>

By default, the overlay uses 0.02 for the Step (increment amount) and 0.20 for the Maximum Step. If you want the starting step value to be different than the increment amount, then use the optional Initial Step field to set this value. These parameters can be adjusted to meet your technical analysis needs.

## Scanning for Parabolic SAR <a href="#scanning_for_parabolic_sar" id="scanning_for_parabolic_sar"></a>

StockCharts members can screen for stocks based on Parabolic SAR values. Below are some example scans that can be used for Parabolic SAR-based signals. Copy and paste the scan text into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a Parabolic SAR-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can also be used as a starting point for setting up alerts. Copy and paste the scan text into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Break Above Falling SAR <a href="#break_above_falling_sar" id="break_above_falling_sar"></a>

This scan starts with stocks that have an average price of $10 or greater over the last three months and average volume greater than 40,000. The scan then filters for stocks that have a bullish SAR reversal (Parabolic SAR (.01,.20)). This scan is just meant as a starter for further refinement.

```
[type = stock] AND [country = US] 
AND [SMA(20,Volume) > 40000] 
AND [SMA(60,Close) > 10] 

AND [Yesterday's High < Yesterday's Parabolic SAR(0.01,0.2)] 
AND [High > Parabolic SAR(0.01,0.2)]
```

### Break Below Rising SAR <a href="#break_below_rising_sar" id="break_below_rising_sar"></a>

This scan starts with stocks that have an average price of $10 or greater over the last three months and average volume greater than 40,000. The scan then filters for stocks that have a bearish SAR reversal (Parabolic SAR (.01,.20)). This scan is just meant as a starter for further refinement.

```
[type = stock] AND [country = US] 
AND [SMA(20,Volume) > 40000] 
AND [SMA(60,Close) > 10] 

AND [Yesterday's Low > Yesterday's Parabolic SAR(0.01,0.2)] 
AND [Low < Parabolic SAR(0.01,0.2)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Parabolic SAR scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#parabolic_stop_and_reverse_parabolic_sar) in the Support Center.
{% endhint %}

***

## Parabolic SAR FAQs <a href="#parabolic_sar_faqs" id="parabolic_sar_faqs"></a>

<details>

<summary>What does the Parabolic SAR tell us about market trends?</summary>

The Parabolic SAR follows the price like a trailing stop. In an uptrend, it continuously rises, protecting profits as prices increase. In a downtrend, it follows prices lower. Thus, it serves to identify and confirm the trend direction and can indicate potential reversal points.

</details>

<details>

<summary>How effective is the Parabolic SAR in different market conditions?</summary>

The Parabolic SAR works best with trending securities, which, according to Welles Wilder's estimates, occur roughly 30% of the time. This means the indicator will be prone to whipsaws over 50% of the time or when a security is not trending.

</details>

<details>

<summary>How should the Parabolic SAR be used in conjunction with other indicators?</summary>

The Parabolic SAR should be used alongside other indicators and technical analysis techniques. For example, Wilder's Average Directional Index can be used to estimate the trend's strength before considering signals.

</details>

<details>

<summary>What is the function of the Acceleration Factor (AF) in the Parabolic SAR calculation?</summary>

The Acceleration Factor, starting at .02, increases by .02 each time the extreme point makes a new high in an uptrend or a new low in a downtrend. It's used to influence the rate of change in SAR, meaning it impacts how closely SAR follows the price movements.

</details>

<details>

<summary>What does the term 'Step Increment' mean in the context of Parabolic SAR?</summary>

The 'Step Increment,' also called the Acceleration Factor, is a multiplier that influences the rate of change in SAR. It gradually increases as the trend extends until it reaches the maximum set by the user.

</details>

<details>

<summary>Can Parabolic SAR values be used for screening stocks?</summary>

Yes, StockCharts members can screen for stocks based on Parabolic SAR values. They can set up alerts to notify them when a Parabolic SAR-based signal is triggered for a stock.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
