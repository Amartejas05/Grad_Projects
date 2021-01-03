# Name:Amartejas Manjunath
# ID no: 1001742606
# NetID:axm2606

import socket  # Create the socket
import sys      # system commands
import threading    # threads
import PySimpleGUI as sg    # for GUI
import time

count = 0
ulist = []
conn_list = []

def disp_usr():
    layout = [[sg.Txt(' ', size=(6, 10), key='output')],
              [sg.Button('Show Clients Connected', bind_return_key=True)]]
    window = sg.Window('Clients', layout)
    while True:
        event, values = window.Read()
        if event is not None:
            window.Element('output').Update((ulist))
        else:
            break

def delete(id):
    print("deleting....")
    for sok in conn_list:  # This loops all the connected client socket values
        if sok != id:
            dell = "deleting file"
            dell = bytes(dell, encoding="utf-8")
            sok.send(dell)
            print("sent")
            while 1:
                a = sok.recv(1024)
                a = a.decode("utf-8")
                print("rere")
                if a == "one":
                    print("abort")
                else:
                    print("deleted")

# This function receives and sends files

def check_usr(id, usr1):
    try:
        while 1:
            print("waiting for file")
            filename = id.recv(1024)
            filename = filename.decode("utf-8")
            print("filename 1", filename)
            if "vote" in filename:
                #t3 = threading.Thread(target=delete, args=id)  # start a thread to send and receive files
                #t3.start()
                global fname
                fname = filename.split("&")[1]
                print(fname)
                print("deleting....")
                for sok in conn_list:  # This loops all the connected client socket values
                    if sok != id:
                        dell = "deleting file&" + fname
                        dell = bytes(dell, encoding="utf-8")
                        sok.send(dell)
                        print("sent")
                time.sleep(5)
                global count
                if count == 2:
                    print("All commit to delete")
                    for sok in conn_list:  # This loops all the connected client socket values
                        if sok != id:
                            comit = "commit"
                            comit = bytes(comit, encoding="utf-8")
                            sok.send(comit)
                            print("commit sent")
                else:
                    global redata
                    rename = usr1 + "\\" + fname
                    file = open(rename, 'w')
                    file.write(redata)
                    file.close()
            elif filename == "0":
                print("abort")
                comit = "abort"
                comit = bytes(comit, encoding="utf-8")
                id.send(comit)
                print("sent abort")
                redata = id.recv(1024)
                redata = redata.decode("utf-8")
            elif filename == "1":
                count = count + 1
            else:
                data1 = id.recv(1024)
                # sg.PopupTimed('Invalidation from' + usr1, auto_close_duration=8, non_blocking=True)
                filename = filename.split(usr1)[1]
                filename = filename.replace("\\", "")
                print("filename", filename)
                filename = bytes(filename, encoding="utf-8")
                data1.decode("utf8")
                print("data", data1)
                for sok in conn_list:  # This loops all the connected client socket values
                    if sok != id:  # If the value is not equal to the current connected socket then send the file to that socket
                        sok.send(filename)
                        sok.send(data1)  # send the file to other two sockets which did not send the file to the server


    except:
        ulist.remove(usr1)
        s.close()
        exit(0)

if __name__ == '__main__':                  # The execution starts here
    try:
        t2 = threading.Thread(target=disp_usr,)  # start a thread to send and receive files
        t2.start()
        host = ''
        port = 8585                             # Assign a port number
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create a socket
        # using IPv4 and TCP connection
        print("socket created")

        try:
            s.bind((host, port))  # binding the server socket with host IP and port number
        except socket.error:
            print("Cannot bind")

        print("Binding complete")

        while 1:
            s.listen(10)                                # waiting for Connections
            clientsocket, addr = s.accept()             # Accept the connection
            data = clientsocket.recv(1024)               # receive the username
            data = data.decode("utf-8")                     # decode the username
            print(data)
            username = data
            if str(username) in ulist:                          # check for username duplicates
                reply = "Change Username"
                reply = bytes(reply, encoding="utf8")
                clientsocket.send(reply)                    # Send the reply to the client
                clientsocket.close()                        # close the socket if duplicate is present
                continue
            else:
                conn_list.append(clientsocket)              # Add the successful connection to the to a list
                reply = "connected"
                reply = bytes(reply, encoding="utf8")
                clientsocket.send(reply)                    # Send to the reply to client
                ulist.append(str(username))
                print(ulist)
            t1 = threading.Thread(target=check_usr, args=(clientsocket, username))    # start a thread to send and receive files
            t1.start()
            # t1.join()

    except:
        exit(0)















