import json
import requests
from tqdm import tqdm

url = 'https://farasa.qcri.org/webapi/diacritize/'
# text = 'يُشار إلى أن اللغة العربية' 
api_key = "aItBxjInUPLFaLZpcq"
index = "/home/jeremy/github/arabic-text-diacritization/dataset/cleaned_test.txt"
output = "/home/jeremy/github/arabic-text-diacritization/existing_systems/farasa_api/fixed_output.txt"

# with open(index) as fp:
#     text = fp.readline().strip()

# text = text.strip()
# payload = {'text': text, 'api_key': api_key}
# data = requests.post(url, data=payload)
# result = json.loads(data.text)
# print(result)   


with open(index) as fp:
    lines = fp.readlines()

with open(output, "w") as fo:
    for text in tqdm(lines):
        text = text.strip()
        payload = {'text': text, 'api_key': api_key}
        data = requests.post(url, data=payload)

        if data.status_code == 200:
            result = json.loads(data.text)
            fo.write(result["text"] + "\n")

        elif data.status_code == 400:
            print("Bad request.")

        else:
            print(data)
            breakpoint()
            print()
        
