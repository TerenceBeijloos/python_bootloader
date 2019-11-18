import serial

class common_rxtx_inh:
    def __init__(self,port,speed=115200,timeout=None,keep_trying_to_open=True):
        self.__serial = serial.Serial()#must be first
        self.set_keep_trying_to_open(keep_trying_to_open)
        self.set_timeout(timeout)
        self.set_port(port)
        self.set_speed(speed)
    
    # def __exit__(self):

#speed
    def set_speed(self,speed):
        try:
            if speed > 0:
                self.__serial.baudrate = int(speed)
                return True
            else:
                return False
        except:
            return False

    def get_speed(self):
        return self.__serial.baudrate
#end speed

#port
    def set_port(self,port):
        if self.is_valid_port(port):
            self.__serial.port = port
            return True
        else:
            print("Invalid port")
            return False

    def get_port(self):
        return self.__serial.port

    def is_valid_port(self,port: str):
        if port[:3] != "COM":
            return False
    
        try:
            return (1 <= int(port[3:]) <= 65535)
        except:
            return False
#end port

#timeout
    def set_timeout(self,timeout):
        if timeout == None:
            self.__serial.timeout = None
            return True
        if 0 <= timeout <= 100:
            self.__serial.timeout = timeout
            return True
        else:
            print("Invalid timeout value")
            return False

    def get_timeout(self):
        return self.__serial.timeout
#end timeout

#open
    def is_open(self):
        return self.__serial.is_open

    def open(self):
        if self.is_open():
            print("Port: " + self.get_port() + " is already open ready to be used")
            return True

        try:
            self.__serial.open()
        except:
            print("ERROR unable to open " + self.get_port())

            if self.get_keep_trying_to_open() and self.is_valid_port(self.get_port()):
                print("Keep trying to open " + self.get_port())
                while not self.__serial.is_open:
                    try: 
                        self.__serial.open()
                    except:
                         pass
            else: 
                return False
        
        return True

    def set_keep_trying_to_open(self,keep_trying):
        if type(keep_trying) is not bool:
            print("set_keep_trying_to_open: keep_trying must be a bool, value not set")
            return False
            
        self.__keep_trying_to_open = keep_trying
        return True

    def get_keep_trying_to_open(self):
        return self.__keep_trying_to_open
#end open

#close
    def close(self):
        self.__serial.close()
#end close

#serial
    def get_serial(self):
        return self.__serial

    def set_serial(self,new_serial):
        self.__serial = new_serial
#end serial
#convertion
    def int_to_byte_str(self,number: int):
        if number == 0:
            return b'\x00'
        else:
            return number.to_bytes((number.bit_length() + 7) // 8,byteorder='big')

    def byte_str_to_int(self,byte_string: bytes):
        return int.from_bytes(byte_string,byteorder='big')
#end convertion

    #Item may only be int bytes or a list of ints or bytes
    def item_to_list(self,item):
        
        if type(item) is bytes:
            return [item]
        elif type(item) is int:
            return [self.int_to_byte_str(item)]

        elif type(item) is list:
            index = 0
            byte_item = b''
            return_list = [None] * len(item)

            for i in item:

                if type(i) is int:
                    byte_item = self.int_to_byte_str(i)
                elif type(i) is not bytes:
                    print("seek_patern: type_error, patern[" + index + "] is of type: " + type(i) + " EXIT")
                    exit()
                else:
                    byte_item = i

                return_list[index] = byte_item
                index += 1

            return return_list

        else:
            print("item_to_list: type_error, patern is of type: " + type(item) + " EXIT")
            exit()