import numpy as np
import matplotlib.pyplot as plt

# Define the time range and sampling rate
T = 10  # Total time duration (seconds)
N = 100  # Number of samples
dt = T / N  # Sampling interval (seconds)

# Create a time vector
t = np.linspace(0, T-dt, N)  # Adjust end point to avoid duplicate at T

# Define the unit step function
def unit_step(t, n0):
  """
  This function defines the unit step function with a customizable delay (n0).

  Args:
      t: A NumPy array representing the time vector.
      n0: The delay of the unit step (starts at n0*dt).

  Returns:
      A NumPy array containing the unit step signal values.
  """
  u = np.zeros_like(t)  # Create an array of zeros with the same shape as t
  u[t >= n0*dt] = 1  # Set elements to 1 where t is greater than or equal to n0*dt (delayed step)
  return u

# Generate the unit step signal with a delay of n0 = 2 samples
n0 = 2  # Delay the step by 2 samples
step_signal = unit_step(t, n0)

# Plot the unit step signal
plt.plot(t, step_signal)

# Set plot labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Unit Step Signal (Delayed by ' + str(n0) + ' samples)')

# Adjust plot limits (optional)
plt.xlim(0, T)  # Set x-axis limits to show the entire time range
plt.ylim(-0.1, 1.1)  # Set y-axis limits slightly above and below 0 and 1

# Show the plot
plt.grid(True)
plt.show()
