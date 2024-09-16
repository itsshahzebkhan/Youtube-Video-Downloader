# step 1 - to start this project you need to install PyCharm community edition or VS Code
# step 2 - you need to install the "pytube" package from your terminal
# step 3 - you need to import a package that is already installed in PyCharm and VS Code - "tkinter"
# step 4 - start coding 


from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Started downloading")
        download_video(video_url, save_dir)

    else:
        print("Invalid save location")
