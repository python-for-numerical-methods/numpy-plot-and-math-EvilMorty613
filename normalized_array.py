import numpy as np

def normalize_array(input_array):
    arr = np.array(input_array)
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    if max_val == min_val:
        return np.zeros_like(arr)
    
    return (arr - min_val) / (max_val - min_val)
