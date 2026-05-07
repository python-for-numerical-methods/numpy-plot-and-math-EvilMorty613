import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
    
    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    # המרת הקלט ל-numpy array לצורך חישובים וקטוריים
    data = np.array(data)
    
import numpy as np

def normalize_array(input_array):
    """
    Normalizes a 1D array to [0, 1] using Min-Max scaling.
    Returns zeros if all values are the same.
    """
    arr = np.array(input_array)
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    if max_val == min_val:
        return np.zeros_like(arr)
    
    return (arr - min_val) / (max_val - min_val)


# Test code (you can keep or remove)
if __name__ == "__main__":
    test_data = [10, 20, 30, 40, 50]
    print("Original:", test_data)
    print("Normalized:", normalize_array(test_data))
