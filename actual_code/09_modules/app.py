import library.util as ut
from library.util import printer, Shape as ShapeMaker




# import numpy as np
# import pandas as pd

triangle = ut.Shape("triangle")

ut.printer(triangle)

ut.printer(ut.default_shape)

printer("Hello!!")
print(ShapeMaker("circle"))

print(f"This is the app.py")
print(__name__)
print(__file__)
print(__doc__)

print("This is util.py from app.py")
print(ut.__name__)
print(ut.__file__)
print(ut.__doc__)



