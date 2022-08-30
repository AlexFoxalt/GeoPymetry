import tkinter as tk
import typing

from config import Config as Cfg
from gui.frames.base import BaseFrame, Calculating
from models.quadrangles import Rectangle, Parallelogram, Rhombus, Trapezoid
from utils.setters import (
    set_home_btn,
    set_background,
    set_linked_button,
    set_tooltip_panel,
    set_input_form,
    set_calculation_btns,
)
from utils.utils import get_resized_image

if typing.TYPE_CHECKING:
    from gui.app import App


class ChooseQuadranglePage(BaseFrame):
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
            text=Cfg.lng.TXT_SELECT_QUADRANGLE,
            font=self.controller.font_header,
            fill=Cfg.QUADRANGLE_COLOR,
        )

        set_linked_button(
            frame=self,
            filename="selectors/rectangle.png",
            size=(300, 225),
            coords=(300, 308),
            target="RectangleSheetPage",
            description=Cfg.lng.TXT_SELECT_RECTANGLE_TIP,
        )
        set_linked_button(
            frame=self,
            filename="selectors/parallelogram.png",
            size=(300, 225),
            coords=(900, 308),
            target="ParallelogramSheetPage",
            description=Cfg.lng.TXT_SELECT_PARALLELOGRAM_TIP,
        )
        set_linked_button(
            frame=self,
            filename="selectors/trapezoid.png",
            size=(300, 225),
            coords=(300, 608),
            target="TrapezoidSheetPage",
            description=Cfg.lng.TXT_SELECT_TRAPEZOID_TIP,
        )
        set_linked_button(
            frame=self,
            filename="selectors/rhombus.png",
            size=(300, 225),
            coords=(900, 608),
            target="RhombusSheetPage",
            description=Cfg.lng.TXT_SELECT_RHOMBUS_TIP,
        )


class RectangleSheetPage(Calculating):
    Figure = Rectangle

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
            filename="sheets/rectangle_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_side_ab",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_SIDE}: AB/CD",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_bc",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_SIDE}: BC/AD",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_angle_x",
            text_pos=(550, 550),
            input_pos=(610, 550),
            text=f"{Cfg.lng.TXT_ANGLE}: x",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_y",
            text_pos=(550, 615),
            input_pos=(610, 615),
            text=f"{Cfg.lng.TXT_ANGLE}: y",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_diag",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₁/d₂",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(925, 680),
            input_pos=(980, 680),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.QUADRANGLE_COLOR,
        )


class ParallelogramSheetPage(Calculating):
    Figure = Parallelogram

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
            filename="sheets/parallelogram_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_side_ab",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_SIDE}: AB/CD",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_bc",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_SIDE}: BC/AD",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_height",
            text_pos=(175, 680),
            input_pos=(235, 680),
            text=f"{Cfg.lng.TXT_HEIGHT}: h",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_angle_x",
            text_pos=(550, 550),
            input_pos=(610, 550),
            text=f"{Cfg.lng.TXT_ANGLE}: x°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_y",
            text_pos=(550, 615),
            input_pos=(610, 615),
            text=f"{Cfg.lng.TXT_ANGLE}: y°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_a",
            text_pos=(550, 680),
            input_pos=(610, 680),
            text=f"{Cfg.lng.TXT_ANGLE}: a°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_b",
            text_pos=(550, 745),
            input_pos=(610, 745),
            text=f"{Cfg.lng.TXT_ANGLE}: b°",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_diag_1",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₁",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_diag_2",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₂",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(925, 680),
            input_pos=(980, 680),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(925, 745),
            input_pos=(980, 745),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.QUADRANGLE_COLOR,
        )


class TrapezoidSheetPage(Calculating):
    Figure = Trapezoid

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
            filename="sheets/trapezoid_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_side_ab",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_SIDE}: AB",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_bc",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_SIDE}: BC",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_cd",
            text_pos=(175, 680),
            input_pos=(235, 680),
            text=f"{Cfg.lng.TXT_SIDE}: CD",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_side_da",
            text_pos=(175, 745),
            input_pos=(235, 745),
            text=f"{Cfg.lng.TXT_SIDE}: DA",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_angle_a",
            text_pos=(425, 550),
            input_pos=(485, 550),
            text=f"{Cfg.lng.TXT_ANGLE}: a°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_b",
            text_pos=(425, 615),
            input_pos=(485, 615),
            text=f"{Cfg.lng.TXT_ANGLE}: b°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_c",
            text_pos=(425, 680),
            input_pos=(485, 680),
            text=f"{Cfg.lng.TXT_ANGLE}: c°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_d",
            text_pos=(425, 745),
            input_pos=(485, 745),
            text=f"{Cfg.lng.TXT_ANGLE}: d°",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_diag_1",
            text_pos=(675, 550),
            input_pos=(730, 550),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₁",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_diag_2",
            text_pos=(675, 615),
            input_pos=(730, 615),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₂",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_height",
            text_pos=(675, 680),
            input_pos=(730, 680),
            text=f"{Cfg.lng.TXT_HEIGHT}: h",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_median",
            text_pos=(675, 745),
            input_pos=(730, 745),
            text=f"{Cfg.lng.TXT_MEDIAN}: m",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.QUADRANGLE_COLOR,
        )


class RhombusSheetPage(Calculating):
    Figure = Rhombus

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
            filename="sheets/rhombus_sheet.png", size=(1000, 400)
        )
        self.canvas.create_image(600, 250, image=self.sheet_img)

        self.form_text = self.canvas.create_text(
            (600, 480),
            text=Cfg.lng.TXT_FILL_THE_FORM,
            font=self.controller.font_filler,
            fill=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_angle_a",
            text_pos=(175, 550),
            input_pos=(235, 550),
            text=f"{Cfg.lng.TXT_ANGLE}: a°",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_angle_b",
            text_pos=(175, 615),
            input_pos=(235, 615),
            text=f"{Cfg.lng.TXT_ANGLE}: b°",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_side",
            text_pos=(550, 550),
            input_pos=(610, 550),
            text=f"{Cfg.lng.TXT_SIDE}: AB/BC/CD/DA",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_height",
            text_pos=(550, 615),
            input_pos=(610, 615),
            text=f"{Cfg.lng.TXT_HEIGHT}: h",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_small_r",
            text_pos=(550, 680),
            input_pos=(610, 680),
            text=f"{Cfg.lng.TXT_SMALL_R}: r",
            color=Cfg.QUADRANGLE_COLOR,
        )

        set_input_form(
            frame=self,
            attr="input_diag_1",
            text_pos=(925, 550),
            input_pos=(980, 550),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₁",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_diag_2",
            text_pos=(925, 615),
            input_pos=(980, 615),
            text=f"{Cfg.lng.TXT_DIAGONAL}: d₂",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_square",
            text_pos=(925, 680),
            input_pos=(980, 680),
            text=f"{Cfg.lng.TXT_SQUARE}: S",
            color=Cfg.QUADRANGLE_COLOR,
        )
        set_input_form(
            frame=self,
            attr="input_perimeter",
            text_pos=(925, 745),
            input_pos=(980, 745),
            text=f"{Cfg.lng.TXT_PERIMETER}: P",
            color=Cfg.QUADRANGLE_COLOR,
        )
