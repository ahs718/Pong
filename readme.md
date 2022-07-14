# Pong Game made with Python

## Example
![Example](demo/demo.gif)

## Features

-   This project is a Pong game created with Python.

-   Uses the turtle library to help create the window display for the game.
-   Includes sound effects are included whenever the ball bounces off of the border or the paddles. (Works only on macOS at the moment!)
-   Includes a score system that increases whenver the ball gets past the opposing player.

## Controls

-   <kbd>w</kbd> (W key) - left paddle up
-   <kbd>s</kbd> (S key) - left paddle down
-   <kbd>&uarr;</kbd> (Up arrow key) - right paddle up
-   <kbd>&darr;</kbd> (Down arrow key) - right paddle down

## How to Play

In order to play the game, you can clone the repository and run the `Game.py` file. The commands to do so on a macOS / linux terminal are shown below:

```bash
git clone https://github.com/ahs718/Pong.git
cd Pong-Game
python3 Game.py
```

## My experience making this project

Pong is a classic game that is recreated by many programmers as a part of their beginner projects. I also decided to undergo the challenge of making this game, but decided to add some differences now that I have experience with object-oriented programming.

By separating the components of the Pong game into modules, It makes it a lot easier to add additional features to the game. For example, by making the ball into a class with options to set its direction and speed, it is very easy to create multiple balls by just instantiating another instance of the ball class.

This project allowed me to apply the object oriented concepts that I learned into an actual project, and can serve as a guidline for structures for future projects.
