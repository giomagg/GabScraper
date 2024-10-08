import requests
import json
import pandas as pd
import time
import random

def GabScraper(query, file):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    df = pd.DataFrame()

    for i in range(0, 1000):
        webpage_url = f'https://gab.com/api/v3/search?type=status&onlyVerified=false&q={query}&resolve=true&page={i}'
        response = requests.get(webpage_url, headers=headers)
        if response.status_code == 200:
            print(f"Page {i} - Response status: 200. Gathering Gabs...")
            json_data = json.loads(response.text)
            if 'statuses' in json_data and json_data['statuses']:
                temp_df = pd.json_normalize(json_data['statuses'])
                df = pd.concat([df, temp_df], ignore_index=True)
            else:
                print(f"Page {i} - No statuses found. Breaking the loop.")
                break
        else:
            print(f"Page {i} - Response status: {response.status_code}. Breaking the loop.")
            break


        if i % 15 == 0:
            n = random.randint(1, 10)
            print(f"System sleeping for {n} seconds to avoid rate limits.")
            time.sleep(n)

    df.to_csv(file, compression="zip", index=False)

    print(f"The dataset contains {len(df)} Gabs and it has been saved at {file}.")
