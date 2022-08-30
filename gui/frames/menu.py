import tkinter as tk
import tkinter.font as tkfont
import typing

from config import Config as Cfg
from gui.frames.base import BaseFrame
from utils.setters import set_linked_button, set_background, set_tooltip_panel

if typing.TYPE_CHECKING:
    from gui.app import App


class MenuPage(BaseFrame):
    def __init__(self, parent: tk.Frame, controller: "App"):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self.controller,
            height=Cfg.FRAME_HEIGHT,
            width=Cfg.FRAME_WIDTH,
            highlightthickness=0,
        )

        set_background(self)
        set_tooltip_panel(self)

        self.canvas.create_text(
            (600, 208),
            text=Cfg.lng.TXT_WELCOME.format(app=Cfg.APP_TITLE),
            font=self.controller.font_title,
            anchor="center",
            fill=Cfg.MENU_COLOR,
        )

        set_linked_button(
            frame=self,
            filename="base/start.png",
            size=(100, 110),
            coords=(600, 408),
            target="ChooseFigurePage",
            description=Cfg.lng.TXT_START_TIP,
        )


class ChooseFigurePage(BaseFrame):
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
        set_tooltip_panel(self)

        # Set frame title
        self.canvas.create_text(
            (600, 100),
            text=Cfg.lng.TXT_SELECT_FIGURE,
            font=self.controller.font_header,
            fill=Cfg.MENU_COLOR,
        )

        set_linked_button(
            frame=self,
            filename="menu/circle.png",
            size=(150, 150),
            coords=(300, 308),
            target="CircleSheetPage",
            description=Cfg.lng.TXT_SELECT_CIRCLE_TIP,
        )
        self.canvas.create_text(
            (300, 420),
            text=Cfg.lng.TXT_CIRCLE_TYPES,
            font=tkfont.Font(family="Ubuntu", size=20, slant="italic"),
            fill=Cfg.CIRCLE_COLOR,
        )

        set_linked_button(
            frame=self,
            filename="menu/triangle.png",
            size=(150, 150),
            coords=(600, 308),
            target="ChooseTrianglePage",
            description=Cfg.lng.TXT_SELECT_TRIANGLE_TIP,
        )
        self.canvas.create_text(
            (600, 450),
            text=Cfg.lng.TXT_TRIANGLE_TYPES,
            font=tkfont.Font(family="Ubuntu", size=20, slant="italic"),
            fill=Cfg.TRIANGLE_COLOR,
        )

        set_linked_button(
            frame=self,
            filename="menu/quadrangle.png",
            size=(150, 150),
            coords=(900, 308),
            target="ChooseQuadranglePage",
            description=Cfg.lng.TXT_SELECT_QUADRANGLE_TIP,
        )
        self.canvas.create_text(
            (900, 465),
            text=Cfg.lng.TXT_QUADRANGLE_TYPES,
            font=tkfont.Font(family="Ubuntu", size=20, slant="italic"),
            fill=Cfg.QUADRANGLE_COLOR,
        )
