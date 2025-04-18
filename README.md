# flet_gradient_borders
A custom Flet component that renders beautiful gradient borders around any control.

## ✨ Features

- Supports `LinearGradient`, `RadialGradient`, and `SweepGradient`
- Auto-adjusts border radius and hides original control borders
- Fully customizable border width and radius

## 📦 Installation

```pip install flet_gradient_borders```

## 🚀 Usage

```python
import flet as ft
from gradient_border import GradientBorder  # Adjust this import to your file structure

def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Example with LinearGradient
    gb1 = GradientBorder(
        content=ft.Text("Linear Gradient"),
        gradient=["#00c6ff", "#0072ff"]
    )

    # Example with RadialGradient
    gb2 = GradientBorder(
        content=ft.Text("Radial Gradient"),
        gradient=ft.RadialGradient(
            center=ft.alignment.center,
            radius=1,
            colors=["#ff9a9e", "#fad0c4"]
        )
    )

    # Example with SweepGradient
    gb3 = GradientBorder(
        content=ft.Text("Sweep Gradient"),
        gradient=ft.SweepGradient(
            center=ft.alignment.center,
            colors=["#fceabb", "#f8b500", "#fceabb"]
        )
    )

    page.add(gb1, gb2, gb3)

ft.app(target=main)
```