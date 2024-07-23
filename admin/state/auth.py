"""The authentication state."""
import reflex as rx
from sqlmodel import select

from admin.state.base import AdminState as State, Login


class AuthState(State):
    """The authentication state for sign up and login page."""

    username: str
    password: str
    confirm_password: str

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            if session.exec(select(Login).where(Login.correo == self.username)).first():
                return rx.window_alert("Username already exists.")
            self.user = Login(correo=self.username, contrasena=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(Login).where(Login.correo == self.username)
            ).first()
            if user and user.contrasena == self.password:
                self.user = user
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password.")
