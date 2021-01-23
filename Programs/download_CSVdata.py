"""
1. Download the list of csv files from data world
2. Name the CSV files like downloaded_csv_1.csv
"""

from utilFile import download_csv_data

# CSV web urls are part of the list
'''
csv_url = [r'https://query.data.world/s/a3enqvytj64p2s7shuudvydwjhdqlq',
           r'https://query.data.world/s/lfxtifseqwj2bwkzlcdak45x3gyj44',
           r'https://query.data.world/s/buxhjexptv753sdsppjgbgtq7pillm']
'''
# CSV web urls are part of the dictionary.

csv_url_dict = {"inc500euSummary.csv": r'https://query.data.world/s/a3enqvytj64p2s7shuudvydwjhdqlq',
                "DiversityList-Worldwide-Grid.csv": r'https://query.data.world/s/lfxtifseqwj2bwkzlcdak45x3gyj44',
                "Forbes Cloud 100.csv": r'https://query.data.world/s/buxhjexptv753sdsppjgbgtq7pillm'
                }

csv_dest = r'C:/GWS/csv_files/'

'''
for i in range(1, len(csv_url) + 1):
    csv_filename = 'download_csv_' + str(i) + '.csv'
    csv_idx_url = csv_url[i - 1]
    rv = download_csv_data(csv_idx_url, csv_filename, csv_dest)
    print(rv)
'''
for (k, v) in csv_url_dict.items():
    ret_val = download_csv_data(url=v, file_name=k, dest=csv_dest)
    print(ret_val)
