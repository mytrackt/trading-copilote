> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-by-price.md).

# Volume-by-Price

## What Is Volume-by-Price? <a href="#what_is_volume-by-price" id="what_is_volume-by-price"></a>

Volume-by-Price is a charting tool that shows the trading volume for a particular price range, based on closing prices. Volume-by-Price bars are horizontal and shown on the left side of the chart to correspond with these price ranges. You can view these bars as a single color or with two colors to separate up volume and down volume. By combining volume and closing prices Volume-by-Price bars identify high-volume price ranges to mark support or resistance levels. StockCharts displays 12 Volume-by-Price bars on a chart by default, but you can increase or decrease this number to suit your preferences.

## Calculating Volume-by-Price <a href="#how_do_you_calculate_volume-by-price" id="how_do_you_calculate_volume-by-price"></a>

Volume-by-Price calculations are based on the entire period displayed on the chart. On a five-month daily chart, Volume-by-Price would be based on **ALL** five months of daily closing data, while on a two-week 30-minute chart, it would be based on two weeks of 30-minute closing data, and on a three-year weekly chart, it would be based on three years of weekly closing data. Volume-by-Price calculations do not extend beyond the historical data shown on the chart. You get the idea!

{% code overflow="wrap" %}

```
There are four steps involved in the calculation. 
This example is based on closing prices and the default parameter setting (12). 

  1. Find the high-low range for closing prices for the entire period.  
  2. Divide this range by 12 to create 12 equal price zones.
  3. Total the amount of volume traded within each price zone.  
  4. Divide the volume into positive and negative volume (optional). 
```

{% endcode %}

Negative volume for a price zone is the sum of volume for all down days in that zone, while positive volume is the total of volume for all up days in that price zone.

The example below shows a Volume-by-Price calculation taken for the Nasdaq 100 ETF from April 12 until September 15, 2010. Closing prices ranged from $40.32 to $47.87 during this period ($47.87 - $40.32 = 7.55). The 110 closing prices (one for each trading day) were sorted from low to high and divided into 12 even price zones (7.55/12 = 0.6292).

<figure><img src="/files/FXQmlzziHi6iq6LoXVkc" alt=""><figcaption></figcaption></figure>

The chart below highlights the first three price zones ($40.32–$40.95, $40.96–$41.58, and $41.59–$42.21). Starting from the low ($40.32), we can add the zone size (0.6292) to create the price zones leading to the high. Only prices within these zones are used for that particular Volume-by-Price calculation.

<figure><img src="/files/LH0lnWzYCZtUJZLhz8Ji" alt=""><figcaption></figcaption></figure>

The Volume-by-Price bars represent the total volume for each price zone. Volume can then be separated into positive and negative volume. The Volume-by-Price bars in the chart below are displayed in red and green to separate positive from negative volume.

<figure><img src="/files/ri2iCWK8JhsV1cgqfv1S" alt=""><figcaption></figcaption></figure>

## Interpreting Volume-by-Price Bars <a href="#how_do_you_interpret_volume-by-price_bars" id="how_do_you_interpret_volume-by-price_bars"></a>

Volume-by-Price can be used to identify current support and resistance levels and estimate future support and resistance levels. Price zones with heavy volume reflect elevated interest levels that can influence future supply or demand (a.k.a. resistance or support). Long Volume-by-Price bars underneath prices should be watched as potential support during a pullback. Similarly, long Volume-by-Price bars above prices should be watched as potential resistance on a bounce.

Price breaks above or below long Volume-by-Price bars can also be used as signals. A break above a long bar shows strength because demand was strong enough to overcome a supply overhang. Similarly, a break below a long bar shows weakness because supply was ample enough to overwhelm demand.

{% hint style="info" %}
**Learn More.** [Support and Resistance](/table-of-contents/chart-analysis/support-and-resistance.md)
{% endhint %}

### Nuances <a href="#nuances" id="nuances"></a>

Before looking at some examples, it is important to understand how Volume-by-Price works. Volume-by-Price can be used to identify current support or resistance. Current bars **should not be used to validate past support or resistance levels** because the indicator is based on all the price-volume data shown on the chart. This means six months of data for a chart that extends from January to June. Bars may appear to identify support in March, but remember that the indicator data extends well beyond March because the chart ends in June.

Chartists should also understand that big gaps can produce bars that equal zero. This makes sense because Volume-by-Price equals zero when there are no closing prices within a specific price zone.

<figure><img src="/files/JTIe7wVcKsRFiZv2mEtm" alt=""><figcaption></figcaption></figure>

### Identifying Support Using Volume-by-Price <a href="#how_do_you_identify_support_using_volume-by-price" id="how_do_you_identify_support_using_volume-by-price"></a>

The chart for Netflix (NFLX) shows Volume-by-Price identifying support around $95–$100 at the end of June. Notice that this is the longest bar. Also, notice that NFLX is beginning a pullback, so we can use Volume-by-Price to estimate support in the near future. The second chart shows NFLX with the yellow area marking Volume-by-Price support from the first chart. Support was expected in the 95–100 area, and the stock reversed here in late July. Notice that volume surged in August to validate the reversal off support.

<figure><img src="/files/LTtejkuK7GsslFgrAYxH" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/2nZYYdWTKlNXRHB4Rjpy" alt=""><figcaption></figcaption></figure>

### Identifying Resistance Using Volume-by-Price <a href="#how_do_you_identify_resistance_using_volume-by-price" id="how_do_you_identify_resistance_using_volume-by-price"></a>

The chart for TE Connectivity (TEL) shows Volume-by-Price identifying resistance around 26-26.5 in early August. Remember, the April break above this bar is not a breakout because the current Volume-by-Price calculation extends from January to early August. The second longest bar marks current resistance in the 26-26.5 area. TEL is at its make-or-break point, with prices near resistance. The second chart shows Volume-by-Price resistance from the first and the ultimate failure at resistance.

