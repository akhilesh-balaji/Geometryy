# Geometryy
<!-- ## A tool to accurately describe transformations on the Cartesian plane, given the image and pre-image coordinates. -->

![](./Screenshot.svg)

The Cartesian Plane was popularized by René Descartes. In fact, the plane itself in named after him. It is defined by two perpendicular number-lines, called axes. In the Cartesian plane, a slice of Cartesian space, these two number lines are called <img src="https://render.githubusercontent.com/render/math?math=x"> and <img src="https://render.githubusercontent.com/render/math?math=y"> axes. Any point in the Cartesian plane can be uniquely described by two numbers—one that describes the point's vertical position, the <img src="https://render.githubusercontent.com/render/math?math=y"> coordinate, and one that describes the point's horizontal position, the <img src="https://render.githubusercontent.com/render/math?math=x"> coordinate. Thus, any point in the plane can be described by the set of numbers <img src="https://render.githubusercontent.com/render/math?math=(x,y)">. Together, these two numbers that describe the object's position in the plane are called the object's coordinates.

An object may be transformed in the cartesian plane. Some common transformations include:
- Translation
- Reflection
- Dilation
- Rotation
- Stretches

There are set formulas for computing each of these transformations, and they can easily be done by computer programs such as GeoGebra or Desmos. However, it is quite a bit harder to describe a transformation given the object (pre-image) coordinates <img src="https://render.githubusercontent.com/render/math?math=A(x,y)"> and the image coordinates <img src="https://render.githubusercontent.com/render/math?math=A'(x,y)">. This can be done manually, but it's a tedious process. Further, geometry tools such as GeoGebra do not have a feature to describe these transformations given <img src="https://render.githubusercontent.com/render/math?math=A"> and <img src="https://render.githubusercontent.com/render/math?math=A'">.

This is why I developed Geometryy. Simply choose the transformation you feel is most likely to have occurred, feed it the image and object coordinates, and it describes the transformation assuming that <img src="https://render.githubusercontent.com/render/math?math=A"> has been transformed to get <img src="https://render.githubusercontent.com/render/math?math=A'">. Some transformations might require the image and object of two points, as this requires simultaneously solving the equations of two lines to get a significant coordinate.

As of now, Geometryy is slightly buggy, due to there being multiple ways of describing a transformation in different scenarios (more on this later).

## Using Geometryy
Download the source-code from the releases page, extract the `.zip` to another folder. `cd` to the directory in your terminal and run `python flow.py`. There might be a few dependencies you need to install: `rich` for a colourful output and `numpy`. Install them with the following commands:
```
$ pip install rich
$ pip install numpy
```
Then run
```
$ python flow.py
```
Preferably, use a terminal that supports rich output such as the VSC integrated terminal or Windows Terminal.

Then, you will be presented with the screen shown in the screenshot at the top of the page. If you are using a terminal with rich output, the options will appear in different colours and option `[D] Stretches` will appear dimmer than the rest, as I have not completed work on it yet. The rest of the options will work, however.

Simply enter the letter next to the transformation, and press <kbd>Enter</kbd>. Now, enter the first object coordinate <img src="https://render.githubusercontent.com/render/math?math=A"> and the first image coordinate <img src="https://render.githubusercontent.com/render/math?math=A'">. If it asks for <img src="https://render.githubusercontent.com/render/math?math=B"> and <img src="https://render.githubusercontent.com/render/math?math=B'">, supply it with the second object and image coordinates. It doesn't matter if a shape, such as a triangle has been transformed—simply pick a few of the points, and enter them. If all goes well, it should describe the transformation.

If all *doesn't* go well, you have either encountered a bug, or you have provided a set of coordinates which have not gone through the same transformation, or the object coordinate, when that transformation is applied to it, cannot possibly map on to the image.

## How it works
### Translation
<img src="https://render.githubusercontent.com/render/math?math=A"> is translated by a column vector <img src="https://render.githubusercontent.com/render/math?math=\begin{pmatrix} a\\b\end{pmatrix}">, where <img src="https://render.githubusercontent.com/render/math?math=a"> describes lateral movement and <img src="https://render.githubusercontent.com/render/math?math=b"> represents the vertical movement of the point. Thus, to find the column vector that describes the translation of <img src="https://render.githubusercontent.com/render/math?math=A"> to map it on to <img src="https://render.githubusercontent.com/render/math?math=A'">, one simply subtracts <img src="https://render.githubusercontent.com/render/math?math=A"> from <img src="https://render.githubusercontent.com/render/math?math=A'"> (subtracting <img src="https://render.githubusercontent.com/render/math?math=x_1"> from <img src="https://render.githubusercontent.com/render/math?math=x_2">, and <img src="https://render.githubusercontent.com/render/math?math=y_1"> from <img src="https://render.githubusercontent.com/render/math?math=y_2">, where coordinates with subscript <img src="https://render.githubusercontent.com/render/math?math=1"> belong to <img src="https://render.githubusercontent.com/render/math?math=A"> and coordinates with subscript <img src="https://render.githubusercontent.com/render/math?math=2"> belong to <img src="https://render.githubusercontent.com/render/math?math=A'">).

### Reflection
When an object is reflected about a mirror line <img src="https://render.githubusercontent.com/render/math?math=f(x)">, its image will be the same distance from the mirror line as the object. Thus, the mirror line will be the perpendicular bisector of the line that connects <img src="https://render.githubusercontent.com/render/math?math=A"> and <img src="https://render.githubusercontent.com/render/math?math=A'">.

### Rotation
The point of rotation <img src="https://render.githubusercontent.com/render/math?math=P"> can be found by finding the point of intersection of the perpendicular bisectors of <img src="https://render.githubusercontent.com/render/math?math=\overline{AA'}"> and <img src="https://render.githubusercontent.com/render/math?math=\overline{BB'}">. The point of intersection can be found by simultaneously solving the equations of both bisectors. However, this method does not work is the perpendicular bisectors have the same equation. Then, the angle of rotation <img src="https://render.githubusercontent.com/render/math?math=\theta"> can be found by computing the angle between <img src="https://render.githubusercontent.com/render/math?math=\overline{AP}"> and <img src="https://render.githubusercontent.com/render/math?math=\overline{A'P}">. This angle, in radians, is simply

<div style="text-align:center">
<img src="https://render.githubusercontent.com/render/math?math=\tan^{-1}\left(\frac{m_1 - m_2}{1+m_1 m_2}\right)" width=120px></div>

where <img src="https://render.githubusercontent.com/render/math?math=m_1"> and <img src="https://render.githubusercontent.com/render/math?math=m_2"> are the slopes of <img src="https://render.githubusercontent.com/render/math?math=\overline{AP}"> and <img src="https://render.githubusercontent.com/render/math?math=\overline{A'P}">. The value in radians can easily be converted to degrees.

### Dilation
The scale factor of the dilation can be found by dividing the length of one side of the image shape by the length of one side of the object shape.

<div style="text-align:center">
<img src="https://render.githubusercontent.com/render/math?math=k = \frac{A'B'}{AB}" width=88px></div>

The centre of rotation is simply the point of intersection of the equations of <img src="https://render.githubusercontent.com/render/math?math=AA'"> and <img src="https://render.githubusercontent.com/render/math?math=BB'">, which can be achieved by simultaneously solving their equations.
