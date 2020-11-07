<h1 align="center">GRA</h1>
<h5>A program which performs specific actions based on recognized gestures.</h5>

> This repository is a submission to the [REVA HACK 2020](https://revahack.netlify.app/) by team 
awake ? code : sleep
<br>

## :sparkles: Features
* Detect gestures: To detect hand gestures with acceptable accuracy.
* Carryout function: Perform keystrokes when a gesture is detected. For example: Show/Hide desktop (Win + D), switch between applications (Alt + Tab) and switch between virtual desktops (Ctrl + Win + ←/→)
* Provide a GUI to view/change what each gesture can do.
<br>

## :nut_and_bolt: Behind the scenes
* Our application identifies the gestures through images through image classification.
* This image classifier is obtained from a machine learning model, which is trained using a large-enough dataset.
* When it detects a specific gesture from the webcam, it performs action assigned to that gesture.
* We’ll also make sure it doesn’t take accidental gestures or take too many inputs in a row.
<br>

## :seedling: Applications
* This can help us use the computer in a much more __accessible__ way
* It is also very helpful to __differently abled__ people
* The way we use technology hasn't changed since a lot of years, so love it or hate it, gestures are the future!
<br>

## :hammer: Tools Used
* [Python](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/api_docs) for Image-classification using ML.
* [OpenCV](https://docs.opencv.org/master/d9/df8/tutorial_root.html) for image manipulation.
* Custom Created and a few open source datasets.
* [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) for building GUI.
  
  >Install by running `pip install PyQt5` on terminal.  
  >Qt for Python [documentation](https://doc.qt.io/qtforpython/).
<br>

## :page_facing_up: License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<br>

## :man_technologist: Contributors

<table>
    <tr>
    <td align="center"><a href="https://github.com/guruprasadv22"><img src="https://avatars0.githubusercontent.com/u/44210009?s=400&u=483e3d8b62f635befb6bdb258c8b4db3bfb06990&v=4" width="100px;" alt=""/><br /><sub><b>Guruprasad V</b></sub></a></td>
    <td align="center"><a href="https://github.com/Karthikeshwar1"><img src="https://avatars2.githubusercontent.com/u/43902130?s=400&u=f8f84eaf888d3a32eaa758db8ec036a7e9f3466d&v=4" width="100px;" alt=""/><br /><sub><b>Karthikeshwar</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/Siddhanta-10"><img src="https://avatars0.githubusercontent.com/u/49256432?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Siddhanta Mandal</b></sub></a></td>
        <td align="center"><a href="https://github.com/vikasgn2"><img src="https://avatars3.githubusercontent.com/u/46003079?s=400&u=a122cc714e9090d4e1e24634c137116b84d672b9&v=4" width="100px;" alt=""/><br /><sub><b>Vikas G N</b></sub></a></td>
    </tr>
    </table>
