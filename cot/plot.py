import numpy as np 
import matplotlib.pylab as pl
from matplotlib import gridspec
from typing import Tuple


def plot_matrix(a: np.ndarray, b: np.ndarray, M: np.ndarray, title: str = "", 
                fig: int = 1, size: Tuple[int, int] = (5, 5)):
    
    '''
    Slightly modified version of ot.plot.plot1D_mat that fixes some visual bugs.

    Parameters:
        a: np.ndarray    - Vertical axis.
        b: np.ndarray    - Horizontal axis.
        M: np.ndarray    - Matrix to be plotted.
        title: str       - Sets title of plot.
        fig: int = 1     - Sets plot ID.
        size: Tuple[int, int] - Sets dimensions of plot.

    Returns:
        None
    '''

    pl.figure(fig, figsize=size)

    gs = gridspec.GridSpec(3, 3)

    ax1 = pl.subplot(gs[0, 1:])
    pl.plot(np.arange(M.shape[1]), b, 'r', label='Target distribution')
    pl.yticks(())
    pl.title(title)

    ax2 = pl.subplot(gs[1:, 0])
    pl.plot(a, np.arange(M.shape[0]), 'b', label='Source distribution')
    pl.gca().invert_xaxis()
    pl.gca().invert_yaxis()
    pl.xticks(())

    pl.subplot(gs[1:, 1:], sharex=ax1, sharey=ax2)
    pl.imshow(M, interpolation='nearest')
    pl.axis('off')

    pl.tight_layout()
    pl.subplots_adjust(wspace=0.2, hspace=0.2)
