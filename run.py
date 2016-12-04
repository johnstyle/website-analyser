#!/usr/bin/env python

import os.path
import sys
import requests
import yaml
import lib.prompt as prompt
import lib.headers as headers
import lib.content as content

args = sys.argv[1:]
parametersFile = 'parameters.yml'

if not args:
    print('Veuillez renseigner une URL')
    exit()

if not os.path.isfile(parametersFile):
    print('Veuillez creer le fichier de parametres')
    exit()

config = yaml.load(file(parametersFile, 'r'))
url = args[0]

prompt.title('Website : ' + url)
request = requests.get(url)

prompt.subtitle('Headers')
headers.find(config['headers'], request)

prompt.subtitle('Content')
content.find(config['content'], request)

print('')
