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
            print("Serial port: " + self.get_port() +  " is not open EXIT")
            exit()

        self.set_timeout(max_time)
 
        message = self.get_serial().read(size=read_size)

        if close_port:
            self.close()

        return message


    #Item may only be int bytes or a list of ints or bytes
    def item_to_list(self,item):
        
        if type(item) is bytes:
            return [item]
        elif type(item) is int:
            return [self.int_to_byte_str(item)]

        elif type(item) is list:
            index = 0
            return_list = [None] * len(item)

            for i in item:

                if type(i) is int:
                    i = self.int_to_byte_str(i)
                elif type(i) is not bytes:
                    print("seek_patern: type_error, patern[" + index + "] is of type: " + type(i) + " EXIT")

                return_list[index] = i
                index += 1

            return return_list

        else:
            print("item_to_list: type_error, patern is of type: " + type(item) + " EXIT")
            exit()

    #max_time in seconds, this is the maximum time this method will seek for pathern. 
    #Recieve time is the time per message that the recieve function will wait, used for print_recieved. 
    #NOTE if recieve_time is set this function may take longer than max_time
    def seek_patern(self,patern_passed,max_time=10,keep_seeking=False,patern_size=1,print_recieved=False,recieve_time=0):
        
        start_time = time.time()
        found = False
        max_time = int(max_time)
        patern_recieved = b''
        patern = self.item_to_list(patern_passed)

        if max_time <= 0 and not keep_seeking:
            print("max_time must be greater than 0, EXIT")
            exit()

        self.open()

        if not keep_seeking:
            
            while time.time() - start_time < max_time:
                patern_recieved = self.recieve(recieve_time,patern_size,False,False)
                if print_recieved: print(patern_recieved)
                if patern_recieved in patern:
                    found = True
                    break
        else:
            
            patern_recieved = self.recieve(recieve_time,patern_size,False,False)

            while patern_recieved not in patern: 
                patern_recieved = self.recieve(recieve_time,patern_size,False,False) 
                if print_recieved: print(patern_recieved)

            found = True

        self.close()

        if type(patern_passed) is not list:
            return found  
        else:
            return patern_recieved