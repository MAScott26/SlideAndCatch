Slide And Catch Game Part One

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

Game Class crreation
  init
  set background
  create player variable
  create a list for multiple coins
  for loop add X number of coins to list
  sprites on screen are player, and the list of coins
  
  def main
  game = Game()
  game.start

  if__name__ == "__main__":
  main()

