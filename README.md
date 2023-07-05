# Calculator-App-Using-Python
## There are two distinct calculator implementations available: one designed specifically for Android using the Kivy package, and another for PC that utilizes a Graphical User Interface (GUI).

This repository includes two distinct implementations of a basic calculator written in Python. The first implementation, located in the "calculator_gui_pc.py" file, utilizes a straightforward Graphical User Interface (GUI) to generate the desired output. On the other hand, the second implementation employs the Kivy package for Android and is compiled using a subsystem for linux or linux terminal and the Buildozer tool. Buildozer is a tool designed to facilitate the packaging of mobile applications. The Android implementation of the calculator consists of the "calculator_for_android.py" and "mycalculator.kv" files, while the details and specifications for the app itself, such as its name and icon, can be found in the "buildozer.spec" file. To compile the code independently, the user needs to download a subsystem for linux, if he is on Windows (such as Ubuntu, or Debian) and follow the instructions provided in the documentation found at htps://buildozer.readthedocs.io/en/latest/installation.html. After the installation, the user simply needs to execute the following command: "buildozer -v android debug" and after some time, an ".apk" file will be generated in the "bin" folder. Alternatively, the user can download the already compiled ".apk" version located at "myCalculator.apk" file or copy the "calculator_for_android.py" and "mycalculator.kv" files into an Integrated Development Environment (IDE) of his choice and run the app from there. Keep in mind that the visual result provided by the IDE may be different than the actuall ".apk" file.
