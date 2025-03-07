import pygame
pygame.init()

# Window stuff
WIDTH, HEIGHT = 800, 400
FONT = pygame.font.SysFont('Arial', 9, bold=True)  # Small, bold font
from ball import *
# we initialize the game



WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AI learns 8 ball pool')


# create the cue ball IN MEMORY in the center
cue_ball = Ball(WIDTH // 1.5, HEIGHT //2, 10, WHITE, stripe = False, number = 0) # //2 to put it in the middle of the screen

# Solids
ball_1_solid_yellow = Ball(WIDTH // 3, HEIGHT //3, 10, YELLOW, stripe = False, number = 1) 
ball_2_solid_blue = Ball(WIDTH // 4, HEIGHT //3, 10, BLUE, stripe = False, number = 2) 
ball_3_solid_red = Ball(WIDTH // 5, HEIGHT //3, 10, RED, stripe = False, number = 3) 
ball_4_solid_purple = Ball(WIDTH // 3.5, HEIGHT //3, 10, PURPLE, stripe = False, number = 4) 
ball_5_solid_orange = Ball(WIDTH // 4.4, HEIGHT //3, 10, ORANGE, stripe = False, number = 5) 
ball_6_solid_green = Ball(WIDTH // 5.5, HEIGHT //3, 10, GREEN, stripe = False, number = 6) 
ball_7_solid_brown = Ball(WIDTH // 3.62, HEIGHT //3, 10, BROWN, stripe = False, number = 7) 
ball_8_solid_black = Ball(WIDTH // 2.1, HEIGHT //3, 10, BLACK, stripe = False, number = 8) 

# Stripes
ball_9_stripe_yellow = Ball(WIDTH // 1.5, HEIGHT //3, 10, YELLOW, stripe = True, number = 9) 
ball_10_stripe_blue = Ball(WIDTH // 8, HEIGHT //3, 10, BLUE, stripe = True, number = 10) 
ball_11_stripe_red = Ball(WIDTH // 9, HEIGHT //3, 10, RED, stripe = True, number = 11) 
ball_12_stripe_purple = Ball(WIDTH // 7, HEIGHT //3, 10, PURPLE, stripe = True, number = 12) 
ball_13_stripe_orange = Ball(WIDTH // 5.32, HEIGHT //3, 10, ORANGE, stripe = True, number = 13) 
ball_14_stripe_green = Ball(WIDTH // 6, HEIGHT //3, 10, GREEN, stripe = True, number = 14) 
ball_15_stripe_brown = Ball(WIDTH // 3.67, HEIGHT //3, 10, BROWN, stripe = True, number = 15) 

running = True
while running:
    
    # loops through events to know when an event is quitting stopping the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cue_ball.dx = 5
            cue_ball.dy = 3

            ball_1_solid_yellow.dx = 5
            ball_1_solid_yellow.dy = 3

            ball_2_solid_blue.dx = 5
            ball_2_solid_blue.dy = 3

            ball_3_solid_red.dx = 5
            ball_3_solid_red.dy = 3

            ball_4_solid_purple.dx = 5
            ball_4_solid_purple.dy = 3

            ball_5_solid_orange.dx = 5
            ball_5_solid_orange.dy = 3

            ball_6_solid_green.dx = 5
            ball_6_solid_green.dy = 3

            ball_7_solid_brown.dx = 5 
            ball_7_solid_brown.dy = 3

            ball_8_solid_black.dx = 5 
            ball_8_solid_black.dy = 3

    # Draw the table
    WINDOW.fill(DARK_GREEN)
    cue_ball.move()
    ball_1_solid_yellow.move()
    ball_2_solid_blue.move()
    ball_3_solid_red.move()
    ball_4_solid_purple.move()
    ball_5_solid_orange.move()
    ball_6_solid_green.move()
    ball_7_solid_brown.move()
    ball_8_solid_black.move()

    # Draw the cue ball
    cue_ball.draw(WINDOW)
    ball_1_solid_yellow.draw(WINDOW)
    ball_2_solid_blue.draw(WINDOW)
    ball_3_solid_red.draw(WINDOW)
    ball_4_solid_purple.draw(WINDOW)
    ball_5_solid_orange.draw(WINDOW)
    ball_6_solid_green.draw(WINDOW)
    ball_7_solid_brown.draw(WINDOW)
    ball_8_solid_black.draw(WINDOW)
    ball_9_stripe_yellow.draw(WINDOW)
    ball_10_stripe_blue.draw(WINDOW)
    ball_11_stripe_red.draw(WINDOW)
    ball_12_stripe_purple.draw(WINDOW)
    ball_13_stripe_orange.draw(WINDOW)
    ball_14_stripe_green.draw(WINDOW)
    ball_15_stripe_brown.draw(WINDOW)

    # Update the display
    pygame.display.flip() # this flips the internal buffer with the updated one


pygame.quit()

