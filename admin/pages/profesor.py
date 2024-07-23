import reflex as rx
from datetime import datetime

class AddProfessorState(rx.State):
    nombre: str = ""
    apellido: str = ""
    correo: str = ""
    contrasena: str = ""

    def add_professor(self, form_data):
        self.nombre = form_data.get('nombre', '')
        self.apellido = form_data.get('apellido', '')
        self.correo = form_data.get('correo', '')
        self.contrasena = form_data.get('contrasena', '')

        with rx.session() as session:
            # Create Login
            login = Login(correo=self.correo, contrasena=self.contrasena)
            session.add(login)
            session.flush()  # This will assign an ID to login

            # Create Persona
            persona = Persona(nombre=self.nombre, apellido=self.apellido, login_id=login.id)
            session.add(persona)
            session.flush()  # This will assign an ID to persona

            # Create Profesor
            profesor = Profesor(persona_id=persona.id)
            session.add(profesor)

            session.commit()

        # Reset form fields
        self.nombre = ""
        self.apellido = ""
        self.correo = ""
        self.contrasena = ""

        return rx.window_alert("Professor added successfully!")


def add_professor_form():
    return rx.vstack(
        rx.heading("Add New Professor", size="4"),  # Changed size to "4"
        rx.form(
            rx.vstack(
                # First Name input field
                rx.input(
                    placeholder="First Name",
                    name="nombre",
                    value=AddProfessorState.nombre,
                    on_change=AddProfessorState.set_nombre,
                ),
                # Last Name input field
                rx.input(
                    placeholder="Last Name",
                    name="apellido",
                    value=AddProfessorState.apellido,
                    on_change=AddProfessorState.set_apellido,
                ),
                # Email input field
                rx.input(
                    placeholder="Email",
                    name="correo",
                    type="email",
                    value=AddProfessorState.correo,
                    on_change=AddProfessorState.set_correo,
                ),
                # Password input field
                rx.input(
                    placeholder="Password",
                    name="contrasena",
                    type="password",
                    value=AddProfessorState.contrasena,
                    on_change=AddProfessorState.set_contrasena,
                ),
                # Submit button
                rx.button(
                    "Add Professor",
                    type="submit",
                ),
            ),
            on_submit=AddProfessorState.add_professor,
        ),
        width="100%",          # Set width to 100%
        max_width="400px",     # Set max width to 400px
        spacing="4",           # Set spacing to 4
    )

