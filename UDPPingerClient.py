from socket import * 
import time
from socket import AF_INET, SOCK_DGRAM

print('Running')
serverName = '127.0.0.1'  # setting localhost address as mentioned in project
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # timeout set to be 1 second
packets = 50
s_num = 1
maxRTT = 0
minRTT = 666666
count = 0
total = 0

while s_num <= packets:
    message = 'Ping'  # message 
    start=time.time()  # assigns the current time to a variable
    clientSocket.sendto(message.encode('utf-8'),(serverName,12231))  # send a message to the server at port number 12231

    try:
        message,address = clientSocket.recvfrom(1024)  # recieves message from server
        elapsed = (time.time()-start)
        elapsed = elapsed*1000000

        if elapsed<minRTT:
            minRTT=elapsed
        if elapsed>maxRTT:
            maxRTT=elapsed

        total = total+elapsed

        print('Ping No.:',s_num,' Message: ',message.decode('utf-8'))

        print('Round Trip Time RTT:' + str(elapsed) + " microseconds")
        

    except timeout:  # if response takes longer than 1 second
        count = count+1
        print('Ping No.:',s_num,'  Request timed out')

    s_num += 1  # sequence number is increased after all of the other statements in the while
    avg = total/(packets-count)

    if s_num > packets:  # closes the socket order 30 packets
        clientSocket.close()

LOSS_RATE = (count/packets)*100
print('Maximum value of RTT: ',maxRTT,' Minimum value of RTT: ',minRTT, 'Average RTT: ',avg)
print('LOSS_RATE: ', LOSS_RATE, '%')