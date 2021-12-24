from mne.io import read_raw_edf

import RhythmsCalculation as rc
import PLot as plot

path = input("EDF file path: ")
d = int(input("Step: "))
kernel_size = int(input("Smoothing kernel size: "))

raw = read_raw_edf(path, eog=(), preload=True)
raw.describe()

channel_names = [str.split(c, '-')[0] for c in raw.ch_names]

while True:
    print(channel_names)
    picks = str.split(input('Pick channels: '), ',')
    for pick in picks:
        channel = channel_names.index(pick)
        time_scale, rel_delta_power_values, rel_theta_power_values, rel_alpha_power_values, rel_beta_power_values, rel_gamma_power_values = \
            rc.rel_power_values(raw, channel, d)

        channel_name = raw.ch_names[channel]
        plot.plot(time_scale, rel_delta_power_values, rel_theta_power_values, rel_alpha_power_values, rel_beta_power_values, rel_gamma_power_values, kernel_size, channel_name)









