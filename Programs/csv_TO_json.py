import csv
import json

'''
with open('names.csv','r') as f:
    reader = csv.reader(f)
    next(reader)

    data_dict = {"Persons":[]}

    for rows in reader:
        data_dict["Persons"].append({"First_name":rows[0],"Age":rows[1]})

with open('names.json','w',encoding='utf-8') as jf:
    json.dump(data_dict,jf,indent=2)
'''

with open("C:/GWS/csv_files/inc500euSummary.csv") as cf:
    reader = csv.reader(cf)
    next(reader)

    data_dict = {"AllData": []}

    for row in reader:
        data_dict["AllData"].append({
            "Url": row[0],
            "Rank": row[1],
            "City": row[2],
            "Growth": row[3],
            "Company": row[4],
            "Country": row[5],
            "Revenue": row[6],
            "Industry": row[7],
            "Years_on_list": row[8]
        })

with open("C:/GWS/json_files/inc500euSummary.json", 'w', encoding='utf-8') as jf:
    json.dump(data_dict, jf, indent=2)
