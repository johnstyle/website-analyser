import prompt
import requests
import hashlib

matches = {}

def find(parameters):

    prompt.text('Scan files...', '')
    prompt.separator()

    for parameter in parameters['files']['removed']:
        for file in parameter['files']:
            request = requests.get(parameters['url'] + '/' + file, allow_redirects=False)
            if 200 == request.status_code:
                hash = hashlib.md5(request.content).hexdigest()
                if hash != parameters['hash']:
                    prompt.error(file, 'File exists')
                    if 'interpreter' in parameter.keys():
                        category = parameter['interpreter']['category']
                        if category not in matches.keys():
                            matches[category] = []

                        if 'json' == parameter['interpreter']['type']:
                            for item in request.json():
                                value = ''
                                for path in parameter['interpreter']['path']:
                                    value += item[path] + ' '
                                matches[category].extend(value)
                                prompt.error(' -> ' + category, value)
