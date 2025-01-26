import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list) 

    mean_1 = [arr[[0,3,6]].mean(), arr[[1,4,7]].mean(), arr[[2,5,8]].mean()]
    mean_2 = [arr[[0,1,2]].mean(), arr[[3,4,5]].mean(), arr[[6,7,8]].mean()]
    
    var_1 = [arr[[0,3,6]].var(), arr[[1,4,7]].var(), arr[[2,5,8]].var()]
    var_2 = [arr[[0,1,2]].var(), arr[[3,4,5]].var(), arr[[6,7,8]].var()]

    std_1 = [arr[[0,3,6]].std(), arr[[1,4,7]].std(), arr[[2,5,8]].std()]
    std_2 = [arr[[0,1,2]].std(), arr[[3,4,5]].std(), arr[[6,7,8]].std()]
    
    max_1 = [arr[[0,3,6]].max(), arr[[1,4,7]].max(), arr[[2,5,8]].max()]
    max_2 = [arr[[0,1,2]].max(), arr[[3,4,5]].max(), arr[[6,7,8]].max()]    

    min_1 = [arr[[0,3,6]].min(), arr[[1,4,7]].min(), arr[[2,5,8]].min()]
    min_2 = [arr[[0,1,2]].min(), arr[[3,4,5]].min(), arr[[6,7,8]].min()]
    
    sum_1 = [arr[[0,3,6]].sum(), arr[[1,4,7]].sum(), arr[[2,5,8]].sum()]
    sum_2 = [arr[[0,1,2]].sum(), arr[[3,4,5]].sum(), arr[[6,7,8]].sum()]

    calculations = {
      'mean': [mean_1, mean_2, arr.mean()],
      'variance': [var_1, var_2, arr.var()],
      'standard deviation': [std_1, std_2, arr.std()],
      'max': [max_1, max_2, arr.max()],
      'min': [min_1, min_2, arr.min()],
      'sum': [sum_1, sum_2, arr.sum()]
    }
    return calculations
