> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/why-and-how-to-use-correlation.md).

# Why and How To Use Correlation

## What Is Correlation? <a href="#what_is_correlation" id="what_is_correlation"></a>

In statistics, correlation measures the degree to which two (or more) variables move together. Positive correlation values indicate movement together in the same direction. Negative correlation values indicate movement in opposite directions. Correlation values range from -1.0 to +1.0, with a value of 0 indicating no relationship between the variables.

In finance and financial markets, correlation measures the relationship between two securities (stocks, bonds, ETFs, mutual funds, indexes, etc.) and the degree to which they move together. Securities with high positive correlation values move together in the same direction. Securities with high negative correlation values move in exactly opposite directions. Securities with very low correlation values (at or around 0) are unrelated with respect to the directions in which they move.

## Why Use Correlation? <a href="#why_use_correlation" id="why_use_correlation"></a>

Correlation values can be used to construct a well-diversified portfolio, reducing risk while also improving returns. By building a portfolio that consists of a diverse set of securities across multiple asset classes, each with low correlation values, you can limit risk by reducing exposure to singular market shocks.

## How To Use Correlation <a href="#how_to_use_correlation" id="how_to_use_correlation"></a>

To use correlation to your advantage, balance the securities in your portfolio according to their correlation values, while ensuring that the correlation values against a common benchmark (such as the S\&P 500) are not all clustered in a specific range. For example, if you have 10 stocks and funds in your portfolio, all with correlation values against the S\&P 500 ranging from +0.87 to +0.98, the assets in your portfolio can be shown to move in very similar directions, increasing your risk exposure to singular market shocks. If, however, the set of stocks and funds in your portfolio is more diverse and the correlation values range from, for example, -0.79 to +0.95, your portfolio can be considered more broadly diversified and thus less exposed to singular market shocks.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/why-and-how-to-use-correlation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
