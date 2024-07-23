import reflex as rx

from admin.navigation import navbar
from admin.template import template
from reflex.components import lucide

from admin.styles import FONT_FAMILY

def cards():
    return rx.flex(
        rx.card(
            rx.text("Card 1"),
            lucide.icon(tag="user", size=16),
            
        ),
        rx.card("Card 2"),
        rx.card("Card 3"),
        spacing="5",
        width="100%",
    )

def grid_cards():
    rx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
    ),
    columns="3",
    spacing="4",
    width="100%",
)
    

@template
def usuarios() -> rx.Component:
    return rx.box(
            navbar(heading="Team"),
            rx.box(
               cards(),
               margin_top="calc(50px + 2em)",
            ),
            padding_left="250px",
        )

