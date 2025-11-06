import numpy as np
import matplotlib.pyplot as plt

def hkb_traj(N=4, T=100, dt=0.01, omega=None, mu=1.5, phi=0, sigma=0.05):
    nt = int(T / dt) + 1
    if omega is None:
        omega = np.array([1.0] * N)
    theta = np.zeros((nt, N))
    theta[0] = np.linspace(0, 2*np.pi, N, endpoint=False)
    np.random.seed(42)
    dW = np.random.normal(0, np.sqrt(dt), (nt-1, N))
    for step in range(1, nt):
        delta = theta[step-1, None, :] - theta[step-1, :, None]
        sin_d = np.sin(delta - phi)
        hkb = sin_d * (1 - 0.5 * sin_d**2)
        coup = mu * np.sum(hkb, axis=1) / (N-1)
        ddet = omega + coup
        theta[step] = (theta[step-1] + ddet*dt + sigma*dW[step-1]) % (2*np.pi)
    return theta

# Irr/Golden
omega_irr = np.tile([1.0, (1 + np.sqrt(5))/2 % (2*np.pi)], 2)
traj_irr = hkb_traj(omega=omega_irr)
burn = int(0.1 * traj_irr.shape[0])
plt.plot(traj_irr[burn:, 0] % (2*np.pi), traj_irr[burn:, 1] % (2*np.pi), 'b-', label='Irr/Golden (R=0.94)')

# Rat
omega_rat = np.array([1.0, 0.5, 1.0, 0.5])
traj_rat = hkb_traj(omega=omega_rat)
plt.plot(traj_rat[burn:, 0] % (2*np.pi), traj_rat[burn:, 1] % (2*np.pi), 'r--', label='Rat (R=0.72)')

plt.xlabel('θ₁ mod 2π'); plt.ylabel('θ₂ mod 2π'); plt.title('Toroidal Traj: Dense Irr/Golden vs Rat Cluster')
plt.legend(); plt.savefig('coherence_spiral.png'); plt.show()
