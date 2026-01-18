# Stochastic Simulation of Market Panic Using Monte Carlo Methods

## 1. Introduction
Financial markets exhibit inherently stochastic behavior driven by uncertainty, external information, and investor sentiment. Under normal conditions, asset prices fluctuate around an expected trend with moderate volatility. However, during periods of market panic, this behavior can change abruptly, leading to increased volatility and sudden price movements.

The objective of this project is to numerically simulate the time evolution of a financial asset price and analyze the effect of a market panic event using stochastic modeling and Monte Carlo methods. Rather than relying on analytical solutions, the system is solved numerically in order to capture realistic market dynamics under changing conditions.

## 2. Mathematical Model
The asset price is modeled as a stochastic process influenced by two main components:

- **Deterministic trend**: representing the expected market return  
- **Stochastic component**: representing random market fluctuations  

This behavior is commonly described using a stochastic differential equation framework, where:

- The deterministic term captures the average growth or decay of the asset price  
- The stochastic term captures uncertainty and volatility in the market  

During a panic event, the mathematical structure of the model remains unchanged. Instead, key parameters such as volatility and expected return are modified to reflect increased uncertainty and negative market sentiment. This approach allows the panic event to be modeled as a sudden shift in market conditions rather than as an entirely new system.

## 3. Why Numerical Methods Are Required
An analytical solution is not suitable for this problem for several reasons:

- The system contains stochastic (random) components  
- Model parameters change dynamically during the panic event  
- Closed-form solutions are impractical or unavailable under such conditions  

Therefore, numerical methods are required to approximate the evolution of the system over time. The continuous-time model is discretized and solved step by step using numerical integration techniques.

## 4. Numerical Methods

### 4.1 Euler Method
The Euler method is used to discretize time and approximate the evolution of the asset price. At each time step, the price is updated based on its current value and a small incremental change derived from both deterministic and stochastic components. This method provides a simple and transparent numerical framework that aligns with the techniques covered in the course.

### 4.2 Monte Carlo Simulation
Due to the stochastic nature of the system, a single simulation is insufficient to fully capture market behavior. To address this, the numerical solution is repeated multiple times using different random realizations. These repeated simulations form a Monte Carlo experiment, allowing observation of the variability and dispersion of possible price trajectories under identical model assumptions.

## 5. Market Panic Modeling
The market panic is introduced as a time-dependent event occurring at a predefined moment during the simulation. When this event occurs:

- Volatility is increased  
- Expected return is reduced  

This parameter-based approach ensures that the panic is modeled realistically while maintaining numerical stability and conceptual clarity.

## 6. Simulation Output and Visualization
The simulation produces multiple price trajectories over time. These trajectories are visualized on a single time–price graph to illustrate:

- Normal market behavior before the panic event  
- Increased volatility and divergence after the panic event  
- The panic moment is visually highlighted to emphasize its impact on the system dynamics  

All axes and labels are clearly defined to ensure interpretability. In addition to individual Monte Carlo realizations, the mean price trajectory is plotted to represent the expected system behavior. After the panic event, the dispersion of trajectories increases significantly, indicating heightened market uncertainty.

## 7. Project Structure
- `parameters.py` – Contains all model and simulation parameters  
- `simulation.py` – Implements the numerical solver and Monte Carlo simulations  
- `visualization.py` – Handles plotting and graphical interpretation of results  
- `README.md` – Provides theoretical background and usage instructions  
- `requirements.txt` – Lists required Python libraries  

This separation ensures clarity, reproducibility, and ease of experimentation.

## 8. How to Run the Project

1. Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt

2.Adjust model parameters in parameters.py if desired.

3.Run the simulation module:

python simulation.py


4.Execute the visualization module to generate the final output:

python visualization.py

9. Contribution Statement

Sumeyra Erdem – Mathematical modeling of the stochastic system, parameter design, and theoretical framework

Rumeysa Soydan – Numerical methods implementation, Monte Carlo simulations, data visualization, and documentation assistance

10. Conclusion

This project demonstrates how numerical methods can be used to model complex stochastic systems where analytical solutions are impractical. By combining the Euler method with Monte Carlo simulations, the project provides insight into the dynamics of market panic and highlights the importance of numerical analysis in financial modeling.
