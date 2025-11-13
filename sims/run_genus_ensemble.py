import numpy as np
from scipy.integrate import odeint

# [Paste: kuramoto_genus, knn_mi, total_knn_mi, box_dim, lyapunov_max, diffeological_torus_alpha, order_param_xi]

def run_genus_ensemble(N=21, genus=3, T_steps=50, dt=0.01, num_ens=10, K=0.5, irr_scale=1.0, trans_coup=0.05, k=3, num_pairs=10, eta_noise=0.01):
    """
    Full g=3 filtered ensemble: Irr vs rat, orientable adj pi/3, + ξ slaving calc.
    Adds noise η for synergy probe (v1 Eq 1).
    Returns dict: lifts, mis, les, dims, xis.
    """
    t = np.arange(0, T_steps * dt, dt)
    rng = np.random.default_rng(42)
    alpha_density = diffeological_torus_alpha(np.sqrt(2) + 1)  # Diffeology tie
    irr_scale *= 1.0 / alpha_density if alpha_density < 0.1 else 0.5  # Boost if ergodic
    
    lifts, irr_mis, rat_mis, irr_les, rat_les, irr_dims, rat_dims, irr_xis, rat_xis = [], [], [], [], [], [], [], [], []
    
    for ens in range(num_ens):
        omega = rng.uniform(-1, 1, N)
        theta0 = rng.uniform(0, 2 * np.pi, N)
        
        # Irr run (add η_noise to dtheta in kuramoto_genus if needed; here post-hoc for sim)
        theta_irr = odeint(kuramoto_genus, theta0, t, args=(omega, K, N, genus, irr_scale, False, trans_coup, True))
        theta_irr += rng.normal(0, eta_noise, theta_irr.shape) % (2 * np.pi)  # Structured noise proxy
        mi_irr = total_knn_mi(theta_irr, k, num_pairs)
        le_irr = lyapunov_max(theta_irr, omega, K, N, genus)
        dim_irr = box_dim(theta_irr, dim_mode='1d')
        xi_irr = order_param_xi(theta_irr)
        irr_mis.append(mi_irr)
        irr_les.append(le_irr)
        irr_dims.append(dim_irr)
        irr_xis.append(xi_irr)
        
        # Rat run (same init + noise for fair comp)
        theta_rat = odeint(kuramoto_genus, theta0, t, args=(omega, K, N, genus, irr_scale, True, trans_coup, True))
        theta_rat += rng.normal(0, eta_noise, theta_rat.shape) % (2 * np.pi)
        mi_rat = total_knn_mi(theta_rat, k, num_pairs)
        le_rat = lyapunov_max(theta_rat, omega, K, N, genus)
        dim_rat = box_dim(theta_rat, dim_mode='1d')
        xi_rat = order_param_xi(theta_rat)
        rat_mis.append(mi_rat)
        rat_les.append(le_rat)
        rat_dims.append(dim_rat)
        rat_xis.append(xi_rat)
        
        lift = (mi_irr - mi_rat) / mi_rat * 100 if mi_rat != 0 else 0
        lifts.append(lift)
    
    wins = np.sum(np.array(lifts) > 0) / num_ens * 100
    return {
        'lifts': lifts, 'mean_lift': np.mean(lifts), 'std_lift': np.std(lifts),
        'irr_mi_mean': np.mean(irr_mis), 'irr_mi_std': np.std(irr_mis),
        'rat_mi_mean': np.mean(rat_mis), 'rat_mi_std': np.std(rat_mis),
        'irr_le_mean': np.mean(irr_les), 'rat_le_mean': np.mean(rat_les),
        'irr_dim_mean': np.mean(irr_dims), 'rat_dim_mean': np.mean(rat_dims),
        'irr_xi_mean': np.mean(irr_xis), 'rat_xi_mean': np.mean(rat_xis),  # New: Slaving sync
        'win_rate': wins
    }

# Run ex: results = run_genus_ensemble(N=21, genus=3, num_ens=10, eta_noise=0.01)
# print(f"Mean lift: {results['mean_lift']:.1f}% | Irr ξ: {results['irr_xi_mean']:.3f}")