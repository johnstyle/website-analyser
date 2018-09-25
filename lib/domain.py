import prompt
import OpenSSL
import ssl, socket
from urlparse import urlparse
from datetime import datetime


def find(parameters, request):

    try:
        uri = urlparse(parameters['url'])
        cert = ssl.get_server_certificate((uri.netloc, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        prompt.text('SSL', "Oui")
        prompt.text(
            'SSL expiration date',
            datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ').strftime('%Y-%m-%d %H:%M:%S')
        )
    except socket.error:
        prompt.text('SSL', "Non")
        pass
