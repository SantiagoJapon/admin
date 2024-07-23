"""The state for the home page."""
from datetime import datetime

import reflex as rx
from sqlmodel import select

from .base import AdminState as State
from admin.db_model import  User

class HomeState(State):
  
    
    @rx.var
    def search_users(self) -> list[User]:
        """Get a list of users matching the search query."""
        if self.friend != "":
            with rx.session() as session:
                current_username = self.user.username if self.user is not None else ""
                users = session.exec(
                    select(User).where(
                        User.username.contains(self.friend),
                        User.username != current_username,
                    )
                ).all()
                return users
        return []
