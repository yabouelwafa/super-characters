Character Data Analysis Project

04/05/2024

Wing 101 (ver. 9)

Yusuf Abouelwafa

Description:


The purpose of the “Character Data Analysis Project” is to organise certain data for characters of a video game. This is done through written and visual methods. The written methods include sorting algorithms and data loading while the visual ones include a histogram and a curve fit.


Dependencies:


* Python 11.8 or higher
* Matplotlib.pyplot
* Numpy
* Wing 101


Installation:


After the installation of the zip file a few steps must be completed to start the program. Firstly, the program must be opened on the Wing101 IDE version 9 to ensure proper functionality.


Use package manager [pip] to install:

* python -m pip install matplotlib
* python -m pip install numpy
* python -m pip install scipy


The python version must be newer than 3.10


Usage:


The user will be prompted with options for different data analysis techniques and must choose one of the options provided. If “e” or “E” is inputted, the program will end while an invalid input would cause an error message. Below is an example.


The available commands are:

L)oad Data

S)ort Data

C)urve Fit

H)istogram

E)xit

Please type your command: s


Please enter the attribute you want to use for sorting:

'Agility', 'Armor', 'Intelligence', 'Health'

: <the user enters response>

Ascending (A) or Descending (D) order: < the user enters

response>

Data Sorted. Do you want to display the data?:

<user enters Y or N. Assume the user enters Y>

<<<<Data is displayed>>

<The UI in figure 1 is displayed again>


Credits:


Load\_data:

character\_occupation\_list: Ian Manning

character\_occupation\_list: Waleed Gabr

character\_luck\_list: Yusuf Abouelwafa

character\_occupation\_list: Charlie Ballantyne


Sort:

sort\_characters\_agility\_bubble: Ian Manning

sort\_characters\_intelligence\_selection: Waleed Gabr

sort\_characters\_health\_insertion: Yusuf Abouelwafa

sort\_characters\_armor\_bubble: Charlie Ballantyne


curve\_fit: Ian Manning

text UI: Yusuf Abouelwafa

histogram: Waleed Gabr

batch UI: Charlie Ballantyne


License: Apache License 2.0

\> Written with [StackEdit](https://stackedit.io/).
