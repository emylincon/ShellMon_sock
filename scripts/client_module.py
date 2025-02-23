'''
sends data to the server

@author : Saptarshi Ghosh
test
'''


import socket
import time
import random
import fetch_util as util
import json

def send_loop(client_port, host_ip, host_port, buffer_size=1024, cpu_interval=2, delay=1, mypass='', intf='eth0', is_wl=True):
    print('================= TRANSMISSION INITIATED ==============')

    #initiate socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0',client_port))
    s.connect((host_ip, host_port))

    while True:
        try:
            #msg=input('Enter a message : ')
            msg=util.main_fetch_util(loop=False,
                                     delay=delay,
                                     cpu_interval=cpu_interval,
                                     my_pass=mypass,
                                     intf=intf,
                                     is_wl=is_wl)

            time.sleep(3)
            msg_byte=str.encode(json.dumps(msg))
            s.send(msg_byte)
            print(f'| sent     \t | {msg_byte} \t |')
            data = s.recv(buffer_size)
            print(f'| received \t | {data} \t |')
            print('------------------------------------------')
        except KeyboardInterrupt:
            s.close()

def main():
    client_port = int(input('Enter port number \t : '))
    host_ip = input('Enter Server IP \t : ')
    host_port = int(input('Enter Server Port \t : '))
    buffer_size = int(input('Enter Buffer size \t : '))
    client_password=input('Enter your password : ')
    intf=input('Enter interface to monitor \t : ')
    while True:
        is_wl=input('is this a wireless interface ? (y/n) : \t')
        if is_wl == 'y':
            is_wl=True
            break
        elif is_wl == 'n':
            is_wl = False
            break
        else:
            continue

    send_loop(client_port=client_port,
              host_ip=host_ip,
              host_port=host_port,
              mypass=client_password,
              intf=intf,
              is_wl=is_wl)

main()