"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width = styles.MAX_WIDTH,
                width="100%",
                margin_y= styles.Size.BIG.value
            ) ,
            width = "100%",
        ),
        footer()
    )

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)

