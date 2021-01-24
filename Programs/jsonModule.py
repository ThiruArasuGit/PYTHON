import json

data = '''{"Employee": [
{"name": "Thiru", "Age": 35, "Height": 157.6, "Married": "true", "Job Status": null},
                     {"name": "MK", "Age": 35, "Height": 152.6, "Married": "true", "Job Status": null},
                     {"name": "Gsg", "Age": 31, "Height": 167.6, "Married": "true", "Job Status": null},
                     {"name": "Roshan", "Age": 34, "Height": 154.6, "Married": "true", "Job Status": null}
                     ]
          }'''

# Convert un-formatted JSON to python object
python_data = json.loads(data)

# print("Python Data: \n\n" + str(python_data))

for rec in python_data['Employee']:
    del rec['Job Status']

# Convert to JSON
json_str = json.dumps(python_data, indent=2)
# print("Json data: \n\n" + json_str)

# remove an element and save the file as json.

with open('C:/GWS/VS_IDE/Python/movie_sample.txt', 'r', encoding='utf-8') as json_txt:
    python_data_obj = json.load(json_txt)

del python_data_obj['budget']
# print(python_data_obj)

with open('C:/GWS/VS_IDE/Python/movie_sample.json', 'w', encoding='utf-8') as json_txt:
    json.dump(python_data_obj, json_txt, indent=2, ensure_ascii=False)
