import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup

# Extract from HTML

HTML_PATH = '/home/gordon_local/local_workplace/swsWorkBringHome/toll_id/toll_tag_id_source.html'
html = open(HTML_PATH, 'rb')
soup = BeautifulSoup(html, 'html.parser')
all_box = soup.find_all('div', class_='tagDetailsBox')

def capture_plate_b(box_elem : object):
    data = []
    
    all_b = box_elem.find_all('b')
    
    data = [b.text if b else 'No B' for b in all_b]
    
    plate = plate = box_elem.find('center', class_='tagPlateRego')
    
    if plate:
        data.append(plate.text)
    else:
        data.append("No_Plate")
        
    return data

# It becomes 2d array 
new = [capture_plate_b(box) for box in all_box]


# 2d array to DF
df = pd.DataFrame(new, columns=['Tag_ID', 'Date', 'Vehicle_type', 'Payment_method', 'rego'])

df['rego'] = [df.rego.iloc[i] if df.Payment_method.iloc[i] == 'Deposit' else df.Payment_method.iloc[i] for i, pay_method in enumerate(df.Payment_method)]


df['Date'] = df.Date.str.replace('[^\d|/]+','' ,regex=True)




