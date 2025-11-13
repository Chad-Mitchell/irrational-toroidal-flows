import numpy as np

def box_dim(traj, scales=np.logspace(-1, 0, 10), dim_mode='1d'):
    """
    Box-counting Hausdorff dim proxy.
    dim_mode='1d' (flatten); '2d' (pair osc, e.g., [θ_i, θ_j]).
    """
    if dim_mode == '2d':
        # Pair first two osc for 2D proxy
        traj = np.column_stack((traj[:, 0], traj[:, 1]))
    
    counts = []
    for eps in scales:
        # Grid boxes
        boxes = np.floor(traj / eps).astype(int)
        unique_boxes = np.unique(boxes, axis=0)
        count = len(unique_boxes)
        counts.append(count)
    
    # Log-log fit: slope ≈ dim
    log_scales = np.log(1 / scales)
    log_counts = np.log(counts)
    coeffs = np.polyfit(log_scales, log_counts, 1)
    return coeffs[0]  # Dim estimate

# Ex: dim_irr = box_dim(theta, dim_mode='1d')  # Or '2d' for ~+0.2 lift
# print(f"Fractal dim: {dim_irr:.3f}")