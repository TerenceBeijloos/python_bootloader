from common_rxtx_inh import common_rxtx_inh
import threading
import time
import serial.tools.list_ports

class rxtx_inh_test(common_rxtx_inh):
    def __init__(self):
        common_rxtx_inh.__init__(self,"")

    def test_speed(self):
        
        test_value = -1

        self.set_speed(test_value)
        if self.get_serial().baudrate < 0:
            print("test_speed: ERROR speed may not be set lower than 0, EXIT")
            exit()
        
        test_value = 0
        self.set_speed(test_value)
        if self.get_serial().baudrate <= 0:
            print("test_speed: ERROR speed may not be set lower or equal to 0, EXIT")
            exit()

        test_value = 1

        for test_value in range(1,10):
            if not self.set_speed(test_value):
                print("test_speed: ERROR " + str(test_value) + " should be a valid speed, EXIT")
                exit()

            if self.get_serial().baudrate != test_value:
                print("test_speed: ERROR baudrate did not change to " + str(test_value) +", EXIT")
                exit()
        
            if self.get_serial().baudrate != self.get_speed():
                print("test_speed: ERROR get_speed is not equal to baudrate, EXIT")
                exit()

        test_value = 1.2
        self.set_speed(test_value)
        if type(self.get_speed()) is not int:
            print("test_speed: ERROR get_speed type is not int, EXIT")
            exit()

        print("test_speed: all PASSED")
        
    def port_test(self):
        test_value = "ojsadnajosdnsadjon as"
        if self.set_port(test_value) or self.get_serial().port == test_value:
            print("port_test: ERROR set_port(" + str(test_value) + ") should NOT be a valid port, EXIT")
            exit()

        test_value = "com1"
        if self.set_port(test_value) or self.get_serial().port == test_value:
            print("port_test: ERROR set_port(" + str(test_value) + ") should NOT be a valid port, EXIT")
            exit()

        test_value = "COM-1"
        if self.set_port(test_value) or self.get_serial().port == test_value:
            print("port_test: ERROR set_port(" + str(test_value) + ") should NOT be a valid port, EXIT")
            exit()

        test_value = "COMa"
        if self.set_port(test_value) or self.get_serial().port == test_value:
            print("port_test: ERROR set_port(" + str(test_value) + ") should NOT be a valid port, EXIT")
            exit()

        test_value = "COM6"
        if not self.set_port(test_value):
            print("port_test: ERROR set_port(" + str(test_value) + ") SHOULD BE a valid port, EXIT")
            exit()

        if self.get_serial().port != test_value or self.get_serial().port != self.get_port():
            print("port_test: ERROR port was not correctly set or get, EXIT")
            exit()

        print("port_test: all PASSED")

    def timeout_test(self):
        test_value = -1
        if self.set_timeout(test_value) or self.get_serial().timeout == test_value:
            print("timeout_test: ERROR set_timeout(" + str(test_value) + ") should NOT be a valid timeout, EXIT")
            exit()

        test_value = 101
        if self.set_timeout(test_value) or self.get_serial().timeout == test_value:
            print("timeout_test: ERROR set_timeout(" + str(test_value) + ") should NOT be a valid timeout, EXIT")
            exit()

        test_value = None
        if not self.set_timeout(test_value):
            print("timeout_test: ERROR set_timeout(" + str(test_value) + ") SHOULD BE a valid timeout, EXIT")
            exit()

        if self.get_serial().timeout != test_value or self.get_serial().timeout != self.get_timeout():
            print("timeout_test: ERROR " + str(test_value) + " was not correctly set or get, EXIT")
            exit()

        test_value = 0

        for test_value in range(0,101):
            if not self.set_timeout(test_value):
                print("timeout_test: ERROR set_timeout(" + str(test_value) + ") SHOULD BE a valid timeout, EXIT")
                exit()

            if self.get_serial().timeout != test_value or self.get_serial().timeout != self.get_timeout():
                print("timeout_test: ERROR " + str(test_value) + " was not correctly set or get, EXIT")
                exit()
        
        print("timeout_test: all PASSED")

    def open_close_test(self):
        
        ports = list(serial.tools.list_ports.comports())
        port_2_open = ""

        for p in ports:
            if "USB Serial Port" in p.description:
                port_2_open = p.device

        print("Port = " + str(port_2_open))
        if port_2_open == "":
            print("keep_trying_to_open_test: ERROR please connect a USB Serial Port device and test it again, EXIT")
            exit()

        self.set_keep_trying_to_open(False)

        if not self.open():
            print("open_close_test: ERROR could not open port " + str(port_2_open) + ", EXIT")
            exit()

        if not self.get_serial().is_open:
            print("open_close_test: ERROR open() return fault port " + str(port_2_open) + " is not open, EXIT")
            exit()

        if self.get_serial().is_open != self.is_open():
            print("open_close_test: ERROR port is open but is_open() returns False, EXIT")
            exit()

        if not self.open():
            print("open_close_test: ERROR opening a port twice should not be an issue, EXIT")
            exit()

        if not self.is_open():
            print("open_close_test: ERROR opening a port twice should not be an issue, EXIT")
            exit()

        self.close()

        if self.get_serial().is_open:
            print("open_close_test: ERROR close() did not close port " + str(port_2_open) + ", EXIT")
            exit()

        if self.get_serial().is_open != self.is_open():
            print("open_close_test: ERROR port is closed but is_open() returns True, EXIT")
            exit()

        print("open_close_test: all PASSED")
    
    def all(self):
        self.test_speed()
        self.timeout_test()
        self.port_test()
        self.open_close_test()
        print("All tests PASSED")

    # def keep_trying_to_open_test(self): DOES NOT FUNCTION YET

    #     test_value = "a"
    #     if self.set_keep_trying_to_open(test_value):
    #         print("keep_trying_to_open_test: ERROR " + str(test_value) + " should NOT be valid, EXIT")
    #         exit()
    
    #     test_value = [1]
    #     if self.set_keep_trying_to_open(test_value):
    #         print("keep_trying_to_open_test: ERROR " + str(test_value) + " should NOT be valid, EXIT")
    #         exit()

    #     test_value = False

    #     for i in range(0,2):
    #         if not self.set_keep_trying_to_open(test_value):
    #             print("keep_trying_to_open_test: ERROR " + str(test_value) + " SHOULD BE valid, EXIT")
    #             exit()

    #         if self.get_keep_trying_to_open() != test_value:
    #             print("keep_trying_to_open_test: ERROR " + str(test_value) + " was not set, EXIT")
    #             exit()
            
    #         test_value = not test_value

    #     ports = list(serial.tools.list_ports.comports())
    #     port_2_open = ""

    #     for p in ports:
    #         if "USB Serial Port" in p[1]:
    #             port_2_open = p[0]

    #     if port_2_open == "":
    #         print("keep_trying_to_open_test: ERROR please connect a USB Serial Port device and test it again, EXIT")

    #     self.set_port(port_2_open)

if __name__ == "__main__":
    test = rxtx_inh_test()
    test.all()