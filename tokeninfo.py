#!/usr/bin/env python3
import tokens
import datetime
import requests
import logging
import hashlib

tokens.configure(dir='./meta/credentials', url='https://auth.zalando.com/oauth2/access_token?realm=/services')
tokens.manage('marauder', ['uid'])
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s')

while True:
        a = tokens.refresh('marauder')
        a= a['data']
        data = requests.get('https://auth.zalando.com/oauth2/tokeninfo?access_token={}'.format(a['access_token'])).json()
        if data['uid'] == 'stups_marauder':
                tokenhash = '[ERROR] - HASHED ACCESS_TOKEN: {0} - BEARER: {1}'.format(hashlib.sha1((a['access_token']).encode()).hexdigest(), hashlib.sha1(str(a).encode()).hexdigest())
                logging.error(tokenhash)
                for i in range(3):
                        t = requests.get('https://auth.zalando.com/oauth2/tokeninfo?access_token={}'.format(a['access_token'])).json()
                        logging.error('[DEBUG] - CAPTURED TOKEN FOR: \" {0}\" WITH HASHED ACCESS TOKEN: {1}'.format(t['uid'], t['access_token']))
        elif data['uid'] != 'stups_marauder':
                logging.warning('[OK]')
        else:
                logging.warning('[UNKONWN ERROR]')
