import numpy as np
from scipy.spatial.distance import cdist
from scipy.special import digamma

def knn_mi(X, Y, k=3, metric='euclidean'):
    """
    KSG estimator for MI between two vars (1D phases ok).
    """
    if X.ndim == 1:
        X, Y = X.reshape(-1, 1), Y.reshape(-1, 1)
    n = len(X)
    Z = np.hstack((X, Y))
    dists_joint = cdist(Z, Z, metric)
    np.fill_diagonal(dists_joint, np.inf)
    eps = np.sort(dists_joint, axis=1)[:, k]  # k-th NN dist
    
    dists_x = cdist(X, X, metric)
    np.fill_diagonal(dists_x, np.inf)
    count_x = np.sum(dists_x < eps[:, np.newaxis], axis=1)
    
    dists_y = cdist(Y, Y, metric)
    np.fill_diagonal(dists_y, np.inf)
    count_y = np.sum(dists_y < eps[:, np.newaxis], axis=1)
    
    return digamma(k) - np.mean(digamma(count_x + 1)) - np.mean(digamma(count_y + 1)) + digamma(n)

def total_knn_mi(theta_traj, k=3, num_pairs=10):
    """
    Proxy total MI: Avg pairwise over random osc pairs.
    """
    N, T = theta_traj.shape[1], theta_traj.shape[0]
    mi_sum, count = 0, 0
    rng = np.random.default_rng(42)
    while count < num_pairs:
        i, j = rng.integers(0, N, 2)
        if i != j:
            mi_sum += knn_mi(theta_traj[:, i], theta_traj[:, j], k)
            count += 1
    return mi_sum / num_pairs

# Ex: mi_irr = total_knn_mi(theta, k=3, num_pairs=10)
# print(f"Irr MI: {mi_irr:.3f}")