import numpy as np

def calculate(list):
  
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

    arr = np.array(list)
    matrix = arr.reshape(3,3)

    describe = {
      'mean': 'mean', 
      'variance': 'var', 
      'standard deviation': 'std', 
      'max': 'max', 
      'min': 'min', 
      'sum': 'sum'}

    calculations = {
      label: [
        getattr(matrix, method)(axis=0).tolist(),
        getattr(matrix, method)(axis=1).tolist(),
        getattr(arr, method)().tolist()
      ] for label, method in describe.items()
    }

    return calculations