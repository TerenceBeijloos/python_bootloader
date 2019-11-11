import serial
import time 
from common_rxtx_inh import common_rxtx_inh

class recieve_obj(common_rxtx_inh):
    def __init__(self,port,speed,timeout=1,keep_trying_to_connect=True):
        common_rxtx_inh.__init__(self,port,speed=speed,timeout=timeout,keep_trying_to_open=True)

    #read_size in bytes and max_time in seconds (float allowed)
    def recieve(self,max_time,read_size,open_port=True,close_port=True):

        if open_port:
            self.open()

        if not self.is_open():
            print("Serial port: " + self.__serial.port +  " is not open EXIT")
            exit()

        self.__serial.timeout = max_time
        message = self.__serial.read(size=read_size)

        if close_port:
            self.close()

        return message

    #max_time in seconds, this is the maximum time this method will seek for pathern
    def seek_patern(self,patern,max_time=10,keep_seeking=False,patern_size=1):
        
        max_time = int(max_time)
        if max_time <= 0 and not keep_seeking:
            print("max_time must be greater than 0, EXIT")
            exit()
        
        recieve_time = 0.2 
        start_time = time.time()
        found = False

        self.open()

        if not keep_seeking:
            
            while time.time() - start_time < max_time:
                
                if self.recieve(recieve_time,patern_size,False,False) == patern:
                    found = True
                    break
        else:
            patern_recieved = self.recieve(recieve_time,patern_size,False,False)

            while patern_recieved != patern: patern_recieved = self.recieve(recieve_time,patern_size,False,False) #print(patern_recieved)

            found = True

        self.close()

        return found  