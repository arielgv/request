import requests

def get_from_page():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print('------------')
    if r.status_code == 200: 
        print('200 Means everything was fine')
    else:
        print('something went wrong with the link')
    print(r.text)
    print('---------------------')
    print('---------------------')
    jason = r.json()
    print(jason)
    print(type(jason))
    
    for category in jason:
        print(category['name'])