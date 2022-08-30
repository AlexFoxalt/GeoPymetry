import os
import tkinter as tk
import tkinter.font as tkfont
import typing
from typing import Literal, Union

from PIL import ImageTk, Image

from config import Config as Cfg
from gui.frames.base import BaseFrame, Calculating
from utils.utils import get_resized_image

if typing.TYPE_CHECKING:
    from gui.app import App


def set_icon(app: "App") -> None:
    app.icon = ImageTk.PhotoImage(
        Image.open(os.path.join(Cfg.STATIC_DIR, Cfg.ICON_IMG))
    )
    app.iconphoto(False, app.icon)


def set_background(frame: BaseFrame) -> None:
    # For correct saving pic, tkinter requires to save it to some var.
    frame.bg = get_resized_image(
        filename=Cfg.BG_IMG, size=(Cfg.FRAME_WIDTH, Cfg.FRAME_HEIGHT)
    )
    frame.canvas.create_image((0, 0), image=frame.bg, anchor="nw")


def set_linked_button(
    frame: BaseFrame,
    filename: str,
    size: tuple[int, int],
    coords: tuple[int, int],
    target: str = None,
    description: str = "",
    state: Literal["normal", "hidden"] = "normal",
) -> None:
    """
    Set image with hyperlink on click to next frame.
    :param frame: Frame to place button
    :param filename: Path and filename of button image
    :param size: Size of image. Tuple(vertical, horizontal) in pixels. Image will be resized on demand
    :param coords: Coords of image. Tuple(x, y)
    :param target: Anchor of hyperlink represented by frame name
    :param description: Text that will be displayed in tooltip on hover
    :param state: If set to hidden, button will be not visible
    :return: None
    """
    fn = os.path.splitext(os.path.basename(filename))[0]
    normal_img = f"{fn}_normal_img"  # No mouse hover img
    active_img = f"{fn}_active_img"  # On hover img
    btn = f"{fn}_btn"

    setattr(frame, normal_img, get_resized_image(filename=filename, size=size))
    setattr(
        frame,
        active_img,
        get_resized_image(filename=filename, size=(size[0] + 5, size[1] + 5)),
    )
    setattr(
        frame,
        btn,
        frame.canvas.create_image(
            *coords,
            image=getattr(frame, normal_img),
            activeimage=getattr(frame, active_img),
            state=state,
        ),
    )
    if target:
        frame.canvas.tag_bind(
            getattr(frame, btn),
            "<Button-1>",
            lambda event, to=target: frame.controller.switch_frame_to(event, to),
        )

    def one_hover_btn_enter(_: tk.Event, frame: BaseFrame, text: str) -> None:
        """Increase image size on hover"""
        frame.canvas.config(cursor="hand2")
        frame.canvas.itemconfig(frame.tooltip_panel, text=text)

    def one_hover_btn_exit(_: tk.Event, frame: BaseFrame) -> None:
        """Normalize image size not on hover"""
        frame.canvas.config(cursor="")
        frame.canvas.itemconfig(frame.tooltip_panel, text="")

    frame.canvas.tag_bind(
        getattr(frame, btn),
        "<Enter>",
        lambda event, frame=frame, text=description: one_hover_btn_enter(
            event, frame, text
        ),
    )
    frame.canvas.tag_bind(
        getattr(frame, btn),
        "<Leave>",
        lambda event, frame=frame: one_hover_btn_exit(event, frame),
    )


def set_home_btn(frame: BaseFrame) -> None:
    set_linked_button(
        frame=frame,
        filename="base/home.png",
        size=(35, 35),
        coords=(25, 23),
        target="ChooseFigurePage",
        description=Cfg.lng.TXT_HOME_TIP,
    )


def set_tooltip_panel(frame: BaseFrame) -> None:
    frame.tooltip_panel = frame.canvas.create_text(
        5,
        805,
        text="",
        anchor="w",
        fill="#282828",
        font=tkfont.Font(family="Roboto", size=10),
    )
    frame.version_info = frame.canvas.create_text(
        1100,
        805,
        text=f"Version: {Cfg.VERSION}",
        anchor="w",
        fill="#282828",
        font=tkfont.Font(family="Roboto", size=10, slant="italic"),
    )


def set_input_form(
    frame: BaseFrame,
    attr: str,
    text_pos: tuple[int, int],
    input_pos: tuple[int, int],
    text: str = "",
    color: str = "white",
    num_only: bool = True,
) -> None:
    """
    Set input form on passed frame.
    :param frame: Frame to place input form
    :param attr: Name of attribute to assign form to frame object
    :param text_pos: Text position. Tuple(x, y)
    :param input_pos: Form position. Tuple(x, y)
    :param text: Text of form that will be displayed near
    :param color: Color of cursor in form
    :param num_only: Flag that provides validation of int/float only input
    :return: None
    """

    def is_number(value: Union[int, float]) -> bool:
        """
        Simple validation for only float/int input
        """
        if value and num_only:
            try:
                float(value)
            except ValueError:
                return False
        return True

    setattr(
        frame,
        attr,
        tk.Entry(
            frame.canvas,
            width=8,
            justify="center",
            font=frame.controller.font_input,
            validate="key",
            validatecommand=(frame.register(is_number), "%P"),
            state="normal",
            bd=0,
            insertbackground=color,
            highlightthickness=0,
        ),
    )
    getattr(frame, attr).insert(0, "0")
    frame.canvas.create_window(*input_pos, window=getattr(frame, attr))
    frame.canvas.create_text(
        *text_pos,
        text=text,
        font=frame.controller.font_fields,
        fill="black",
        anchor="e",
    )


def set_calculation_btns(frame: Calculating) -> None:
    set_linked_button(
        frame=frame,
        filename="base/calculator.png",
        size=(73, 103),
        coords=(1110, 650),
        description=Cfg.lng.TXT_CONFIRM_FORM,
    )
    set_linked_button(
        frame=frame,
        filename="base/refresh.png",
        size=(103, 103),
        coords=(1110, 650),
        description=Cfg.lng.TXT_REFRESH_THE_FORM,
        state="hidden",
    )
    frame.canvas.tag_bind(frame.calculator_btn, "<Button-1>", frame.calculate)
    frame.canvas.tag_bind(frame.refresh_btn, "<Button-1>", frame.refresh)
