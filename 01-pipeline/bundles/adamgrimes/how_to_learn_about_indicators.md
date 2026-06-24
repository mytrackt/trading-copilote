# SOURCE: https://www.adamhgrimes.com/how-to-learn-about-indicators/


# How to learn about indicators


#### AdamHGrimes

This weekend, a reader, Paul, asked:

We had some discussion around this topic, but I think the answers really point to a deeper way of understanding indicators.

In my first book , I showed a way to look at moving averages and the MACD that, to my knowledge, no one had put in print. Too often, someone begins "teaching" by showing "setups" on the indicator: sell when this line crosses. Buy when this line goes into this zone. Watch the slope of this line to get a feel (what?) for the trend. Watch for divergence between price and this line.

Most people teaching indicators like this don't even understand what the tool is measuring. For instance, what does "divergence" really mean? How can divergence set up? Does it depend on the length of the move or the magnitude? What is it really comparing? If we know the answers to those questions, we can begin to ask if it even makes sense to trade based on divergence, but, far too often, these questions are never asked.

The essence of my way of looking at indicators includes three big steps: 1) understand how the indicator is calculated. 2) understand how the indicator responds to changes in the data. 3) understand what this means on market data. From these understandings, we can think about how (and if!) we should use the tool in our trading.


## The procedure

If you really want to understand indicators, the best way is to do the work yourself. No one has put the information you need in print. You can be sure that most of the "traders" you are talking to in online forums, no matter how confident they appear, do not have the answers you want. It's even possible the developer of the tool did not really understand what he had created or how it worked. (If you doubt the truth of that statement, a little research will show you that many of the developers of the standard technical analysis indicators did not trade profitably themselves. There are several interviews in which a few of the much-revered developers of these tools made this admission decades later--that the books they published were the only money they ever saw from the tool. Perhaps we should regard these tools from a default stance of skepticism?)

If you really want to understand an indicator, do this:

- While not strictly relevant, it’s a good idea to start with understanding the history of the indicator. Who invented it? Who changed it? When? What computing power was available to them? Carefully read contemporary source documents (e.g., the first book where the tool was mentioned, magazine articles, etc.) for crumbs of information.

- What is the one key idea behind the indicator? In other words, why might it be better to look at this calculation than to look at raw price charts?

- How much overlap is there with other indicators? This might not be so easy to answer, depending on your knowledge of other indicators, and you don’t have to dig too deeply to answer this. Just be aware of glaring similarities to other indicators.

- Exactly how is the indicator calculated ? Ok, this step is where the real work begins. You should probably be able to explain the calculation in bullet points, and then I would suggest coding the indicator from scratch. An Excel worksheet is ideal for this, even if the calculation requires several columns. The goal is for you to be able to explain the details of the calculation to a smart twelve-year-old child—if you can’t do that you do not really understand it. (Coding in Python or R is another possibility, but be careful of proprietary languages such as TradeStation EasyLanguage or coding in NinjaTrader. These proprietary languages may do some of the work for you that you should be doing yourself.)

- Feed the indicator controlled data that you construct so you can see how it reacts to controlled changes in price. Examples would be: a flat market that begins to trend, then reverts to flat; play with the magnitude of the trend and the timing of both inflections; flat price series with a single, large price spike; “stairstep” markets; trends with inflections to different steady state trends; oscillations (e.g., sine wave) of different periods; constant growth rate trends vs. linear trends.

- Take the knowledge you have gained so far, and look at the indicator on price charts . Notice how it responds to inflections in price. Consider this an information gathering stage; your goal is to see the indicator on a lot of data, rather than digging deeply.

- Now figure out how you can test what you think you see in #6. These tests may be manual backtests, or they may be coded.

- Decide what place, if any, the indicator has in your trading.

Consider how different this is from the procedure usually recommended: “just slap the indicator on your chart and make some trades when the lines do ______.”

This is difficult work, and it will take considerable time. If you do it right, it will take days or weeks (not hours) to understand a single indicator.

On the other hand, you will have understanding that you can get no other way--you'll know things that other traders simply do not know. You will grok the indicator!

You may decide to use it or discard it, but you will do so from a position of knowledge and strength. Who knows, you might also learn something about the market in the process!