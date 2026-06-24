> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-5.md).

# TA 101 – Part 5

*This is the fifth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Candlestick Charts <a href="#candlestick_charts" id="candlestick_charts"></a>

Compared to traditional OHLC bar charts, many traders consider candlestick charts more visually appealing and easier to interpret. Each candlestick provides an easy-to-decipher picture of price action. An analyst can quickly understand the relationship between the opening and closing price as well as the high and low price.

<figure><img src="/files/rPwSyPFDx208Rthj0mDd" alt=""><figcaption></figcaption></figure>

The graphic above shows how candlesticks are constructed.

Candlesticks with hollow bodies indicate buying pressure and filled bodies indicate selling pressure. Long upper or lower shadows form when the market moves significantly in a particular direction during the day and then reverses before the end of the day. As a result, long lower shadows can infer bullishness while long upper shadows can infer a bearish market.

## Candlestick Colors <a href="#candlestick_colors" id="candlestick_colors"></a>

<figure><img src="/files/aHknLHK7SIBfYp2eUMvK" alt=""><figcaption></figcaption></figure>

When the 'Color Prices' option is selected on the Chart Attributes workbench, the Candlestick's outline and body will be colored black or red, depending on the candlestick's opening and closing prices and the previous day's closing price.

If the closing price is higher than the opening price, the body will be displayed hollow. If the closing price is lower than the opening price, the body will be filled red with the following exception; if the closing price is higher than the previous day's closing price, the body will then be filled black.

The candlestick's shadows and body outline are colored black or red depending on the closing price compared to the previous day's closing price. If the closing price is higher than the previous day's, the candlestick's shadows and body outline will be colored black. If the closing price is lower than the previous day's, however, the candlestick's shadows and body outline will be red.

Market psychology is reflected in each of these candlestick formations in the following ways.

**Up Day, Higher Close:**\
Typically results from expectations of higher prices (greed) out weighing expectations of lower prices (fear). The length of the candlestick body shown indicates especially strong buying.

**Down Day, Lower Close:**\
Expectations of lower prices (fear) are stronger than those of higher prices (greed). As with the first candlestick, a longer candlestick body infers greater urgency of investors to sell their shares.

**Down Day, Higher Close:**\
A rare candlestick, this one begins with an opening gap up in price from the previous day's closing price but closes down for the day. A gap is defined as a price range where no trading takes place and is the result of a significant change in demand (gap up) or supply (gap down) before trading begins for the day. In this case, heavy buying at the beginning of the day reversed but still closed higher than the previous day. This is a bearish sign when it occurs well into an upward price move.

**Up Day, Lower Close:**\
Another rare candlestick, this one begins with an opening gap down in price from the previous day's closing price but closes up for the day. This price action can be considered bullish during a downward price move since initial strong selling in the day becomes exhausted and buyers push the price higher at close.

<figure><img src="/files/XIkdWKtOoZuk9biepvwi" alt=""><figcaption></figcaption></figure>

The SharpChart AAPL above illustrates the candlestick format. The up and down days are readily apparent with the use of candlestick charting. When the balance between buyers and sellers change, candlesticks often form recognizable patterns signaling the change. These candlestick patterns will be discussed in a later article.

Below, you can see how the three types of charts compare visually:

<figure><img src="/files/SRvxPr52a1tt440czqFk" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/b6XiczFiQ8Xc1YS8yb8v" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/wE6dKnuzsS6CHINGYQh0" alt=""><figcaption></figcaption></figure>

*In part 6, we'll get into chart scaling, volume, and CandleVolume charts.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-5.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
