def html_ext():
    import requests
    import json
    url = 'https://api.vision.teleporthq.io/v2/detection'
    body = {"image": "https://i.imgur.com/HzTWzLS.jpg", "threshold": 0.5}
    headers = {'content-type': 'application/json','Teleport-Token':'lh!N4mZnazqa&2h$i9MTP46R%@m*FvFT'}
    #Extract the json data from the file
    r = requests.post(url, data=json.dumps(body), headers=headers)
    x = json.dumps(r.text)
    j = json.loads(r.text)
    return j