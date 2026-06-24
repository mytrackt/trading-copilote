> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-14.md).

# TA 101 – Part 14

*This is the fourteenth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand,” these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Fibonacci Lines <a href="#fibonacci_lines" id="fibonacci_lines"></a>

How high is “too high?” How low is “too low?” Think back to any time that you've owned a stock and think about when you started to get worried about its performance. At what point did “your gut” start to tell you that you needed to sell? Chances are your gut started talking to you after the stock had moved up (or down) by 38.2%.

Wow, that's a really specific number - “38.2”! It seems kind of arbitrary, also. There's no way that could be correct, right? I mean, without knowing anything about the stock you were trading, or the amount of money involved, or the overall market conditions, or anything else - how can we stand here and tell you that you got nervous right at 38.2%?

The reason is because 38.2 appears to be programmed into the human psyche (as well as many other parts of nature). It's one of a set of numbers called “Fibonacci Percentages.” They are derived from the “Fibonacci Sequence” which is a list of numbers where each number equals the sum of the previous two, i.e.,

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 etc.

The branching in trees, the arrangement of leaves on a stem, the flowering of artichokes, an uncurling fern and the arrangement of a pine cone - all these things exhibit Fibonacci characteristics. In addition, if you take any large Fibonacci number and divide it by the previous number, you'll get something very close to 1.6180339887 (the larger the number, the closer you'll get). Now, 1.6180 has been known for centuries as “The Golden Ratio,” mostly, because we humans tend to prefer things - art, sculpture, architecture, etc. - that have proportions that equal the golden ratio.

<figure><img src="/files/NCEUJ79MPs4mcVjo31V5" alt=""><figcaption></figcaption></figure>

Which of these picture looks the most natural to you? The middle one has golden ratio proportions.

Getting back to stock charting, R.N. Elliott made the first well-known connection between price movements and the golden ratio. He noted that many reversals occurred around 61.8% or its complement 38.2% (i.e., 100 - 61.8). Combined with 50% and 100%, they make up the standard set of Fibonacci Percentages.

Regardless of how the numbers were arrived at, chart analysts have observed that prices often will reverse after moving up (or down) by one of those percentages. Basically, those percentages are where something tells many people that it is time to take action - and thus prices reverse. Strange but true. Check it out:

<figure><img src="/files/w8sbmEAXQJWD0adzdyJe" alt=""><figcaption></figcaption></figure>

The Fibonacci Lines on this chart were created based on the move from Feb. 9th to May 30th - so just focus on the shaded blue area of the chart. Like a weatherman, the lines “forecast” that support for IBM would occur around 88.79 essentially because lots of people would probably feel that IBM had “fallen enough” and would start buying it again. That is precisely what happened at the end of June (red circle).

Unfortunately, many people have gone on to claim that Fibonacci lines (and their variants) have almost “magical powers” to predict price movements. Like most technical analysis tools, we think Fibonacci Lines are useful forecasting tools - but not magical.

You can add Fibonacci Lines to your charts using our ChartNotes annotation tool. To get started, simply click on the “Annotation” link below any SharpCharts.

{% hint style="info" %}
If you hold down “CTRL” while drawing Fibonacci lines, we'll add the 23.6% and 161.8% lines as well.
{% endhint %}

*In part 15, we'll cover Price Gaps.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-14.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
