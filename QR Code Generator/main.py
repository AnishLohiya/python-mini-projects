import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)

qr.add_data("#Enter URL here")
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
