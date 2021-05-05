from kivy.lang import Builder
from kivy import Config
import re
from requests import get
Config.set('graphics', 'multisamples', '0')
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.screen import Screen



class MyLayout(Screen):
    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width)/2
    
    def is_url(self, url):
        import re
        regex = ("((http|https)://)(www.)?" +
                "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                "{2,256}\\.[a-z]" +
                "{2,6}\\b([-a-zA-Z0-9@:%" +
                "._\\+~#?&//=]*)")
        
        p = re.compile(regex)

        if (url == None):
            return False
    
        if(re.search(p, url)):
            return True
        else:
            return False
    
    def connect(self, ip, url):
        import socket
        import webbrowser
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((ip, 1234))
        print(self.is_url(url))
        if self.is_url(url):
            socket.send(url.encode())


    def toggle_mode(self, theme=""):
        if theme == "Dark" or theme == "Light":
            MainApp().theme_cls.theme_style = theme
            return

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file("main.kv")
class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)
MainApp().run()