> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/alligator.md).

# Alligator

## What Is the Alligator Overlay?

The Alligator overlay, developed by Bill Williams, is a technical analysis tool based on three offset smoothed moving averages (SMMAs) set at three Fibonacci-based periods - 13, 8, and 5. The three lines - Jaw, Teeth, and Lips - make up the Alligator's mouth, and the relationship between these lines helps to identify trend presence, direction, and potential market entries and exits. The forward shift of these averages is intended to help project future potential price movements, aiding in trend confirmation.

<figure><img src="/files/FZd3xiz360tUo6zD41Qk" alt=""><figcaption></figcaption></figure>

Williams created this overlay on the premise that trends occur only 15% to 30% of the time, with the remaining periods consisting of sideways or non-trending movements. The Alligator was, therefore, designed to signal the “awakening” of a new trend from its non-trending, or “sleeping,” state.&#x20;

Fractals are five-bar chart patterns that are often used with the Alligator overlay to help define entry and exit points. The arrows on the chart mark the center of each five-bar pattern.

## Calculating the Alligator Overlay

### SMMA Settings

The Alligator overlay consists of three smoothed moving averages (SMMA):

* **Jaw (Blue Line)**: This line is calculated as a 13-period SMMA of the midpoint prices (average of the high and low prices), shifted forward (into the future) by eight bars.
* **Teeth (Red Line)**: This line is calculated as an eight-period SMMA of the midpoint prices, shifted forward by five bars.
* **Lips (Green Line)**: This line is calculated as a five-period SMMA of the midpoint prices, shifted forward by three bars.

The calculation of smoothed moving averages (SMMAs) is similar to the calculation for other moving averages, and it weights recent data points more heavily than historical data. The SMMA uses more historical data than a simple moving average (SMA), but recent data is not weighted as heavily as with an exponential moving average (EMA). The resulting line is smoother than either the SMA or EMA, but lags both.

### Fractal Identification

Fractals are five-bar chart patterns marked with an arrow above or below the center of the five bars.&#x20;

* With **Bullish Fractals**, the center bar has the lowest low of the five, with the surrounding bars showing higher lows. The arrow appears below the center bar.
* **Bearish Fractals** are the opposite: the center bar has the highest high of the five, with the surrounding bars showing lower highs. The arrow appears above the center bar.

In the chart below, the May 18 bar is marked as a bullish fractal, with that bar having a lower low than the lows of the two previous or next bars. The May 26 bar is marked as a bearish fractal, with a higher high than the highs of the two previous or next bars.

<figure><img src="/files/WsjTx6Tu35RAKESGAAi2" alt=""><figcaption><p>Fractals added to a chart with the Alligator Overlay</p></figcaption></figure>

## Interpreting the Alligator Overlay

### The Alligator's Market Phases

The Alligator overlay shows three possible market phases - sleeping, awakening, and hungry - based on the relative position of the Alligator’s three moving averages: the Jaw (blue line), Teeth (red line), and Lips (green line).&#x20;

#### **The Sleeping Alligator**

A “sleeping” Alligator corresponds with a non-trending market. In this condition, the three Alligator lines are intertwined or very close together, indicating a lack of trending movement. Sleeping Alligators are typically found during a market consolidation phase in which there’s no clear direction. Generally, you’d avoid trading during this phase of the market.

#### **The Awakening Alligator**

During the “awakening” phase, the Lips (green line) crosses the other lines (Teeth and Jaw). This indicates the likelihood that a new trend may be forming; hence, the Alligator is "waking up," so to speak. For some traders, this crossover may signal a potential entry point; for others, it alerts them that a significant market movement may be underway. The direction of the cross (upward or downward) indicates whether the potential trend may be bullish or bearish​.

#### **The Hungry Alligator**

Once the trend gathers strength and momentum, the three moving average lines will separate and expand. In this market phase, the Alligator is considered “hungry.” At this point, traders who haven't entered their positions (long or short, depending on the direction of the trend) will likely be waiting for the next opportunity to do so. The point here is to ride the trend until you see signs of exhaustion or reversal, typically when the three lines converge again.

The chart below displays the Alligator action in a chart of Intel (INTC).

<figure><img src="/files/y5Eq3MxRj87GDpdUIpkl" alt=""><figcaption><p>Sleeping, Awakening, and Hungry phases of the Alligator overlay</p></figcaption></figure>

INTC is in a sleeping phase throughout March, trading sideways with all three moving averages intertwined. It enters a bullish "awakening" phase in early April when the green (lips) line crosses above the other two lines. Throughout April and May, the lines expand outward in a bullish "hungry" phase. In June, the lines begin to come together again, hinting at a new sleeping phase in this stock's near future.

### Alligator Trading Signals

As a set of actionable signals, you might consider entering a trade (long or short) during the “awakening” phase. Ideally, you will want to see the Alligator shift into a “hungry” phase, which signals a strengthening trend. If the trend is already established, you should finesse your market entry using a trading setup that aligns with your preferred trading strategy.

Fractals can also be used to choose an entry point while the Alligator is awakening. In a bullish awakening phase (with the shorter SMMA on top), watch for a bullish fractal, then wait for price to break above the highest high of the fractal.

Conversely, consider exiting your position when the lines begin to converge. This indicates that the Alligator is about to enter a resting or “sleeping” phase and that the trend is weakening.&#x20;

Bearish fractals can be used to choose an exit point during this phase. Set your stop below the lowest low of the most recent bearish fractal.&#x20;

## The Bottom Line

The Alligator overlay, with or without Fractals, helps chartists analyze trends and generate trend-based entry and exit signals. This overlay highlights the different phases of the market - represented by the sleeping, awakening, and hungry Alligator conditions - and emphasizes the importance of timing in trading strategies. You might consider using the Alligator with other technical analysis tools to boost the overlay's accuracy, confirm trends, and refine your trading decisions.

## Charting with the Alligator Overlay

The Alligator overlay can be added to SharpCharts and ACP charts.

### Using with SharpCharts

Alligator can be added to your charts as an overlay in the SharpCharts Workbench. The default settings for this overlay are 13,8,8,5,5,3. These lines represent the number of periods used in the calculation of each line and the number of periods each line is offset. The Jaw line uses 13 periods and is shifted forward 8 periods; the Teeth line uses 8 periods and is shifted forward 5 periods; and the Lips line uses 5 periods and is shifted forward 3 periods. To add the fractal markers to your chart, add the word FRACTALS as an optional seventh parameter in the Parameters box.

[Click here for a live version of the chart.](https://stockcharts.com/sc3/ui/?s=CAT\&a=2294383423\&p=D\&b=5\&g=0\&id=p36753651741)

<figure><img src="/files/vchlMBNdMiUrPX6XYg5C" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/cZP7kDt06gAJzdQMfZCB" alt=""><figcaption><p>SharpCharts settings for the Alligator overlay</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Alligator overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#alligator) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This overlay can be added from the Chart Settings panel for your StockChartsACP chart.

<figure><img src="/files/Ksj9EYecChRnY2hXTyo0" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/pHbQhcID)

The Jaw line defaults to 13 periods with an 8-period offset, the Teeth line defaults to 8 periods with a 5-period offset, and the Lips line defaults to 5 periods with a 3-period offset. These settings can be adjusted to meet your technical analysis needs.&#x20;

By default, the Jaw, Teeth, and Lips lines are shown, but these can be removed by unchecking the **Show Lines** checkbox. You can also add the fractal arrows by checking the **Show Fractals** checkbox.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/alligator.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
