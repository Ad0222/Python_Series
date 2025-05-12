import sqlite3
conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')
def list_videos():
    cursor.execute("SELECT * FROM Videos")
    for raw in cursor.fetchall():
        print(raw)

def Add_video(name,time):
    cursor.execute("INSERT INTO Videos(name,time) values (?,?)",(name,time))
    conn.commit()

def Update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE Videos SET name=?,time=? WHERE id=?" ,(new_name ,new_time ,video_id ))
    conn.commit()

def Delete_video(video_id):
    cursor.execute("DELETE FROM videos where id=?",(video_id) ,)
    conn.commit()

def main():
    while True:
        print("\n youtube manager sqllite3")
        print("1.List videos")
        print("2.Add videos")
        print("3.Update videos")
        print("4.Delete videos")
        print("5.Exit app")
        choice=input("Enter your choice: ")
        if choice=='1':
          list_videos()

        elif choice=='2':
           name=input("Enter a name: ")
           time=input("Enter a time: ")
           Add_video(name,time)

        elif choice=='3':
            video_id=input("Enter a video ID Update: ")
            name=input("Enter a video name: ")
            time=input("Enter a video time: ")
            Update_video(video_id,name,time)

        elif choice=='4':
            video_id=input("Enter a video Id Delete: ")
            Delete_video(video_id)

        elif choice=='5':
            break
         
        else:
            print("invalid choice")

    conn.close()

if __name__=="__main__":
    main()