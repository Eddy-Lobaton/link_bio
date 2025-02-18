import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
       link_button("Twich","https://www.facebook.com"),
       link_button("Youtube","http://twicht.tv/mouredev"),
       link_button("Discord","http://twicht.tv/mouredev")
    )