<figure><img src="/files/eKcljQqz1Xip9cDJox84" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/isk4RuhhldlYkl4tc0LC" alt=""><figcaption></figcaption></figure>

### Identifying Support Breaks <a href="#support_breaks" id="support_breaks"></a>

A break below a long Volume-by-Price bar signals increasing supply or selling pressure that can foreshadow lower prices. Long bars below prices show elevated interest areas and potential support. A break below this support zone signals a significant increase in selling pressure, and lower prices are expected.

The SanDisk (SNDK) chart shows a long Volume-by-Price bar marking support in the 39-43 area in mid-August. Also, notice that the stock forged at least three reaction lows around 42 from early July to mid-August. This support (demand) zone is clearly marked. The second chart shows SNDK breaking below the previously identified Volume-by-Price support zone with high volume. Demand crumbled, supply won the day and prices moved sharply lower.

<figure><img src="/files/sHqvKM8gwnc3jL8n81pF" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/Rz5VfAaBWkw6nqdj9akB" alt=""><figcaption></figcaption></figure>

### Identifying Resistance Breaks <a href="#resistance_breaks" id="resistance_breaks"></a>

A break above a long Volume-by-Price bar signals an increase in demand that can foreshadow higher prices. Long bars above prices mark supply overhangs that demand has not been able to overcome. A break above this resistance zone signals strengthening demand and higher prices are expected.

Sometimes chartists need to combine price action and Volume-by-Price to identify support zones and resistance zones. The McDonald's (MCD) chart shows a long bar marking overhead supply between 60 and 61. The stock also met resistance between 61 and 62 with reaction highs in late April and mid-June. For support, the second and third longest bars mark potential demand in the 57.5-58.5 area and the stock is near the late May low. Overall, a large [Symmetrical Triangle](/table-of-contents/chart-analysis/chart-patterns/symmetrical-triangle.md) could be forming on the price chart as MCD tries to hold above the late May low. The second chart shows MCD breaking resistance in July and surging to new highs in August.

<figure><img src="/files/1EIfF981Ih1BUpRpYaLb" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/doRQIpkIu9sds4yvJcml" alt=""><figcaption></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Volume-by-Price is best suited for identifying present or future support and resistance. The indicator marks potential support when prices are above a long bar and potential resistance when prices are below a long bar. Chartists can enhance their analysis by looking at the positive (green) and negative (red) volume within the Volume-by-Price bars. Long green portions reflect more demand that can further validate support. Long red portions reflect more supply that can further validate resistance. It is important to confirm Volume-by-Price findings with other indicators and analysis techniques. Momentum oscillators and chart patterns are good complements to this volume-based indicator.

{% hint style="info" %}
**Learn More.** [Momentum Oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) | [Chart Patterns](/table-of-contents/chart-analysis/chart-patterns.md)
{% endhint %}

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Volume-by-Price can be found in SharpCharts in the “overlays” section. Initially, the parameter box is empty, and the default value of 12 periods is used. Chartists can increase or decrease the default setting depending on the desired detail. Remember that Volume-by-Price is based on closing prices, which means highs and lows are omitted. This is why chartists may sometimes see a spike low or high without a Volume-by-Price bar. Volume-by-Price is one color when the “color volume” box is not checked and two-toned when this box is checked. Chartists can also use the advanced indicator settings to set the opacity. The example below shows Apple with 20-bar Volume-by-Price, colored volume, and 0.3 opacity.&#x20;

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here](https://stockcharts.com/sc3/ui/?s=AAPL\&p=D\&yr=0\&mn=6\&dy=0\&id=p03412996346\&listNum=30\&a=209159944) for a live example.

***

<figure><img src="/files/4oiBH5FvRrzoPNJc8nMB" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure Volume-by-Price overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#volume_by_price) in the Support Center.&#x20;
{% endhint %}

## Volume-by-Price FAQs <a href="#volume-by-price_faqs" id="volume-by-price_faqs"></a>

<details>

<summary>What does it mean when there's a gap in the Volume-by-Price bars?</summary>

Gaps can produce bars that equal zero. This occurs because the Volume-by-Price equals zero when there are no closing prices within a specific price zone.

</details>

<details>

<summary>How does Volume-by-Price help in understanding potential price movements?</summary>

Long Volume-by-Price bars beneath prices can indicate potential support during a price drop, while long bars above prices might indicate potential resistance during a price increase.

</details>

<details>

<summary>Are there nuances to be aware of when interpreting the Volume-by-Price indicator?</summary>

Yes. It's crucial to understand that the indicator is based on all the price-volume data shown on the chart. Therefore, it may not validate past support or resistance levels. Also, chartists should be aware that large gaps can produce zero bars.

</details>

<details>

<summary>How can chartists enhance their analysis using Volume-by-Price?</summary>

Chartists can look at the positive (green) and negative (red) volume within the Volume-by-Price bars. Furthermore, confirming Volume-by-Price findings with other indicators and analysis techniques, such as momentum oscillators and chart patterns, can provide a more holistic view.

</details>

<details>

<summary>Can you adjust the number of Volume-by-Price bars shown on StockCharts?</summary>

Yes, StockCharts shows twelve Volume-by-Price bars by default, but users can increase or decrease this number based on their preferences.

</details>

<details>

<summary>How can the Volume-by-Price be used for support and resistance?</summary>

Price zones with heavy volume indicate elevated interest levels that can influence future supply or demand, marking them as resistance or support. Breaks above or below long Volume-by-Price bars can also be seen as signals indicating strength or weakness.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-by-price.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
