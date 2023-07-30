## Battleships
Battleships is a Python terminal game.
users can try and beat the computer by finding all the battleships on the computers board 
before the computer finds the players battleships.

Live website[here](https://m3battleships-500bfc128fe5.herokuapp.com/)

![Am I responsive image](/images/battleshipsresposive.png)

# How to play
* player board and computer board are generated randomly
* Player can see where theyere ships are. witch are indicated with @ sign
* The computer ships are hidden 
* Guesses are shown with X sign and hits are show with a * sign
* Player and computer take turn and guess ship locations 
* The winner is the one that sinks all ships 

Info about playing battleships can be found in wiki (https://en.wikipedia.org/wiki/Battleship_(game))

# Features
* Random board generation 
* User inputs validation
* Scores 
* win condition 

# Testing
Manualy tested by
* Using PEP8 making sure no issues with code
* Inputing incorect cordinates 
* Inputing strings when numbers are expected 

# Deployemnt
project deployed on heroku
* Create new app
* navigate to settings 
* set up Config Vars
* add buildpacks Python and NodeJs in order
* navigate to deploy scroll down to Deployment method
* connect to github and connect project 
* scroll down and click Deploy

# Credits
* Code institue for game idea and start of point 
* stack overflow for code ideas and solving code issues