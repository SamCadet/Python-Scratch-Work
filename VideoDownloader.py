import tkinter as tk
from pytube import YouTube


def downloadVid():
    global E1
    string = E1.get()
    print(string)
    yt = YouTube(str(string))
    videos = yt.get_videos()
    s = 1
    for v in videos:
        print(str(s) + '.' + str(v))
        s += 1
    n = int(input("Enter a number to choose the video you want: "))
    vid = videos[n - 1]
    destination = str(input("Enter file location for your downloaded video: "))
    vid.download(destination)
    print(f'\n{n} has been downloaded.')


root = tk.Tk()
w = tk.Label(root, text='YouTube Downloader')
w.pack()

E1 = tk.Entry(root, bd=5)
E1.pack(side=tk.TOP)

button = tk.Button(root, text="Download", fg="red", command=downloadVid())

root.mainloop()
