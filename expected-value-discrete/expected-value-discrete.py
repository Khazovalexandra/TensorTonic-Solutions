import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    E = 0.0
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    
    if x.shape != p.shape:
        raise ValueError("Shapes of x and p must match")

    if not np.allclose(np.sum(p), 1.0, rtol=1e-6):
        raise ValueError("Probabilities must sum to 1")
        
    for i in range(len(x)):
        E += x[i] * p[i]
        
    return E
    pass
