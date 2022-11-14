#!/usr/bin/python

import argparse
import requests


parser = argparse.ArgumentParser(description='dirb')

parser.add_argument(
    '-u',
     '--url',
     type=str,
     help='pass the url to scan'
    )

parser.add_argument(
    '-w',
    '--wordlist',
    help="pass the wordlist"
)

args = parser.parse_args()




