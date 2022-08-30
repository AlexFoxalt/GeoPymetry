import tkinter as tk
import typing

from config import Config as Cfg
from gui.frames.base import BaseFrame, Calculating
from models.circles import Circle
from utils.setters import (
    set_home_btn,
    set_background,
    set_tooltip_panel,
    set_calculation_btns,
    set_input_form,
    set_linked_button,
)
from utils.utils import get_resized_image

if typing.TYPE_CHECKING:
    from gui.app import App


class ChooseCirclePage(BaseFrame):
    """
    This page is not available because there is only 1 possible choice on Circle page.
    For now, we'll just skip this step.
    But if we have more circles, we can easily activate this page.
    """

    def __init__(self, parent: tk.Frame, controller: "App"):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self.controller,
            height=Cfg.FRAME_HEIGHT,
            width=Cfg.FRAME_WIDTH,
            highlightthickness=0,
            borderwidth=0,
        )

        set_background(self)
        set_home_btn(self)
        set_tooltip_panel(self)

        self.canvas.create_text(
            (600, 100),
            text=Cfg.lng.TXT_SELECT_CIRCLE,
            font=self.controller.font_header,
            fill=Cfg.CIRCLE_COLOR,
        )
        set_linked_button(
            frame=self,
            filename="menu/circle.png",
            size=(300, 225),
            coords=(300, 308),
            target="CircleSheetPage",
            description=Cfg.lng.TXT_SELECT_CIRCLE_TYPE_TIP,
        )


class CircleSheetPage(Calculating):
    Figure = Circle

    def __init__(self, parent: tk.Frame, controller: "App"):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self.controller,
            height=Cfg.FRAME_HEIGHT,
            width=Cfg.FRAME_WIDTH,
            highlightthickness=0,
            borderwidth=0,
        )

        set_background(self)
        set_home_btn(self)
        set_tooltip_panel(self)
        set_calculation_btns(self)

        self.sheet_img = get_resized_image(
            filename="sheets/circle_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.CIRCLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_radius",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_RADIUS}: r",
            color=Cfg.CIRCLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_diameter",
            text_pos=(550, 550),
            input_pos=(610, 550),
            text=f"{Cfg.lng.TXT_DIAMETER}: d",
            color=Cfg.CIRCLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.CIRCLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_CIRCUMFERENCE}: L",
            color=Cfg.CIRCLE_COLOR,
        )
