import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="EL",
                radius="full",
                size="6",
                color_scheme="indigo"),
            rx.vstack(
                rx.heading("EddyLobaton",size="4"),
                rx.text("Hola mi nombres Eddy"),
                rx.hstack(
                link_icon("https://x.com/mouredev"),
                link_icon("https://x.com/mouredev"),
                link_icon("https://x.com/mouredev")
                ),
                align_items="start"
            )
        ),
        rx.text("""Egresado de la carrera de Geomática de SENCICO. Cuento con una experiencia de 9 años en actividades orientadas a la Geomática tanto en el sector público y privado. La formación académica recibida me permite desenvolverme en cualquier ambiente de trabajo de manera eficaz"""),
        gap = Size.BIG.value,
        align_items="start"
    )