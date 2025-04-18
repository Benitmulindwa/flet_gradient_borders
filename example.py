from flet_gradient_borders import GradientBorders
import flet as ft


def main(page: ft.Page):

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "light"

    box = GradientBorders(
        content=ft.Container(height=100, width=100, border=ft.border.all(2, "yellow")),
        gradient=ft.RadialGradient(
            center=ft.alignment.top_center,
            radius=1,
            colors=["#ffff55", "red", "yellow", "blue", "#c5f6f8"],
        ),
        border_radius=100,
        border_width=3,
    )
    box1 = GradientBorders(
        content=ft.Container(
            width=100,
            height=100,
        ),
        gradient=ft.LinearGradient(
            colors=["blue", "grey", "orange"],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
        ),
        border_radius=0,
        border_width=3,
    )
    box2 = GradientBorders(
        content=ft.TextField(
            hint_text="Enter your name",
            hint_style=ft.TextStyle(color=ft.Colors.with_opacity(0.5, "black")),
            height=40,
            content_padding=8,
        ),
        gradient=ft.LinearGradient(
            colors=["blue", "green", "yellow"],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
        ),
        border_radius=100,
        border_width=3,
    )

    page.add(box, box1, box2)


ft.app(main)
