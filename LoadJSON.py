import json

def LoadJSON():
    with open('C:\Projects\DIMBoard\DIM.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    LoadJSON()