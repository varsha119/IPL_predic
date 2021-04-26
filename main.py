### Imports ###
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

#path = "C:/Users/Varsha/Downloads/ipl_csv2_mujeer"
#os.path.join(path, "C:/Users/Varsha/Downloads/ipl_csv2_mujeer", "all_matches.csv")
#raw_data = pd.read_csv(path)
# add imports - classes and defs
from predictor import predictRuns


"""
sys.argv[1] is the input test file name given as command line arguments

"""
runs = predictRuns('inputFile.csv')
print("Predicted Runs: ", runs)