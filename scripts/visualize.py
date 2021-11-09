import matplotlib.pyplot as plt
import numpy as np

with open("hipass_impulse_response.txt", "r") as f: raw = f.read()

l = [float(r.strip()) for r in raw[1:-1].split(",")]

plt.plot(l)
plt.ylabel('Impulse response')
plt.show()
