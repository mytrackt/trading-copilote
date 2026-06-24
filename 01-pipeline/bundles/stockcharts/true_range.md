> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/true-range.md).

# True Range

## What Is the True Range (TR) Indicator?

The True Range (TR) indicator measures the daily price range plus any gap from the prior day’s closing price. This is different from the traditional price range, which takes the difference between the high and low prices.

## Calculating True Range

True Range looks at three prices: the previous bar’s close, the current bar’s high, and the current bar’s low.

True Range (TR) is the greater of the following:

* High minus low
* High minus the previous close
* Previous close minus the low

By using the greater of these values the TR accounts for any price gaps that may have taken place.&#x20;

This raw True Range is smoothed to give the Average True Range (ATR). J. Welles Wilder introduced the TR and ATR in [*New Concepts in Technical Trading Systems*](https://www.amazon.com/New-Concepts-Technical-Trading-Systems/dp/0894590278).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/true-range.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
