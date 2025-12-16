import qrcode
import PIL
import io

def generate_qr_code(data: str, fill_color: str = "black", back_color: str = "white", box_size: int = 10):
    """
    Generates a QR code image from the provided data.   
    Parameters:
    data (str): The data to encode in the QR code.
    fill_color (str): The color of the QR code dots.
    back_color (str): The background color of the QR code.
    box_size (int): Pixel size of each QR code box (default: 10) 5-10-20.
    Returns:
    BytesIO: The generated QR code image as bytes.
    """
    qr = qrcode.QRCode(
        version=None,  # Otomatik boyut - veriye göre ayarlanır
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    image_bytes = io.BytesIO()
    img.save(image_bytes, format="PNG")
    image_bytes.seek(0)
    return image_bytes
