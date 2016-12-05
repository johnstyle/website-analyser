import prompt

def find(parameters, request):

    headers = {}
    for header in request.headers:
        headers[header.lower()] = request.headers[header]

    for index in parameters['required']:
        param = parameters['required'][index]
        loname = param['name'].lower()
        if loname in headers:
            value = headers[loname]
            if param['values'] is None or value.lower() in map(lambda x:x.lower(), param['values']):
                prompt.text(param['name'], value)
            else:
                prompt.warning(param['name'], value)
        else:
            prompt.error(param['name'], None)

    for index in parameters['removed']:
        param = parameters['removed'][index]
        loname = param['name'].lower()
        if loname in headers:
            value = headers[loname]
            prompt.error(param['name'], value)
        else:
            prompt.text(param['name'], None)
