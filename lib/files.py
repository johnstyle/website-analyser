import prompt
import requests
import hashlib

matches = {}


def find(parameters):

    found_data = False
    prompt.text('Scan files...', '')
    prompt.separator()

    for parameter in parameters['files']['removed']:
        for test_file in parameter['files']:
            request = requests.get(parameters['url'] + '/' + test_file, allow_redirects=False)
            if 200 == request.status_code:
                hash_file = hashlib.md5(request.content).hexdigest()
                if hash_file != parameters['hash']:
                    prompt.error(test_file if 32 >= len(test_file) else test_file[:28] + '[...]', 'File exists')
                    found_data = True
                    if 'interpreter' in parameter.keys():
                        category = parameter['interpreter']['category']
                        if category not in matches.keys():
                            matches[category] = []

                        if 'json' == parameter['interpreter']['type']:
                            json_data = request.json()
                            if isinstance(json_data, list):
                                for items in json_data:
                                    value = ''
                                    for path in parameter['interpreter']['path']:
                                        try:
                                            value += str(items[path]) + ':'
                                        except NameError:
                                            err=1
                                    if value and value not in matches[category]:
                                        matches[category].append(value.strip(':'))
                            else:
                                for path in parameter['interpreter']['path']:
                                    try:
                                        for item in json_data[path]:
                                            value = str(item) + ':' + json_data[path][item]
                                            if value and value not in matches[category]:
                                                matches[category].append(value)
                                    except NameError:
                                        err=1

    if not found_data:
        prompt.text(' > No data found', '')
    else:
        print('')
        prompt.text('Critical data', '')
        prompt.separator()
        if matches:
            for category in matches:
                prompt.error(category, '')
                for index in matches[category]:
                    prompt.error(' > ', index)
        else:
            prompt.text(' > No data found', '')
