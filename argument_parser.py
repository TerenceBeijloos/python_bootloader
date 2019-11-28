import argparse
import os.path
from os import path

def variable_check(value,border_low,border_high,name,exit=False):
    if border_low <= value <= border_high:
        return True
    else:
        print("ERROR " + str(name) + " must be between " + border_low + " and " + border_high)
        if exit:
            print("EXIT")
            exit()
        else:
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("-program_path","--program_path",help="Path to your .hex or .bin file that will be used to program the device",type=str,required=True)
    parser.add_argument("-sequence","--sequence",help="Specify booting process", required=False,type=str)
    parser.add_argument("-SOH","--SOH",help="Value of start of header",required=False,type=int,metavar="[0-255]")
    parser.add_argument("-ACK","--ACK",help="Value of acknowledge message recieved from the device",required=False,type=int,metavar="[0-255]")
    # parser.add_argument("-ACK","--ACK",help="Value of acknowledge message recieved from the device",required=False,type=int)
    # parser.add_argument("-SOH","--SOH",help="Value of start of header",required=False,type=int)
    args = parser.parse_args()

    print(args.SOH)
    file_type="hex"

    # if args.program_path.endswith(".hex"):
    #     file_type="hex"
    # elif args.program_path.endswith(".bin"):
    #     file_type="bin"
    # else:
    #     print("ERROR file must be either .hex or .bin file, EXIT")
    #     exit()

    # if not path.isfile(args.program_path):
    #     print("ERROR path does not exist, EXIT")
    #     exit()
    # else:
    #     print("ok")

# C:\Users\tbeijloo\Downloads\SDKs\6.0.12.1020_old\projects\target_apps\peripheral_examples\blinky\Keil_5\out_DA14531\Objects\blinky_531.hex
