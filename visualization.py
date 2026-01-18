"""
Numerical simulation of stochastic market dynamics using
the Euler method and Monte Carlo simulations.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize
from simulation import run_simulation
from parameters import PANIC_TIME, TOTAL_TIME, INITIAL_PRICE

TIME_CHECKPOINTS = [5, 10, 15]

def animate_results():
    time, prices = run_simulation()

    prices = prices[:60]
    mean_price = np.mean(prices, axis=0)
    n_agents = prices.shape[0]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.set_xlim(0, TOTAL_TIME)
    ax.set_ylim(0, 200)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Asset Price")
    ax.set_title("Monte Carlo Market Panic Simulation")

    lines = [ax.plot([], [], linewidth=0.6, alpha=0.15)[0] for _ in range(n_agents)]
    mean_line, = ax.plot([], [], linewidth=3, color='blue', label="Mean Price")
    scatter = ax.scatter(np.zeros(n_agents), prices[:, 0], s=25, alpha=0.8)

    ax.axvline(PANIC_TIME, linestyle="--", linewidth=2, color="red", label="Panic Event")

    for sec in TIME_CHECKPOINTS:
        ax.axvline(sec, linestyle=":", color="gray", alpha=0.6)
        ax.text(sec, ax.get_ylim()[1]*0.97, f"{sec}s", ha="center", va="top", fontsize=10, color="gray")

    time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, weight="bold")
    state_text = ax.text(0.02, 0.90, "", transform=ax.transAxes, fontsize=10)

    color_legend_text = (
        "Color meaning:\n"
        "Green  : Stable market\n"
        "Yellow → Red : Panic escalating\n"
        "Red -- : Panic event"
    )
    ax.text(0.72, 0.02, color_legend_text, transform=ax.transAxes,
            fontsize=9, verticalalignment="bottom",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

    ax.legend()
    ax.grid(True)

    cmap = plt.get_cmap('autumn')
    norm = Normalize(vmin=PANIC_TIME, vmax=TOTAL_TIME)

    def init():
        for line in lines:
            line.set_data([], [])
        mean_line.set_data([], [])
        scatter.set_offsets(np.c_[[], []])
        time_text.set_text("")
        state_text.set_text("")
        return lines + [mean_line, scatter, time_text, state_text]

    def update(frame):
        current_time = time[frame]

        for i, line in enumerate(lines):
            line.set_data(time[:frame], prices[i, :frame])

        mean_line.set_data(time[:frame], mean_price[:frame])

        x = np.full(n_agents, current_time)
        y = prices[:, frame]

        jitter_scale = 0.01
        if current_time >= PANIC_TIME:
            jitter_scale = 0.02
        y += np.random.normal(0, np.std(y) * jitter_scale, n_agents)

        if current_time >= PANIC_TIME:
            colors = [cmap(norm(current_time))] * n_agents
        else:
            colors = ['green'] * n_agents

        state = "Panic regime" if current_time >= PANIC_TIME else "Stable market"

        scatter.set_offsets(np.column_stack((x, y)))
        scatter.set_color(colors)
        scatter.set_sizes(np.full(n_agents, 25))

        time_text.set_text(f"Time = {current_time:.2f} s")
        state_text.set_text(f"State: {state}")

        return lines + [mean_line, scatter, time_text, state_text]

    anim = FuncAnimation(fig, update, frames=range(1, len(time), 3),
                         init_func=init, interval=35, blit=False)

    anim.save("market_panic_simulation.gif", writer="pillow", fps=20)
    plt.show()


if __name__ == "__main__":
    animate_results()