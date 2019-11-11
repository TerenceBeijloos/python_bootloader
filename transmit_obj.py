import serial

class transmit_obj:
    def __init__(self,port,speed):
        self.__serial = serial.Serial()
        self.__serial.port = port
        self.__serial.baudrate = speed

    def transmit(self,data):
        self.__serial.open()

        if not self.__serial.is_open:
            print("Unable to transmit, cannot open serial port: " + self.__serial.port )
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