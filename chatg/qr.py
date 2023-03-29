import qrcode
from io import BytesIO

# Define the 24 seed words
seed_words = "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12 word13 word14 word15 word16 word17 word18 word19 word20 word21 word22 word23 word24"

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# Add the seed words as data to the QR code
qr.add_data(seed_words)

# Create the QR code image
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save("bitcoin_seed_words_qr.png", "PNG")

# Alternatively, save the image to a BytesIO object
buffer = BytesIO()
img.save(buffer, "PNG")
