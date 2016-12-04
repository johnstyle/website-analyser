import prompt
from lxml import html

def find(parameters, request):

    tree = html.fromstring(request.content)

    for index in parameters:
        content = parameters[index]
        value = tree.xpath(content['selector'])
        if value:
            prompt.text(content['name'], value[0])
        else:
            prompt.error(content['name'], None)

