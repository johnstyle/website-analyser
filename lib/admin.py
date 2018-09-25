import prompt
import requests
import hashlib
import lib.content as content


def find(parameters):

    found_data = False
    prompt.text('Scan admin...', '')
    prompt.separator()

    for parameter in parameters['admin']:
        for path in parameter['path']:
            request = requests.get(parameters['url'] + path, allow_redirects=False)
            if 200 == request.status_code:
                hash = hashlib.md5(request.content).hexdigest()
                if hash != parameters['hash']:
                    prompt.error(path if 32 >= len(path) else path[:28] + '[...]', 'Path exists')
                    found_data = True

    if not found_data:
        prompt.text(' > No data found', '')
