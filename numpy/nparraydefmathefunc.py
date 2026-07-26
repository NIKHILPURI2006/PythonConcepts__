import numpy as np

# ======workung with math formulas========

# defining math operations not defined in numpy


# defining sigmoid
def sigmoid(arr):
    return 1/(1+np.exp(-arr))


a = np.arange(12).reshape(3,4)

print(f"for sigmoid func")
print(sigmoid(a))

# mean square error
a1 = np.random.randint(1,50,25)
a2 = np.random.randint(1,50,25)

def MSE(actual,predicted):
    return np.mean((actual-predicted)**2)

print(f"for mean square error")
print(MSE(a1,a2))
