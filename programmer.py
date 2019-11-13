from recieve_obj import recieve_obj
from transmit_obj import transmit_obj

class programmer_obj(transmit_obj,recieve_obj):

    def __init__(self,port,speed,SOH=1,STX=2,ACK=6,NACK=21):

        transmit_obj.__init__(self,port,speed,timeout=1,keep_trying_to_connect=True)
        recieve_obj.__init__(self,port,speed,timeout=1,keep_trying_to_connect=True)

        self.set_SOH(SOH)
        self.set_STX(STX)
        self.set_ACK(ACK)
        self.set_NACK(NACK)

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

    def wait_for_STX(self):
        self.seek_patern(self.__STX,keep_seeking=True)

    def wait_for_ACK_or_NACK(self):
        return self.seek_patern([self.__ACK,self.__NACK],keep_seeking=True,recieve_time=0,print_recieved=False) == self.get_ACK()

    def wait_for_RCR(self):
        return self.recieve(1,1)

    def send_SOH(self):
        self.transmit(1)