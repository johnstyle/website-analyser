#!/usr/bin/env python

import os.path
import sys
import requests
import yaml
import lib.prompt as prompt
import lib.headers as headers
import lib.content as content
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
request = requests.get(parameters['url'])

prompt.subtitle('Headers')
headers.find(parameters['headers'], request)

prompt.subtitle('Content')
content.find(parameters['content'], request)

# prompt.subtitle('Files')
# files.find(parameters)

print('')
