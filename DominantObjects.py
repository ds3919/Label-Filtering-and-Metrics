import csv
import os
import pandas as pd
import xml.etree.ElementTree as ET
from collections import Counter

xml_folder = "../Annotations"

data = []  # List to store extracted data

for xml_file in os.listdir(xml_folder):
    if not xml_file.endswith(".xml"):  # Ensure only XML files are processed
        continue

    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()
    
    filename = root.find("filename").text.replace(".jpg", "")

    for obj in root.findall("object"):
        object_name = obj.find("name").text
        bndbox = obj.find("bndbox")
        bbox = {
            "xmin": int(bndbox.find("xmin").text),
            "ymin": int(bndbox.find("ymin").text),
            "xmax": int(bndbox.find("xmax").text),
            "ymax": int(bndbox.find("ymax").text),
        }
        
        # Append as a row to the list
        data.append([filename, object_name, bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"]])

# Create DataFrame
df = pd.DataFrame(data, columns=["Filename", "Object", "Xmin", "Ymin", "Xmax", "Ymax"])

# Display DataFrame
print(df)

ymax = df['Ymax'].tolist()
ymin = df['Ymin'].tolist()
xmax = df['Xmax'].tolist()
xmin = df['Xmin'].tolist()
area = []

filenames = df['Filename'].tolist()
objects = df['Object'].tolist()

for i in range(0, len(ymax)-1):
    area.append((ymax[i]-ymin[i])*(xmax[i]-xmin[i]))


#count = Counter(filenames)

csv_files = []
csv_object = []

'''
for i in range(0, len(filenames)-1):
    population = count[filenames[i]]
    if population == 1:
        csv_files.append(filename[i])
        csv_object.append(objects[i])
    elif population > 1:
        '''

max_area = 0
current_file = ""
max_index = 0
print(filenames[0])
for i in range(0, len(filenames)-1):
    if filenames[i] == current_file:
        if area[i] > max_area:
            max_area = area[i]
            max_index = i
    elif filenames[i] != current_file:
        csv_files.append(current_file)
        csv_object.append(objects[i])
        current_file = filenames[i]
        max_area = area[i]
        max_index = i

csv_files.pop(0)
csv_object.pop(0)

for i in range(0, len(csv_files)-1):
    print(csv_files[i], csv_object[i])

csv = pd.DataFrame({'Filename':csv_files, 'Object':csv_object})
csv.to_csv("DominantObjects.csv", index=False)
