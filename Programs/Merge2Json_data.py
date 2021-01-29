import json
import requests

# Get the all USA states and their abbreviations from a website
req = requests.get(
    r'https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json',
    stream=True)
state_data = json.loads(req.content)
state_data_sorted = json.dumps(state_data, sort_keys='name')
print(state_data_sorted)
js_sd = json.loads(state_data_sorted)
print(type(js_sd))

# Get area codes of all the states from local machine json txt file.
with open(r'C:/GWS/VS_IDE/Python/state_areacodes.txt') as stateCodeFile:
    area_data = json.load(stateCodeFile)
area_data_sorted = json.dumps(area_data, sort_keys="State")
print(area_data_sorted)
js_ad = json.loads(area_data_sorted)
print(type(js_ad))

for state_rec in js_sd:
    for area_rec in js_ad:
        if state_rec["name"] == area_rec["State"]:
            print("Matching")
        else:
            print("Not Matching")