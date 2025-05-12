import requests
import json

def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    respose=requests.get(url)
    data=respose.json()

    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed")
    
def main():
    try:
        username,country=fetch_random_user_freeapi()
        print(f"username:{username}\ncountry:{country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()