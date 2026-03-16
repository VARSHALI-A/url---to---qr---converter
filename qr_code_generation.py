import qrcode
import time # new name for every image 

# 1. user link
data = input("Enter the link or URL: ")

# 2. QR Code Ready period
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# 3.new iamges generate with this extension
# Example: QR_171059.png, QR_171060.png 
qr_code_generation= "QR_" + str(int(time.time())) + ".png"

# 4. Save 
img.save(qr_code_generation)

print("QR Code Image: " + qr_code_generation)