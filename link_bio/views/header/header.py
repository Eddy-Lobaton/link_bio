import reflex as rx
def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            fallback="EL",
            radius="full",
            size="6",
            color_scheme="indigo"),
        rx.text("EddyLobaton"),
        rx.text("Hola mi nombres Eddy"),
        rx.text("Soy técnico en geomática")
    )