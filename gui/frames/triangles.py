import tkinter as tk
import typing

from config import Config as Cfg
from gui.frames.base import Calculating, BaseFrame
from utils.utils import get_resized_image
from models.triangles import RightTriangle, EquilateralTriangle, ArbitraryTriangle
from utils.setters import (
    set_home_btn,
    set_background,
    set_linked_button,
    set_tooltip_panel,
    set_input_form,
    set_calculation_btns,
)

if typing.TYPE_CHECKING:
    from gui.app import App


class ChooseTrianglePage(BaseFrame):
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
            text=Cfg.lng.TXT_SELECT_TRIANGLE,
            font=self.controller.font_header,
            fill=Cfg.TRIANGLE_COLOR,
        )

        set_linked_button(
            frame=self,
            filename="selectors/right_triangle.png",
            size=(300, 225),
            coords=(300, 308),
            target="RightTriangleSheetPage",
            description=Cfg.lng.TXT_SELECT_RIGHT_TRIANGLE_TYPE_TIP,
        )
        set_linked_button(
            frame=self,
            filename="selectors/equilateral_triangle.png",
            size=(300, 225),
            coords=(900, 308),
            target="EquilateralTriangleSheetPage",
            description=Cfg.lng.TXT_SELECT_EQUILATERAL_TRIANGLE_TYPE_TIP,
        )
        set_linked_button(
            frame=self,
            filename="selectors/arbitrary_triangle.png",
            size=(300, 225),
            coords=(600, 608),
            target="ArbitraryTriangleSheetPage",
            description=Cfg.lng.TXT_SELECT_ARBITRARY_TRIANGLE_TYPE_TIP,
        )


class RightTriangleSheetPage(Calculating):
    Figure = RightTriangle

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
            filename="sheets/right_triangle_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_cathetus_ab",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_CATHETUS}: AB",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_cathetus_ac",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_CATHETUS}: AC",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_hypotenuse_bc",
            text_pos=(175, 680),
            input_pos=(235, 680),
            text=f"{Cfg.lng.TXT_HYPOTENUSE}: BC",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(175, 745),
            input_pos=(235, 745),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_small_r",
            text_pos=(635, 550),
            input_pos=(695, 550),
            text=f"{Cfg.lng.TXT_SMALL_R}: r",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_big_r",
            text_pos=(635, 615),
            input_pos=(695, 615),
            text=f"{Cfg.lng.TXT_BIG_R}: R",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_height",
            text_pos=(635, 680),
            input_pos=(695, 680),
            text=f"{Cfg.lng.TXT_HEIGHT}: h",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(635, 745),
            input_pos=(695, 745),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_median",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_MEDIAN}: m",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_a",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_ANGLE}: a°",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_b",
            text_pos=(925, 680),
            input_pos=(980, 680),
            text=f"{Cfg.lng.TXT_ANGLE}: b°",
            color=Cfg.TRIANGLE_COLOR,
        )


class ArbitraryTriangleSheetPage(Calculating):
    Figure = ArbitraryTriangle

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
            filename="sheets/arbitrary_triangle_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_side_ab",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_SIDE}: AB",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_ac",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_SIDE}: AC",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_bc",
            text_pos=(175, 680),
            input_pos=(235, 680),
            text=f"{Cfg.lng.TXT_SIDE}: BC",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(175, 745),
            input_pos=(235, 745),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_small_r",
            text_pos=(635, 550),
            input_pos=(695, 550),
            text=f"{Cfg.lng.TXT_SMALL_R}: r",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_big_r",
            text_pos=(635, 615),
            input_pos=(695, 615),
            text=f"{Cfg.lng.TXT_BIG_R}: R",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_height",
            text_pos=(635, 680),
            input_pos=(695, 680),
            text=f"{Cfg.lng.TXT_HEIGHT}: h",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(635, 745),
            input_pos=(695, 745),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_median",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_MEDIAN}: m",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_a",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_ANGLE}: a°",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_b",
            text_pos=(925, 680),
            input_pos=(980, 680),
            text=f"{Cfg.lng.TXT_ANGLE}: b°",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_c",
            text_pos=(925, 745),
            input_pos=(980, 745),
            text=f"{Cfg.lng.TXT_ANGLE}: c°",
            color=Cfg.TRIANGLE_COLOR,
        )


class EquilateralTriangleSheetPage(Calculating):
    Figure = EquilateralTriangle

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
            filename="sheets/equilateral_triangle_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_side",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_SIDE}",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_small_r",
            text_pos=(635, 550),
            input_pos=(695, 550),
            text=f"{Cfg.lng.TXT_SMALL_R}: r",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_big_r",
            text_pos=(635, 615),
            input_pos=(695, 615),
            text=f"{Cfg.lng.TXT_BIG_R}: R",
            color=Cfg.TRIANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_height",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_HEIGHT}: h",
            color=Cfg.TRIANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.TRIANGLE_COLOR,
        )
