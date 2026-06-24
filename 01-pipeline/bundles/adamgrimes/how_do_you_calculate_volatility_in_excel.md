# SOURCE: https://www.adamhgrimes.com/how-do-you-calculate-volatility-in-excel/


# How Do You Calculate Volatility In Excel?

How to calculate a simple historical volatility using Microsoft Excel.


#### AdamHGrimes

[dc]I[/dc] received a question from a reader who asked, "Can you calculate volatility in Excel?" The answer is, yes you can, but there are a few things you need to know. Without going into too much detail here, there are many ways to calculate volatility. Two of the most common measures are implied and historical (also called realized or statistical) volatility. It is fairly simple to calculate historical volatility in excel, and I will show you how in this post. Calculating implied is quite a bit more complicated. You technically can do it in excel, but you have to impute it from an option price. In addition, there's actually a volatility surface , or different values of implieds for different strike prices and maturities. That's a topic for another day; today let's just look at how to calculate a simple historical volatility in Excel.

- Collect your raw data, in the form of a closing price for each time period. Many people do not know, but Yahoo Finance is a good source of daily data that can be downloaded into a spreadsheet. ( See this example for SPY.) Your data will likely include other data points such as high, low, volume, etc, but just ignore everything except the close.

2. The first step is to convert the prices into a return series . Again, let's not dig too deeply into the theory in this post, but prices are somewhat arbitrary. Is a $50 price a change a lot? Well, that depends on the price of the asset and how much prices usually change. Converting to returns is nothing more than changing the price series into a series of percentage changes. This is the first step in nearly all quantitative or mathematical market analysis. In Excel, start at the second price from the top in your series (assuming closing prices are in a column with the newest price at the bottom). In the cell to the right of prices, divide the second price by the first and subtract one, as in the pic. Copy this formula down the entire column.

3. Next, find the standard deviation of the returns. The formula for standard deviation in Excel is =STDEV(...), and takes a range of prices as an input. In the graphic, I have calculated a 10 day standard deviation of prices, but that is for the illustration only. Set your window to whatever time period you want to evaluate, and, again, copy the formula down. Twenty days is a good starting point if you haven't done this analysis before.

4. So far, the procedure has been straightforward: calculate a return series, and then calculate the standard deviation of that series. There is one more step, which is perhaps the only part of this that is conceptually a little bit complicated. You have calculated the standard deviation of the returns for whatever the time interval of your data is. If you have daily data, you have calculated a daily standard deviation, and so on for hourly, weekly or any period. Historical volatility is the annualized standard deviation of returns. We must multiple the standard deviation by an annualization factor , which is the square root of how ever many of your periods are in a year. This example is daily data; there are 262 trading days in a year, so we multiply the standard deviation by SQRT(262). If you are using weekly data, the annualization factor is SQRT(52), etc.

This is one example, but a slightly more complex example, with graphs, can be found step by step on the tabs in this spreadsheet . We will consider exactly what this measure of volatility is, what it does, what we can do with it, and, even more importantly, what's wrong with it in a future post.

Edit: This sheet and article use an annualization factor of 262. There is some debate over what number to use here, but you'll see it doesn't really make much of a difference. 252 is probably the most accurate number (and is what I use in my calculations now), but, as long as you're consistent in your calculations, the actual number doesn't really matter.