import serial
import time 

class recieve_obj:
    def __init__(self,port,speed,timeout=1):
        self.__serial = serial.Serial()
        self.__serial.port = port
        self.__serial.baudrate = speed
        self.__serial.timeout = timeout

    def __exit__(self, exc_type, exc_value,traceback):
        if self.__serial.is_open:
            self.__serial.close()

    #read_size in bytes and max_time in seconds (float allowed)
    def recieve(self,max_time,read_size,open_port=True,close_port=True):

        if open_port:
            self.__serial.open()

        if not self.__serial.is_open:
            print("Unable to read, cannot open serial port: " + self.__serial.port )
            return

        self.__serial.timeout = max_time
        message = self.__serial.read(size=read_size)

        if close_port:
            self.__serial.close()

        return message

    #max_time in seconds, this is the maximum time this method will seek for pathern
    def seek_patern(self,patern,max_time=10,keep_seeking=False,patern_size=1):
        
        if max_time <= 0 and not keep_seeking:
            print("max_time must be greater than 0, EXIT")
            exit()
        
        # patern = patern&(bin(pow(2,8*patern_size)-1)
        recieve_time = 0.2 
        start_time = time.time()
        found = False

        self.__serial.open()

        if not keep_seeking:
            
            while time.time() - start_time < max_time:
                
                if self.recieve(recieve_time,patern_size,False,False) == patern:
                    found = True
                    break

        else:
            patern_recieved = self.recieve(recieve_time,patern_size,False,False)

            while patern_recieved != patern:
                patern_recieved = self.recieve(recieve_time,patern_size,False,False)
                print(patern_recieved)

            found = True

        self.__serial.close()
        return found  


    def set_read_speed(self,speed):
        self.__serial.speed = speed

    def get_read_speed(self):
        return self.__serial.speed

    def set_read_port(self,port):
        self.__serial.port = port
    
    def get_read_port(self):
        return self.__serial.port