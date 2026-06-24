> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-3.md).

# TA 101 – Part 3

*This is the third part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Chart Data <a href="#chart_data" id="chart_data"></a>

Charts are created from data such as price data and index data.

### Price Data <a href="#price_data" id="price_data"></a>

Exchanges record the price and number of shares for each stock transaction, which is called tick data. Tick data is compiled over different periods of time to construct price bar data. Price bars show the beginning, highest, lowest, and ending prices for a chosen period. Individual price bar time periods can range from one minute to one year. Daily, weekly, and 60-minute price bars are other common examples.

Price bars less than a day long are known as intraday price bars. They range from one minute to one hour and are typically used in technical analysis by day traders who hold positions for minutes or hours.

A daily price bar is constructed of all the transactions during a full trading day. Investors who hold positions for days or years most often use daily price bars in technical analysis.

The number of shares traded in each transaction is called volume. Volume is recorded as tick data just like price. Volume tick data is added together to construct volume bars and are then charted with their corresponding price bars for technical analysis.

### Index Data <a href="#index_data" id="index_data"></a>

Data for hundreds of indices, published by financial service companies and the major exchanges, are provided to StockCharts.com through third party data providers. Indices are not tradable financial instruments. Indices represent domestic and foreign market averages, industries, commodities, currencies, bonds and many other price, volume, and breadth measurements of market activity. Examples of market indices include the Dow Jones Industrial Average ($INDU), NYSE Healthcare Index ($NYP) and the New Zealand Dollar ($NZD). The financial service companies are responsible for the accuracy of the indices they publish.

Breadth indices measure how many issues move within a particular market index. Breadth indices give analysts insight into investor sentiment. Examples of breadth indices include NASDAQ Advance-Decline Issues ($NAAD), NYSE Advance-Decline Volume ($NYUD) and AMEX Issues Unchanged ($AMADU).

## Key Assumptions of Technical Analysis <a href="#key_assumptions_of_technical_analysis" id="key_assumptions_of_technical_analysis"></a>

There are three things that you must verify are true about a security before you can apply standard chart and/or indicator analysis to the security's chart. These three key assumptions are:

### High Liquidity <a href="#high_liquidity" id="high_liquidity"></a>

Liquidity is essentially volume. It means that shares have the ability to trade quickly without dramatically affecting prices. If someone buys 100 shares of Microsoft today, that trade by itself will have almost no effect on the price of the stock. Why? Because MSFT is extremely liquid with lots of buyers and selling at any given moment.

Low Liquidity is a trap that many amateur investors can fall into. When you buy a stock with low liquidity, you probably won't get it at the price you were quoted because there are no sellers at that price. The broker has to raise the price - often significantly - before a seller can be found. Similarly, when you sell a low liquidity stock, the broker will need to lower the price significantly to find a buyer.

In addition, these thinly-traded stocks are often very low priced - often less than 1 cent - and that means that their price can be manipulated by someone with lots of resources (and lots of time).

None of this is illegal or hidden or “wrong” in any way. It is just that the principles upon which Technical Analysis is based assume that only normal market forces move a stock's price - not the manipulation or issues with trading volumes that low liquidity stocks can have.

### No Artificial Price Changes <a href="#no_artificial_price_changes" id="no_artificial_price_changes"></a>

Similar to the reason for high liquidity, prices cannot be changed by forces other than the fear and greed that drives the market. Anything else that changes prices is considered “artificial” and needs to be eliminated before standard technical analysis techniques can be applied.

So what is an example of an “artificial” price change? Splits, dividends, and distributions are the most common “culprits.” When a stock splits, let's say 2-for-1, the market participants don't really care. They get double the shares at half the price - a net-zero transaction that doesn't change their opinion of the stock one way or the other.

However, consider what happens to the stock's chart. It now has a huge (50%) gap down on it. If you didn't know about the split, you'd be very worried about the stock. And, because technical indicators are dumb, they would all give bearish “sell” signals at that point.

For this reason, the effects of these “artificial” price changes must be removed from the data before standard technical analysis techniques can be used. Ironically, this is done by adjusting all of the data prior to the split downwards, thus eliminating the gap on the chart.

### No Extreme News <a href="#no_extreme_news" id="no_extreme_news"></a>

Technical Analysis cannot predict extreme events such as, for example, a company's CEO dying unexpectedly or the huge tragedy of 9/11. When “extreme news” happens, technicians have to wait patiently until the chart settles down and starts to reflect the “new normal” that results from such news.

This is not to say that charts are useless when one or more of these three things occur. It means that the philosophical underpinnings of the signals and chart patterns that traditional technical analysis uses are gone in those cases. Standard technical signals and predictions cannot be accurately used in those circumstances.

## Chart Construction <a href="#chart_construction" id="chart_construction"></a>

The security's price data is displayed on a price chart: a graph which shows how price and volume changes with time. This visual representation of price data is very helpful when using technical analysis techniques.

Price charts on StockCharts.com are called SharpCharts (Time-independent charting methods like Point & Figure charting will be discussed in detail later).

<figure><img src="/files/mZzfm9ESSNN3gYQeZphs" alt=""><figcaption><p>Chart showing sections of a SharpChart</p></figcaption></figure>

The example above illustrates the layout of a typical SharpChart. Price data, volume data and technical indicators are displayed on a SharpChart. A technical indicator is a mathematical expression of price and/or volume which can provide insight into future price movements. We will talk more about technical indicators later.

Price data and overlays are plotted in the Price Plot Area. Overlays are technical indicators that are normally expressed in terms of price. Non-price values of overlays are displayed on the left axis as shown above.

Technical indicators that cannot be expressed in terms of price are normally plotted in the Indicator Panels. Although only a single Indicator Panel is shown above, SharpCharts can be created with multiple Indicator Panels displayed above and below the Price Plot Area. Additional date/time axes can be added between the Indicator Panels if needed. The legend for both the Price Plot Area and Indicator Panel contain the information used to create the SharpChart.

*In Part 4, we'll get into the specifics of line charts, OHLC Bar charts, and candlestick charts.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-3.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
