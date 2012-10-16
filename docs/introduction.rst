Introduction
============

This is a short introduction to pyflat.

What is pyflat?
---------------
pyflat is a library for the creation of 2D interactive applications such as games and animations. It aims to abstract away platform specific details, such as window opening and sound playback, and provide a single consistent interface to those features. On top of that it makes your life easier by including functions that can be found in nearly every 2D application, such as image loading, drawing primitives and font rendering.

What is pyflat not?
-------------------
pyflat strictly focuses on 2D application-level input/output, providing a minimal framework to build upon.

This means pyflat is not:

 - a complete OS abstraction containing every feature possibly related to "applications", such as the clipboard, opening/closing CD drives, opening child processes, etc.
 - a game engine
 - a full-flexed rendering library