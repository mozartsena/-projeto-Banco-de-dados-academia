import gtk, gtk.glade
dic = { "gtk_main_quit" : gtk.main_quit }
gladefile=gtk.glade.XML("frm_cliente.glade")
gladefile.signal_autoconnect(dic)
gtk.main()