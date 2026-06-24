> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/bump-and-run-reversal.md).

# Bump and Run Reversal

As the name implies, the Bump and Run Reversal (BARR) is a reversal pattern that forms after excessive speculation drives prices up too far, too fast. Developed by Thomas Bulkowski, the pattern was introduced in [the June-97 issue](http://stockcharts.com/h-mem/tascredirect.html?artid=\V15\C06\THEBUMP.pdf) of *Technical Analysis of Stocks and Commodities* and included in his book, the *Encyclopedia of Chart Patterns*.

The pattern was originally named the Bump and Run Formation, or BARF. Bulkowski decided that Wall Street was not ready for such an acronym and changed the name to Bump and Run Reversal. Bulkowski identified three main phases to the pattern: **lead-in, bump, and run.** We will examine these phases and also look at volume and pattern validation.

<figure><img src="/files/IhcejzJGDAWaEWXKHWCe" alt=""><figcaption><p>Example of a Bump and Run Reversal (BARR) pattern.</p></figcaption></figure>

* **Lead-in Phase.** The first part of the pattern is a lead-in phase that can last one month or longer and forms the basis for drawing the trend line. The price advance will be orderly during this phase, and no excess speculation will exist. The trend line should be moderately steep. If it's too steep, the ensuing bump is unlikely to be significant enough. If the trend line is not steep enough, then the subsequent trend line break will occur too late. Bulkowski advises that an angle of 30 to 45 degrees is preferable. The angle size will depend on the scaling ([semi-log](/table-of-contents/glossary/glossary-s.md#semi-logarithmic_percentage_scaling) or arithmetic) and the chart size. It's probably easier to judge the soundness of the trend line with a visual assessment.
* **Bump Phase.** The bump forms with a sharp advance, and prices move further away from the lead-in trend line. Ideally, the angle of the trend line from the bump's advance should be about 50% greater than the angle of the trend line extending up from the lead-in phase. Roughly speaking, this would call for an angle between 45 and 60 degrees. If measuring the angles is impossible, then a visual assessment will suffice.
* **Bump Validity.** The bump must represent a speculative advance that cannot be sustained for long. Bulkowski developed an “arbitrary” measuring technique to validate the level of speculation in the bump. The distance from the highest high of the bump to the lead-in trend line should be at least twice the distance from the highest high in the lead-in phase to the lead-in trend line. These distances can be measured by drawing a vertical line from the highest highs to the lead-in trend line. An example can be seen in the chart below.
* **Bump Rollover.** After speculation dies down, prices peak, and a top forms. Sometimes, a small [double top](/table-of-contents/glossary/glossary-d.md#double_top_breakout) or a series of descending peaks forms instead. Prices decline toward the lead-in trend line, and the right side of the bump forms.
* **Volume.** As the stock advances during the lead-in phase, volume is usually average and sometimes low. When the speculative advance begins to form the left side of the bump, volume expands as the advance accelerates.
* **Run Phase.** The run phase begins when the pattern breaks [support](/table-of-contents/glossary/glossary-s.md#support) from the lead-in trend line. Prices will sometimes hesitate or bounce off the trend line before breaking through. Once the break occurs, the run phase takes over, and the decline continues.
* **Support Turns Resistance.** After the trend line is broken, a retracement sometimes tests the renewed resistance level. Potential support-turned-resistance levels can also be identified from the reaction lows within the bump.

The Bump and Run Reversal pattern can be applied to daily, weekly, or monthly charts. As stated above, it is designed to identify long-term unsustainable speculative advances. Because prices rise quickly to form the bump's left side, the subsequent decline can be just as ferocious.

<figure><img src="/files/MOO7djcWOoeBLnT7RcZH" alt="Example of a Bump and Run Reversal pattern from StockCharts.com"><figcaption><p>Bump and Run Reversal pattern after prices advance in a speculative frenzy in 2000. </p></figcaption></figure>

Level Three Communications (LVLT) formed a Bump and Run Reversal pattern after prices advanced in a speculative frenzy at the beginning of 2000. Prices advanced from 72 to 132 in 2 months and this advance ultimately proved unsustainable.

* The lead-in phase formed over three months from early Oct 1999 to early Jan 2000. Volume during this phase was relatively subdued and declined during the November and December advance.
* The trend line extending higher from the lead-in phase lows formed a 34-degree angle. A visual assessment also reveals that this trend line is neither too steep nor too flat.
* The bump phase began in early January when the advance accelerated with a large increase in volume. A conservatively drawn trend line formed a 51-degree angle that was exactly 50% larger than the angle from the lead-in trend line.
* The distance from the lead-in phase's highest high to the trend line was 13. The distance from the bump phase's highest high to the trend line was 38. This is almost three times larger and validates the speculative excesses in the bump.
* After reaching a high of around $132, prices declined sharply and bounced off the lead-in trend line. A lower high formed around $115 (red arrow), and the trend line was soon broken.
* The decline continued after the trend line break and reached $67 before a reaction rally began. The stock price advanced to around $95 during the reaction rally but fell just short of the horizontal support line before falling back to new lows.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/bump-and-run-reversal.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
