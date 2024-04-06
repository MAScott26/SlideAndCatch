Slide And Catch Game Part One


All assets are created by me


Player Class creation
  init
  set image, size, original position, and movespeed.
    define Process
    if left is pressed
    flip image to face left
    walk left
    If right is pressed,
    flip image right,
    walk right
    
Coin Class creation
  init
  set image, 
  set size,
  reset

reset
  set to top of screen
  set to random space on X axis
  set falling speed to a random number

check boundary
  if coin reaches bottom of screen, reset to top

process
  if coin collides with player,
  reset
  
lblScore Class creation
init
  super init
  set position, original score, set label text

addscore
+1 when coin collected
update scoreboard
  
  
lblTimer Class creation
init
  superInit
  set placement, and original text.


startScreen Class creAtion
init
  superinit
  set background
  create instruction label, and location
  play button,
  Quit button

  previous score label creation
  placement, size, font&BG color, and text

  place all as sprites on start screen

  process if quit button or down is pressed, quit

  if play button is pressed, or up, play game.


Game Class crreation
  init
  set background
  create player variable
bring in BGM
play BGM when game starts
bring in Grab sound effect

  
  create a list for multiple coins
  for loop add X number of coins to list
  sprites on screen are player, and the list of coins

  process
  when coin is collected reset,
  add to scoore
  coin sound plays
Timer text is updated
if timer is 0 or less, previous score is saved,
game stops
print score
add sprites


  
def main
  keepGoing = true
  score = 0
  while keepgoing
  start menu loads
    if play, 
    play game
    else
    quit
    

  if__name__ == "__main__":
  main()

