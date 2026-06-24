# SOURCE: https://www.adamhgrimes.com/understanding-returns/


# Gains and losses: understanding returns in assets and trading accounts


#### AdamHGrimes

One of my readers, Anthony, sent me a good question about doing some statistical analysis on stock indexes. I think there are some important lessons here. Here's the question

Just so you know where we're going this week, here are the lessons we can tease out of Anthony's question:

- Understanding how returns compound.

- Doing the TLAR test as a first check to statistical analysis.

- Thinking about how stable a market pattern might (or might not) be.


## Net and gross returns

First, a definition: when we talk about returns , we are simply talking about percent changes, in most cases. (There are other kinds of returns, and if you read finance research you'll run into continuously compounded returns soon enough, but for the sake of this blog post a return is a percent change.) This is a term that, for whatever reason, is not common in technical analysis, but it's absolutely fundamental to any mathematical thinking about markets: a return is a percent change.

Let's go one step further and grab another definition. Returns can apply to market data, to your checking account, to your trading account, or to any other amount. If you make 10% on your trading account that is your net return on the account, but you end up with 110% of the money you started with. This 110% is your gross return . The relationship between net and gross returns is simply this:

Gross return = Net return + 1.0

With those definitions, we can go a little further.


## "Adding" returns

Now, here's an important quiz (and don't read ahead.) Let's say you have a trading account that experiences a 50% net (all-in, including transactions costs) loss. Next, you make 50% net back. Do you have: a) more money than when you started, b) the same amount of money (back to breakeven), or c) less money than when you started? Think about the answer carefully before you check yourself. The answer follows in white on white text, so highlight from here ==>

<== to here to read the answer.

The reason this is true is that you cannot add simple (percent) returns. The correct math is that you have to 1) add 1.0 to get the gross return and 2) then you multiply the gross returns together. In the example above: (1 + 50%) * (1 - 50%) = 1.50 * 0.50 = 75%. One last detail: this 75% is a gross return, so we can subtract 1.0 from it to find that we had a net return of -25% in this example.

So, in general, we can find the total return by multiplying gross returns together. This generalizes to any number of returns we wish to "add" together. Note that the "add" in the section header was deliberately misleading and now you should know, clearly, that we cannot add returns together. The right math is:

Total gross return = Gross return for period 1 * Gross return for period 2 * ...


## Compounding returns

If two returns are the same, multiplying them together is the same as squaring them or raising them to the power of 2. If we wanted to multiply five of the same returns together, it would be the same as raising them to the fifth power. This is compounding returns . For instance, if we have an investment that returns exactly 2.0% every day without any variation, at the end of five days we would have a net return of 10.408%. In general, the math is:

Compound net return = ( (1 + net return) ^ number of periods) - 1

Working with investments, we often have situations where we want to annualize a return. If we have daily returns, there are 252 trading days in a year, so we simply work the formula above. If we earn 1% a day, we'll end up with a nice 1,127.4% return for the year. If we are not working with daily returns, then the correct annualization factor is simply the number of the periods under consideration that make up a year. For instance, we would annualize a 1% weekly return to 67.8% (1.01 ^ 52 - 1) and a 1% monthly return to 12.7%.


## Does this matter? Do you need to know this?

Yes, I think this matters a lot. It's not exciting and but understanding this math is important for understanding how financial markets grow and move and also for how your trading account will respond to gains and losses. As an aside, I've seen a lot of perplexing errors on this front over the years. I gave a formula for calculating a measure of volatility changes in a market, and stumbled upon an extensive discussion on a very active trading board where a guru was trying to unfold what I meant. He came to the conclusion that I was hiding the good, secret sauce, but it was simply because he (and, in fairness, the 50 other people involved in that thread) did not know what a return was. I have seen a CMT-type person, who writes with great authority on the importance of the math behind the sacred Fibonacci ratios, not understand that a 10% gain one trade does not get you back to breakeven after a 10% loss on another trade. If you understand this so, but very important math, you'll find lots of errors like this on your own, and will develop even more respect for drawdowns and volatility!

Now, equipped with this knowledge, we're ready to tackle Anthony's question. He gives two returns in his question and is skeptical that the 20 day return might be "too good to be true." Is he asking the right question?