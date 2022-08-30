import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from typing import Any

from config import Config as Cfg
from gui.frames.circles import CircleSheetPage
from gui.frames.menu import MenuPage, ChooseFigurePage
from gui.frames.quadrangles import (
    ChooseQuadranglePage,
    RectangleSheetPage,
    ParallelogramSheetPage,
    RhombusSheetPage,
    TrapezoidSheetPage,
)
from gui.frames.triangles import (
    ChooseTrianglePage,
    RightTriangleSheetPage,
    EquilateralTriangleSheetPage,
    ArbitraryTriangleSheetPage,
)
from utils.setters import set_icon


class App(tk.Tk):
    frameset = (
        MenuPage,
        ChooseFigurePage,
        ChooseQuadranglePage,
        # Temporary unavailable. For now we have only 1 type of circle.
        # ChooseCirclePage,
        ChooseTrianglePage,
        RightTriangleSheetPage,
        EquilateralTriangleSheetPage,
        ArbitraryTriangleSheetPage,
        RectangleSheetPage,
        ParallelogramSheetPage,
        RhombusSheetPage,
        TrapezoidSheetPage,
        CircleSheetPage,
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        tk.Tk.__init__(self, className=Cfg.APP_TITLE, *args, **kwargs)

        # We can define fonts only in initialized Tkinter app context.
        self.font_title = tkfont.Font(family=Cfg.FONT_TITLE, size=40, weight="bold")
        self.font_header = tkfont.Font(family=Cfg.FONT_HEADER, size=24, weight="bold")
        self.font_filler = tkfont.Font(family=Cfg.FONT_FILLER, size=20, weight="bold")
        self.font_input = tkfont.Font(family=Cfg.FONT_INPUT, size=16, weight="bold")
        self.font_fields = tkfont.Font(family=Cfg.FONT_FIELDS, size=16, slant="italic")

        self.title(Cfg.APP_TITLE)
        self.resizable(Cfg.FRAME_RESIZE_ABILITY, Cfg.FRAME_RESIZE_ABILITY)
        # Set confirm window on exit
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        set_icon(self)

        # Base Frame. Should never be displayed
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self._frames = {}
        self._previous_frame = None

        for Frame in self.frameset:
            page_name = Frame.__name__
            frame = Frame(parent=container, controller=self)
            self._frames[page_name] = frame

        # First frame of app will be MenuPage
        self.switch_frame_to(to="MenuPage")

    def on_close(self) -> None:
        # We want to translate Yes/No buttons if it possible
        self.tk.eval(f"::msgcat::mclocale {Cfg.APP_LANG.lower()}")
        response = messagebox.askyesno(Cfg.lng.ON_CLOSE_TITLE, Cfg.lng.ON_CLOSE_MSG)
        if response:
            self.destroy()

    def switch_frame_to(self, _: tk.Event = None, to: str = "MenuPage") -> None:
        if to == self._previous_frame:
            # Prevents bug if target page is the same as current.
            return

        next_frame = self._frames[to]
        next_frame.canvas.pack()

        if self._previous_frame:
            self._frames[self._previous_frame].canvas.pack_forget()

        self._previous_frame = to

        # Raise frame at the top layer of window
        next_frame.tkraise()
