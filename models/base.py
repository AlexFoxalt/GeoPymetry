import math
from typing import Union
from tkinter import messagebox

from config import Config as Cfg
from utils.utils import get_time


class Processable:
    """
    Class that provides functionality of data processing & error handling
    """

    def process(self) -> dict[str, Union[int, float]]:
        # We give the model the opportunity to calculate all possible parameters of the figure
        # Just call every property for N times
        try:
            for _ in range(Cfg.CALC_DEPTH):
                [getattr(self, attr[1:]) for attr in self.__dict__.keys()]
        except ValueError as err:
            print(
                Cfg.LOG_MSG_TEMPLATE.format(
                    time=get_time(), type="ERROR", msg=err.args[0]
                )
            )
            messagebox.showerror(Cfg.lng.ERR_TITLE, Cfg.lng.ERR_FIGURE_NOT_EXIST)
        else:
            result = {
                "input" + key: round(getattr(self, key[1:]), Cfg.FLOAT_ROUNDING)
                for key in self.__dict__.keys()
            }
            for key, value in result.items():
                # If it possible to return integer, let's return integer
                # Values like '3.0' are not beautiful
                if int(value) == value:
                    result[key] = int(value)
            return result


class Trigonometric:
    """
    Class that provides simple trigonometric operations with angles
    """

    @staticmethod
    def to_rad(angle: Union[int, float]) -> Union[int, float, None]:
        return math.radians(angle) if angle else None

    @staticmethod
    def to_deg(angle: Union[int, float]) -> Union[int, float, None]:
        return math.degrees(angle) if angle else None
