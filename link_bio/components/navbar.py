import reflex as rx
def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Nexus Motos",
            height="48"
        ),
        position="sticky",
        bg = "red",
        padding = "16px",
        z_index = "999"
    )
