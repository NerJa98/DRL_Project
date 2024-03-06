# Portfolio Optimization with Deep Reinforcement Learning - Comparison of Actor-Critic Algorithms

## Overview

This project delves into the realm of applying Deep Reinforcement Learning (DRL) models for portfolio optimization, contrasting their performance with traditional deterministic portfolio allocation strategies based on Modern Portfolio Theory (MPT). Our focus is to investigate how various factors such as state representations, reward functions, and different actor-critic learning algorithms impact the decision-making process and overall return of the DRL-model.

Portfolio allocation is an essential aspect of financial management, aiming to maximize returns while minimizing risk through the strategic distribution of assets. Deep Reinforcement Learning, with its ability to learn complex patterns and make decisions under uncertainty, presents a novel approach to this classic problem. By simulating numerous scenarios, DRL models can potentially uncover more robust and adaptive strategies compared to traditional methods.

### Key Components of the Project

- **Data Preparation**: Techniques to prepare financial data for DRL models.
- **Model Implementation**: Implementation of DRL models like Proximal Policy Optimization (PPO), Advantage Actor-Critic (A2C), and Soft Actor-Critic (SAC).
- **Performance Analysis**: Comparing DRL models with traditional portfolio strategies.
- **Visualization**: Graphs and plots showcasing performance metrics.

## Code

The code in this repository represents the implementation and analysis of the aforementioned DRL models in portfolio optimization. It includes data preprocessing, model setup, performance evaluation, and result visualization segments.

The project is implemented in the Jupyter notebook. utils.py stores the DRL environments and the helper functions.

## Requirements

To run the code in this repository, you may need to install third-party libraries such as:

- [stable_baselines3](https://stable-baselines3.readthedocs.io/en/master/)
- [pyfolio](https://github.com/quantopian/pyfolio)

These libraries can be installed via pip:

```bash
pip install stable_baselines3 pyfolio
```

## Conclusion

This project aims to bridge the gap between traditional portfolio management strategies and the evolving field of Deep Reinforcement Learning, providing insights into the efficacy of DRL models in financial decision-making contexts.
