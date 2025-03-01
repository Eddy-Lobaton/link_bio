import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def links() -> rx.Component:
   return rx.vstack(
      title("Comunidad"),
      link_button("Twich","Directos lunes a viernes","https://www.facebook.com"),
      link_button("Youtubeeeeeeeeeeeeeee","Tutoriales semanales","http://twicht.tv/mouredev"),
      link_button("Discord","El chat de la comunidad","http://twicht.tv/mouredev"),
      title("Comunidad"),
      link_button("Twich","Directos lunes a viernes","https://www.facebook.com"),
      link_button("Youtubeeeeeeeeeeeeeee","Tutoriales semanales","http://twicht.tv/mouredev"),
      link_button("Discord","El chat de la comunidad","http://twicht.tv/mouredev"),
      width="100%",
      gap=Size.DEFAULT.value
   )