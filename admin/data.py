"""Mock data to populate the admin charts and tables."""

import reflex as rx
from admin.graphs import Area, Line

stat_card_data = [
    [
        "Promedio Tareas",
        "8.3",
        "+12%",
    ],
    [
        "Promedio Lecciones",
        "7.8",
        "+5%",
    ],
    [
        "Promedio Actividades",
        "8.6",
        "-3%",
    ],
    [
        "Promedio Total",
        "8.23",
        "+2%",
    ],
]

line_chart_data = [
    {"name": "Paraelo A", "pt": 8.1, "pl": 7.5 ,"cal": 10},
    {"name": "Paralelo B", "pt": 8.5, "pl": 8.2,"cal": 10},
    {"name": "Paralelo C", "pt": 7.5, "pl": 7.8, "cal": 10},
]


lines = [
    Line(data_key="pt", stroke="#8884d8"),
    Line(data_key="pl", stroke="var(--accent-8)"),
]


pie_chart_data = [
    {"name": "Paralelo A", "value": 400, "fill": "var(--red-7)"},
    {"name": "Paralelo B", "value": 300, "fill": "var(--green-7)"},
    {"name": "Paralelo C", "value": 300, "fill": "var(--purple-7)"},
   
]

area_chart_data = line_chart_data

areas = [
    Area(data_key="pv", stroke="#8884d8", fill="#8884d8"),
    Area(data_key="uv", stroke="var(--accent-8)", fill="var(--accent-8)"),
]


tabular_data = [
    ["Nombre", "Email", "Rol"],
    ["Daddy Acacho", "danilo@example.com", rx.badge("Profesor")],
    ["Santiago Japon", "zahra@example.com", rx.badge("Admin", variant="surface")],
    ["Anthony Perez", "jasper@example.com", rx.badge("Profesor")],
]
