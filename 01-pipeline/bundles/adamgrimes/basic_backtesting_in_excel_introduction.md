# SOURCE: https://www.adamhgrimes.com/basic-backtesting-in-excel-introduction/


# Basic backtesting in Excel: Introduction


#### AdamHGrimes

I've received many questions about how to do basic backtesting in Excel. I think I wrote in my book that we all have a love/hate relationship with Excel: it's a good way to do some quick and dirty tests, it is on practically every computer you're likely to come across, but it has some limitations. However, the learning curve is pretty short so you can be up and running basic tests quickly, so it's often the first introduction to data analysis for developing traders.

Why use Excel? Well, first, as I just wrote, it's everywhere. You can do your basic data analysis on any computer without a lot of setup. It's also a good way to visualize data and relationships, at least at first. If you are new to this, the idea of seeing data in aligned rows and columns, with additional calculations referring to other data elements and leading to calculated results that are then tabulated--this flow can help you build solid intuition for the process.

I also strongly believe that traders should understand any tool they use, to a very deep level. At a bare minimum, if you use some indicator (e.g., stochastics or MACD), then you should be able to calculate it. Forcing yourself to go through the process of doing the indicator calculation stage-by-stage in Excel will make you think about what the indicator does and how it does it. Many new traders treat indicators as magic lines and "buy when the lines cross", but you need to understand exactly what is being measured. Once you do understand, you'll be a lot more skeptical, and, perhaps, a few steps further down the path to enlightenment.

Though there are convincing reasons to use Excel, we should think about the limitations before we begin.


## Limitations

It's probably worth taking a few moments to think about the limitations of using Excel. Excel is not really designed for data analysis, so you certainly may find yourself stretching the tool to its limits. Excel can be slow and can have some frustrating crashes. The built-in statistics are sorta adequate, but you may find yourself wanting more. These are issues that are to be expected when we are pushing a tool to do something slightly outside its design specs, but, to my mind, there are three deeper concerns.

First, Excel will do nothing to protect you from yourself. You want to write a system that says "buy today if the market will be higher a week from today"? Excel will happily let you refer to data from the future that you could not have known at the time. Even the tiniest amount of "data leakage" like this will completely invalidate your test, so you must be very careful. (I wrote a post on this concept here .) I know you're thinking you will just have to be very careful, but, do enough testing in Excel, and you'll eventually make this error. Your first line of defense is to realize that something that seems too good to be true is not true--tests that suffer from this error always appear fantastic, but, without a working crystal ball, you're going to be out of luck in real time.

Second, complicated trading rules quickly become very complicated in Excel . I'm going to show you how to calculate simple measures based on price, how to trigger trading rules, and how to calculate some basic stats, and we're going to do it all right in Excel. However, you'll quickly find this isn't the best way to do things. A (very slightly) better way is to code things in VBA in Excel, where you can deal with more complicated relationships and trading rules much more easily. However, once you've done that, you've taken the first real steps toward legitimately coding your tests, and then a language like Python or R probably makes more sense than VBA. Just realize that what I'm showing you in this series of posts is only the beginning.

Third, managing data in Excel can really suck. That's the best way I can say it without using a pile of four letter words. If you want to create a static database of historical prices and run tests on them, that's not so hard to do in Excel, but if you want to update those price records and keep a real database... well, you need a real database.

The bottom line is this: Excel is a good introduction, a "gateway" tool, if you will. Though you can do most things in Excel, most things are better done elsewhere. When you find yourself struggling down the road, it might be time to make the leap to another testing platform, but this is a series of posts on how to do backtesting in Excel. :)


## The plan

Here's a quick snapshot of where we are going this week

- Getting data and getting it into Excel. We can't really do anything unless we have data to look at, so this is a good first step. It's also a step that is often underestimated--if you get serious about testing, you are likely to find that much of your life becomes wrapped up in managing, massaging, updating, or otherwise wrangling data.

- Calculating basic measures. I'll show you how to calculate a moving average or other measures based on price. We will also look at calculation relationships between two markets, and you can use these ideas as a departure point from which to calculate your own favorite tools.

- Triggering trading rules. Here's where the rubber meets the road: we'll look at how to calculate simple buy/sell signals and how to apply logical rules to your tests.

- Calculating basic stats: Last, I'll show you how to scrape up the results from your test, and how to see if there might be an edge to your trading signal.

All you need to follow along with these posts is a working copy of Excel (any version should work) and some time to play with a few numbers. We'll get started with data tomorrow.