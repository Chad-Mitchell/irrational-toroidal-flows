import sympy as sp
import numpy as np

def diffeological_torus_alpha(alpha_sym, n=100):
    """
    Ergodic density metric for arithmetic α (e.g., √2+1) on T_α.
    Low <0.1 → dense windings (Iglesias-Zemmour 2025).
    """
    alpha = sp.N(alpha_sym)
    theta = np.linspace(0, 2 * np.pi, n)
    winding = (theta + alpha * theta) % (2 * np.pi)
    density = np.abs(np.mean(np.exp(1j * winding)))
    return density

# Probe: √2 + 1 (golden-ratio ish for homotopy Z + αZ)
alpha_probe = sp.sqrt(2) + 1
ergodic_density = diffeological_torus_alpha(alpha_probe)
print(f"Ergodic density for α={alpha_probe}: {ergodic_density:.4f} (target <0.1 for mixing)")

# Hybrid tie-in: Use as irr_scale scalar in kuramoto_genus
# e.g., irr_scale = 1.0 / ergodic_density if ergodic_density < 0.1 else 0.5