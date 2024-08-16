from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from fractions import Fraction

def get_decimal_from_dms(dms, ref):
    degrees, minutes, seconds = dms
    decimal = degrees + minutes / 60.0 + seconds / 3600.0
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_image_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if not exif_data:
        return "EXIF verisi bulunamadı."

    exif = {TAGS.get(tag): value for tag, value in exif_data.items()}

    # Çekim tarihi
    creation_date = exif.get('DateTimeOriginal') or exif.get('DateTime')

    # GPS bilgileri
    gps_info = exif.get('GPSInfo')
    if gps_info:
        gps_data = {}
        for tag, value in gps_info.items():
            decoded_tag = GPSTAGS.get(tag)
            gps_data[decoded_tag] = value

        # Enlem ve boylam bilgileri
        lat = get_decimal_from_dms(gps_data['GPSLatitude'], gps_data['GPSLatitudeRef'])
        lon = get_decimal_from_dms(gps_data['GPSLongitude'], gps_data['GPSLongitudeRef'])

        location = f"Enlem: {lat}, Boylam: {lon}"
    else:
        location = "GPS bilgisi bulunamadı."

    return f"Fotoğrafın çekildiği tarih: {creation_date}\nÇekim yeri: {location}"

# Örnek kullanım
image_path = 'ornek_fotograf.jpg'  # Buraya fotoğrafın yolunu yazın
print(get_image_metadata(image_path))
