import os
import base64
import codecs

import logging
from io import BytesIO
from ..commons.types import Any

logger = logging.getLogger(__name__)
DEFAULT_DELAY = 1.5
DEFAULT_PIXEL_RATIO = 2
PNG_FORMAT = "png"
JPG_FORMAT = "jpeg"
GIF_FORMAT = "gif"
PDF_FORMAT = "pdf"
SVG_FORMAT = "svg"
EPS_FORMAT = "eps"
B64_FORMAT = "base64"

SUPPORTED_IMAGE_FORMATS = [
    PNG_FORMAT,
    JPG_FORMAT,
    GIF_FORMAT,
    PDF_FORMAT,
    SVG_FORMAT,
    EPS_FORMAT,
    B64_FORMAT,
]

NOT_SUPPORTED_FILE_TYPE = "Not supported file type '%s'"

MESSAGE_GENERATING = "Generating file ..."
MESSAGE_FILE_SAVED_AS = "File saved in %s"


def make_snapshot(
    driver: Any,
    file_name: str,
    output_name: str,
    delay: float = DEFAULT_DELAY,
    pixel_ratio: int = DEFAULT_PIXEL_RATIO,
    verbose: bool = True,
    is_remove_html: bool = False,
    **keywords
):
    logger.info(MESSAGE_GENERATING)
    file_type = output_name.split(".")[-1]

    content = driver.make_snapshot(
        file_name, file_type, delay, pixel_ratio, **keywords)
    if file_type in [SVG_FORMAT, B64_FORMAT]:
        save_as_text(content, output_name)
    else:
        # pdf, gif, png, jpeg
        content_array = content.split(",")
        if len(content_array) != 2:
            raise OSError(content_array)
        base64_imagedata = content_array[1]
        imagedata = decode_base64(base64_imagedata)
        if file_type in [PDF_FORMAT, GIF_FORMAT, EPS_FORMAT]:
            save_as(imagedata, output_name, file_type)
        elif file_type in [PNG_FORMAT, JPG_FORMAT]:
            save_as_png(imagedata, output_name)
        else:
            raise TypeError(NOT_SUPPORTED_FILE_TYPE.format(file_type))
    if "/" not in output_name:
        output_name = os.path.join(os.getcwd(), output_name)

    if is_remove_html and not file_name.startswith('http'):
        os.unlink(file_name)
    logger.info(MESSAGE_FILE_SAVED_AS % output_name)


def decode_base64(data: str) -> str:
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += "=" * (4 - missing_padding)
    return base64.decodestring(data.encode("utf-8"))


def save_as_png(imagedata: str, output_name: str):
    with open(output_name, "wb") as f:
        f.write(imagedata)


def save_as_text(imagedata: str, output_name: str):
    with codecs.open(output_name, "w", encoding="utf-8") as f:
        f.write(imagedata)


def save_as(imagedata: str, output_name: str, file_type: str):
    try:
        from PIL import Image
        m = Image.open(BytesIO(imagedata))
        m.load()
        color = (255, 255, 255)
        b = Image.new("RGB", m.size, color)
        b.paste(m, mask=m.split()[3])
        b.save(output_name, file_type, quality=100)
    except ModuleNotFoundError:
        raise Exception('Please install PIL for % image type' % file_type)
