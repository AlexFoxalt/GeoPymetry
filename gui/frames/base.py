import pdb
import tkinter as tk

from config import Config as Cfg
from models.base import Processable


class BaseFrame(tk.Frame):
    """
    Defines default attributes that should have valid frame.
    """

    controller = None
    tooltip_panel = None
    bg = None
    Figure = None
    canvas = None
    form_text = None
    calculator_btn = None
    refresh_btn = None


class Calculating(BaseFrame):
    """
    Defines methods that are required for every frame that make calculation.
    """

    Figure: Processable = None

    def get_form(self) -> list:
        return [form for form in self.__dict__.keys() if form.startswith("input")]

    def calculate(self, _: tk.Event) -> None:
        pdb.set_trace()
        form_data = {
            form.replace("input_", ""): float(getattr(self, form).get())
            for form in self.get_form()
        }
        processed_data = self.Figure(**form_data).process()
        if processed_data:
            self._fill_forms(processed_data)
            self._freeze_forms()
            self.canvas.itemconfig(self.form_text, text=Cfg.lng.TXT_CALCULATED)
            self.canvas.itemconfig(self.calculator_btn, state="hidden")
            self.canvas.itemconfig(self.refresh_btn, state="normal")

    def refresh(self, _: tk.Event) -> None:
        self._reset_forms()
        self.canvas.itemconfig(self.calculator_btn, state="normal")
        self.canvas.itemconfig(self.refresh_btn, state="hidden")
        self.canvas.itemconfig(self.form_text, text=Cfg.lng.TXT_FILL_THE_FORM)

    def _reset_forms(self) -> None:
        for form in self.get_form():
            attr = getattr(self, form)
            attr["state"] = "normal"
            attr.delete(first=0, last=tk.END)
            attr.insert(0, "0")
            attr["foreground"] = "black"

    def _freeze_forms(self) -> None:
        for form in self.get_form():
            attr = getattr(self, form)
            attr["state"] = "readonly"

    def _fill_forms(self, data: dict) -> None:
        for key, value in data.items():
            attr = getattr(self, key)
            attr.delete(first=0, last=tk.END)
            attr.insert(0, value)
            if not value:
                attr["foreground"] = "#7B7B7B"
