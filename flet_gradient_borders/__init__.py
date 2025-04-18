import flet as ft
from typing import Union


class GradientBorders(ft.Container):
    def __init__(
        self,
        content: ft.Control,
        border_radius: float = 10,
        border_width: float = 4,
        gradient: Union[
            ft.LinearGradient, ft.RadialGradient, ft.SweepGradient
        ] = ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["blue", "yellow", "red"],
        ),
    ):
        self.gradient = gradient

        super().__init__(
            padding=border_width,
            border_radius=border_radius,
            gradient=self.gradient,
        )

        if hasattr(content, "border"):
            content.border = None
            content.border_radius = border_radius
        if hasattr(content, "border_color"):
            content.border_color = "transparent"
            content.focused_border_color = "transparent"
            content.border_radius = border_radius

        self.content = ft.Container(
            content=content,
            padding=0,
            border_radius=border_radius - border_width,
            bgcolor=ft.Colors.SURFACE,
        )
