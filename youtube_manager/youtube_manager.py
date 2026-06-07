import json


def save_data_helper(videos):
    with open("youtube_manager/youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print("*" * 50)
        print(f"Index : {index}, Name : {video['name']}, Duration : {video['time']}")
    print("*" * 50)


def add_video(videos):
    name = input("enter video name: ")
    time = input("enter video time :")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    vid_up_index = int(input("Enter the video ID that you want to update : "))
    if 1 <= vid_up_index <= len(videos):
        name = input("Enter the video name : ")
        time = input("Enter the time : ")
        videos[vid_up_index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print(f"video with id : {vid_up_index} deleted")
    else:
        print("Invalid index!!!")


def delete_video(videos):
    list_all_videos(videos)
    vid_del_index = int(input("Enter the video ID that you want to deleted : "))
    if 1 <= vid_del_index <= len(videos):
        del videos[vid_del_index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index selected!!!")


def load_data():
    try:
        with open("youtube_manager/youtube.txt", "r") as file:
            test = json.load(file)
            # print(test)
            return test
    except FileNotFoundError:
        return []


def main():

    videos = load_data()

    while True:
        print("\n")
        print("Welcome to youtube manager app!!!")
        print("Choose any one option : ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app.")

        choice = input("Enter your choice : ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice!!!")


if __name__ == "__main__":
    main()
