#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:07:51 2017

@author: richard
"""

# nextbus
import sys

if len(sys.argv) != 3:
        raise SystemExit('Usage:',  sys.argv[0], 'route, stopid')

route = sys.argv[1]
stopid = sys.argv[2]
# to terminate program 
#raise SystemExit(0)

import urllib.request as ur

# valid route = 22, valid stopid = 14787 / 14791
# valid route = 6, valid stopid = 5037
u = ur.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
 