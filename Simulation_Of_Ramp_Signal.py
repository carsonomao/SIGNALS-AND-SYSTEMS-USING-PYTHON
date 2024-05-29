import numpy as np
import matplotlib.pyplot as plt

def generate_ramp(amplitude, start_time, stop_time, sampling_rate):
  """
  Generates a ramp signal with specified parameters.

  Args:
      amplitude: The peak amplitude of the ramp signal.
      start_time: The starting time of the ramp (in seconds).
      stop_time: The ending time of the ramp (in seconds).
      sampling_rate: The sampling rate for the signal (in samples per second).

  Returns:
      A NumPy array containing the ramp signal values.
  """
  t = np.linspace(start_time, stop_time, int(sampling_rate * (stop_time - start_time)))
  ramp = amplitude * (t - start_time)  # Linear ramp equation
  return ramp,t

# Define parameters
amplitude = 2  # Volts
start_time = 0  # seconds
stop_time = 5  # seconds
sampling_rate = 1000  # Samples per second

# Generate the ramp signal
ramp_signal,t = generate_ramp(amplitude, start_time, stop_time, sampling_rate)

# Plot the ramp signal
plt.plot(t, ramp_signal)

# Set plot labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (Volts)')
plt.title('Ramp Signal')

# Optional: Adjust plot limits
# plt.xlim(start_time - 0.1, stop_time + 0.1)  # Adjust x-axis limits
# plt.ylim(-amplitude - amplitude/5, amplitude + amplitude/5)  # Adjust y-axis limits

# Show the plot
plt.grid(True)
plt.show()

        


