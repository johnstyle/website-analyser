#!/usr/bin/env python

import os.path
import sys
import requests
import yaml
import hashlib
import lib.prompt as prompt
import lib.domain as domain
import lib.headers as headers
import lib.content as content
import lib.admin as admin
import lib.files as files

args = sys.argv[1:]
parametersFile = 'parameters.yml'

if not args:
    print('Veuillez renseigner une URL')
    exit()

if not os.path.isfile(parametersFile):
    print('Veuillez creer le fichier de parametres')
    exit()

parameters = yaml.load(file(parametersFile, 'r'))
parameters['url'] = args[0]

prompt.title('Website Analyser : ' + parameters['url'])

try:
    request = requests.get(parameters['url'])
except Exception:
    print('Cette URL ne repond pas')
    pass

parameters['hash'] = hashlib.md5(request.content).hexdigest()

prompt.subtitle('Domain')
domain.find(parameters, request)

prompt.subtitle('Headers')
headers.find(parameters, request)

prompt.subtitle('Content')
content.find(parameters, request)

prompt.subtitle('Admin')
admin.find(parameters)

prompt.subtitle('Files')
files.find(parameters)

print('')
