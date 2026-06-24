# SOURCE: https://www.adamhgrimes.com/basic-backtesting-in-excel-more-data/


# Basic backtesting in Excel: More data


#### AdamHGrimes

Today, we will add another data series to our file we created yesterday that had daily SPY data in it. It's not quite as simple as pasting the new data into the sheet; we need to make sure they line up correctly. Tomorrow, we will take a little break from pounding in data and consider a few issues with different data series and also some pointers on learning to use Excel well.


## More data

- Open your SPY.xlsx file you created yesterday. If you don't have that file, it's simply a two column spreadsheet with dates (oldest to newest at bottom) in column A and SPY closing prices in column B, with a header row that is labeled "Date, Close" for those two columns. You also should have a .csv of TLT daily data, downloaded from Yahoo! Finance.

- Open the TLT.csv file, as well.

- So now we need to pull data in from the TLT sheet into the SPY sheet. When you start combining datasets on one sheet, things can get confusing quickly, so you need a naming convention to keep things separate. Because I tend to move data from Excel to Stata to do some types of analyses, I use a convention that is "TICKER_DATAELEMENT", so I will change the label in cell B1 to read "SPY_C". It doesn't matter how you name things, as long as you are utterly consistent so you can figure out what you did if you come back to this sheet years later. In the SPY.xlsx sheet, change B1 to read "SPY_C" or whatever you'd like to use. Since we are going to put TLT data into this sheet, put "TLT_C" in cell C2.

- Now we need to use a VLOOKUP to match the old data to the new data based on date. Let's do it first, then I'll explain. Type this =VLOOKUP(A2,tlt.csv!$A:$G,5,0) into cell C2 and you will get... an error ("#N/A" is one of Excel's error messages), but that's ok for now. (The = at the beginning of the cell says to Excel "this cell is going to include a formula or another calculation, rather than a simple value, so get ready to do something here. All Excel formulas begin with the =, otherwise you are entering static values. Try entering "2+2" into a cell and then "=2+2" to see the difference.)

- You now need to copy C2 all the way down to the end of the data. There are at least two ways to do this. 1) You can double click the little dark "dot" in the lower right hand corner of the selection box when you have C2 selected. That's quick and easy, but more old school is a keyboard combination: use arrow keys to make sure C2 is selected. Type Control-C. Left Arrow. Hold down control and tap down arrow (release both). Right arrow. Hold down control, hold down shift, tap up arrow and release all keys. Then tap control-V. I realize that seems like a lot, but with a little practice you can probably do it three times in a single second. Ctrl-C and Ctrl-V are the shortcuts for copy and paste, respectively, and the combination also includes some selection magic with the arrow keys. If this is all new to you, spend some time figuring out what that key combination does and why, and you'll have begun to understand some important things about using keys with Excel.

- Spend a few moments understanding what vlookup does. I won't explain it here in detail, since using Google to understand Excel functions is also a legitimate and important skill. Google "Vlookup Excel" to get started, and make sure you understand, for instance, why the ,5, is in the function above. (Hint: it has to do with how your TLT file is laid out.) The only thing that might not be immediately obvious is the ,0 at the end, and this is just telling Excel that we require an exact match on the dates.

- Ok, now scroll around your data and look and you will see that we have errors near the top and numbers near the bottom for TLT. This is simply because TLT doesn't have price history going that far back, and this is why we had the errors in step 5. Let's deal with the errors.

- There are a few ways to manage the errors, depending on your data and what you want to do. Leaving the error message as-is is not bad at first, but it's visually offensive, so let's replace it with a "." to show missing data. In cell C2, modify the formula to read:" =IF(ISERROR(VLOOKUP(A2,tlt.csv!$A:$G,5,0)),".",VLOOKUP(A2,tlt.csv!$A:$G,5,0)) and you will see the error disappear and be replaced by a .

- Now let's copy this formula down the column. Since the column is full, we have the option of using a slightly simpler keyboard series: make sure C2 is selected. Tap ctrl-C. Hold down shift and control, tap down arrow, release all. Tap Ctrl-V. Again, make sure you understand what each piece of that does and why we could not have used that simpler combination earlier. Another option is to click the handle at the lower right of the selection box around C2, but I strongly encourage you to learn to love the keyboard shortcuts!

- We're going to discuss the errors a bit at the end of this post, but let's do one more thing. Column C is now "live", meaning that any changes in the TLT.CSV file will fall through to the SPY sheet. (Go try it. Change a closing price for TLT in the TLT.CSV sheet and see the same change automatically happen in the SPY sheet.) This can be a good or a bad thing, but we might delete the TLT file or might not always want to have it open. As a last step, we should take these live formulas and nail them down to simple values, as if you had just typed them in by hand. Here's how to do that: Select the whole data range for column C. There are a few ways to do this, but the best is probably to navigate to C1 (use control and the arrow keys!), then hold down shift and tap ctrl-down arrow to select the column's data. (Selecting the whole column by clicking on the C label box is not a good idea for memory reasons with some versions of Excel. That's a sloppy shortcut--don't do it!) Type Ctrl-C to copy the data range. You should see the "marching ants" selection box telling you that this will be copied. Now for probably the most useful Excel key combination: paste-special values. If we simply paste (which you know how to do with control-V!), we will paste the formulas and everything exactly as we copied them. Sometimes that's great, but it's not what we want here. So do this: Alt-E (release), tap S, tap V, Enter. That's the keyboard combination that says to paste the values instead of the formulas, and you'll end up using it a lot.

- Select the whole data range for column C. There are a few ways to do this, but the best is probably to navigate to C1 (use control and the arrow keys!), then hold down shift and tap ctrl-down arrow to select the column's data. (Selecting the whole column by clicking on the C label box is not a good idea for memory reasons with some versions of Excel. That's a sloppy shortcut--don't do it!)

- Type Ctrl-C to copy the data range. You should see the "marching ants" selection box telling you that this will be copied.

- Now for probably the most useful Excel key combination: paste-special values. If we simply paste (which you know how to do with control-V!), we will paste the formulas and everything exactly as we copied them. Sometimes that's great, but it's not what we want here. So do this: Alt-E (release), tap S, tap V, Enter. That's the keyboard combination that says to paste the values instead of the formulas, and you'll end up using it a lot.

- Save the SPY. xlsx file. We will be using it tomorrow.