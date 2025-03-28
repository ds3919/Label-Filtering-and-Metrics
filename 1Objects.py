import csv
import pandas as pd
import xml.etree.ElementTree as ET
import os

xml_folder = input("XML Folder Path: ")

xml_files = []

for xml_file in os.listdir(xml_folder):
    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()
    filename = root.find('filename').text.replace('.jpg', '')
    for obj in root.findall('object'):
        object_name = obj.find('name').text
        xml_files.append({'filename': filename, 'object_name': object_name})

xmls = pd.DataFrame(xml_files)

print(xmls)


filenames = xmls['filename'].tolist()
objects = []
singleObjectFilenames = []
filenamesLen = len(filenames)

if filenames[0] != filenames[1]:
    singleObjectFilenames.append(filenames[0])
    objects.append(xmls['object_name'][0])

for fIndex in range(1, filenamesLen-1):
    if filenames[fIndex-1] != filenames[fIndex] and filenames[fIndex+1] != filenames[fIndex]:
        singleObjectFilenames.append(filenames[fIndex])
        objects.append(xmls['object_name'][fIndex])

if filenames[filenamesLen-2] != filenames[filenamesLen-1]:
    singleObjectFilenames.append(filenames[filenamesLen-1])
    objects.append(xmls['object_name'][filenamesLen-1])


filteredXMLs = pd.DataFrame({'filename':singleObjectFilenames, 'object_name': objects})

for i in range(0, len(objects)-1):
    print(singleObjectFilenames[i], objects[i])

filteredXMLs.to_csv("filtered1ObjectXMLs.csv", index=False)
