import serial
from common_rxtx_inh import common_rxtx_inh

class transmit_obj(common_rxtx_inh):
    def __init__(self,port,speed,timeout=None,keep_trying_to_connect=True):
        common_rxtx_inh.__init__(self,port,speed=speed,timeout=timeout,keep_trying_to_open=True)

    def transmit(self,data,open_port=True,close_port=True):
        
        if open_port:
            self.open()

        if not self.is_open():
            print("Unable to transmit, cannot open serial port: " + self.get_port() )
            return
        
        if type(data) is int:
            data = self.int_to_byte_str(data)
        elif not (type(data) is bytes):
            print("transmit: Type error")
            
        self.get_serial().write(data)

        if close_port:
            self.close()
