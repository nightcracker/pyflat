Introduction
============

What is pyflat?
---------------
pyflat is a library for the creation of 2D interactive applications such as games and animations. It aims to abstract away platform specific details, such as window opening and sound playback, and provide a single consistent interface to those features. On top of that it tries makes your life easier by including functions that can be found in nearly every 2D application, such as image loading, drawing primitives and font rendering. pyflat runs on Windows, Linux and Mac.

pyflat is tightly coupled to OpenGL. It's impossible to capture all 2D rendering techniques in a library while keeping an abstraction from the underlying layer, so pyflat doesn't attempt that. Therefore pyflat contains most basic rendering methods (more than enough for most games and applications), and even some advanced ones (particles), but the more advanced stuff has to be done in OpenGL.

What is pyflat not?
-------------------
pyflat strictly focuses on 2D application-level input/output, providing a minimal framework to build upon. This means pyflat is not a complete OS abstraction containing every feature possibly related to "applications", such as the clipboard, opening/closing CD drives, opening child processes, etc, is not a game engine nor a full-flexed rendering library. These features aren't included in pyflat because they aren't useful, they aren't because they're out of scope.

Features
--------
Everything you need to start writing 2D applications should be included in pyflat.

The first and foremost feature in pyflat is opening OpenGL windows and handling input from those windows. Fullscreen windows, window icons, movable, resizable windows, it's all included. A lot of effort has gone into making the most responsive input system as possible. In order to achieve this pyflat uses a strict callback system - pyflat input handling calls you, not the other way around.

pyflat has a neat system for loading and managing your resources. It contains decoders for common image sound and font formats such as PNG, BMP, WAV, OGG, TrueType and OpenType, and plugging your own decoders/encoders is a breeze.

For most things in pyflat you don't even have to resort to OpenGL, drawing primitives such as squares, circles and lines can be done with a simple command. Rotated, scaled, translated and colored sprites with various blending modes are included, of course. Some advanced techniques such as particle systems are included as well.


Technologies used
-----------------
pyflat uses OpenGL for all rendering. GLFW3 is used for opening cross-platform OpenGL windows. 