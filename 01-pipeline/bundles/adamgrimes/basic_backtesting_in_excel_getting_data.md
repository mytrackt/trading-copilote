# SOURCE: https://www.adamhgrimes.com/basic-backtesting-in-excel-getting-data/


# Basic backtesting in Excel: Getting data


#### AdamHGrimes

Continuing from yesterday's post , let's roll up our sleeves and get into the process of managing data in Excel. The purpose of this short series of posts is to give you tools to look into the market's motions and begin to tease out some tendencies and possible trading edges. This is important work and you can probably get excited about finding those trading edges, but it's hard to get excited about data! If you don't have good data, everything else you do is likely to be a waste of time, so spend some time considering the issues here before you begin.

The biggest decision you need to make is whether you need to update the data. For most applications, the answer is eventually yes, but you can get away at the beginning working with static sets of historical data. Storage space is not an issue given the price of hard drives and cloud storage, but be aware that intraday data, especially tick data, can take up a lot of room. One of the limitations of Excel is that you're basically limited to about a million datapoints; this might not seem to be an issue--a full year of 1 minute data for the New York session is about 98,280 bars. Even including pre and post market data for many instruments, you could cram several years of 1 minute data into Excel. No problem, right?

Well, keep in mind that some instruments (currencies) trade more or less 24 hours, but the real problem is that Excel becomes very, very, very slow and subject to crashes with large datasets. If you do a multistep calculation and don't give Excel time to finish each step, you will be provided with a partial and very wrong answer, so be careful.

There are a lot of other issues that traditional chartists don't consider and aren't even aware of. (In fact, leaning about these issues drove me away from charting and traditional TA, but that's another post.) How do you back-adjust futures? How do you back-adjust stocks for splits, dividends, reissues and other corporate actions? How do you deal with currency issues for non-USD instruments? How often is fundamental or economic data restated and modified and how do you manage it? There's more than one answer to each of those questions (and there are many more questions), but the answers do matter. My advice, if you're just getting started, is to ignore those issues at first and concentrate on the mechanics of making Excel dance for you. However, come back to those issues soon, and make sure you understand the choices you make. Now, about getting Excel to dance...


## Sources of data

I'd like to point you to two sources of free data. Yahoo! Finance is the traditional first stop for people crunching numbers, and I'll show you how to get data from Yahoo into Excel today. However, you also need to know about Quandl --a superb source, with a pile of free data and many interesting datasets. If you want to look at economic numbers, Fred (the Federal Reserve Bank of St. Louis), is a good place to start. If you're looking for intraday data, you'll probably have to pay for it, and there are a number of data vendors who do a good job.


## Getting daily data into Excel from Yahoo!

Let's get daily closing data for the last 10 years for SPY into an Excel spreadsheet; that's a pretty good start for the first day, so let's go step by step.

- Go to Yahoo! Finance , and type SPY in the quote lookup window.

- Check your dates, and click on "Get Prices." Scroll all the way down to the bottom of the window and click on "Download to Spreadsheet." Depending on your browser, you will probably find a spreadsheet named Table.csv in your download folder. Go rename it to SPY.csv.

- Open SPY.csv in Excel. On many systems, you simply double click the file, but you might have to open Excel and navigate to the file from the Open window. Once you've opened it, you should see something that looks like this:

- Take a moment to make sure you understand what you are seeing here. Excel works so that each cell has an address. You can see the address labels outside the spreadsheet, labeled A,B,C... across (columns), and 1,2,3... down (rows). This dataset has its own set of labels, which occupy row 1 on the spreadsheet. Most datasets do, and you might consider adding them if you get data from a source that does not label the columns. Each row represents a "bar" (day, in this case), and each column represents a different attribute for that bar. We could have many columns stretching to the right of the sheet, each one being a different datapoint for the day. Today, let's keep it simple. Notice we can't read the "Date" column? Let's fix that.

- I'm going to teach you some keyboard shortcuts, and they are worth your time to learn. Working with the keyboard shortcuts is a lot (maybe 4 or 5) times faster than using a mouse, so little repetitive actions can add up to a real time savings. First, use the arrow keys to make sure a cell in the first column is selected. (Control-arrow keys take you to that edge of the data. Try that: hold down control and type left arrow, then down arrow. You've now gone to the end of the data (unless you were outside the data when you started, in which case you've gone to the edge of the sheet (= max possible data range.)) Tap control left arrow twice and then control up arrow twice, and this should assure you that you have cell A1 selected, as in the picture above.

- Now, let's resize that column so we can read the dates. Type control-space bar to select the whole A column. If you need to select a row, the keyboard shortcut is shift-space bar. (Again, I'm only showing you a handful of keyboard shortcuts, but they are well worth memorizing.) Any time the data is too wide to fit a column, Excel will spit out a bunch of #####'s. We generally want to fix these, so follow this procedure any time you see a cell full of number signs: select the column (which you just did), and then type Alt-O-C-A. The way you do this is to hold down Alt and then press O (letter, not number). Release both, and then type C, release, and then type A. The column will automatically resize to fit the data, and we can now read the dates, but we have another problem.

- You need to make some decisions whether you want time to flow up or down in your spreadsheets. To me, down is the only thing that makes sense (new data at the bottom), but Yahoo!, for whatever reason, does it the other way. If using Yahoo! data, the first thing I need to do is to sort the data by the date field. First select all the data by typing control-A. (If you want to select the whole sheet, including empty cells, type control-A again, but don't do that now.) So far, I think you need to memorize the shortcuts, but here's one you might not need to memorize. Let's sort the data by typing alt-D-S (alt, then D, then release them both and tap S), or select it from the menu above (Data, Sort). Make sure you have "My data has headers" selected (because it does), and then fill in the boxes to sort by date descending, from oldest to newest.

- We're getting there, so let's just clean up a few things. Select the B column (Open); you know how to do this: use the arrow keys to navigate to any cell in that column, tap control-space bar and notice the whole column is selected. Now, if you hold down shift and press the right arrow, you will find the C column is also selected. (Holding down shift while moving around a sheet stretches the selection. Play with it and you will see.) Select columns B, C, and D this way (Open, High, Low), and then delete those columns with alt-E-D (hold down alt, type E, release both, and then tap D).

- If you ever want to undo anything in Excel, control-Z will undo any action, but you don't need that now. You will in the future, so remember that "undo" shortcut.

- Now, delete the Volume and Adj Close columns, so you are left with only Date and Close fields.

- Save the sheet as a new copy under a new name and type. F12 brings up the "save as" menu. Select "Excel Workbook (*.xlsx)" from the Save as type field, and then hit Save. You're done and the sheet should look like this.

This may not seem like much, but if this is your first time working with Excel and price data, it's a pretty good start. Those keyboard shortcuts and useful and are well worth remembering. I would suggest you go back to the beginning of this post and work through it again, reading as you go along. Then do it again without reading. Then do it at least four or five more times on other price sets from Yahoo!. A lot of this really is muscle memory, and you'll probably be surprised how quickly you pick it up. Do it, don't just read about doing it.

That's enough for today. Tomorrow we will add TLT data to this spreadsheet, and take our first steps toward doing a little analysis.