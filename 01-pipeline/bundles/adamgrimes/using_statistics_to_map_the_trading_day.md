# SOURCE: https://www.adamhgrimes.com/using-statistics-to-map-the-trading-day/


# Using statistics to map the trading day


#### AdamHGrimes

This will be a very quick blog, as I'm just typing a few thoughts here in the first few minutes of what might be a volatile trading day.

This morning, I noticed an extreme negative NYSE TICK reading on the open, and ran some quick stats.

- The low of today's TICK in the first minute of the trading day was -1309. Quick stats on 1 minute TICK bars back to 1997 (2.2 million observations... so you can't do this kind of work in Excel!) show an average of -37 for the first minute with a stdev of 446. Percentiles break out at 25% = -177, 10% = -532 5% = -885 and 1% = -1318. So we are very close to the 1st percentile.

- Looking at all days this extreme or lower, (only 44 trading days), we find they close up from the previous close only 18% of the time. This is not surprising since we can expect these large negative TICK readings are driven by gaps down... unlikely to recover those completely... however...

- Only 34% of the days closed up from the open! That is a significant number and probably an edge for today. Average loss from the open was -0.41% to close, but that's deceptive... stdev is 1.24, so there have been a wide range of volatile outcomes.

- If you're wondering (and I hope you were), all days closed up from the open 53% of the time, with an average gain of 0.02% and a stdev of 1.15%.

Just some stats to think about as the day unfolds...