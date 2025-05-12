# password="UNqoblOlKSDm4T1F"
# username="dhakadamit53"
# url="mongodb+srv://dhakadamit53:<db_password>@test-pro-db.8vl0q.mongodb.net/"
from pymongo import MongoClient
from bson import ObjectId

client=MongoClient("mongodb+srv://dhakadamit53:UNqoblOlKSDm4T1F@test-pro-db.8vl0q.mongodb.net/", tlsAllowInvalidCertificates=True)

print(client)
db=client["ytmaneger"] 
videos_collection=db["videos"]

#print(videos_collection)

def list_videos():
    for video in videos_collection.find():
        print(f"ID:{video['_id']}, name:{video['name']} and time:{video['time']}")

def Add_videos(name,time):
    videos_collection.insert_one({"name": name,"time": time})

def update_videos(video_id,new_name,new_time):
    videos_collection.update_one({'_id':ObjectId(video_id)},{'$set':{"name":new_name,"time":new_time}})

def delete_videos(video_id):
    videos_collection.delete_one({"_id":video_id})

def main():
  while True:
    print("Youtube manager App")
    print("1. List all videos")
    print("2. Add new videos")
    print("3. update a videos")
    print("4. Delete a videos")
    print("5. Exit the app")
    choice=input("Enter a choice :")

    if choice=='1':
        list_videos()
    elif choice=='2':
         name=input("Enter a name :")
         time=input("Enter a time :")  
         Add_videos(name,time)
    elif choice=='3':
        video_id=input("Enter a id ")
        name=input("Enter a new name :")
        time=input("Enter a new time :")
        update_videos(video_id,name,time)
    elif choice=='4':
        video_id=input("Enter a id ")
        delete_videos(video_id,name,time)
    elif choice=='5':
        break
    else:
        print("Invalid choice")

if __name__=="__main__":
    main()
