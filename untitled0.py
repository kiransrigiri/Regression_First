from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([1,5,3,6,2,1], dtype=np.float64)

def best_fit_slop_and_intercept(xs, ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /(mean(xs)**2 - mean(xs**2)))
    
    b = mean(ys) - m*mean(xs)
    return m, b

m, b = best_fit_slop_and_intercept(xs, ys)
print(m,b)
regression_line = [(m*x)+b for x in xs] 
plt.scatter(xs,ys)
plt.plot(xs, regression_line)
plt.show


 


