> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/aroon.md).

# Aroon

## What Are the Aroon Indicators? <a href="#introduction" id="introduction"></a>

Developed by Tushar Chande in 1995, Aroon is an indicator system that determines whether a stock is trending or not and how strong the trend is. “Aroon” means “Dawn's Early Light” in Sanskrit. Chande chose this name because the indicators are designed to reveal the beginning of a new trend. The Aroon indicators measure the number of periods since price recorded an x-day high or low. There are two separate indicators: Aroon-Up and Aroon-Down. A 25-day Aroon-Up measures the number of days since a 25-day high. A 25-day Aroon-Down measures the number of days since a 25-day low. In this sense, the Aroon indicators are quite different from typical [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators), which focus on price relative to time. Aroon is unique because it focuses on time relative to price. Chartists can use the Aroon indicators to spot emerging trends, identify consolidations, define correction periods and anticipate reversals.

***

## How To Calculate the Aroon Indicators <a href="#calculation" id="calculation"></a>

The Aroon indicators are shown in percentage terms and fluctuate between 0 and 100. Aroon-Up is based on price highs, while Aroon-Down is based on price lows. These two indicators are plotted side-by-side for easy comparison. The default parameter setting in SharpCharts is 25 and the example below is based on 25 days.

```
Aroon-Up = ((25 - Days Since 25-day High)/25) x 100
Aroon-Down = ((25 - Days Since 25-day Low)/25) x 100
```

<figure><img src="/files/fGpkgn1lR0fQSELfZvq6" alt=""><figcaption><p>Aroon - Chart 1</p></figcaption></figure>

Aroon declines as the elapsed time between a new high or low increases. 50 is the cutoff point. Because 12.5 days marks the exact middle, a reading of exactly 50 is impossible on a daily chart, though it is possible with other timeframes. Aroon is either below 50 (48) or above 50 (52) on daily charts. A reading above 50 means a new high or low was recorded within the last 12 days or less. This is the most recent half of the look-back period. A reading below 50 means a new high or low was recorded within the last 13 days or more {(25-13)/25 x 100 = 48)}. This is the latter half of the look-back period. The table below shows the range of values for 25-day Aroon-Up and 25-day Aroon-Down.

<figure><img src="/files/U45rhOSHaRyvLpoLydZ6" alt=""><figcaption><p>Aroon - Chart 1</p></figcaption></figure>

***

## Interpreting the Aroon Indicators <a href="#interpretation" id="interpretation"></a>

The Aroon indicators fluctuate above/below a centerline (50) and are bound between 0 and 100. These three levels are important for interpretation. At its most basic, the bulls have the edge when Aroon-Up is above 50 and Aroon-Down is below 50. This indicates a greater propensity for new x-day highs than lows. The converse is true for a downtrend. The bears have the edge when Aroon-Up is below 50 and Aroon-Down is above 50.

A surge to 100 indicates that a trend may be emerging. This can be confirmed with a decline in the other Aroon indicator. For example, a move to 100 in Aroon-Up combined with a decline below 30 in Aroon-Down shows upside strength. Consistently high readings mean prices are regularly hitting new highs or new lows for the specified period. Prices are moving consistently higher when Aroon-Up remains in the 70-100 range for an extended period. Conversely, consistently low readings indicate that prices are seldom hitting new highs or lows. Prices are NOT moving lower when Aroon-Down remains in the 0-30 range for an extended period. However, this does not mean that prices are moving higher. For that, we need to check Aroon-Up.

***

## New Trend Emerging <a href="#new_trend_emerging" id="new_trend_emerging"></a>

There are three stages to an emerging trend signal. For an uptrend signal, the first stage occurs when Aroon-Up moves above Aroon-Down. This shows new highs becoming more recent than new lows. Keep in mind that Aroon measures the time elapsed, not the price. The second stage is when Aroon-Up moves above 50 and Aroon-Down moves below 50. The third stage is when Aroon-Up reaches 100 and Aroon-Down remains at relatively low levels. The first and second stages do not always occur in that order. Sometimes Aroon-Up will break above 50 and then above Aroon-Down. In a downtrend signal, the positions of the two lines are reversed: Aroon-Down breaks above Aroon-Up, breaks above 50, and reaches 100.

<figure><img src="/files/SlKstsh2urclpfHgMaxJ" alt=""><figcaption><p>Aroon - Chart 2</p></figcaption></figure>

