
import reflex as rx
from enum import Enum


MAX_WIDTH = "560px"


class Spacer(Enum):
    SMALL= "0.5em"
    DEFAULT= "1em"
    BIG= "2em"


BASE_STYLE = {
    rx.button: {
        "width":"100%",
        "heigth":"100%",
        "display":"block",
        "padding": Spacer.SMALL.value,
        "margin": Spacer.SMALL.value,
    }
}