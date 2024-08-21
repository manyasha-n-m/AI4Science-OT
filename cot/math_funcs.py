import numpy as np
from typing import Callable


# TODO: Add docstrings for functions here


def discrete_gaussian(mean: float, variance: float, interval: np.ndarray) -> np.ndarray: 
    '''
    This func...

    Parameters:
        mean: float -
        variance: float -
        interval: np.ndarray -

    Returns:
        np.ndarray -
    '''
    
    f = np.exp(-(interval - mean) ** 2 / (2 * variance)) / np.sqrt(2 * np.pi * variance)
    return f / f.sum()


def construct_tensor(x: np.ndarray, n_marginals: int, func: Callable[[float, float], float]) -> np.ndarray:
    '''
    This func...

    Parameters:
        x: np.ndarray -
        n_marginals: int -
        func: Callable[[float, float], float] -> float -

    Returns:
        np.ndarray -
    '''

    X = []
    C = 0

    for i in range(n_marginals):
        shape = [1] * n_marginals
        shape[i] = len(x)
        X.append(np.reshape(x, tuple(shape)))
        
    for i in range(n_marginals - 1):
        for j in range(i + 1, n_marginals):
            C += func(X[i], X[j])
            
    return C
