raspi-splash-2.0
================

splash animation for pidora

Raspberry Pi Splash Screen

This program runs as a service during the boot sequence of the Raspberry PI. It displays a graphic written in OpenGL ES 2.0. It requires:

-A graphic containging the raspberry pi logo called , "pidora-logo-cmyk.tga" , to be residing in the bin.
-This graphic should scroll to the right and rotate about the x-axis.

Also included in this package is the source for utilites needed by the application to be compiled with. These are located in the "common"  folder.

Also included is a file demonstrating a second approach which is a rotating box with textures mapped to its surface. This example is important because it illustrates an optimazation using vertual buffer objects.
