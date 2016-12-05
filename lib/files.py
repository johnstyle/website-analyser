import prompt
import requests

def find(parameters):

    for path in parameters['files']['removed']:
        request = requests.get(parameters['url'] + '/' + path)
        if 200 == request.status_code:
            prompt.error(path, `request.status_code`)
        else:
            prompt.text(path, `request.status_code`)
