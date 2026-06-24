# SOURCE: https://ninjatrader.com/futures/blogs/ninjascript-best-practices/

- Home

- Futures

- Blogs

- Best Practices for NinjaScript: Clean Code, Maintainability, and Performance


# Best Practices for NinjaScript: Clean Code, Maintainability, and Performance

By NinjaTrader Team

January 15, 2026

Are you writing custom strategies and indicators in NinjaTrader? If so, learning to code smarter with NinjaScript can help you avoid common mishaps, improve performance, and get more out of your trading ideas. Whether you’ve been writing NinjaScript for a while or you’re just starting to build your own tools, following some key best practices can make a huge difference.

From setting up your scripts the right way to knowing when to access market data, these tips are all about writing clean, efficient code that works the way you expect it to. Let’s break it down.


## Why best practices matter

NinjaScript is powerful, but it’s also event-driven and multi-threaded, which means your code is constantly reacting to the market, the platform, and user actions. If your script isn’t written with this in mind, you might run into bugs, slowdowns, and unpredictable behavior. That’s why it’s so important to write with the NinjaScript lifecycle in mind.


### 1. Know the NinjaScript lifecycle

When NinjaTrader loads your script, it moves through different “states,” and each one has a specific purpose. You’ll use OnStateChange() to tell the platform what to do in each state.

Here are a few key ones to remember:

- SetDefaults: Where you define the default properties for NinjaScript, like plot colors or calculation mode

- Configure: Where you add data series or set up custom settings

- DataLoaded: Where it’s safe to work with objects that depend on market data, like indicators, instruments, and bars

- Historical and Realtime: These states allow you to trigger specific logic depending on whether your script is processing historical bars or real-time data.

Using these states properly keeps your code organized and prevents a lot of common bugs... and headaches.


### 2. Set your defaults—but keep it simple

In SetDefaults, you’ll define how your script looks and behaves by default. This is where you can set the name, overlay options, and how often the script will calculate.

Here’s a quick example:

if (State == State.SetDefaults)

{

Calculate = Calculate.OnPriceChange;

IsOverlay = false;

AddPlot(Brushes.Green, "MyPlot");

}

Pro tip: Don’t include any calculations or logic that depends on market data here. This part runs before the script knows anything about the market.


### 3. Save heavy lifting for later

If you’re doing calculations, referencing data, or setting up lists and custom variables, hold off until at least the Configure or DataLoaded states. Why? Because those early states don’t have access to market data yet, and trying to access it too soon can throw errors or produce weird results.

// Better to wait

if (State == State.DataLoaded)

{

myCustomValue = TickSize * 5;

}


### 4. Be smart with your variables

When you’re declaring variables, especially ones that store data between bars, make sure you initialize or reset them in the right state.

For example: if you’re optimizing strategies, NinjaTrader may reuse the same script across iterations. That means leftover values can carry over if you don’t reset them.

To stay safe, reinitialize things like counters or lists in State.DataLoaded.


### 5. Only access market data when it’s ready

Trying to grab data like bars, instruments, or indicators too early is a common mistake. Those objects aren’t fully loaded until you hit the DataLoaded state—so it’s best to wait until then. Also, if you’re working with multiple data series, be sure to add them in the Configure state. That’s the only state that can be used to create additional data series.


### 6. Be careful with UI elements

If your script interacts with the chart (like drawing on the screen or creating custom panels), wait until you’re out of the historical loading phase. Trying to use UI elements too early can break visuals or cause unexpected errors. A good rule of thumb? Don’t mess with the chart until after the historical state has passed.


## Why does this all matter?

Here’s what following these best practices can do for you:

- Cleaner code: Easier to read, easier to debug.

- Better performance: Scripts load faster and run smoother.

- Fewer bugs: No more chasing down null references or strange behavior during optimization.

You’re building your own custom tools, so make sure they’re stable, efficient, and ready for real-time action.


## Want to dig deeper?

There’s a full set of NinjaScript docs available if you’re ready to get more technical:

Whether you’re looking to automate your strategies or fine-tune your approach, these resources can help you take the next step in customizing your trading with NinjaTrader.


## Build your crypto futures experience before going live

Paper trading crypto futures can be an effective way to learn how futures markets work, practice strategies, and understand margin and execution. With NinjaTrader’s simulation environment, traders can practice trading crypto futures using the same tools they would use in live markets while staying focused on education and preparation.

For traders who want to explore crypto futures with confidence, paper trading is often the first step in building real-world experience.

Previous Post

Next Post

Related Posts

- How to Solve 5 of the Most Common Mistakes on the NinjaTrader Mobile App April 11, 2026


### How to Solve 5 of the Most Common Mistakes on the NinjaTrader Mobile App

April 11, 2026

- 8 Reasons Your New NinjaTrader Dashboard Is a Serious Upgrade March 25, 2026


### 8 Reasons Your New NinjaTrader Dashboard Is a Serious Upgrade

March 25, 2026

- Introducing the All-New NinjaTrader Dashboard March 19, 2026


### Introducing the All-New NinjaTrader Dashboard

March 19, 2026

- Futures Trading Hours: Making the Switch From Other Asset Classes June 24, 2026

Futures Trading Hours: Making the Switch From Other Asset Classes

June 24, 2026

- The NinjaTrader Arena Cup Finale Is Over: Here's Why You Should Still Watch It June 16, 2026

The NinjaTrader Arena Cup Finale Is Over: Here's Why You Should Still Watch It

June 16, 2026

- Volume Profile Shapes: The 4 Patterns Every Futures Trader Should Know June 15, 2026

Volume Profile Shapes: The 4 Patterns Every Futures Trader Should Know

June 15, 2026