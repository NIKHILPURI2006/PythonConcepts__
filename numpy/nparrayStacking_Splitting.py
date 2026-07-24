import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

# =====Stacking=====

# horizontal stacking
print(np.hstack((a1,a2)))

print(np.hstack((a1,a2,a1)))


# vertical stacking
print(np.vstack((a1,a2)))

print(np.vstack((a1,a2,a2)))


# ======Splitting======

print(np.hsplit(a1,2))

print(np.hsplit(a1,4))

print(np.vsplit(a2,3))