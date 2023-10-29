import numpy as np

array = np.random.normal(0,1,(5,5))

array = np.where(array > 0.09, array**2, 42)

print(array[:,3])