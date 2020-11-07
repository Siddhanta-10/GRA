<h1 align="center">GRA</h1>
<h5>A program which performs specific actions based on recognized gestures.</h5>

> This repository is a submission to the [REVA HACK</>2020](https://revahack.com/) by team "awake ? code : sleep"
<br>

## :sparkles: Features
* Detect gestures: To detect hand gestures with acceptable accuracy
* Carryout function: Perform keystrokes when a gesture is detected

### Gestures:

<table>
<tr>
<td align="center"><img src="images/one.jpg" width="100px;" alt=""/><br /><sub><b>one</b></sub></a><br /></td>
<td align="center"><img src="images/swipe_up.jpg" width="100px;" alt=""/><br /><sub><b>swipe_up</b></sub></a><br /></td>
<td align="center"><img src="images/swipe_down.jpg" width="100px;" alt=""/><br /><sub><b>swipe_down</b></sub></a><br /></td>
<td align="center"><img src="images/pinch_in.jpg" width="100px;" alt=""/><br /><sub><b>pinch_in</b></sub></a><br /></td>
<td align="center"><img src="images/pinch_out.jpg" width="100px;" alt=""/><br /><sub><b>pinch_out</b></sub></a><br /></td>
<td align="center"><img src="images/two_fingers_left.jpg" width="100px;" alt=""/><br /><sub><b>two_fingers_left</b></sub></a><br /></td>
<td align="center"><img src="images/two_fingers_right.jpg" width="100px;" alt=""/><br /><sub><b>two_fingers_right</b></sub></a><br /></td>
</tr>
</table>

<br>

## :joystick: Usage

`pip install -r requirements.txt`

`python gra1.py`

### Gestures with their functions:
##### One : toggle gesture detection
##### Swipe up -> swipe down : show task view -> show applications
##### Swipe down -> swipe up : show desktop -> show applications
##### Pinch in/out: Zoom in/out
##### Two fingers swipe left/right : Move to virtual desktop left/right


## :nut_and_bolt: Behind the scenes
* Our application identifies the gestures through images through **image classification**
* This image classifier is obtained from training the **MobileNetv2 model**
* Around 1000 images have been trained for each of the 7 image classes
* When it detects a specific gesture from the webcam, it performs action assigned to that gesture
* The **Midas touch problem** (inability to turn off gestures) is solved by providing a gesture (one) to toggle the application
* The program also doesn't take too many inputs in a row
<br>

## :seedling: Applications
* This can help us use the computer in a much more __accessible__ way
* It is also very helpful to __differently abled__ people
* Future is going to be dominated by **mixed reality**, smart glasses, etc. Gestures are the main way to interact with such technologies
* Playing games becomes more **fun**
<br>

## :hammer: Tools Used
* [Python](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/api_docs) for Image-classification using ML.
* [OpenCV](https://docs.opencv.org/master/d9/df8/tutorial_root.html) for image manipulation.
* [Plyer](https://github.com/kivy/plyer) for notifications.
<br>

## :page_facing_up: License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<br>

## :man_technologist: Contributors

<table>
    <tr>
    <td align="center"><a href="https://github.com/Karthikeshwar1"><img src="https://avatars2.githubusercontent.com/u/43902130?s=400&u=f8f84eaf888d3a32eaa758db8ec036a7e9f3466d&v=4" width="100px;" alt=""/><br /><sub><b>Karthikeshwar</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/guruprasadv22"><img src="https://avatars0.githubusercontent.com/u/44210009?s=400&u=483e3d8b62f635befb6bdb258c8b4db3bfb06990&v=4" width="100px;" alt=""/><br /><sub><b>Guruprasad V</b></sub></a></td>
      <td align="center"><a href="https://github.com/Siddhanta-10"><img src="https://avatars0.githubusercontent.com/u/49256432?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Siddhanta Mandal</b></sub></a></td>
        <td align="center"><a href="https://github.com/vikasgn2"><img src="https://avatars3.githubusercontent.com/u/46003079?s=400&u=a122cc714e9090d4e1e24634c137116b84d672b9&v=4" width="100px;" alt=""/><br /><sub><b>Vikas G N</b></sub></a></td>
    </tr>
    </table>
