import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def set_size(width, fraction=1):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 455.24411
    elif width == 'beamer':
        width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio

    return (fig_width_in, fig_height_in)

def plot_cumulative_returns_and_weights(cumulative_returns, portfolio_weights, test_re_df_index, tickers, save=False, size = set_size(width='thesis', fraction=2)):
    """
    Plots and optionally saves cumulative returns and portfolio weights.

    Parameters:
    - cumulative_returns: 2D list or array of cumulative returns.
    - portfolio_weights: 2D list or array of portfolio weights.
    - test_re_df_index: Pandas DataFrame index for the x-axis (time).
    - tickers: List of tickers representing portfolio assets.
    - save: Boolean, if True, saves the plot as a PDF in 'images/' directory.
    """
    # Setup plot dimensions and layout
    fig, axs = plt.subplots(2, 2, figsize=size, constrained_layout=True, sharex=True)
    
    # Calculate mean, std, max, and min cumulative returns
    cr_array = np.array(cumulative_returns)
    mean_cr = np.mean(cr_array, axis=0)
    std_cr = np.std(cr_array, axis=0)
    max_cr = cr_array[np.argmax(cr_array[:, -1])]
    min_cr = cr_array[np.argmin(cr_array[:, -1])]
    
    # Plot cumulative returns
    axs[0, 0].plot(test_re_df_index, mean_cr, color='tab:blue', linewidth=2.0)
    axs[0, 0].fill_between(test_re_df_index, max_cr, mean_cr, alpha=0.2, color='tab:green')
    axs[0, 0].fill_between(test_re_df_index, min_cr, mean_cr, alpha=0.2, color='tab:red')
    axs[0, 0].axhline(1, color='black', linestyle='--', lw=1.5)
    axs[0, 0].set_ylabel("Cumulative Returns")
    
    # Helper function to plot portfolio weights
    def plot_weights(ax, weights, label="Weights (%)"):
        df = pd.DataFrame(weights, index=test_re_df_index, columns=tickers)
        ax.stackplot(test_re_df_index, *df.values.T, labels=tickers)
        ax.legend(loc='upper left')
        ax.margins(x=0, y=0)
        ax.set_ylabel(label)
    
    # Plot mean portfolio weights
    mean_weights = np.mean(np.array(portfolio_weights), axis=0)
    plot_weights(axs[0, 1], mean_weights)
    
    # Plot portfolio weights for max cumulative return
    max_weights = portfolio_weights[np.argmax(cr_array[:, -1])]
    plot_weights(axs[1, 0], max_weights, "Weights (%)")
    axs[1, 0].set_xlabel("Time (Years-Months)")
    
    # Plot portfolio weights for min cumulative return
    min_weights = portfolio_weights[np.argmin(cr_array[:, -1])]
    plot_weights(axs[1, 1], min_weights)
    axs[1, 1].set_xlabel("Time (Years-Months)")
    
    if save:
        plt.savefig('images/cumulative_returns_and_weights.pdf')
    else:
        plt.show()