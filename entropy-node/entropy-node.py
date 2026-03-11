import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    H = 0.0
    _, counts = np.unique(y, return_counts=True)
    total = counts.sum()
    
    for count in counts:
        p = count/total
        if p != 0:
            H -= p*np.log2(p)
    return H
    pass