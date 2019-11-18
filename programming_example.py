from programmer import programmer_obj
import os

# start application
if __name__ == "__main__":
    path = 'your\\path\\blinky_531.bin'
    pr = programmer_obj("COM4",115200,path)

    pr.start_booting()
    # path = 'C:\\Users\\tbeijloo\\Downloads\\python_scripts\\python_bootloader\\blinky_531.bin'
    # print(os.path.getsize(path))

    # counter = 0
    # with open(path, "rb") as f:
    #         byte = f.read(1)
    #         while byte:
    #             counter += 1
    #             byte = f.read(1)

    # print(counter)





































    # tx = transmit_obj("COM16",115200)
    # # rx = recieve_obj("COM16",115200)
    # out = b''

    # tx.transmit(1,close_port=False)
    # time.sleep(1)
    # while tx.get_serial().inWaiting() > 0:
    #     out += tx.get_serial().read(1)

    # print(out)
    # tx.close()
    # # # configure the serial connections (the parameters differs on the device you are connecting to)
    # # ser = serial.Serial(
    # #     port='COM16',
    # #     baudrate=115200,
    # #     parity=serial.PARITY_NONE,
    # #     stopbits=serial.STOPBITS_ONE,
    # #     bytesize=serial.EIGHTBITS
    # # )

    # # ser.isOpen()

    # # # input=1
    # # while 1 :
    # #         ser.write(b'\x01')
    # #         out = b''
    # #         # let's wait one second before reading output (let's give device time to answer)
    # #         time.sleep(1)
    # #         while ser.inWaiting() > 0:
    # #             out += ser.read(1)

    # #         if out != b'':
    # #             print(out)
