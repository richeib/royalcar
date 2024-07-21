import requests
import json

HEADERS = {
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    # 'cookie': cookie
}
URL = "https://api-v2.royaldrive.in/api/allvehicles?page=1&noRdMini=1&type=CAR&undefined"
def fetching_data():
    response=requests.get(URL,headers=HEADERS)
    data= response.json()

    with open('data.json','w')as f:
        json.dump(data,f, indent=4)
        
        
                
fetching_data()
