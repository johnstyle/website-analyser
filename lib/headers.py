import prompt

def find(parameters, request):

    headers = {}
    for header in request.headers:
        headers[header.lower()] = request.headers[header]

    for parameter in parameters['required']:
        loname = parameter['name'].lower()
        if loname in headers:
            value = headers[loname]
            if parameter['values'] is None or value.lower() in map(lambda x:x.lower(), parameter['values']):
                prompt.text(parameter['name'], value)
            else:
                prompt.warning(parameter['name'], value)
        else:
            prompt.error(parameter['name'], None)

    for parameter in parameters['removed']:
        loname = parameter['name'].lower()
        if loname in headers:
            value = headers[loname]
            prompt.error(parameter['name'], value)
        else:
            prompt.text(parameter['name'], None)
