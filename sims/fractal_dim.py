def box_dim(traj, scales=np.logspace(-1, 0, 10)):
    counts = []
    for eps in scales:
        boxes = np.ceil((traj.max() - traj.min()) / eps).astype(int)
        count = np.sum(np.unique(np.floor(traj / eps), axis=0).size)  # Coarse 1D proxy
        counts.append(count)
    return np.polyfit(np.log(1/scales), np.log(counts), 1)[0]  # Slope ≈ dim

# Ex: dim_irr_g = box_dim(theta_irr_g[:,0].flatten())  # Per osc