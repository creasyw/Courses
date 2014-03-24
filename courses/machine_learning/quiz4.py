import numpy as np

def scaling(lst):
    lst = np.array(lst - lst.mean())
    lst = lst/(lst.max()-lst.min())
    return lst

x = np.array([7921,5184,8836,4761])
print scaling(x)


