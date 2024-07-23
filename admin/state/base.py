
from typing import Optional

import reflex as rx
from admin.db_model import Login

class AdminState(rx.State):
    """The base state for the app."""

    user: Optional[Login] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
