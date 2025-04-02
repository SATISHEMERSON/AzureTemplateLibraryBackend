import urllib.request
import json
import re
import dotenv
import os
import sys
dotenv.load_dotenv()

def extract_data():
    try:
        pass
    except Exception as e:
        pass
        raise e

def cost_analysis(data):
    try:
        url = os.environ.get('OPENAI_API_ENDPOINT')
    
        hdr ={
            # Request headers
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'API-Key': os.environ.get('OPENAI_API_KEY'),
        }
        user_requirements = {
            "useCase": data['useCase'],
            "accessFrequency": data['accessfrequency'],
            "redundancy": data['redundancy'],
            "performance": data['performance'],
            "budget": data['budget'],
            "location": data['location'],
            "security": {
                "encryption": True,
                "privateNetworking":  True if data['security'] == 'private' else False,
                "publicAccess": True if data['security'] == 'public' else False
            },
            "features": {
                "softDelete": True,
                "versioning": True,
                "accessLogs": False
            },
            "userComments": data['usercomment']
        }
        data = {
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an Azure cloud expert. Based on the user's high-level storage requirements, "
                        "generate a valid JSON configuration for Azure Storage Account REST API deployment."
                        "**only the JSON configuration** for Azure Storage Account REST API deployment. Provide no other text or explanation."
                        "requested json should follow below format"
                        "\{\"sku\": {\"name\": \"\"},\"kind\": \"\",\"properties\": {\"accessTier\": \"\"}\, \"cost\": \"\"(display cost in USD)\}"
                    )
                },
                {
                    "role": "user",
                    "content": json.dumps(user_requirements)
                }
            ],
            "max_tokens": 500
        }
        # Request body
        data = json.dumps(data)
        req = urllib.request.Request(url, headers=hdr, data = bytes(data.encode("utf-8")))
        req.get_method = lambda: 'POST'
        response = urllib.request.urlopen(req)
        # print(response.getcode())
        res = json.loads(response.read())
        res['choices'][0]['message']['content'] = res['choices'][0]['message']['content'].replace('\n', '')
        # print(res)
        res_data_list = {}
        for choice in res['choices']:
            # print(choice['message']['content'])
            matches = re.findall(r'```json(.*?)```', choice['message']['content'], re.DOTALL)
            # data = re.sub(r'json', '', choice['message']['content']).strip()
            for idx, match in enumerate(matches, start=1):
                # print(f"Code Block {idx}:\n{match.strip()}\n")
                openairesdata = json.loads(match.strip())
                resData = {}
                resData['sku'] = openairesdata['sku']['name']
                resData['accessTier'] = openairesdata['properties']['accessTier']
                resData['kind'] = openairesdata['kind']
                resData['cost'] = openairesdata['cost']
                res_data_list = resData
        return res_data_list
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
