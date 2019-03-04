import requests
from dateutil import parser
from .local_settings import key
import os


secret = key

def query_mars_api(date):
    'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY'
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
    #date = '2015-6-3'

    parameters = {'earth_date':date, 'api_key':secret}

    r = requests.get(url,parameters)

    return r


def download_photos(response, date):
    # Each query by earth-date returns 4 images. One from each of the cameras.
    camera_names = ['frontLeft','frontRight', 'rearLeft', 'rearRight']
    # Get the full path of the current directory
    root = os.path.dirname(os.path.realpath(__file__))
    for i in range(4):
        # Get the image source from the Mars Rover API response.
        img_url = response.json()['photos'][i]['img_src']
        # Response from API
        raw_jpg = requests.get(img_url)
        filename =os.path.join(root,'photos', date, camera_names[i]+'.jpg')
        # If the directory with the given date does not exist, create it. 
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename,'wb') as f:
            f.write(raw_jpg.content)
        

# Read dates from text file using the filename.
def get_date_from_file(filename):
    dates = []
    with(open(filename,'r')) as file:
        w_file = open('error.txt','w')
        lines = file.readlines()
        for line in lines:
            try:
                date = parser.parse(line)
                # Convert date to string with format: 'Y-m-d'
                str_date = date.strftime("%Y-%m-%d")
                dates.append(str_date)
            except:
                w_file.write(line)
            
    file.close()
    w_file.close()
    return dates

# Read dates from a file handle
def read_dates(input_file):
    dates = []
    w_file = open('error.txt','wb')
    lines = input_file.readlines()
    for line in lines:
        try:
            date = parser.parse(line)
            # Convert date to string with format: 'Y-m-d'
            str_date = date.strftime("%Y-%m-%d")
            dates.append(str_date)
        except:
            # Write the bad dates to an error file. 
            # TODO Show bad date to user.
            w_file.write(line)
            
    input_file.close()
    w_file.close()
    return dates

def process_query(file):
    dates = read_dates(file)
    for date in dates:
        response = query_mars_api(date)
        download_photos(response,date)


if __name__ == "__main__":
    get_date_from_file('dates.txt')