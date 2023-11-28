import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gst", "1.0")

from gi.repository import Gtk, Gst, Gdk

class VentanaConfig(Gtk.Window):
    def __init__(self, form_instance):
        Gtk.Window.__init__(self, title="Configuración")
        self.set_default_size(200, 100)
        self.set_border_width(10) 

        

        self.form_instance = form_instance
        current_music_state = self.form_instance.music_state
        current_report_state = self.form_instance.report_state

        print(self.form_instance.music_state)
        self.set_position(Gtk.WindowPosition.CENTER)


        vb = Gtk.VBox(spacing=3)
        hbox1 = Gtk.Box(spacing=3)
        hbox2 = Gtk.Box(spacing=3)
        vb.pack_start(hbox1, True, True, 2)
        vb.pack_start(hbox2, True, True, 2)
        vb_in = Gtk.VBox(spacing=2)
        vb_in2 = Gtk.VBox(spacing=2)
        hbox2.pack_start(vb_in, True, True, 0)
        hbox2.pack_start(vb_in2, True, True, 0)

        lbl_1 = Gtk.Label()
        lbl_1.set_text("Efectos de sonido")
        lbl_2 = Gtk.Label()
        lbl_2.set_text("Reporte de estadísticas")

        sound_switch = Gtk.Switch()
        sound_switch.connect("notify::active", self.sound_switch_activate)
        if current_music_state == True:
            sound_switch.set_active(True)
        else:
            sound_switch.set_active(False)
        
        report_switch = Gtk.Switch()
        report_switch.connect("notify::active", self.report_switch_activate)
        if current_report_state == True:
            report_switch.set_active(True)
        else:
            report_switch.set_active(False)

        boton_nueva_ventana = Gtk.Button(label="Volver")
        boton_nueva_ventana.connect("clicked", self.on_cerrar_clicked)
        boton_nueva_ventana.set_name("btn-menu")
        boton_nueva_ventana.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)

        hbox1.pack_start(boton_nueva_ventana, True, True, 0)

        vb_in.pack_start(lbl_1, True, True, 0)
        vb_in.pack_start(sound_switch, True, True, 0)
        vb_in2.pack_start(lbl_2, True, True, 0)
        vb_in2.pack_start(report_switch, True, True, 0)

        self.add(vb)

    def on_cerrar_clicked(self, widget):
        self.destroy()
        self.form_instance.show_menu()

    def sound_switch_activate(self, sound_switch, gparam):
        if sound_switch.get_active():
            print(sound_switch.get_active())
            print(self.form_instance.music_state)
            state = "on"
            self.form_instance.player.set_state(Gst.State.PLAYING)
            self.form_instance.music_state = sound_switch.get_active()
            print(sound_switch.get_active())
            print(self.form_instance.music_state)
            
        else:
            print(sound_switch.get_active())
            print(self.form_instance.music_state)
            state= "off"
            self.form_instance.player.set_state(Gst.State.NULL)
            self.form_instance.music_state = sound_switch.get_active()
            print("Switch was set", state)
            print(sound_switch.get_active())
            print(self.form_instance.music_state)

    def report_switch_activate(self, report_switch, gparam):
        if report_switch.get_active():
            state = "on"
            self.form_instance.report_state = report_switch.get_active()
            
        else:
            state= "off"
            self.form_instance.report_state = report_switch.get_active()
        print("Switch was set", state)

# Resto del código...
