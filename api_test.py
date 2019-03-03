import requests
from dateutil import parser


secret = 'SWFea2Tvb928fuN4WvfLP19djXxl1On1LvEPebDx'

def get_photo(date):
    'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY'
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
    #date = '2015-6-3'

    parameters = {'earth_date':date, 'api_key':secret}

    r = requests.get(url,parameters)

    return r

def download_photo(filename, img_url):
    raw_jpg = requests.get(img_url)
    open(filename,'wb').write(raw_jpg)

def get_date_file(filename):
    dates = []
    with(open(filename,'r')) as file:
        w_file = open('error.txt','w')
        lines = file.readlines()
        for line in lines:
            try:
                date = parser.parse(line)
                print(date)
                dates.append(date)
            except:
                w_file.write(line)
            
    file.close()
    w_file.close()
    return dates

#print(r.content)


if __name__ == "__main__":
    '''
    r = get_photo('2015-6-3')
    img = r.json()['photos'][0]['img_src']
    print(img)
    '''
    get_date_file('dates.txt')