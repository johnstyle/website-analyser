import prompt
import re
from lxml import html


def find(parameters, request):

    found_data = False
    tree = html.fromstring(request.content)

    for parameter in parameters['content']:

        if 'selector' in parameter:
            values = tree.xpath(parameter['selector'])
            if values:
                for value in values:
                    prompt.text(parameter['name'], value)
                    found_data = True

        if 'regex' in parameter:
            if not isinstance(parameter['regex'], list):
                parameter['regex'] = [parameter['regex']]
            for regex in parameter['regex']:
                values = re.findall(regex, request.content)
                if values:
                    for value in values:
                        if not isinstance(value, tuple):
                            value = [value]
                        prompt.text(parameter['name'], ' ' . join(value))
                        found_data = True

    if not found_data:
        prompt.text(' > No data found', '')
