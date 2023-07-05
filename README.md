# Calculator-App-Using-Python
## Two separate calculator implementations both for android using kivy package, and for pc via the help of a GUI.

This repository includes two distinct implementations of a basic calculator written in Python. The first implementation, located in the "calculator_gui_pc.py" file, utilizes a straightforward Graphical User Interface (GUI) to generate the desired output. On the other hand, the second implementation employs the Kivy package for Android and is compiled using a subsystem for linux or linux terminal and the Buildozer tool. Buildozer is a tool designed to facilitate the packaging of mobile applications. The Android implementation of the calculator consists of the "calculator_for_android.py" and "mycalculator.kv" files, while the details and specifications for the app itself, such as its name and icon, can be found in the "buildozer.spec" file. To compile the code independently, the user needs to download a subsystem for linux, if he is on Windows (such as Ubuntu, or Debian) and follow the instructions provided in the documentation found at htps://buildozer.readthedocs.io/en/latest/installation.html. After the installation, the user simply needs to execute the following command: "buildozer -v android debug" and after some time, an ".apk" file will be generated in the "bin" folder.