The chart above shows CSX Corp (CSX) with weekly bars and 25-week Aroon. First, notice that the downtrend began weakening as Aroon-Down declined below 50 at the end of 2007 (far left). The first stage of an uptrend was signaled when Aroon-Up moved above Aroon-Down in early 2008 (first orange circle). Aroon-Up continued above 50 and hit 100 as Aroon-Down remained at relatively low levels. Notice how Aroon-Up remained near 100 as the advance continued. This emerging uptrend signal lasted until September 2008 when Aroon-Down broke above Aroon-Up, exceeded 50 and surged to 100 (second orange circle). Notice how Aroon-Down remained near 100 as the downtrend extended. The third trend on this chart was signaled when Aroon-Up surged to 100 in June 2009 and remained above 50 for over a year (third orange circle). Also, notice that Aroon-Down remained below 50 for over a year.

***

## Consolidation Period <a href="#consolidation_period" id="consolidation_period"></a>

The Aroon indicators signal a consolidation when both are below 50 and/or both are moving lower with parallel lines. It makes sense that consistent readings below 50 are indicative of flat trading. For 25-day Aroon, readings below 50 mean a 25-day high or low has not been recorded in 13 or more days. Prices are clearly flat when not recording new highs or new lows. Similarly, a consolidation is usually forming when both Aroon-Up and Aroon-Down move lower in parallel fashion and the distance between the two lines is quite small. This narrow parallel decline indicates that some sort of trading range is forming. The first Aroon indicator to break above 50 and hit 100 will trigger the next signal.

<figure><img src="/files/Ahaesmol7yHOELvCiOux" alt=""><figcaption><p>Aroon - Chart 3</p></figcaption></figure>

The chart above shows Omnicom (OMC) with the Aroon indicators moving below 50 in a parallel decline. The width of the channel could be narrower, but we can see the consolidation taking shape on the price chart for confirmation. Both Aroon-Up and Aroon-Down were below 50 in the yellow area. Aroon-Up then broke out and surged to 100, which was before the breakout. Further confirmation came with another Aroon-Up surge at the breakout point. This surge/breakout signaled the end of the consolidation and the beginning of the advance.

<figure><img src="/files/Ix6zrU6UwZ7nP2g3iE04" alt=""><figcaption><p>Aroon - Chart 4</p></figcaption></figure>

The next chart shows Lifepoint Hospitals (LPNT) with 25-day Aroon. Both lines moved lower in May with a parallel decline. The distance between the lines was around 25 points throughout the decline. Aroon-Up and Aroon-Down flattened in June and both remained below 50 for around two weeks as the triangle consolidation extended. Aroon-Down (red) was the first to make its move, with a break above 50 just before the triangle break on the price chart. Aroon-Down hit 100 as prices broke triangle support to signal a continuation lower.

***

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

**Aroon-Up and Aroon-Down are complementary indicators that measure the elapsed time between new x-day highs and lows, respectively.** They are shown together so chartists can easily identify the stronger of the two and determine the trend bias. A surge in Aroon-Up combined with a decline in Aroon-Down signals the emergence of an ***uptrend***. Conversely, a surge in Aroon-Down combined with a decline in Aroon-Up signals the start of a ***downtrend***. A consolidation is present when both move lower in parallel fashion or when both remain at low levels (below 30). Chartists can use the Aroon indicators to determine if a security is trending or trading flat and then use other indicators to generate appropriate signals. For example, chartists might use a [momentum oscillator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md) to identify oversold levels when 25-week Aroon indicates that the long-term trend is up.

***

## Using Aroon With SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Aroon indicators are available on SharpCharts as an indicator. Simply choosing “Aroon” will display Aroon-Up and Aroon-Down. These indicators can be positioned above, below or behind the price plot of the underlying security. Users can click on the green arrow to the right of the indicator to see advanced options and add a horizontal line at 50. Users can even apply another indicator to the Aroon indicators. [**Click here**](https://stockcharts.com/sc3/ui/?s=DIA\&p=D\&yr=0\&mn=8\&dy=0\&id=p93531652664\&listNum=30\&a=191771207) for a live chart with the Aroon indicators.

<figure><img src="/files/xA2HfYnYSz5kzplmjFtl" alt=""><figcaption><p>Aroon - Chart 5</p></figcaption></figure>

***

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Aroon-Up and Aroon-Down are below 20 <a href="#aroon-up_and_aroon-down_are_below_20" id="aroon-up_and_aroon-down_are_below_20"></a>

This simple scan searches for stocks where Aroon-Up and Aroon-Down are below 20. A consolidation is often present when both indicators are at such low levels. The first to break above 50 indicates the next directional clue.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Aroon Up(25) < 20] 
AND [Daily Aroon Down(25) < 20]
```

{% hint style="info" %}
For more details on the syntax to use for Aroon scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#aroon_up) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/aroon.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
