import requests
import time

def check_website(url):
    try:
        response=requests.get(url)
        return response.status_code==200
    except requests.RequestException as e:
        print(f"Error checking Website {e}")
        return False
    
def main():
    url='https://github.com/kahyaburak/isWebsiteServerUp' # Enter the website url inside the quotation marks
    interval=60

    while True:
        if check_website(url):
            print("Website is Up")
            break
        else:
            print ("Website is Down")

        time.sleep(interval)

if __name__=="__main__":
    main()