# save_ozone_layer
A game to promote Environmental Preservation.

![Game](sample.gif?raw=true "Working Screenshot")



## Aim
- Appropriate demonstration for Object Oriented Programming (OOP) paradigm.
- Use of Pygame.
- Spreading environmental awareness through it's storyline.


## Prerequisites
1. Python 2.7
It's mostly installed by default on Linux.
2. Pygame
```
sudo pip install pygame
```


## Running the Game Locally
1. Clone the repository.
```
git clone https://github.com/mraduldubey/save_ozone_layer
```
2. Change to src directory.
```
cd src
```
3. In the terminal type:
```
python ozone_layer.py
```


## Storyline
The extraterrestial species of "Vogons" decided to forego their obscurity to decimate Earth in 1800s for the construction of a proposed intergalactic highway, only to discover that the Earth was inpenetrable for them because the Vogons explode near Ozone. Since then, they have been looking for a solution and humanity offered one, in the form of a Ozone Layer Hole above Antarctica. So, after 2 centuries, Vogons are back and they try to enter the planet through the hole. But, like Earths' favourite obsession of Action Movies, their happens to be a solo hero(named Douglas Adams) when they start the attack. This guy in the plane is the player. Now, you may want to try to save Earth figuratively, but, soon, **you'll realise there is no last stage for the game and the only thing you can do is delay the inevitable invasion. So, after you quit, you should realise the best way to save the planet is to save the environment.**


## Current Features
- The vogon fleet drops down from the top, moving down, right, left and down and so on.
- A "PLAY" button has to be clicked to start the game.
- The player is the Plane, which can shoot a max of 3 bullets/frame.
- The plane can move UP, DOWN, LEFT, RIGHT (Will remove DOWN functionality).
- Gravity acts on the Plane and pulls it down, if it tries to go up.
- Bullets bursts the Vogons. </li>
- If any Vogon is able to get to the bottom of window, you loose a Plane.
- If the Plane touches any Vogon, it's destroyed.</li>
- If you loose all your 3 Planes, "GAME OVER". And the "PLAY" button reappears.
- There are infinite number of levels. (See Storyline for why).
- The speed of vogon fleet increases each time you clear a level.
- The number of vogons in the fleet interestingly, still depend on your screen resolution.(I'll fix it.)
- The limit of Planes that you get is 3, shown as 2 idle Planes in the upper left corner.
- The score is calculated dynamically i.e. the score for shooting a vogon on Level2 is greater than on LEVEL1.
- Score is displayed on the right hand top corner.
- Level is displayed at top.
- The bullets and Vogons end programaticlly as well, when they cross the window.


## Possible Future Features
- Storyline displayed in the game.
- Explode aliens when shot.
- If they are nearby plane, blast it too.
- Bullets tend to get slower and fall back. (let gravity affect them too.)
- The aliens have more interesting trajectory --missiles-like.
- Encryption and file handling for highest scores. They restart at zero everytime game is run.  
- Show the Ozone Layer and clouds.


## Author

* **Mradul Dubey** - *save_ozone_layer* - [MradulDubey](https://github.com/mraduldubey)


## ArtWork Credit

* **Kenney Vleugels** - [Kenney](https://kenney.nl/assets/space-shooter-extension)


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENCE.md](LICENSE?raw=true "LICENCE") file for details.

#Join the team 
 Do you want to collaborate? Join the project at https://crowdforge.io/projects/232