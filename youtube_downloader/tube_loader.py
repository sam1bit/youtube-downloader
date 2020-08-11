from pytube import YouTube
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from threading import *


file_size = 0

# to show the progress of download
def progress_of_download(stream=None, chunk=None, bytes_remaining=None):
    global file_size
    #getting the percentage of the file
    file_downloaded = (file_size - bytes_remaining)
    percntg = (file_downloaded / file_size) * 100
    Download_btn.config(text='{:00.0f} % downloaded'.format(percntg))

def startDownload():
    global file_size
    
    try:
        url = urlfield.get()
        # chnaging button text 
        Download_btn.config(text="please wait...")
        Download_btn.config(state=DISABLED)

        path_to_save_video= askdirectory()
        if path_to_save_video is None:
            return
        ob = YouTube(url, on_progress_callback=progress_of_download)
        strm = ob.streams[0]
        file_size = strm.filesize
        strm.download(path_to_save_video)
        Download_btn.config(text="Start Download")
        Download_btn.config(state=NORMAL)
        showinfo("Download Finished","Downloaded successfully")
        urlfield.delete(0,END)

    except Exception as e:
        print(e)
        print("error !!")

def start_Download_Thread():
    # creating thread
    thread = Thread(target=startDownload)
    thread.start()
 

# starting gui building
main=Tk()
main.title("Youtube Downloader")

#seting icon
main.iconbitmap('icon.ico')
main.geometry("500x400")

#creating icon of the gui
File = PhotoImage(file='image.png')
headingIcon = Label(main, image=File)
headingIcon.pack(side=TOP)

#creating field to enter url 
urlfield = Entry(main, width=25, font=("verdana",17),justify= CENTER)
urlfield.pack(side=TOP)

#creating  download button
Download_btn = Button(main, text="start download",command= start_Download_Thread)
Download_btn.pack(side=TOP,pady=10)

main.mainloop()