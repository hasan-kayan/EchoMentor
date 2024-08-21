from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from fractions import Fraction

def get_decimal_from_dms(dms, ref):
    """
    Convert degrees, minutes, and seconds (DMS) to decimal format.

    Args:
        dms (tuple): A tuple containing degrees, minutes, and seconds.
        ref (str): The reference direction ('N', 'S', 'E', 'W').

    Returns:
        float: The decimal representation of the DMS value.
    """
    degrees, minutes, seconds = dms
    decimal = degrees + minutes / 60.0 + seconds / 3600.0
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_image_metadata(image_path):
    """
    Extract metadata from an image file.

    Args:
        image_path (str): The path to the image file.

    Returns:
        dict: A dictionary containing the metadata such as creation date and GPS location.
    """
    image = Image.open(image_path)
    exif_data = image._getexif()

    if not exif_data:
        return {"error": "No EXIF data found."}

    exif = {TAGS.get(tag): value for tag, value in exif_data.items()}

    # Creation date
    creation_date = exif.get('DateTimeOriginal') or exif.get('DateTime')

    # GPS information
    gps_info = exif.get('GPSInfo')
    if gps_info:
        gps_data = {}
        for tag, value in gps_info.items():
            decoded_tag = GPSTAGS.get(tag)
            gps_data[decoded_tag] = value

        # Latitude and Longitude
        lat = get_decimal_from_dms(gps_data['GPSLatitude'], gps_data['GPSLatitudeRef'])
        lon = get_decimal_from_dms(gps_data['GPSLongitude'], gps_data['GPSLongitudeRef'])

        location = {"latitude": lat, "longitude": lon}
    else:
        location = "No GPS data found."

    return {
        "creation_date": creation_date,
        "location": location
    }

