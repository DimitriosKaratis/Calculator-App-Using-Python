# Calculator-App-Using-Python
## Two separate calculator implementations both for android using kivy package, and for pc via the help of a GUI.

This repository contains two different implementations of a basic calculator in python. The first one, located at "calculator_gui_pc.py" file, uses a simple Graphical User Interface (GUI) to produce the desired result, while the second one is implemented using kivy package for android and is compiled via the help of a Linux terminal and the Buildozer tool, which is a tool that aims to package mobile applications easily. The files responsible for the android implementation of the calculator are "calculator_for_android.py" as well as "mycalculator.kv", while the specifications of the android app (it's name, icon, etc.) are located in "buildozer.spec" file. In order for the user to compile the code by himself he should first download a linux terminal (for excample Ubuntu) and then download and run the buildozer tool as shown in the documentation here: htps://buildozer.readthedocs.io/en/latest/installation.html
Because the buildozer.spec file is already created the user, after the installation, should only execute the following command: 
buildozer -v android debug. After some time an ".apk" file will be created in the folder named "bin". 

