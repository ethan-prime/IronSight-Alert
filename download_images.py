from ast import keyword
from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ['man with pistol', 'man with gun']

for kw in keywords:
    response().download(kw, 300)