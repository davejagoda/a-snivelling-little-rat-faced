#!/usr/bin/env python3

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

URL='https://api.github.com/repos/davejagoda/a-snivelling-little-rat-faced/keys'

token = os.getenv('GITHUB_TOKEN')
if token is None:
   print('set the GITHUB_TOKEN variable')
   sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('key_file', help='SSH deploy key')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='show verbose output')
args = parser.parse_args()

if not args.key_file.endswith('.pub'):
   print('upload a public key only')
   sys.exit(1)

with open(args.key_file, 'r') as f:
   parameters = {
      'title': 'dulwich_deploy_key',
      'key': f.read(),
      'read_only': 'false'
   }
data = json.dumps(parameters).encode()

headers = {
   'Authorization': 'token {}'.format(token)
}
if args.verbose:
   print('data: {}'.format(data))
   print('headers: {}'.format(headers))

req = urllib.request.Request(URL, data, headers)
try:
   res = urllib.request.urlopen(req)
except urllib.error.URLError as e:
   print(e)
else:
   if args.verbose:
      print('response: {}'.format(res.read().decode('utf-8')))
   assert(201 == res.status)
   print('deploy key sucessfully uploaded')
