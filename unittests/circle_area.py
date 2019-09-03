from math import pi

def circle_area(r):
  if type(r) not in [float,int]:
    raise TypeError("value mus be number > 0")
  if r < 0:
    raise ValueError("value must be > 0")
    
  return pi*(r**2)