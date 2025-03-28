import csv
import pandas as pd
import os

#Obtain file paths and column names
objectList_path = input("ObjectList Direct File Path: ")
predictionList_path = input("PredictionList Direct File Path: ")
objectListFilenameColumn = input("ObjectList Filename Column: ")
objectListObjectColumn = input("ObjectList Object Column: ")
predictionListFilenameColumn = input("PredictionList Filename Column: ")
predictionListObjectColumn = input("PredictionList Object Column: ")

#Initialize dataframes
objectList = pd.read_csv(objectList_path, dtype=str)
predictionList = pd.read_csv(predictionList_path, dtype=str)

print(objectList.dtypes)
print(predictionList.dtypes)

TP = 0
FP = 0
FN = 0
TN = 0

objectListLen = len(objectList)
predictionListLen = len(predictionList)

#Format elements of files to make comparisons easy
predictionList[predictionListObjectColumn] = predictionList[predictionListObjectColumn].str.replace(' ', '', regex=True)
predictionList[predictionListFilenameColumn] = predictionList[predictionListFilenameColumn].str.split('.')[0]

objectList = objectList.sort_values(by=objectListFilenameColumn, ignore_index=True)
predictionList = predictionList.sort_values(by=predictionListFilenameColumn, ignore_index=True)
print(objectList)
print(predictionList)
i = 0

for j in range(0, objectListLen, 1):
    olfile = objectList[objectListFilenameColumn][j].lower()
    plfile = predictionList[predictionListFilenameColumn][i].lower()
    
    if olfile == plfile:
        tempTP = TP
        for k in range(i, predictionListLen):
            tempPLFile = predictionList[predictionListFilenameColumn][k].lower()
    
            if olfile == tempPLFile:
                olobj = objectList[objectListObjectColumn][j].lower()
                plobj = predictionList[predictionListObjectColumn][k].lower()

                if olobj == plobj:
                    TP += 1
                else: 
                    FP += 1
            
            else:
                if tempTP == TP:
                    FN += 1
                i = k
                break
    
    elif i == predictionListLen-1:
        FN += objectListLen-j+1
        break

    else:
        FN += 1
        continue

print("TP:", TP, "\nFP: ", FP, "\nFN: ", FN)

print("Accuracy:", ((TP+TN)/(TP+TN+FP+FN)))
print("Recall:", (TP/(TP+FN)))
