from __future__ import print_function

import flat


from collections import defaultdict

window = flat.Window(800, 600, "hi")


@window.event("on_draw")
def on_draw(window):
    global fps, last_time
    
    import flat._glfw
    
    flat.gl.glClearColor(0.5, 0.5, 0.5, 1.0)
    flat.gl.glClear(flat.gl.GL_COLOR_BUFFER_BIT)



flat.run()