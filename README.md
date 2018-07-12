# Medium-Stats-Analysis

### Getting Started
The goal is to collect baseline stats on stories from [Medium Stats](https://medium.com/me/stats) in order to get a better understanding of how readers engage with a writers work. Note that this is a personal project and is in no way associated with Medium. In order to best utilize this repo, follow the following directives depending on your goals. If the Jupyter notebooks give you trouble rendering, just copy/paste the url into [nbviewer](https://nbviewer.jupyter.org/) and it should work. 

### Data Collection
* Download and run `scrape_medium_stats.py` after replacing the `USER` and `PASS` variables with your Google login (your Medium account must be linked with Google)
* If you want to tweak things or alter the code for alternate logins (Facebook, Twitter, etc.), then walk through the `Medium Stats Data Collection` jupyter notebook 
* Once you've collected your data, it will be placed in a file named `mystats.csv` (similar to mine in this repo).

### Data Analysis
* Check out my analysis in `Medium Stats Data Analysis` or perform your own!
* An example of my data is available in `mystats.csv` as a starter dataset, feel free to share and explore.

### See the Post
I wrote a Medium post as well. You can find the post and more about metrics on Medium here: 

[Deconstructing Metrics on Medium](https://towardsdatascience.com/deconstructing-metrics-on-medium-bf5b4863bf96)

### Notes
It's worth noting that this type of analysis should be available to all writers, not just those that are data science practioners. Data analysis should be democratized for writers and content creators. Even with my ~30 post sample size, I was able to walk away with some interesting insights:
* 2 out of my 30+ posts make up over 70% of my total lifetime views
* `Read Ratio` and `Read Time` appear to be strongly correlated
* Publication choice matters for engagement stats like `Fan Ratio`
* `Read Ratio` and `Fan Ratio` correlated - strong posts do both well

This analysis is just from using the fraction of data available to users on the Medium Stats page. Imagine if we had more of our data and information at our disposal; if writers were empowered to use Medium Stats for improving their work and understanding how readers perceive it rather than boosting their ego with simple vanity stats. It's no small task, but I believe it can be done.
