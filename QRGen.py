import qrcode
import io
import base64
from PIL import Image

# Generate the QR code image from a link
def generate_qr_image(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_image_to_file(link, filename="qr_code.png"):
    img = generate_qr_image(link)
    img.save(filename)
    print(f"QR Code saved to {filename}")

def main():
    # Fallback main function for environments that do not support servers
    test_url = "https://www.youtube.com/"
    save_qr_image_to_file(test_url)

if __name__ == "__main__":
    main()
