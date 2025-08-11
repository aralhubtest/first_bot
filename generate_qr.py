import qrcode
import os

def generate(data: str, file_path: str = 'qr_code.png'):

    img = qrcode.make(data)
    img.save(os.path.join('qr_codes', file_path))

    return os.path.join('qr_codes', file_path)

if __name__ == "__main__":
    generate('google.com')