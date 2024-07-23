"""The main admin App."""

from rxconfig import config

import reflex as rx

from admin.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from admin.pages.notas import notas
from admin.pages.usuarios import usuarios 
from admin.pages.login import login 
from admin.pages.signup import signup
from admin.pages.home import home
from admin.pages.profesor import add_professor_form
from admin.state.base import AdminState 



# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

#app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(home, route="/", on_load=AdminState.check_login())
app.add_page(usuarios,route="/usuarios", on_load=AdminState.check_login() )
app.add_page(notas, route="/notas", on_load=AdminState.check_login())
app.add_page(add_professor_form, route="/add_profesor", on_load=AdminState.check_login())