> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-12.md).

# TA 101 – Part 12

*This is the twelfth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Volume Confirmation of Price Patterns <a href="#volume_confirmation_of_price_patterns" id="volume_confirmation_of_price_patterns"></a>

When identifying potential price patterns on a chart, it is crucial to try and verify that the market psychology behind the price pattern is really happening at that point on the chart. One of the best ways to do that is to use volume to confirm things.

<figure><img src="/files/KocWQtRvBj36ptsfNAnf" alt=""><figcaption></figcaption></figure>

In the case of a rectangle pattern, volume should be decreasing while the rectangle is forming. There may be volume spikes whenever prices get near the top or bottom of the pattern, but in general, as a rectangle pattern continues to develop, volume should decrease. Volume will probably spike up heavily immediately after the breakout as people realize that the support or resistance line has been broken.

<figure><img src="/files/Z3x1UzrI2a9UhO9pVbxi" alt=""><figcaption></figcaption></figure>

Triangle patterns should have a similar volume pattern - decreasing volume while the triangle is forming with a sharp increase in volume once a breakout is achieved.

Again, the diagrams above are idealized - the real-world is much messier. Consider this example:

<figure><img src="/files/THflwpiksvl26zEELb2X" alt=""><figcaption></figcaption></figure>

Notice that EWG didn't have a smooth decrease in volume but instead had several mini-spikes that corresponded to changes in direction of the “coil.” The key, however, is that each mini-spike was smaller than the previous one (with the exception of October 30, but that was early in the coil's formation). Once that downward volume trend was well established, a big spike above that trend line would signal the breakout - just like on December 6.

## Consolidation / Continuation Patterns vs. Reversal Patterns <a href="#consolidation_continuation_patterns_vs_reversal_patterns" id="consolidation_continuation_patterns_vs_reversal_patterns"></a>

So far, the two price patterns we've looked at - Rectangles and Triangles - are examples of *Consolidation Patterns*, also known as *Continuation Patterns*. They are called that because, in general, after the pattern completes, prices will usually continue whatever trend they were in prior to the pattern forming. In order words, if prices are in an uptrend prior to a rectangle pattern forming, prices will usually resume the uptrend once the rectangle pattern finishes. Basically, consolidation patterns are places where the bulls and the bears have another short-term argument about the stock, but it is a half-hearted one. The bigger picture doesn't really change.

Next, we are going to start looking at *Reversal Patterns*. These are where the fireworks occur. If consolidation patterns are skirmishes, reversal patterns are the big battles. When reversal patterns start to appear, the current trend is in real danger and lots of people start to pay attention.

*In part 13 we'll look at the granddaddy of all reversal patterns - the Head and Shoulders reversal.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-12.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
