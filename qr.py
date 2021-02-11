import pyqrcode
import png
from pyqrcode import QRCode

s = "https://shekhutsav1962001.github.io/LAB3/index.html"
url = pyqrcode.create(s)
url.png(r"C:\Users\Dell\Desktop\py\a.png",scale=8)