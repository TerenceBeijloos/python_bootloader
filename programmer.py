from recieve_obj import recieve_obj
from transmit_obj import transmit_obj
import os.path
from time import sleep

class programmer_obj(transmit_obj,recieve_obj):

    def __init__(self,port,speed,path,SOH=1,STX=2,ACK=6,NACK=21):

        transmit_obj.__init__(self,port,speed,timeout=1,keep_trying_to_connect=True)
        recieve_obj.__init__(self,port,speed,timeout=1,keep_trying_to_connect=True)

        self.set_SOH(SOH)
        self.set_STX(STX)
        self.set_ACK(ACK)
        self.set_NACK(NACK)
        self.set_program_path(path)
        self.__CRC = 0

    def program(self):
        header_length = 1#calculate length

        self.wait_for_STX()
        self.send_SOH()
        self.send_header_length(header_length)

        if not self.wait_for_ACK_or_NACK():
            print("program: NACK, length was not acknowledged, EXIT")
            exit()
        
        #CRC = self.send_program()
        #if self.wait_for_CRC() != CRC:
        #   print("program: CRC check failed, data recieved by device is incorrect, EXIT")
        #   exit()

    def set_program_path(self,path):
        if os.path.isfile(path):
            self.__path = path
        else: 
            print("ERROR path " + str(path) + " is invalid, EXIT")
            exit()

    def get_program_path(self):
        return self.__path

    def set_SOH(self,new_value):
        if type(new_value) is bytes:
            self.__SOH = new_value
        elif type(new_value) is int:
            self.__SOH = self.int_to_byte_str(new_value)
        else:
            print("Type error value: " + new_value + " is not set")

    def get_SOH(self):
        return self.__SOH

    def set_STX(self,new_value):
        if type(new_value) is bytes:
            self.__STX = new_value
        elif type(new_value) is int:
            self.__STX = self.int_to_byte_str(new_value)
        else:
            print("Type error value: " + new_value + " is not set")

    def get_STX(self):
        return self.__STX

    def set_ACK(self,new_value):
        if type(new_value) is bytes:
            self.__ACK = new_value
        elif type(new_value) is int:
            self.__ACK = self.int_to_byte_str(new_value)
        else:
            print("Type error value: " + new_value + " is not set")

    def get_ACK(self):
        return self.__ACK

    def set_NACK(self,new_value):
        if type(new_value) is bytes:
            self.__NACK = new_value
        elif type(new_value) is int:
            self.__NACK = self.int_to_byte_str(new_value)
        else:
            print("Type error value: " + new_value + " is not set")

    def get_NACK(self):
        return self.__NACK

    def wait_for_STX(self,open_port=True):
        self.seek_patern(self.__STX,keep_seeking=True,open_port=open_port)

    def wait_for_ACK_or_NACK(self):
        return self.seek_patern([self.__ACK,self.__NACK],keep_seeking=True,recieve_time=0,print_recieved=False) == self.get_ACK()

    def wait_for_CRC(self):
        return self.recieve(1,1)

    def send_SOH(self):
        self.transmit(1,open_port=False)

    def send_header_length(self,LSB_first=True):
        length = os.path.getsize(self.get_program_path())
        LSB = (length & 255)
        MSB = ((length>>8) & 255 ) 
        send_list = [None] * 2
        if LSB_first: 
            send_list = [LSB,MSB] 
        else: 
            send_list = [MSB,LSB]
        self.transmit(send_list)

    def send_ACK(self):
        self.transmit(self.__ACK)

    def send_NACK(self):
        self.transmit(self.__NACK)

    def send_program(self):
        self.__CRC = 0
        self.open()

        with open(self.get_program_path(), "rb") as f:
            byte = f.read(1)
            while byte:
                # print(byte)
                self.__CRC ^= (self.byte_str_to_int(byte)&255)
                self.transmit(byte,open_port=False)
                byte = f.read(1)

    def start_booting(self):
        self.wait_for_STX()
        self.send_SOH()
        self.send_header_length()

        print(self.wait_for_ACK_or_NACK() )
        self.send_program()

        crc = self.wait_for_CRC()

        print("crc recieved = " + str(crc))
        print("crc calculated = " + str(self.__CRC))

        if crc == self.int_to_byte_str(self.__CRC):
            self.send_ACK()
            print("success")
        else:
            self.send_NACK()
            print("not so successfull")

        print("end")

    def echo_recieved(self):

        while("I want a cookie"):   #The day he recieves a cookie, everything will break
            out = b''
            while self.get_serial().inWaiting() > 0:
                out += self.get_serial().read(1)

            if out != b'': print(out)
