import os

from languages import EN, RU, UA, BaseLanguage


class Config:
    """
    Main app config that provides major settings
    """

    APP_TITLE = "GeoPymetry"
    APP_LANG = "en"
    FRAME_WIDTH = 1200
    FRAME_HEIGHT = 816
    FRAME_RESIZE_ABILITY = False
    LANGUAGES = (RU, EN, UA)
    ROOT_DIR = os.path.dirname(os.path.abspath("config"))
    STATIC_DIR = f"{ROOT_DIR}/static"
    BG_IMG = "base/bg.jpg"
    ICON_IMG = "base/icon.png"
    FLOAT_ROUNDING = 3
    CALC_DEPTH = 10

    FONT_TITLE = "Segoe UI"
    FONT_HEADER = "Segoe UI"
    FONT_FILLER = "Segoe UI"
    FONT_INPUT = "Times New Roman"
    FONT_FIELDS = "Times New Roman"

    MENU_COLOR = "#ff7f00"
    QUADRANGLE_COLOR = "#cc2f00"
    TRIANGLE_COLOR = "#3bb433"
    CIRCLE_COLOR = "#1e8db9"

    LOG_MSG_TEMPLATE = '[{time}] {type} "{msg}"'
    VERSION = "1.0.1"

    @classmethod
    @property
    def lng(cls) -> BaseLanguage:
        """
        Returns language class according to config
        """
        languages = {lang.__name__: lang for lang in cls.LANGUAGES}
        return languages[cls.APP_LANG.upper()]
