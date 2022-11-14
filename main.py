#!/usr/bin/python

import argparse
import requests
import sys


if (len(sys.argv) < 5):
    print('Please provide url and wordlist')

parser = argparse.ArgumentParser(description='dirb')

parser.add_argument('-u', '--url', type=str, help='pass the url to scan')
parser.add_argument('-w', '--wordlist', help="pass the wordlist")


args = parser.parse_args()


url = args.url
wordlist = args.wordlist


def send_requests():
    with open(wordlist) as file:
        lines = file.readlines()
        lines_count = len(lines)
        request_count = 0

        for line in lines:
            line = line.rstrip()
            try:
                req = requests.get(f"{url}/{line}")
            except requests.exceptions.ConnectionError:
                print("Host seems to be down, try again")
                break

            request_count += 1
            print(f"{request_count}/{lines_count}", end="\r")
            if req.status_code == 200:
                print(f"{url}/{line}")
            else:
                pass


if __name__ == '__main__':
    send_requests()