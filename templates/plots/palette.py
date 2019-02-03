#!/usr/bin/env python3

from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt


# Sample data.
x = np.linspace(1, 10, 100)
y1 = x
y2 = np.sin(x)
y3 = np.log(x)

# We can reorder the default colors (which are pretty nice) as desired.
# See: https://matplotlib.org/examples/color/color_cycle_demo.html
default_color_cycle = plt.rcParams['axes.prop_cycle']
default_colors = [c['color'] for c in default_color_cycle]
palette = [default_colors[idx] for idx in [0, 3, 2]]
plt.rc('axes', prop_cycle=(cycler('color', palette)))

plt.plot(x, y1, label='Y1')
plt.plot(x, y2, label='Y2')
plt.plot(x, y3, label='Y3')

# We could also manually specify default colors.
# See: https://matplotlib.org/users/dflt_style_changes.html
# plt.plot(x, y1, 'C0', label='Y1')
# plt.plot(x, y2, 'C3', label='Y2')
# plt.plot(x, y3, 'C2', label='Y3')

# Or use our own.
# plt.plot(x, y1, color='#555555', label='Y1')

plt.legend()
plt.title('Colors')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
