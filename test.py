from __future__ import print_function

import flat

window = flat.Window(800, 600, "hi")

window.event.on_focus = print
def on_key_press(self, key):
    if key == flat.key.ESCAPE:
        self.close()
    
window.event.on_key_press = on_key_press

flat.run()