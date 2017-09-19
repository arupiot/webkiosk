#!/usr/bin/env python

import pygtk
import gtk
import webkit
import sys
import os

class Browser:

    def __init__(self):
        #print(dir(webkit)
        #webkit.set_proxy("http://localhost:3128")
        gtk.Settings().set_property('gtk-touchscreen-mode', 1)
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.fullscreen()
        #self.window.set_default_size(600,400)
        #self.window.set_resizable(True)
        self.web_view = webkit.WebView()
        #print(dir(self.web_view))
        #self.web_view.open(str(sys.argv[1]))
        self.web_view.open(str("http://watson.ted.com"))
        
        #print(dir(self.web_view))
        
        scroll_window = gtk.ScrolledWindow(None, None)
        scroll_window.set_policy(gtk.POLICY_NEVER, gtk.POLICY_NEVER)
        scroll_window.set_placement(gtk.CORNER_TOP_LEFT)
        scroll_window.add(self.web_view)
        box = gtk.VBox(False, 0)
        box.add(scroll_window)
        #js_code = "window.getElementById(\"wrapper\").style.display = \"none\";"
        #self.web_view.execute_script(js_code)
        #js_code = "document.getElementById(\"extra-links\").style.display = \"none\";"
        #self.web_view.execute_script(js_code)
        #js_code = "console.log(\"test\")";
        """
        js_code = "window.addEventListener(\"readystatechange\", function() {\
  if (document.readyState === \"complete\") {\
      document.getElementById(\"top-bar\").style.display = \"none\";\
      document.getElementById(\"extra-links\").style.display = \"none\";\
      console.log(\"test\");\
    }\
  });"
        """
#        js_code = "window.onload = function() {\
#      document.getElementById(\"top-bar\").style.display = \"none\";\
#      document.getElementById(\"extra-links\").style.display = \"none\";\
#      console.log(\"test\");\
#  };"
#        self.web_view.execute_script(js_code)
        self.window.add(box)
        self.window.show_all()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    #print(dir(webkit.WebSettings))
    #sys.exit()
    browser = Browser()
    browser.main()
