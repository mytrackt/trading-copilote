> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/head-and-shoulders-top.md).

# Head and Shoulders Top

A Head and Shoulders Top reversal pattern forms after an uptrend. Its completion marks a trend reversal. The pattern contains three successive peaks, with the middle peak (**head**) being the highest and the two outside peaks (**shoulders**) being low and roughly equal. The reaction lows of each peak can be connected to form [support](/table-of-contents/glossary/glossary-s.md#support) or a **neckline** (see chart below).

<figure><img src="/files/8UruQZDlgCKt4qnHMqHv" alt="Chart displaying a Head and Shoulders Top reversal pattern from StockCharts.com"><figcaption><p>An example of a Head and Shoulders Top chart pattern.</p></figcaption></figure>

As its name implies, the Head and Shoulders reversal pattern consists of a left shoulder, head, right shoulder, and neckline. Other parts playing a role in the pattern are [volume](/table-of-contents/glossary/glossary-v.md#volume), the breakout, price target, and support turned resistance. We will look at each component of the pattern and then put them together with some examples.

* **Prior Trend.** For this to be a reversal pattern, it is important to establish the existence of a prior uptrend. Without a prior uptrend to reverse, there cannot be a Head and Shoulders reversal pattern (or any reversal pattern, for that matter).
* **Left Shoulder.** While in an uptrend, the left shoulder forms a peak that marks the high point of the current trend. After this peak, a decline ensues to complete the shoulder formation (1). The low of the decline usually remains above the trend line, keeping the uptrend intact.
* **Head.** From the left shoulder's low, an advance begins that exceeds the previous high and marks the top of the head. After peaking, the low of the subsequent decline marks the second point of the neckline (2). The low of the decline generally breaks below the uptrend line, which jeopardizes the uptrend.
* **Right Shoulder.** The advance from the low (2) forms the right shoulder. This peak is lower than the head (a lower high) and usually in line with the high of the left shoulder. While symmetry is preferred, sometimes the shoulders can be out of whack. The decline from the peak of the right shoulder should break the neckline.
* **Neckline.** The neckline forms by connecting low points 1 and 2. Low point 1 marks the end of the left shoulder and the beginning of the head. Low point 2 marks the end of the head and the right shoulder's beginning. Depending on the relationship between the two low points, the neckline can slope up, down, or be horizontal. **The slope of the neckline will affect the pattern's degree of bearishness**—a downward slope is more bearish than an upward slope. In some cases, multiple low points can be used to form the neckline.
* **Volume.** As the Head and Shoulders pattern unfolds, volume plays an important role in confirmation. Volume can be measured as an indicator ([OBV](/table-of-contents/technical-indicators-and-overlays/technical-indicators/on-balance-volume-obv.md), [Chaikin Money Flow](/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-money-flow-cmf.md)) or simply by analyzing volume levels. Ideally, but not always, volume during the advance of the left shoulder should be higher than during the advance of the head. Together, the volume decrease and the head's new high serve as a warning sign. The next warning sign comes when volume increases on the decline from the peak of the head, then decreases during the advance of the right shoulder. Final confirmation comes when volume further increases during the right shoulder's decline.
* **Neckline Break.** The head and shoulders pattern isn't complete, and the uptrend is not reversed until the neckline support is broken. Ideally, this should also occur in a convincing manner, with an expansion in volume.
* **Support Turned Resistance.** Once support is broken, it is common for this same support level to turn into resistance. Sometimes, but certainly not always, the price will return to the support break and offer a second chance to sell.
* **Price Target.** After breaking neckline support, the projected price decline is found by measuring the distance from the neckline to the top of the head. This distance is then subtracted from the neckline to reach a price target. Any price target should serve as a rough guide, and other factors should also be considered. These factors might include previous support levels, Fibonacci retracements, or long-term moving averages.

Archer Daniels Midland Company (ADM) formed a Head and Shoulders Top reversal with a slightly upward-sloping neckline.

<figure><img src="/files/cxQrYbpb6Ry8HL87EjkN" alt="Chart from StockCharts.com showing a head and shoulders top reversal pattern"><figcaption><p>Example of a Head and Shoulders Top reversal pattern.</p></figcaption></figure>

&#x20;**Key points include:**

* The low at $17.50 marked the end of the left shoulder and the beginning of the head (1).
* During the advance to $20.50, volume was still high but not as high as during the left shoulder advance. However, volume tapered off significantly during the next advance to $20.
* Volume continued to decline until the breaking of the neckline. (Note red line on volume bars.)
* The decline from $20.50 to $17.50 formed the second low point (2).
* During the decline of the right shoulder and neckline break, volume expanded (red oval), and Chaikin Money Flow (CMF) turned negative.
* After the initial decline, there was a return to the neckline break (black arrow). Even during this decline, CMF remained negative. The subsequent decline took the stock below $11.
* The measurement from the neckline to the top of the head was 3. With the neckline break at $17.50, this would imply a move to around $14.50. The July 1998 low was $13.50. After a decline from $20.50, at least, a short reaction rally could have been expected.<br>

The head and shoulders pattern is one of the most common reversal formations. **It is important to remember that it occurs after an uptrend and usually marks a major trend reversal when complete.** While the left and right shoulders should be symmetrical, it's not an absolute requirement. They can be different widths as well as different heights. The most critical factor is identifying neckline support and volume confirmation on the break.&#x20;

The support break indicates a renewed willingness for investors to sell at lower prices. Lower prices combined with a volume increase indicate an increase in supply. The combination can be lethal, and sometimes, there is no second chance return to the support break. Measuring the expected length of the decline after the breakout can be helpful, but don't count on it for your ultimate target. As the pattern unfolds, other aspects of the technical picture will likely take precedence.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/head-and-shoulders-top.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
