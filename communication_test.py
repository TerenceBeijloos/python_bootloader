from communication import recieve_obj
from communication import transmit_obj
import serial

class communication_obj_test:
    def __init__(self,read_port,write_port,speed):
        self.__test_speed = speed
        self.__test_write_port = write_port
        self.__test_read_port = read_port
        self.__recieve_obj = recieve_obj(read_port,speed)
        self.__transmit_obj = transmit_obj(write_port,speed)

    def test_write_speed_methodes(self):
        self.__transmit_obj.set_write_speed(self.__test_speed)
        if self.__transmit_obj.get_write_speed() != self.__test_speed:
            print("*   set_speed and or get_speed FAILED\n*")
            return False
        else:
            print("*   set_speed and get_speed PASSED\n*")
            return True

    def test_write_port_methodes(self):
        self.__transmit_obj.set_write_port(self.__test_write_port)
        if self.__transmit_obj.get_write_port() != self.__test_write_port:
            print("*   set_port and or get_port FAILED\n*")
            return False
        else:
            print("*   set_port and get_port PASSED\n*")
            return True

    #Note that the recieve_obj needs to pass the test before the transmitted data can be verified, the read and write port need to be connected to each other
    def test_transmit(self):
        message = b"Hello World"

        self.__transmit_obj.transmit(message)
        self.__recieve_obj.set_read_speed(self.__transmit_obj.get_write_speed())
        self.__recieve_obj.set_read_port(self.__test_read_port)

        if self.__recieve_obj.recieve(1,len(message)) != message:
            print("*   test_transmit FAILED\n*")
            return False
        else:
            print("*   test_transmit PASSED\n*")
            return True


    def test_transmit_obj(self):
        print("*test_transmit_obj\n*")

        if not self.test_write_speed_methodes():
            print("*Stop testing")
            return False

        if not self.test_write_port_methodes():
            print("*Stop testing")
            return False

        if not self.test_transmit():
            print("*Stop testing")
            return False

        print("*End of test_transmit_obj all passed\n")
        return True


    def test_read_speed_methodes(self):
        self.__recieve_obj.set_read_speed(self.__test_speed)
        if self.__recieve_obj.get_read_speed() != self.__test_speed:
            print("*   set_speed and or get_speed FAILED\n*")
            return False
        else:
            print("*   set_speed and get_speed PASSED\n*")
            return True

    def test_read_port_methodes(self):
        self.__recieve_obj.set_read_port(self.__test_read_port)
        if self.__recieve_obj.get_read_port() != self.__test_read_port:
            print("*   set_port and or get_port FAILED\n*")
            return False
        else:
            print("*   set_port and get_port PASSED\n*")
            return True

    def test_recieve(self,use_transmit_obj):
        message = b"Hello World"
        max_wait_time = 5 #in secondes

        if use_transmit_obj:
            self.__transmit_obj.set_write_port(self.__test_write_port)
            self.__transmit_obj.set_write_speed(self.__test_speed)
            self.__transmit_obj.transmit(message)

        recieved_message = self.__recieve_obj.recieve(max_wait_time,len(message))
        if recieved_message == b'':
            print("*   recieve FAILED, nothing recieved within " + str(max_wait_time) + " secondes\n*")
            return False
        elif  recieved_message != message:
            print("*   recieve FAILED, messaged recieved = " + str(recieved_message) + " expected message = " + message)
            return False
        
        print("*   recieve PASSED\n*")
        return True

    def test_recieve_obj(self):
        print("*test_recieve_obj\n*")

        
        if not self.test_read_speed_methodes():
            print("*Stop testing")
            return False

        if not self.test_read_port_methodes():
            print("*Stop testing")
            return False

        if not self.test_recieve(False):
            print("*Stop testing")
            return False

        print("*End of test_recieve_obj all passed\n")

        return True

    def test_all(self):
        pass


        
# start application
if __name__ == "__main__":
    test = communication_obj_test('COM4','COM5',115200)
    test.test_transmit_obj()
    
    	