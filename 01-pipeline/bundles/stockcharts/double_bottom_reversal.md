> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/double-bottom-reversal.md).

# Double Bottom Reversal

The Double Bottom Reversal is a bullish reversal pattern typically found on bar charts, line charts, and candlestick charts. As its name implies, the pattern comprises two consecutive troughs that are roughly equal, with a moderate peak in between.

{% hint style="warning" %}
**Note:** A Double Bottom Reversal on a bar or line chart is different from a Double Bottom Breakdown on a P\&F chart. Double Bottom Breakdowns on P\&F charts are bearish patterns that mark a downside support break.
{% endhint %}

<figure><img src="/files/zmAo7gdvQ1cYw2Msboyt" alt="Chart from StockCharts.com displaying a double bottom reversal"><figcaption><p>Example of a double bottom reversal.</p></figcaption></figure>

Although there can be variations, the classic Double Bottom Reversal usually marks an intermediate or long-term change in trend. Many potential double bottom reversals can form during a downtrend, but until key resistance is broken, a reversal cannot be confirmed. To help clarify, let's look at the key points in the formation and then walk through an example.

* **Prior Trend.** With any reversal pattern, there must be an existing trend to reverse. In the case of the Double Bottom Reversal, a significant downtrend of several months should be in place.
* **First Trough.** The first trough should mark the lowest point of the current trend. The first trough is fairly normal, and the downtrend remains firmly in place.
* **Peak.** Generally, after the first trough, an advance follows, ranging from 10 to 20%. [Volume](/table-of-contents/glossary/glossary-v.md#volume) on the advance from the first trough is usually inconsequential, but an increase could signal early accumulation. The peak's high is sometimes rounded or drawn out a bit from the hesitation to go back down. This hesitation indicates that demand is increasing but still not strong enough for a breakout.
* **Second Trough.** The decline of the reaction high usually occurs with low volume and meets [support](/table-of-contents/glossary/glossary-s.md#support) from the previous low. Support from the previous low should be expected. Even after establishing support, only the possibility of a Double Bottom Reversal exists and still needs to be confirmed. The time between troughs can vary from a few weeks to many months, with the norm being one to three months. While exact troughs are preferable, there is room to maneuver; typically, a trough within 3% of its predecessor is considered valid.
* **Advance From Trough.** Volume is more important for the Double Bottom Reversal than the double top. There should be clear evidence that volume and buying pressure are accelerating during the advance off of the second trough. An accelerated ascent, perhaps marked with a gap or two, also indicates a potential change in sentiment.
* **Resistance Break.** Even after trading up to resistance, the double top and trend reversal are still incomplete. Breaking resistance from the highest point between the troughs completes the Double Bottom Reversal. Like advances, these should occur with increased volume and/or an accelerated ascent.
* **Resistance Turned Support.** Broken resistance becomes potential support, and sometimes, the first correction tests this newfound support level. Such a test can offer a second chance to close a short position or initiate a long one.
* **Price Target.** To estimate a target, the distance from the resistance breakout to trough lows can be added to the price at which the breakout took place. This would imply that the bigger the formation, the larger the potential advance.

It's important to remember that the Double Bottom Reversal is an intermediate- to long-term reversal pattern that doesn't form in a few days. Although formation in a few weeks is possible, having at least four weeks between lows is preferable.&#x20;

Bottoms usually take longer to form than tops; patience can often be a virtue. Give the pattern time to develop and look for the proper clues. The advance off of the first trough should be 10-20%. The second trough should form a low within 3% of the previous low, and volume on the ensuing advance should increase. Volume indicators such as [Chaikin Money Flow](/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-money-flow-cmf.md) (CMF), [OBV](/table-of-contents/technical-indicators-and-overlays/technical-indicators/on-balance-volume-obv.md), and [Accumulation/Distribution](/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md) can be used to look for signs of buying pressure. Just as with the double top, waiting for the resistance breakout is paramount. The formation is not complete until the previous reaction high is taken out.

After trending lower for almost a year, Pfizer, Inc. (PFE) stock formed a Double Bottom Reversal and broke resistance with an expansion in volume (see chart below).

<figure><img src="/files/XFbUZzqTmHW8w8j9jqZ3" alt="Chart showing a double bottom reversal in Pfizer, Inc. stock"><figcaption><p>A double bottom reversal in PFE stock.</p></figcaption></figure>

* From a high near $50 in April 1999, PFE declined to 30 in December 1999, a new 52-week low.
* The stock advanced over 20% off its low and formed a reaction high of around $37.50. Volume expanded, and the January 13 advance (green arrow) occurred at the highest volume since November 5.
* After a short pullback, another attempt to break above resistance failed. Even so, volume on advancing days was generally higher than on declining days. The stock's ability to remain in the mid-thirties for an extended period of time indicated some strengthening in demand.
* The decline from $37.50 back to $30 was sharp, but downside volume didn't expand materially. There were two days when volume on a decline exceeded the 60-day [Exponential Moving Average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMA) of volume, and CMF dipped near -10% twice. However, money flows indicated accumulation throughout the decline by remaining mostly above zero with periodic movements above +10%.
* The second trough formed with a low equal to the previous low ($30). The two lows were a little over two months apart.
* The advance off the second low witnessed an accelerated move with a volume expansion. After the second low at $30, five of the next six advancing days saw volume well above the 60-day EMA. The CMF, which didn't weaken, moved above +20% within six days of the low.
* Resistance at $37.50 was broken with a [gap up](/table-of-contents/glossary/glossary-g.md#gap_-_up_down) on the open and another volume expansion. After running from $30 to $40 in a few weeks, the stock pulled back to the resistance break at $37.50, which now turned into support. There was a brief chance to put on a long position on the pullback. The stock quickly advanced past $45.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/double-bottom-reversal.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
