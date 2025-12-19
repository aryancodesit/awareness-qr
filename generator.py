import qrcode
from PIL import Image

def generate_awareness_qr(target_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(target_url)
    qr.make(fit=True)

    # Use a custom color to make it look unique
    img = qr.make_image(fill_color="#1a1a1a", back_color="#ffffff").convert('RGB')
    img.save("awareness_qr.png")
    print(f"QR Code successfully generated for: {target_url}")

TARGET_URL = "https://aryancodesit.github.io/awareness-qr/"

generate_awareness_qr(TARGET_URL)