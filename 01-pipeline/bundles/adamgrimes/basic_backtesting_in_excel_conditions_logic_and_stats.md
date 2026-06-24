# SOURCE: https://www.adamhgrimes.com/basic-backtesting-in-excel-conditions-logic-and-stats/


# Basic backtesting in Excel: Conditions, logic, and stats


#### AdamHGrimes

Pat yourself on the back if you've come this far in the little backtesting mini-course. After many posts, we've basically gotten data into a spreadsheet and calculated some moving averages. You probably aren't blown away by what we've accomplished, but think again: we've laid the foundation for doing some really good solid work, and have touched on some of the major issues you were likely to encounter along the way. We've done a lot more than you might think from that little spreadsheet, and now it's time to add a few more tools.

Make sure you have the spreadsheet as it stands in the pic at the end of the last post . (Yes, I could just upload it, but then you wouldn't do the work yourself!) If you have trouble following along today, check your starting point with that sheet.

Evaluating simple conditionsRemember the if statement? =IF(condition to test, show this if true, show this if false) We can use this in a cool way do some quick and dirty market stats. Let's say we want to know what percentage of the time the SPY is above the 20 period moving average. We put that test into the 'condition to test' field, and have the formula return a 1 if true and a zero if false. So, in cell I24, use this formula =IF(B21>G21,1,0) and copy it down to the bottom of the sheet. (B21 should be the SPY closing price for the day, not the return, and G21 is the 20 period MA of the closing prices.)

This column is now something we can call an indicator variable . Be clear that this is not "indicator" like technical analysis, but an indicator variable is a statistics tool that gives specific values if something is true or false. Since we are asking "what percentage of the time is close above the MA" then we can simply average this column, using the formula =AVERAGE(I:I) put anywhere in the sheet. The average formula ignores text or blank spaces, and this is why we have to give it a zero when the condition is false.

In this case, we should find that the close is above the 20 period MA 62.6% of the time. Your number might be a bit different if you have different dates in your sheet; mine goes from 8/1/05 - 10/19/15, but you should have roughly the same answer.

A note on references: cell references work with column/row format, e.g., D3, U61, AB3. Ranges are two cells with a colon between them: A1:A3 is a set of three cells in the column A. A1:Z26 is a 26X26 grid of cells. When we want to refer to entire columns, we use the format A:A, which means the entire column A. In general, you probably want to avoid those full column references, but they are a quick and dirty way to be sure you haven't missed something in the formula.


## Now, think

Were you surprised to find the close was above the average that much more than half the time? If so, think a bit more deeply on averages, and why it could be true that far more than half the prices are above a moving average. Would the answer be different for a moving median, or would some of the same reasons apply? You can test this too with the =MEDIAN() formula.

When you calculate basic stats take a minute and look at them and think about what you're seeing. Do they make sense or not? If they don't then trace your steps and see if you can find an error. Sometimes there may be no error, and the "problem" is with your perception and/or assumptions. Drilling down into these situations and thinking through the steps can be a really fantastic learning experience.

(As an aside, I wrote this short book, Quantitative Analysis of Market Data: a Primer , to help people think through these issues. This is a book that really is written for someone just beginning to grapple with the basics--it's a primer, so if you have a strong quantitative background there will probably not be anything new for you here. If you're more on the beginning steps of your journey, trying to think through issues and understand what data might mean, then I wrote this book for you. It's available for free in the Kindle Unlimited program, you also can get a free pdf of it if you sign up for my mailing list (upper right corner of my blog), or you can get a hardcopy. The hardcopy was my first experience with layout and book design, and I'm pretty pleased with how it turned out. Check it out if you like to hold a paper book in your hands!)

[box type="warning"] I made a simplification here that will cause you problems down the road. I tested for the condition "is above MA" and gave a 1 if true and a 0 if false. The problem with this is that there's a third condition: price can be EQUAL to the MA. To do this work correctly, we should not assume that the percentage of the time price is below the MA = (1 - percentage of time above). This is especially true if, for instance, we want to know how many times something closes up for the day/week/whatever; we need to account for the unch periods. There are a few ways to solve this, but probably the easiest is to do the "is above" test as I've shown it, and then do an "is below" in a separate column that specifically tests those conditions. Anything not caught in those two buckets is almost certainly equal to (or unch), but do check this assumption in all your work.[/box]


## More complex conditions

What if we want to test more complex conditions, such as asking how many times the S&P 500 is up two days in a row? Excel provides the AND(), OR(), and NOT() formula (and an XOR() formula in the newest version of Excel.) These tools allow you to apply logic to basically construct any test you want. Very complex tests and conditions are essentially built from AND, OR, and NOT evaluations; if you've never worked with simple logical conditions before, it's easy to underestimate their power.

In this case, there are few ways we can answer the question, and it also depends a bit on style. How deeply do you want to nest conditions in your formulas? One way to do this would be to put this formula in any cell in row 21 =IF(AND(B21>B20,B20>B19),1,0); make sure you understand what that formula does and how it works, and see that the AND() lives inside the condition part of the if formula. If this is all new to you, make sure you understand why every () and , is where it is-- everything matters.

Play with this idea for a few days, and experiment with different ways to solve the problem. It would be nice to have some way to generalize the formula, so we can test for N days up (or down). There are ways to do this, but you could look into the OFFSET() function to start.

You learn by doing. It's not enough to read some posts or look at some examples; the only way to build competence is by manipulating the program, making mistakes, getting confused, and working through those tough spots. Do this, and you'll be well on your way to having a good skill set to do some basic market analysis.

The next post will be important, so make sure you're comfortable with everything in this post before you move on.