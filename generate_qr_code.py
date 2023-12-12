# pip install pyqrcode to attempt to follow QR code standards as closely as possible
# pip install pypng  to save image in png

import pyqrcode
import png
from pyqrcode import QRCode

#a string to represent the QR code
github = "github.com/amcoolalphonce"

#generate QR Code
url = pyqrcode.create(github)

