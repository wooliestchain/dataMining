import pandas as pd
import matplotlib.pyplot as plt


ozoene = pd.read_csv("ozone.csv", delimiter=";")

maxO3 = ozone['maxO3']
T12 = ozone['T12']

plt.scatter(T12, maxO3, alpha=0.5)

plt.xlabel('T12')
plt.ylabel('maxO3')
plt.title('Scatter Plot of maxO3 vs T12')

plt.show()
