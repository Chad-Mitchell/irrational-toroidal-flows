import numpy as np

# Slaving Order Parameter ξ Calculator
# Standalone for ξ = |avg e^{i θ}| (R equiv); time-avg over traj for stability.

def order_param_xi(theta_traj):
    """
    Slaving order param ξ = | (1/N) ∑ e^{i θ_j} | (v1 tie-in; 0=chaos, 1=lock).
    Time-avg over traj for robust sync measure.
    """
    T, N = theta_traj.shape
    xi_vals = []
    for t in range(T):
        complex_phases = np.exp(1j * theta_traj[t])
        xi = np.abs(np.mean(complex_phases))
        xi_vals.append(xi)
    return np.mean(xi_vals)  # Or np.max for peak slaving

# Ex: xi_irr = order_param_xi(theta)
# print(f"ξ (sync): {xi_irr:.3f}")