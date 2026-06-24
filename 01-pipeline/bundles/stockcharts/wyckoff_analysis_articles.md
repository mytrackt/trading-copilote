> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles.md).

# Wyckoff Analysis Articles

[**Wyckoff Market Analysis**](/table-of-contents/market-analysis/wyckoff-analysis-articles/wyckoff-market-analysis.md) \
Describes how Richard D. Wyckoff approached broad market analysis. Learn how to define the broad market trend, identify major tops and bottoms, project prices and determine price position within a move.

[**Wyckoff Stock Analysis**](/table-of-contents/market-analysis/wyckoff-analysis-articles/wyckoff-stock-analysis.md) \
Describes how Richard D. Wyckoff picked individual stocks. Learn how to isolate the strongest groups, cherry-pick stocks within these groups and manage the trade once it is underway.

[**The Wyckoff Method: A Tutorial**](/table-of-contents/market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial.md) \
An alternate explanation of the Wyckoff analysis method with sections on Wyckoff's Five-Step Approach to the Market, his Price Cycle, his Supply/Demand analysis, his Buying and Selling tests and his P\&F counting guide.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
