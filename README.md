# Medium-Engagement-Stats
### Exploratory data analysis and metric analysis of user-specific Medium Stats

The goal is to collect baseline stats on stories from https://medium.com/me/stats in order to get a better understanding of how readers engage with a writers work. Note that this is a personal project and is in no way associated with Medium. In order to best utilize this repo, follow the following directives depending on your goals: 

#### Get your own data
* Download and run `scrape_medium_stats.py` after replacing the `USER` and `PASS` variables with your Google login (your Medium account must be linked with Google in order for this to work)
* If you want to tweak things or alter the code to work for alternate logins (Facebook, Twitter, etc.), then walk through the `Medium Stats Data Collection` jupyter notebook 
* Once you've collected your data, it will be placed in a file named `mystats.csv` (similar to mine in this repo).

#### Explore the data
* Feel free to check out my analysis in `Medium Stats Data Analysis` or perform your own!

#### Notes
It's worth noting that this type of analysis should be available to all writers, not just those that are data science practioners. Data analysis should be democratized for writers and content creators. Even with my ~30 post sample size, I was able to walk away with some interesting insights:
* 2 out of my 30+ posts make up over 70% of my total lifetime views
* `Read Ratio` and `Read Time` appear to be strongly correlated
* Publication choice matters for engagement stats like `Fan Ratio`
* `Read Ratio` and `Fan Ratio` correlated - strong posts do both well

This analysis is just from using the fraction of data available to users on the Medium Stats page. Imagine if we had more of our data and information at our disposal; if writers were empowered to use Medium Stats for improving their work and understanding how readers perceive it rather than boosting their ego with simple vanity stats. It's no small task, but I believe it can be done.

Hope you enjoyed this project, I know I did. Once again, reiterating that I am in no way affiliated with or working for Medium. However, you can follow my writing at the link below if interested. Thanks for reading!

https://medium.com/@conordewey3
