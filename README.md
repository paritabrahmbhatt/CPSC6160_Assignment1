# CPSC6160 2D Game Design 

## Assignment 1 Game Design of Pong

## Contributors:
1. Parita Brahmbhatt
2. Rintu Noelmon

#### Version
OSVersion: 13.2.1

PythonVersion: 3.8.10

PygameVersion: 2.1.2
  

### Introduction
Pong is a two player arcade game which was first introduced in 1972. The game Pong's design requires only basic graphics and sound, which can make it a fun and challenging project to tackle. It is relatively simple compared to modern video games, and it serves as a great starting point to craete a game from scratch.


### Reasoning behind the structure
The design choices for a Pong game are typically driven by a desire to create a fun and engaging experience that is easy to learn but challenging to master. The game's simple mechanics and basic physics engine make it accessible to players of all skill levels, while the fast-paced gameplay and competitive elements keep players engaged.

The following daigram shows the relationship between various classes of our games. 

![Blank diagram](https://user-images.githubusercontent.com/124462732/222328375-7c19a23c-fd86-40f8-ac72-e7560135b9a7.png)

### Future Works
We included various functionalities to our game. This version of game provided different features such as music, welcome screen, score board, etc. However, many functionaltiies and features could be added to the game, which are as follows.
1. We can optimize the game engine by profiling the code, identifying and fixing performance bottlenecks, and using efficient algorithms and data structures.
2. As Artificial Intelligence has become popular in almost all fields, we can add the AI bot playing against the player. In such game engines.
3. We can also provide the difficulty levels, and according to the difficulty level, the speed of the ball should be decided. 

### Generalization

Our game consists of classes such as Screen, Draw, Welcome_Screen, and Button, which are resuable codes. One can also use the ball and paddle to create rectangular shaped objects which can move. The Draw class is inherited from Paddle and Ball classes. These codes can be used to develop any of one-vs-one games. We have also developed various functions to avoide the rewriting of the code. 

The images below shoes the welcome screen, game, and the winner respectively.

![image](https://user-images.githubusercontent.com/67082863/222316264-e98b09a4-c888-424f-ac34-6ea44864d6a8.png)


![image](https://user-images.githubusercontent.com/67082863/222316799-fa838ee1-83a3-4103-abe7-5e4240e99958.png)


![image](https://user-images.githubusercontent.com/67082863/222317907-b991ec93-48ec-4951-a799-7fcf1daa630d.png)



