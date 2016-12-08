import prompt
import requests

matches = {}

def find(parameters):

    prompt.text('Scan files...', '')

    for parameter in parameters['files']['removed']:
        for file in parameter['files']:
            request = requests.get(parameters['url'] + '/' + file, allow_redirects=False)
            if 200 == request.status_code:
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
