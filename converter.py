
import argparse
import string


def get_ip():
    parser = argparse.ArgumentParser(description='Converter')
    parser.add_argument("-b", "--bin", action="store", dest="bin", default="empty", help='bin to dec')
    parser.add_argument("-d", "--dec", action="store", dest="dec", default="empty", help='dec to bin')
    return parser.parse_args()


def convert_to_dec(bin_ip: string):
    if len(bin_ip) != 35:
        print("Wrong ip in bin")
        exit(1)
    address = ""
    octets = bin_ip.split('.')
    for octet in octets:
        dec_octet = 0
        degree = 7
        for digit in octet:
            if digit not in ["1", "0"] or degree < 0:
                print("Wrong bin ip")
                exit(1)
            elif digit == "1":
                dec_octet += 2  degree
            degree -= 1
        address += f"{str(dec_octet)}."
    print(address[:-1])


def convert_to_bin(dec):
    address = ""

    octets = dec.split(".")

    for octet in octets:
        octet = int(octet)
        for i in reversed(range(8)):
            if octet - 2  i >= 0:
                octet -= 2 ** i
                address += "1"
            else:
                address += "0"
        address += "."
    print(address[:-1])


def start():
    ip = get_ip()
    if ip.bin != "empty":
        convert_to_dec(ip.bin)
    elif ip.dec != "empty":
        convert_to_bin(ip.dec)
    else:
        print("IP wasn't provided")


if name == 'main':
    start()
