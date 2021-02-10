import xmltodict
import json
import os

xml_path = r'C:\Users\1022589\Downloads\Cleaned_MATMAS_IDOC.xml'

with open(xml_path) as xml_file:
    xml_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

header_json = {"Header": {"Message type": "BYDM", "Version": "2020.3.4"}}
header_json.update(xml_dict)
json_data = json.dumps(header_json, indent=2)

# print(json_data)

with open(r'C:\Users\1022589\Downloads\Cleaned_MATMAS_IDOC.json', 'w') as json_file:
    json_file.write(json_data)
    json_file.close()


file_dir = os.walk(r'C:\Users\1022589\Downloads\xml')
for (d, sd, files) in file_dir:
    for file in files:
        print(file)
