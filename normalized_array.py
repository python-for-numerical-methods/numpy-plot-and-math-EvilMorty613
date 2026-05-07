import numpy as np

def normalize_array(input_array):
    arr = np.array(input_array)
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    if max_val == min_val:
        return np.zeros_like(arr)
    
    return (arr - min_val) / (max_val - min_val)


# Test (optional)
if __name__ == "__main__":
    test_data = [10, 20, 30, 40, 50]
    print("Original:", test_data)
    print("Normalized:", normalize_array(test_data))
