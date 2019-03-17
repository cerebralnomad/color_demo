# color_demo
GUI to browse the 558 colors available to tkinter on Ubuntu

There's a ton of colors available to tkinter and I wanted an easy way to preview them.  
Note that this works on Ubuntu flavors. I do not know if it will work properly on other 
distros or operating systems.

The list of colors is from the rgb.txt file located at /etc/X11 on Ubuntu.

## Installation

Download both .py files to their own directory or clone the repo.
Make color_demo.py executable and run it

## Usage

When first opened, this screen is displayed:

![Screenshot](/screenshots/color_demo1.png?raw=true "Screenshot")

Click the combo box at the bottom and choose the color you wish to see.
Click the button 'Change Color' and the main field above will change
to the color you selected.

![Screenshot](/screenshots/color_demo2.png?raw=true "Screenshot")

Choose another color or click 'Exit' to quit the program.

The color names you decide on are used in the "background = <color>" parameters in tkinter.
  



