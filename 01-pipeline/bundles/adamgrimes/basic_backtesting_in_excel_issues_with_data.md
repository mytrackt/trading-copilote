# SOURCE: https://www.adamhgrimes.com/basic-backtesting-in-excel-issues-with-data/


# Basic backtesting in Excel: issues with data


#### AdamHGrimes

If you've been following along with the short Excel course , you've created a spreadsheet using SPY daily data, and added daily TLT data to the sheet in another column. I received a few questions about why we needed to match the two series with a VLOOKUP instead of simply pasting the data into another column. Answering that question leads us to considering some other issues about market data, so this is a good time to take a day or two to think about those issues.

You might think this should be simple, and perhaps you're right--markets trade, prices are published, and we should be able to just look at those past prices and call it a day. In reality, it's a lot more complicated, and it's not unusual to find, for instance, academic researchers spending the vast majority of their time dealing with data issues. (Some researchers estimate that 85% of their time is spent on mundane data tasks.) Let's look at some of those issues so we can better understand what can go wrong when working with market data.

These errors fall into two categories. One we could call "problems" rather than errors because no mistake has been made in the recording or transmission of the data. The other category is these actual errors, and we should look at how to catch some of the more common actual errors as well. The "problems" are instructive, so let's start there.


## Problems with data that are not errors

The most obvious reason we needed the VLOOKUP is that not everything trades every day. For instance, if we were matching foreign currencies with a US-listed stock, the currency will have traded many days that the US stock market was closed. If we were to simply paste the data series together, we'd find one has "missing dates" which were dates the exchange was closed. VLOOKUP fixes this problem, but makes us vulnerable to another.

Another, very serious, issue is asynchronous trading, which means that you may be looking at datapoints that, while they bear the same time stamp, did not happen at the same time. A good example on daily data might be Brent crude and WTI; if you're using end of session prices for both, they probably didn't happen at the same time. How about US stocks and European stocks? If you compare end of session quotes, the US stocks are probably from 16:00 EDT, while the European close was many hours earlier. If you create a trading strategy based on a relationship, you won't be able to execute one leg of the spread.

This is also a serious problem with intraday data, and particularly when mixing data from many sources. Some bars are timestamped at the beginning of the bar, some at the end. Which are yours? How about if you are comparing intraday data from an active stock and from one that does not trade for many minutes? The active stock will show a price change, while the less active stock will display the same price. Again, there's a spread relationship here that is only an illusion, as the bid ask spread for the less active stock will likely have moved (and here's your solution to that particular problem.)

Let's not even get into the issues of back-adjusting data for futures rolls or stock corporate actions. There are established methodologies for doing these things, and they work--but they have to be done properly. (Also, too many naive technical analysts have no idea what these issues are or what their charts actually show. The more I learned about these issues, the less I trusted "levels" and many traditional chart formations.)


## Actual data issues

Now let's consider the actual issues, and they are legion. You might also think that paying for data would fix these problems, but you will find issues even in data purchased from commercial vendors. Some of the favorites to watch for:

- Missing entries

- Entries that display the same price (e.g., seeing a string of 5 minute bars in the ES futures that show the same prices.)

- H = L = C in an active market (not likely)

- H < L or L > H. Some errors are obvious, but you have to look for them. This little gem is not so easy to find when you have 40,000 datapoints.

- Missing or incorrectly placed decimals. The way to check for this is to look for very large price changes. For instance, seeing a change of +/- 1000% in 1 minute bars would be, shall we say, unlikely, and probably points to an error.

- Volume or open interest data with errors.

- Missing data points. (Example: a high price missing for a random bar. It happens.)

The list goes on, but you need to be aware of these issues and you need to have some way to check for them. I'm not going to focus too much on data issues in this short series, but I thought these serious issues--and they are serious because they can create completely misleading tests and destroy a lot of your time work--I thought these issues deserved our respect and some attention.

Tomorrow we will get into the fun stuff and start to do calculations with the data that we now have in our spreadsheet.