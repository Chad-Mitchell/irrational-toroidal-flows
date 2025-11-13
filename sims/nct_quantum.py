import qutip as qt
import numpy as np

def nct_irr_bridge(alpha=1.0, theta_dim=2, num_states=10):
    """
    Noncommutative torus proxy: Weyl ops for irr windings (bridges classical to quantum).
    Low ent <0.35 flags synergy (v1 probe); rational locks var.
    """
    # NCT basis: Noncomm coords (theta_dim=2 for T^2 deform)
    x = qt.position(num_states)
    p = qt.momentum(num_states)
    theta_op = alpha * np.sqrt(2) * x + p  # Irr deform [x,p]=i
    if alpha == 1.0:  # Rational proxy
        theta_op = x + p  # Commutative edge
    
    # Ent probe: Von Neumann S(ρ) for thermal state
    rho = qt.thermal_dm(num_states, 1.0)  # Weak K analog
    evolved = (-1j * theta_op * 0.1).expm() * rho * (1j * theta_op * 0.1).expm()  # Time evo tease
    ent = qt.entropy_vn(evolved)
    return ent  # Target <0.35 for irr synergy

# Ex: ent_irr = nct_irr_bridge(alpha=np.sqrt(2))
# print(f"Quantum ent depth: {ent_irr:.3f} (irr damped synergy)")