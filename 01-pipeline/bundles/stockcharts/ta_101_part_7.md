> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-7.md).

# TA 101 – Part 7

*This is the seventh part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Chart Analysis - Support and Resistance <a href="#chart_analysis_-_support_and_resistance" id="chart_analysis_-_support_and_resistance"></a>

Prices are driven by two of humanity's strongest emotions: Fear and Greed. When more investors are fearful that a stock will fall, it does! It will continue to decline until the balance between Fear and Greed is re-established. The same is true for greed and rising prices. This phenomenon is referred to as *Market Psychology.*

***Support*** is the price level where “greedy” buyers enter the market to prevent prices from declining further. Support can develop at a specific price or, more commonly, in a price zone. Areas of support can exist for many months at a time.

<figure><img src="/files/Hv5LZ6qP9NKxJE5HfsgC" alt=""><figcaption></figcaption></figure>

The diagram above illustrates how market psychology causes the previous area of price support to turn into resistance. After breaking support, traders who bought in the zone of support are now holding losses and, in order to break even, want to sell as soon as prices approach their original purchase prices.

The ***Volume by Price*** overlay (volume traded in incremental price ranges) in the following SharpChart of Dover Corp. illustrates how strong support at 24 later became significant resistance as greed turned into fear.

<figure><img src="/files/yi1VEqLRdOgEkCaH95e2" alt=""><figcaption></figcaption></figure>

The concept of ***resistance*** is opposite of the support as discussed above. Resistance is the price level where “fearful” sellers suddenly come into the market and prevent prices from advancing further. Like support, resistance can develop at a specific price or in a price zone and can be held for months at a time.

<figure><img src="/files/hsx7YjGd71wBL0YS9fUJ" alt=""><figcaption></figcaption></figure>

If resistance is broken, market psychology causes the previous area of price resistance to turn into support. The diagram above illustrates this market behavior. Stock holders who sold in the zone of resistance are now regretting selling and want to buy as soon as prices approach the level they sold at earlier. Prices that seemed too high before now look like a bargain. The following SharpChart of Parker Hannifin Corp. illustrates resistance later becoming support. Notice how Volume by Price indicates the potential number of previous sellers willing to buy again if given the opportunity.

<figure><img src="/files/GoiZ0U3V6CANAT9YgyTP" alt=""><figcaption></figcaption></figure>

*In part 8 we'll discuss trend line analysis and trend channels.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-7.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
