> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/quadrant-lines.md).

# Quadrant Lines

## What Are Quadrant Lines? <a href="#introduction" id="introduction"></a>

Quadrant Lines divide the high-low range into four equal sections. There are five lines and four quadrants. The *top line* marks the **high**, the *bottom line* marks the **low,** and the other three lines form the quadrants. The *middle line* marks the **midpoint** of the range. Quadrant Lines are not an indicator as such. Instead, they are used as a measuring stick for price action. Quadrant Lines allow you to visually quantify price levels relative to the defined range.

## Calculating Quadrant Lines <a href="#calculation" id="calculation"></a>

```
Quadrant Range: High to Low
Quadrant Size: (High - Low)/4

Bottom Line = Low
First Line = Low + Quadrant Size
Middle Line = First Line + Quadrant Size
Third Line = Middle Line + Quadrant Size
Top Line = High

********************************************

Quadrant Range: 60 to 40
Quadrant Size: (60 - 40)/4 = 5

Bottom Line = 40
First Line = 40 + 5 = 45
Middle Line = 45 + 5 = 50
Third Line = 50 + 5 = 55
Top Line = 60
```

## Interpreting Quadrant Lines <a href="#interpretation" id="interpretation"></a>

**Quadrant Lines visually reference current prices relative to the defined high-low range.** As you can see from the formula, quadrants are the same size because each equals 1/4 or 25% of the high-low range. After an advance, Quadrant Lines allow you to quickly identify price points that retrace 25%, 50%, and 75%. Prices have retraced 50% when they reach the middle quadrant line. Corresponding retracements can also be seen when drawing Quadrant Lines over a decline. These lines help you quickly identify advances that retrace 25%, 50%, or 75% of the defined decline.

<figure><img src="/files/U7j7QrvfzpFR3sIzRDY3" alt="Quadrant lines on chart using StockCharts.com help identify potential highs and lows"><figcaption><p>Quadrant Lines help to identify potential highs and lows.</p></figcaption></figure>

## Log Scaling <a href="#log_scaling" id="log_scaling"></a>

Quadrant Lines might not look equidistant on the log scale, but they are equidistant in absolute terms. **Log scaling shows price movements in percentage terms.** An advance from $65 to $75 is 10 points in absolute terms or 15.3% in percentage terms. An advance from $100 to $110 is also 10 points, but much less in percentage terms (just 10%).&#x20;

A 10-point 15.3% move on a log scale will appear bigger than a 10-point 10% move. A 10-point move on an arithmetic scale will look the same regardless of the starting point ($65 or $100). For this reason, the bottom quadrant may appear bigger than the top quadrant when using log scaling. Even though the point moves are equal, an equal advance from a lower starting point produces a bigger percentage gain, which is reflected in the log chart. You can see the difference in the charts below.

<figure><img src="/files/9plag8diZiroeLrrNgwW" alt="Chart from StockCharts.com showing Quadrant Lines in a log scale chart"><figcaption><p>Log scale chart showing Quadrant Lines.</p></figcaption></figure>

<figure><img src="/files/HP2vjjjlwjc9jcdvS05D" alt="Chart from StockCharts.com showing Quadrant Lines in an arithmetic scale chart"><figcaption><p>Arithmetic scale chart showing Quadrant Lines.</p></figcaption></figure>

## Quadrant Lines To Identify Pullback Depths <a href="#advance_with_retracement" id="advance_with_retracement"></a>

The chart below shows IBM with the Quadrant Lines covering an advance from late October to mid-January. The stock firmed near the 75% retracement, the top of the lowest quadrant. This is not an argument for 75% as a key retracement that you should watch carefully. Quadrant Lines simply help quantify the depth of the pullback.

<figure><img src="/files/Bee00D4IKOYgvWerZyH4" alt="Chart from StockCharts.com showing how to use Quadrant Lines to help identify the depth of a pullback"><figcaption><p>Quadrant Lines help identify how deep pullbacks can go during an advancing move.</p></figcaption></figure>

The chart below shows Google (GOOG) with the Quadrant Lines covering the decline from early January to late February. GOOG exceeded the 25% and 50% retracements with the advance above $590 but did not exceed the 75% retracement.

<figure><img src="/files/aopZvGl7cOLE99wpGRLG" alt="Chart from StockCharts.com showing how Quadrant Lines can identify resistance levels during a down move"><figcaption><p>Quadrant Lines can be used to identify resistance levels during a decline. </p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

**Quadrant Lines can identify retracements or determine the relative location of current prices within a given high-low range.** Even though these lines are not indicators per se, there are some similarities with the Fibonacci Retracements Tool, which uses 38.2%, 50%, and 61.8% retracements. After an advance, a decline that retraces only 25% would be deemed shallow and could be used as a sign of strength. A decline that retraces 75% could be deemed excessive, and the most one could expect from a correction. This could be viewed as the last reversal point before the move returns back to the original low. As with all indicators and line studies, Quadrant Lines should be used in conjunction with other aspects of technical analysis.

## SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

You can use our [ChartNotes annotation tool](https://help.stockcharts.com/charts-and-tools/sharpcharts/chartnotes#adding_annotations) to add Quadrant Lines to your charts. Below, you'll find an example of a chart annotated with Quadrant Lines.

<figure><img src="/files/JO6KxSS77Q4e8Dvosxi7" alt="Chart from StockCharts.com showing Quadrant Lines using SharpCharts"><figcaption><p>Adding Quadrant Lines in SharpCharts.</p></figcaption></figure>

{% hint style="info" %}
**Learn More.** Check out our Support Center article on [ChartNotes' Line Study Tools](https://help.stockcharts.com/charts-and-tools/sharpcharts/chartnotes#line_studies).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/quadrant-lines.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
