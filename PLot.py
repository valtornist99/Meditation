from matplotlib import pyplot as plt
import numpy as np

def plot(time_scale, rel_delta_power_values, rel_theta_power_values, rel_alpha_power_values, rel_beta_power_values, rel_gamma_power_values, kernel_size, channel_name):
    kernel = np.ones(kernel_size) / kernel_size

    time_scale_padded = time_scale[kernel_size // 2:len(time_scale) - kernel_size // 2]
    plt.plot(time_scale_padded, np.convolve(rel_delta_power_values, kernel, mode='valid'), label="delta")
    plt.plot(time_scale_padded, np.convolve(rel_theta_power_values, kernel, mode='valid'), label="theta")
    plt.plot(time_scale_padded, np.convolve(rel_alpha_power_values, kernel, mode='valid'), label="alpha")
    plt.plot(time_scale_padded, np.convolve(rel_beta_power_values, kernel, mode='valid'), label="beta")
    plt.plot(time_scale_padded, np.convolve(rel_gamma_power_values, kernel, mode='valid'), label="gamma")
    plt.title(channel_name)
    plt.legend(loc="upper left")
    plt.show()