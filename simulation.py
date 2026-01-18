"""
Numerical simulation of stochastic market dynamics using
the Euler method and Monte Carlo simulations.
"""

import numpy as np
from parameters import (
    TOTAL_TIME,
    DT,
    NUM_STEPS,
    NUM_SIMULATIONS,
    INITIAL_PRICE,
    MU_NORMAL,
    SIGMA_NORMAL,
    MU_PANIC,
    SIGMA_PANIC,
    PANIC_TIME
)


def run_simulation():
    """
    Runs Monte Carlo simulations of the stochastic price model.
    Returns time array and simulated price paths.
    """

    time = np.linspace(0, TOTAL_TIME, NUM_STEPS)
    prices = np.zeros((NUM_SIMULATIONS, NUM_STEPS))

    for sim in range(NUM_SIMULATIONS):
        prices[sim, 0] = INITIAL_PRICE

        for t in range(1, NUM_STEPS):
            current_time = time[t]

            if current_time < PANIC_TIME:
                mu = MU_NORMAL
                sigma = SIGMA_NORMAL
            else:
                mu = MU_PANIC
                sigma = SIGMA_PANIC

            dW = np.random.normal(0.0, np.sqrt(DT))
            prices[sim, t] = (
                prices[sim, t - 1]
                + mu * prices[sim, t - 1] * DT
                + sigma * prices[sim, t - 1] * dW
            )

    return time, prices
