import pandas as pd

#Old ObjectList and PredictionList
oldOL_path = input("OldObjectList Direct File Path: ")
oldPL_path = input("OldPredictionList Direct File Path: ")
oLF = input("OldObjectList Filename Column: ")
oLO = input("OldObjectList Object Column: ")
pLF = input("OldPredictionList Filename Column: ")
pLO = input("OldPredictionList Object Column: ")

#Merged elements/the filter
filter = set(input("List of merged elements: ").split(', '))

#Initialize dataframes with formatted data
oldOL = pd.read_csv(oldOL_path)
oldPL = pd.read_csv(oldPL_path)
oldPL[pLF] = oldPL[pLF].str.split('.').str[0]

exclusion = set()
drops = []

for i in range(len(oldOL)):
    if str(oldOL[oLO][i]) not in filter:
        exclusion.add(str(oldOL[oLF][i]))
        drops.append(i)

newOL = oldOL.drop(axis=0, index=drops)
print(exclusion)
newPL = oldPL[~oldPL[pLF].astype(str).isin(exclusion)]


newOL.to_csv('ObjectList.csv', index=False)
newPL.to_csv('PredictionList.csv', index=False)