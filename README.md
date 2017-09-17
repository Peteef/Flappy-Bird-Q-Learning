# Flappy-Bird-Q-Learning
Implementation of ML bot for Flappy Bird game, made by:

* Rafał Słaby
* Miłosz Świerad
* Kamil Turek

as a final project for Python in the Enterprise laboratory.

## About project
This is our first step into machine learning. The project is quite simple, but shows directly the basics of this topic.
We used modified version of Python Flappy Bird made by [chncyhn][1] and his bot as a example to implement ours.
Bots are using `.json` files to store Q-values and score. There are some useful scripts in several branches such, as logger or plotting scripts. The branch [modifications][2] contains some tries with various modified parameters with result plots.
The original version of game [here][3].

[1]: https://github.com/chncyhn/flappybird-qlearning-bot
[2]: https://github.com/Peteef/Flappy-Bird-Q-Learning/tree/modifications
[3]: https://github.com/sourabhv/FlapPyBird

## How to start
  1. Clone repository `git clone https://github.com/Peteef/Flappy-Bird-Q-Learning.git` or click `Download ZIP` in right panel and extract it.
  2. Make sure you are using 3.6 version of Python.
  3. If you want to be sure that bot "knows nothing" run `initialize_qvalues.py`. Bot saving data into `.json` file so it remebers everything it learned even when you close the game.
  4. Run `flappy.py`
  5. Enjoy about 1000 fails before it starts make some sensible progress

## Some data
![alt-text](https://user-images.githubusercontent.com/26136274/30525076-c303a08c-9bff-11e7-85fb-3a251f6023ae.png "Comparision")
Here is the result of our best modifications (on the right) compared to bot by  **_chncyhn_** (on the left).
As you can see, we achieved much better score with 2000 less iterations.
After 3000 iterations single round cae take much time so bot starts to learn slower.

## At the end
ML is much more interesting that it looks like. In our opinion this is the future of programming and IT at all.
As we observed, computers start revealing abilities to learn and do stuff much efficiently than we do.
This simple game is just a demo of its potential.

*AGH, Faculty of Physics and Computer Science
2017*
