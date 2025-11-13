import numpy as np
from scipy.linalg import norm

# Lyapunov Exponent Estimator (Chaos Bound Layer)
# Max LE via Jacobian growth—tames sensitivity in irr flows (lower tails = stable mixing).

def lyapunov_max(theta_traj, omega, K, N, genus=1, dt=0.01, steps=50):
    """
    Proxy max LE: Tangent vec growth over traj (Gram-Schmidt norm).
    Positive mild → bounded chaos; irr should clip vs rat.
    NOTE: For high-genus/multi-ring (N>20), full J @ tangent blows dim (NxN matrix); 
    scalar approx via max(eig(J)) per step for speed/stability.
    To fix: Replace tangent growth with le_step = np.log(np.linalg.eigvals(J).max().real) if J is symm; avg over steps.
    Current: Full ortho for low-N; comment out for ens if snag. 
    """
    T = len(theta_traj)
    le_sum = 0
    tangent = np.eye(N)  # Initial ortho basis
    
    for t in range(1, steps, 10):  # Subsample for speed
        # Jacobian approx: Finite diff on dtheta/dt
        theta_pert = theta_traj[t-1] + 1e-6 * tangent
        dtheta = kuramoto_genus(theta_pert, 0, omega, K, N, genus, 1.0, False, 0.05, True)[:N]  # No t-dep
        J = (dtheta - kuramoto_genus(theta_traj[t-1], 0, omega, K, N, genus, 1.0, False, 0.05, True)[:N]) / 1e-6
        
        # Grow tangent
        tangent = J @ tangent
        norms = np.linalg.norm(tangent, axis=0)
        tangent /= norms[:, np.newaxis]  # Gram-Schmidt
        le_sum += np.log(norms).max()  # Max growth
    
    return le_sum / (steps / 10 * np.log(1 / dt))  # Avg per unit time

# Ex: le_irr = lyapunov_max(theta, omega, K, N, genus=3)
# print(f"Max LE: {le_irr:.3f}")
