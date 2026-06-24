> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-11.md).

# TA 101 – Part 11

*This is the eleventh part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="info" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Price Patterns <a href="#price_patterns" id="price_patterns"></a>

Price Patterns result when the market is not in agreement on the value of a stock. Essentially, they are the *visual remains* of a big battle between bulls and bears. In many ways, they are like weather patterns that you see on the nightly news. Often today's weather can be forecast by looking at yesterday's atmospheric data, but occasionally (frequently?) the forecast is wrong. Similarly, chart patterns often but not always indicate future price movements.

At their core, most price patterns are combinations of several trend lines. The simplest pattern is the **Rectangle Pattern**.

In a rectangle pattern, price moves between two horizontal lines of support and resistance. In order to qualify as a rectangle pattern, both support and resistance lines must be touched at least twice. Rectangle patterns have a narrow or wide price range and last from days to months. The pattern ends once the line of support or resistance is broken.

<figure><img src="/files/2ir5B08qiz3KmMa5Gd2r" alt=""><figcaption></figcaption></figure>

A price break through resistance may be anticipated if volume expands when prices rise and contracts when prices fall within the rectangle pattern. An imminent price break above resistance may exist if prices don't fall to the support line before rising again.

<figure><img src="/files/P39TJ1GxSrUfTjYFHz9O" alt=""><figcaption></figcaption></figure>

A price break through support may be anticipated if volume expands when prices fall and contracts when prices rise within the rectangle pattern. An imminent price break below support may exist if prices don't rise to the resistance line before falling again.

As illustrated above, as soon as the pattern breaks down, the top (or bottom) of the rectangle changes into a support (or resistance) line for the stock.

Rectangle patterns clearly show the battle between bulls and bears, with the bulls repeatedly buying when prices hit the support level, and bears repeatedly selling when prices hit the resistance level. At some point, one of those groups will win, and prices will break out of the pattern. The longer prices have been in the pattern, then the larger the *breakout move* will be and the more significant the new support/resistance line becomes.

Another common price pattern is the **Triangle Pattern**. The triangle pattern is very similar to the rectangle, except that the upper and/or lower trend lines that define the pattern are sloped instead of horizontal.

Go back to the rectangle diagram above and imagine that bearish sentiment about the stock was growing over time. What would that look like? Well, in that case, more and more sellers would not wait for prices to return to the level of the red resistance line before selling. Instead, they would sell sooner. That would cause the red resistance line to become a downward trend line forming a Descending Triangle Pattern.

<figure><img src="/files/LDDGn7dn6fygmnLHC8y2" alt=""><figcaption></figcaption></figure>

Alternately, what if buyers started getting impatient and started buying before the stock got back to its green support line? Then a Rising Triangle Pattern would form.

<figure><img src="/files/iRh5rFPqcl764WX8vGcW" alt=""><figcaption></figcaption></figure>

And what if both the bulls became more bullish while at the same time, the bears became more bearish? Then both the red and green lines would be slanted and we'd have a [Symmetric Triangle ](/table-of-contents/chart-analysis/chart-patterns/symmetrical-triangle.md)Pattern.

<figure><img src="/files/Qy5R50BI2XzBeGyXRKxv" alt=""><figcaption></figcaption></figure>

By the way, triangle patterns are also referred to as “coils.” Can you see why? As the upper and lower parts of the triangle get closer together, the battle between the bulls and the bears gets more intense and the suspense builds. Obviously, at some point, prices are going to move outside of the triangle's boundaries - but will they move higher or lower? Psychological energy coils up like a spring inside of the triangle and the closer the lines get, the bigger the inevitable breakout will be.

As you probably guessed, the diagrams above are not realistic. Typically, triangle patterns have a breakout well before the apex of the triangle is reached. It is the direction of the breakout that is the key question when watching a triangle form. Will the bulls win? Will the bears win?

A couple of clues can be found in the price action that precedes the triangle. If the stock was in an uptrend prior to the triangle, there is a good chance it will break out of the triangle pattern on the upside and continue the uptrend. In addition, rising triangles tend to break out to the upside while descending triangles often break lower. Symmetric triangles are usually not completely *even*, i.e., the support side may be stronger than the resistance side making the triangle *point up* or, if the support side is weaker, *point down*. In that case, the triangle often breaks in the direction it is pointing.

*In part 12 we'll look at how to confirm these patterns with volume and examine some real-world examples.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-11.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
