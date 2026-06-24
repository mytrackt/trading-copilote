> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/the-pre-holiday-effect.md).

# The Pre-Holiday Effect

Over the past century, there have been nine holidays during which the Exchanges have traditionally been closed. Historical research shows that stock prices often behave in a specific manner in each of the two trading days preceding these holidays. By becoming aware of this behavior, short-term traders and longer-term investors can benefit.

## The Pre-Holiday Trading Strategy

The general strategy is to purchase equities one or two days before a holiday. Short-term traders would look to sell just after the holiday, while longer-term investors would wait until the year's end. Both strategies have proven to be profitable plays. The theory behind this effect is that traders lighten up their holdings (selling) before the three-day holiday to avoid any unexpected bad news. The selling pressure drives stock prices down, making those days a good opportunity for buying lower in the range.

Here are the average pre-holiday results for the last 50 years (excluding Juneteenth), based on the S\&P 500 Index:

| **Holiday**       | Buy two days before, sell at year end | Buy one day before, sell at year end |
| ----------------- | ------------------------------------- | ------------------------------------ |
| President's Day\* | -0.1%                                 | 12.2%                                |
| Good Friday       | 7.3%                                  | 17.8%                                |
| Memorial Day      | -4.7%                                 | 22.8%                                |
| Independence Day  | 13.3%                                 | 37.3%                                |
| Labor Day         | 16.8%                                 | 33.7%                                |
| Election Day      | 17.9%                                 | 4.6%                                 |
| Thanksgiving      | 4.3%                                  | 1.1%                                 |
| Christmas         | -7.1%                                 | 15.2%                                |
| New Year's        | 31.1%                                 | 19.6%                                |

{% hint style="warning" %}
**Note:** President's Day data is comprised of the aggregate of both Washington and Lincoln's birthdays before 1998.
{% endhint %}

The original research was based on the behavior of the S\&P 500 Index around the 419 holiday market closings that occurred from 1928 to 1975.

To put those returns in perspective, if you had invested $10,000 in the S\&P 500 Index in January 1928 and sold it all in December 1975, you would have ended up with $51,441. However, if you had invested one-ninth of your money just before each pre-holiday period (selling everything at the end of the year), you would have finished with $1,440,716. Not bad!

## The Short-Term Trading Strategy <a href="#the_short-term_trading_strategy" id="the_short-term_trading_strategy"></a>

Short-term trading using this pre-holiday effect can provide excellent results. In the chart for General Electric (GE) below, we see that a buy near the open on June 30th would be accomplished at around $47.75. Selling at open on July 5th at $50.25 provided excellent returns.

<figure><img src="/files/lnD13ncCcdMh4yLSTecF" alt=""><figcaption><p>General Electric Co. (GE) Pre-Holiday example chart from StockCharts.com</p></figcaption></figure>

It is important to note that there are two holidays which often have a partial trading day during the holiday weekend - the day before Independence Day and the day after Thanksgiving. These days usually have a shortened trading session that can be extremely volatile. While they can be traded, volume is always very light and it may be difficult to get limit orders filled.

In the chart below for Motorola (MOT), we can see that a buy at $30 on June 30th would have been a flat trade on July 3rd, but rose $2 and $3 a share in the two days following the July 4th holiday.

<figure><img src="/files/0GOpaCzJW9Y1wUMw4CHL" alt=""><figcaption><p>Motorola, Inc. (MOT) Pre-Holiday example chart from StockCharts.com</p></figcaption></figure>

For Realty Income (O), we have a buy near close at $21.2 and a sell just after the open on July 5th at $22. The volume is less than 50,000 shares on average and the stock is generally down-trending, but the method is still viable.

<figure><img src="/files/1kihSHoNgPPRTjI5hl4O" alt=""><figcaption><p>Realty Income Corp. Md. (O) Pre-Holiday example chart from StockCharts.com</p></figcaption></figure>

## The Long-Term Trading Strategy <a href="#the_long-term_trading_strategy" id="the_long-term_trading_strategy"></a>

Again, the theory says that stocks generally fall just before holidays because traders offload their holdings in order to avoid the risk of significant news appearing while the markets are closed. Longer-term investors who are willing to ride out any short-term negative news are rewarded with lower entry prices.

Here are four examples from the 2000 Memorial Day holiday (May 26th) where excellent entry points appeared:

<figure><img src="/files/fziuRBg9WUbiqj18NYcr" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/4lkdCCqUn2lAmWEU9gNo" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/8pAWVY5p2rz4o7EqS5uU" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/FhegAyysnuVwZrdjL5Kz" alt=""><figcaption></figcaption></figure>

Investors that took advantage of those dips would likely be rewarded by year-end.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/the-pre-holiday-effect.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
