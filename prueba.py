import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio

class MyApplication(Gtk.Application):

    def __init__(self, application_id, flags):
        super().__init__(application_id=application_id, flags=flags)

    def activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Test Application")
        window.set_default_size(400, 300)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_border_width(10)
        window.get_style_context().add_class("mi_ventana")

        grid = Gtk.Grid()

        boton1 = Gtk.Button(label="Boton 1")
        boton1.set_margin_top(10)
        boton1.get_style_context().add_class("boton1")

        boton2 = Gtk.Button(label="Boton 2")
        boton2.set_margin_top(10)
        boton2.get_style_context().add_class("boton2")

        etiqueta = Gtk.Label(label="Soy una etiqueta con diseño")
        etiqueta.set_margin_top(10)
        etiqueta.get_style_context().add_class("etiqueta")

        css = """
            .mi_ventana {				
                background: linear-gradient(to right, rgba(180,255,0,0.5), rgba(180,255,0,1));
            }		
            .boton1 {
                background-color: white;
                color: black;
                font-size: 14px;
                border: 2px solid #4CAF50;
                border-radius: 50%;
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
            }
            .boton2 {
                background: red;
                color: #FFFF00;
                padding: 32px 16px;
                font-size: 14px;
                border-radius: 12px;
                box-shadow: 0 9px #999;
            }
            .etiqueta {
                color: #0101DF;
                font-size: 24px;
                padding: 10px;
                font-weight: bold;
                font-family: "Times New Roman", Times, serif;
                text-shadow: 3px 2px red;
            }
        """

        provider = Gtk.CssProvider()

        try:
            provider.load_from_data(css.encode())
        except GLib.Error as e:
            print(f"Hoja de estilo no cargada: {e.message}")

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER
        )

        grid.attach(boton1, 0, 0, 2, 1)
        grid.attach_next_to(boton2, boton1, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(etiqueta, 0, 3, 4, 1)

        window.add(grid)
        window.show_all()

app = MyApplication("test.application", Gio.ApplicationFlags.FLAGS_NONE)
app.run([])
