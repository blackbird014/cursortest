# Statistical Arbitrage Analysis Agent (statisticalArbsAi)

## Overview
An automated agent that performs statistical arbitrage analysis on Injective DEX pairs, enhances findings with Allora's price predictions, and publishes results through an automated pipeline to a static website and Twitter.


## Project Structure
```
├── Firstfile
├── README.md
├── requirements.txt
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── data_collector.py
│   │   └── stat_analyzer.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── allora_predictor.py
│   ├── publishers/
│   │   ├── __init__.py
│   │   ├── report_generator.py
│   │   └── twitter_publisher.py
│   └── website/
│       └── website_publisher.py
├── tests/
│   └── __init__.py
├── update_readme.py
```
