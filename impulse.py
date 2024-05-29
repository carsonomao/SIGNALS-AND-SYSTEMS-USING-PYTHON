import numpy as np
import matplotlib.pyplot as plt

# Define the time range and sampling rate
T = 10  # Total time duration (seconds)
N = 100  # Number of samples
dt = T / N  # Sampling interval (seconds)

# Create a time vector
t = np.linspace(0, T-dt, N)  # Adjust end point to avoid duplicate at T

# Define the impulse function (delta function approximation)
def impulse(t, n0):
  """
  This function defines an approximation of the discrete-time impulse function with a peak at n0.

  Args:
      t: A NumPy array representing the time vector.
      n0: The position of the impulse (peak at n0*dt).

  Returns:
      A NumPy array containing the impulse signal values.
  """
  impulse_signal = np.zeros_like(t)
  # Simulate impulse with a narrow peak at n0*dt (adjust width as needed)
  impulse_signal[n0] = 1 / dt  # Higher value for a stronger impulse
  return impulse_signal

# Generate the impulse signal at n0 = 50 samples
n0 = 50
impulse_signal = impulse(t, n0)

# Plot the impulse signal
plt.plot(t, impulse_signal)

# Set plot labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Discrete-Time Impulse Signal (Peak at ' + str(n0) + ' samples)')

# Adjust plot limits (optional)
plt.xlim(0, T)  # Set x-axis limits to show the entire time range
plt.ylim(-0.1, 1.1)  # Set y-axis limits slightly above and below 0

# Show the plot
plt.grid(True)
plt.show()
