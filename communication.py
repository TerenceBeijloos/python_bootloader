import serial
import time

communication_state = ["idle","transmitting","recieving"]

class transmit_obj:
    def __init__(self,port,speed):
        self.__serial = serial.Serial()
        self.__serial.port = port
        self.__serial.baudrate = speed

    def transmit(self,data):
        self.__serial.open()

        if not self.__serial.is_open:
            print("Unable to read, cannot open serial port: " + self.__serial.port )
            return

        self.__serial.write(data)

        self.__serial.close()

    def set_write_speed(self,speed):
        self.__serial.baudrate = speed

    def get_write_speed(self):
        return self.__serial.baudrate

    def set_write_port(self,port):
        self.__serial.port = port
    
    def get_write_port(self):
        return self.__serial.port

class recieve_obj:
    def __init__(self,port,speed):
        self.__serial = serial.Serial()
        self.__serial.port = port
        self.__serial.baudrate = speed

    #read_size in bytes and max_time in seconds (float allowed)
    def recieve(self,max_time,read_size):
        self.__serial.open()

        if not self.__serial.is_open:
            print("Unable to read, cannot open serial port: " + self.__serial.port )
            return

        self.__serial.timeout = max_time
        message = self.__serial.read(size=read_size)

        self.__serial.close()

        return message

    def set_read_speed(self,speed):
        self.__serial.speed = speed

    def get_read_speed(self):
        return self.__serial.speed

    def set_read_port(self,port):
        self.__serial.port = port
    
    def get_read_port(self):
        return self.__serial.port

# class communication_obj(recieve_obj,transmit_obj):
#     def __init__(self,speed,read_port,write_port):
#         self.__reci
        



    


        