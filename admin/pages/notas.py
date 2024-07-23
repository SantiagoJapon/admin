import reflex as rx

from admin.navigation import navbar
from admin.template import template

@template
def notas() -> rx.Component:
    return rx.box(
            navbar(heading="Tools"),
            rx.box(
                rx.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )
