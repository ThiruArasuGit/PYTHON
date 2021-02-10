import json
import xmltodict

xml_path = r'C:\Users\1022589\Downloads\order-cona-1.xml'

with open(xml_path) as xml_file:
    xml_dict = xmltodict.parse(xml_file.read())
    if xml_file.closed == 'False':
        xml_file.close()


json_data = json.dumps(xml_dict, indent=2)
print(f'The json formatted file content: \n {json_data}')
print(f'xml file closed: {xml_file.closed}')

with open (r'C:\Users\1022589\Downloads\order-cona-1.json', 'w') as json_file:
    json_file.write(json_data)
    json_file.close()