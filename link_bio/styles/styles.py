
import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor


MAX_WIDTH = "560px"


class Size(Enum):
    SMALL= "0.5em"
    MEDIUM = "0.8em"
    DEFAULT= "1em"
    BIG= "2em"


BASE_STYLE = {
    "background_color":Color.BACKGROUND.value,
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "margin": "0px",
        "border_radius": Size.DEFAULT.value,
        "background_color":Color.CONTENT.value,
        "_hover":{
            "background_color":Color.SECUNDARY.value,
        }
    },
    rx.link: {
        "text_decoration":"none",
        "_hover":{}
    }
}

title_style =dict(
    width="100%",
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)