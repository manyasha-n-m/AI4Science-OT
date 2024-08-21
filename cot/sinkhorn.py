import numpy as np
from typing import List


# TODO: add error rate and potentials
# TODO: add docstrings


def dual_sinkhorn(marginals: List[np.ndarray], C: np.ndarray, eps: float) -> np.ndarray:
    '''
    This func...

    Parameters:
        marginals: List[np.ndarray] -
        C: np.ndarray -
        eps: float -

    Returns:
        np.ndarray - 
    '''

    K = np.exp(-C / C.max() / eps)
    N = len(C.shape)

    potentials = [np.zeros(len(marginal)) for marginal in marginals]

    for _ in range(100):
        for i in range(N):
            shape = [1] * N
            shape[i] = len(potentials[i])
            K /= np.reshape(np.exp(potentials[i] / eps), tuple(shape))                                  
            u = eps * np.log(marginals[i]) -eps * np.log(K.sum(axis=tuple(np.delete(range(N), i))))     
            potentials[i] = u                                                                           
            K *= np.reshape(np.exp(u / eps), tuple(shape))                                            

    return K
