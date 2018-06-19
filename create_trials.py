import csv
from psychopy import data
import numpy as np

newConditions = [] # define an initially empty list 
for fileName in ['conditions_v2-1.xlsx', 'conditions_v2.xlsx']: 
    conditions = data.importConditions(fileName) # create a list of dictionaries 
    np.random.shuffle(conditions) # randomise their order 
    conditions = conditions[0:10] # select just ten of them 
    newConditions.extend(conditions) 
    # will end up as 20 randomly selected but balanced-for-consistency trials 

# write out the conditions for this run of the experiment 
header = newConditions[0].keys() # get the header labels as a list
with open('newConditionList1.csv','w') as file: # create a new CSV file 
    output = csv.DictWriter(file, fieldnames=header) # arrange to write our dictionaries to it 
    output.writeheader() 
    output.writerows(newConditions)

