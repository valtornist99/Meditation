import numpy as np
import mne

delta_min, delta_max, theta_min, theta_max, alpha_min, alpha_max, beta_min, beta_max, gamma_min, gamma_max = 1, 4, 4, 8, 8, 13, 13, 30, 30, 45
fmin, fmax = 1, 45

def fr_band(x, y, min, max):
    a = 0
    b = len(x)
    for i in range(len(x)):
        if x[i] >= min:
            a = i
            break
    for i in range(len(x) - 1, 0, -1):
        if x[i] <= max:
            b = i + 1
            break

    return x[a:b], y[a:b]


def rhythms_rel_power(psd, channel):
    x, y = psd[1], psd[0][channel]
    delta_x, delta_y = fr_band(x, y, delta_min, delta_max)
    theta_x, theta_y = fr_band(x, y, theta_min, theta_max)
    alpha_x, alpha_y = fr_band(x, y, alpha_min, alpha_max)
    beta_x, beta_y = fr_band(x, y, beta_min, beta_max)
    gamma_x, gamma_y = fr_band(x, y, gamma_min, gamma_max)

    total_power = np.trapz(y, x)
    delta_power = np.trapz(delta_y, delta_x)
    theta_power = np.trapz(theta_y, theta_x)
    alpha_power = np.trapz(alpha_y, alpha_x)
    beta_power = np.trapz(beta_y, beta_x)
    gamma_power = np.trapz(gamma_y, gamma_x)

    rel_delta_power = delta_power / total_power
    rel_theta_power = theta_power / total_power
    rel_alpha_power = alpha_power / total_power
    rel_beta_power = beta_power / total_power
    rel_gamma_power = gamma_power / total_power

    return rel_delta_power, rel_theta_power, rel_alpha_power, rel_beta_power, rel_gamma_power

def rel_power_values(raw, channel, d):
    tmax = int(raw.times[-1])

    time_scale = []
    rel_delta_power_values = []
    rel_theta_power_values = []
    rel_alpha_power_values = []
    rel_beta_power_values = []
    rel_gamma_power_values = []

    for i in range(0, tmax, d):
        psd = mne.time_frequency.psd_multitaper(raw, fmin=fmin, fmax=fmax, tmin=i, tmax=i + d)
        rel_delta_power, rel_theta_power, rel_alpha_power, rel_beta_power, rel_gamma_power = rhythms_rel_power(psd,
                                                                                                               channel)
        time_scale.append(i + d / 2)
        rel_delta_power_values.append(rel_delta_power)
        rel_theta_power_values.append(rel_theta_power)
        rel_alpha_power_values.append(rel_alpha_power)
        rel_beta_power_values.append(rel_beta_power)
        rel_gamma_power_values.append(rel_gamma_power)

    return time_scale, rel_delta_power_values, rel_theta_power_values, rel_alpha_power_values, rel_beta_power_values, rel_gamma_power_values