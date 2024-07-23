"""Login page. Uses auth_layout to render UI shared with the sign up page."""

import reflex as rx
from admin.layouts import auth_layout
from admin.state.auth import AuthState


def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_username,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Prueba de crear usuario ",
            rx.link("Crear usuario", href="/signup"),
            color="gray",
        ),
    )
