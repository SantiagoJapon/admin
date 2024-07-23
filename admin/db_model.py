
from datetime import datetime
from typing import List, Optional
from sqlmodel import Field, Relationship

import reflex as rx


class Login(rx.Model, table=True):
    #id: Optional[int] = Field(default=None, primary_key=True)
    correo: str
    contrasena: str
    persona: Optional["Persona"] = Relationship(back_populates="login")


class Persona(rx.Model, table=True):
    #id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    login_id: Optional[int] = Field(default=None, foreign_key="login.id")
    login: Optional[Login] = Relationship(back_populates="persona")
    administrador: Optional["Administrador"] = Relationship(back_populates="persona", sa_relationship_kwargs={"uselist": False})
    profesor: Optional["Profesor"] = Relationship(back_populates="persona", sa_relationship_kwargs={"uselist": False})
    estudiante: Optional["Estudiante"] = Relationship(back_populates="persona", sa_relationship_kwargs={"uselist": False})
    #mensajes_enviados: List["Mensaje"] = Relationship(back_populates="remitente")
    #mensajes_recibidos: List["Mensaje"] = Relationship(back_populates="destinatario")


class Administrador(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    persona_id: int = Field(default=None, foreign_key="persona.id")

    persona: Persona = Relationship(back_populates="administrador")
    reportes: List["Reporte"] = Relationship(back_populates="administrador")


class Profesor(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    persona_id: int = Field(default=None, foreign_key="persona.id")

    persona: Persona = Relationship(back_populates="profesor")
    cursos: List["Curso"] = Relationship(back_populates="profesor")


class Estudiante(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    persona_id: int = Field(default=None, foreign_key="persona.id")

    persona: Persona = Relationship(back_populates="estudiante")
    cursos: List["EstudianteCurso"] = Relationship(back_populates="estudiante")
    calificaciones: List["Calificacion"] = Relationship(back_populates="estudiante")


class Curso(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: Optional[str]
    codigo: str
    profesor_id: Optional[int] = Field(default=None, foreign_key="profesor.id")

    profesor: Optional[Profesor] = Relationship(back_populates="cursos")
    horarios: List["Horario"] = Relationship(back_populates="curso")
    calificaciones: List["Calificacion"] = Relationship(back_populates="curso")
    estudiantes: List["EstudianteCurso"] = Relationship(back_populates="curso")


class Horario(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    inicio: datetime
    fin: datetime
    aula: Optional[str]
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id")

    curso: Optional[Curso] = Relationship(back_populates="horarios")


class Calificacion(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str
    nota: float
    comentarios: Optional[str]
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id")
    estudiante_id: Optional[int] = Field(default=None, foreign_key="estudiante.id")

    curso: Optional[Curso] = Relationship(back_populates="calificaciones")
    estudiante: Optional[Estudiante] = Relationship(back_populates="calificaciones")


class Reporte(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str
    fechaGeneracion: datetime
    contenido: Optional[str]
    administrador_id: Optional[int] = Field(default=None, foreign_key="administrador.id")

    administrador: Optional[Administrador] = Relationship(back_populates="reportes")



class EstudianteCurso(rx.Model, table=True):
    estudiante_id: Optional[int] = Field(default=None, foreign_key="estudiante.id", primary_key=True)
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id", primary_key=True)

    estudiante: Optional[Estudiante] = Relationship(back_populates="cursos")
    curso: Optional[Curso] = Relationship(back_populates="estudiantes")



