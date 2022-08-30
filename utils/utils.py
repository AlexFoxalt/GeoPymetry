import os
from datetime import datetime

from PIL import ImageTk, Image

from config import Config as Cfg


def get_resized_image(filename: str, size: tuple[int, int]) -> ImageTk.PhotoImage:
    """Returns resized image according to passed size"""
    path = os.path.join(Cfg.STATIC_DIR, filename)
    raw = Image.open(fp=path)
    resized = raw.resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized)


def get_time() -> str:
    return datetime.now().time().strftime("%H:%M:%S")
