import pyqrcode # gera o QRCOde
from pyqrcode import QRCode

# Captura a URL desejada:
qrstring = 'https://www.brunos.blog.br'

# Gera o QRCode
url = pyqrcode.create(qrstring)

# Imprime o QRCode
url.png(r'qr.png', scale=8)