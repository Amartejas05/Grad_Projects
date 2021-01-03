#Name:Amartejas Manjunath
#ID no: 1001742606

import socket              # To create socket
import sys                  # system commands
import os                       # create directory
import PySimpleGUI as sg            # for GUI
import threading                        # for threading
import queue                                # for monitor
import time
import itertools
import numpy as np                              # to generate random number
from watchdog.observers import Observer             # For watchdog to watch
from watchdog.events import FileSystemEventHandler      # for watchdog
import glob

fname = ""
val = ""
paths = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8585))
prob = "11"
#count = 0

# A class to take action when a file in added to the shared directory

class Myhandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':             # A event when file in uploaded to the shared directory
            # Take any action here when a file is first created.
            print("Received modified event - %s" % event.src_path)
            #paths.append(event.src_path)
            sg.PopupTimed('File updated in Directory', auto_close_duration=8, non_blocking=True)
            sendfile(event.src_path)     # send the file path detected to sendfile function to send the file to server
        elif event.event_type == 'deleted':
            print("Deleted")
            pd = event.src_path
            print(pd)
            td = threading.Thread(target=delete, daemon=True, args=(pd, ))
            td.start()

def delete2():
    print("voting to delete or not")
    time.sleep(3)
    prob = np.random.randint(2, size=1)
    prob = prob[0]
    print(prob)
    prob = str(prob)
    prob = bytes(prob, encoding="utf-8")
    s.send(prob)
    print("vote sent")
def delete(fname1):
    messa = val + 'is coordinator'
    sg.PopupTimed(messa, auto_close_duration=3, non_blocking=True)
    fname1 = fname1.split(val)[1]
    fname1 = fname1.replace("\\", "")
    text = "vote&" + fname1
    print(text)
    text = bytes(text, encoding="utf-8")
    s.send(text)

# This Function is used to send the username to the server to check for duplicates and create a directory with the user.

def conn(usr):
    username = str(usr)                       # Save the username
    print(username)
    username = bytes(username, encoding='utf8')  # convert the username to bytes to send
    s.send(username)                              # send the username to server to check
    reply = s.recv(1024)                            # Receive the reply from server about the username
    reply1 = reply.decode("utf8")                     # convert the sent data to string
    print("reply1", reply1)
    if reply1 == "connected":                           # check if connected
        print("Connected")
        sg.PopupTimed('Connected', auto_close_duration=8, non_blocking=True)  # using GUI to pop a window to show connected
        if not os.path.exists(username):
            os.mkdir(username, 777)                         # if a file of same name does not exist create a directory
        tt = threading.Thread(target=monitor, args=(username,), daemon=True) # Start a thread to monitor the shared directory
        tt.start()
        #tt.join()
        #monitor(username)
    else:
        sg.PopupTimed('Change Username', auto_close_duration=8, non_blocking=True)
# This function is to stop the client from sending files in a loop so client will not send files that a it recieved from the server

# also send file to server which was put in shared directory

def sendfile(filename):
    if "received" in filename:
        return
    print("filename:", filename)
    file = open(filename, 'r')  # open file in read mode from the shared directory
    data = file.read(1024)  # read the file
    data = str.encode(data)  # encode the file to send
    print("data", data)
    filename = bytes(filename, encoding="utf-8")
    s.send(filename)
    s.send(data)# Send data to the server
    print("sent")


# This function is part of the watchDog library which monitors a folder
# https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
# Also sending the file in shared directory, to the server

def monitor(usr1):
    usr1 = usr1.decode("utf8")
    event_handler = Myhandler()                                        # Assigning handler class
    observer = Observer()                                              # assign observer class
    pathFile = r"C:\Users\Amar\Project" + "\\" + usr1                  # assigning the shared directory to be watched
    #paths.append(usr1)
    observer.schedule(event_handler, path=pathFile, recursive=False)  # schedule class to set up watcher
    observer.start()                                                  # start the watcher
    print("Receving")
    try:
        while True:
            time.sleep(1)               # keep checking every second
            filename12 = s.recv(1024)   # waiting for invalidation
            filename12 = filename12.decode("utf-8")
            print("down", filename12)
            if "deleting file" in filename12:
                global fname
                fname = filename12.split("&")[1]
                td2 = threading.Thread(target=delete2, daemon=True)
                td2.start()
            elif filename12 == "abort":
                path2 = val + "\**"
                configfiles = glob.glob(path2, recursive=True)
                print(configfiles)
                for x in configfiles:
                    if fname in x:
                        f = open(x, 'r')
                        data = f.read(1024)
                        f.close()
                        data = bytes(data, encoding="utf-8")
                        s.send(data)
            elif filename12 == "commit":
                path1 = val + "\**"
                print(path1)
                configfiles = glob.glob(path1, recursive=True)
                print(configfiles)
                for x in configfiles:
                    if fname in x:
                        os.remove(x)
            else:
                data = s.recv(1024)         # receiving file from server
                data = data.decode("utf-8")
                filename2 = pathFile
                filename21 = "{}\\received_{}".format(filename2, filename12)   # add a received tag to filename
                print(filename21)
                file = open(filename21, 'w')                                             # open file to write
                file.write(data)                                                            # write the data on file
                file.close()                                                                  # close the file
    except KeyboardInterrupt:
        observer.stop()  # close watcher
    observer.join()


if __name__ == '__main__':     # This is where the Program for client begins everytime
    layout = [
        [sg.Text('Please enter Username')],
        [sg.Text('Client  Username', size=(15, 1)), sg.InputText()],
        [sg.Button("Connect 1"), sg.Button("Kill")],
    ]                                  # The GUI for client to accept the the username, it has connect and kill buttons

    window = sg.Window('File sharing Client-Server', layout)

    # The window function used from PySimpleGUI to create the above layout and give the window name

    # Starting a loop to take the input values and create a event f or the button click.

    while True:
        event, values = window.Read()                             # Read the values and events from the GUI
        print(event, values)
        val = str(values[0])                                  # Store username from imput to the variable val
        if event == "Connect 1":                                  # Once the Button is clicked
            t1 = threading.Thread(target=conn, args=(val,), daemon=True) # Creating a Thread to
            t1.start()                                            # Start the Thread
            #t1.join()
        elif event == "Kill":                           # If kill Button is clicked close the connection and the window
            s.close()
            break
    window.Close()

