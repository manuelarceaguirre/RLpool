import pygame
# we initialize the game
pygame.init()

# Window stuff
WIDTH, HEIGHT = 800, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AI learns 8 ball pool')

#colors 
GREEN = (0, 128, 0)
WHITE = (255,255,255,)
RED = (139,0,0)
BLACK = (0, 0, 0)  # For number text
FONT = pygame.font.SysFont('Arial', 9, bold=True)  # Small, bold font

# Ball class
class Ball:
    def __init__(self, x, y, radius, color, stripe = False, number = None ):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.stripe = stripe
        self.number = number
        self.dx = 0
        self.dy = 0
        

    def draw(self, window):
        pygame.draw.circle(window, WHITE, (self.x, self.y), self.radius)
        if self.stripe == True:
            band_height = int(self.radius * 0.99)
            pygame.draw.rect(window, self.color,
            (int(self.x - self.radius), int(self.y - band_height // 2), self.radius * 2, band_height))
            
            if self.number is not None:
                #Draw a circle
                number_circle_radius = int(self.radius * .4)
                pygame.draw.circle(window, WHITE, (int(self.x), int(self.y)), number_circle_radius)
                # Render the number as text
                text = FONT.render(str(self.number), True, BLACK)
                # Center the text on the ball
                text_rect = text.get_rect(center=(int(self.x), int(self.y)))
                window.blit(text, text_rect)

    
    def move(self):
        self.x += self.dx
        self.y += self.dy

        #simple bounce off walls
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx = -self.dx
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy = -self.dy

# create the cue ball IN MEMORY in the center
cue_ball = Ball(WIDTH // 1.5, HEIGHT //2, 10, WHITE, stripe = False, number = 0) # //2 to put it in the middle of the screen

# Solids
red_ball = Ball(WIDTH // 3, HEIGHT //3, 10, RED, stripe = True, number = 2) 

running = True
while running:
    
    # loops through events to know when an event is quitting stopping the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cue_ball.dx = 5
            cue_ball.dy = 3
            red_ball.dx = 5
            red_ball.dy = 2

    # Draw the table
    WINDOW.fill(GREEN)
    cue_ball.move()
    red_ball.move()

    # Draw the cue ball
    cue_ball.draw(WINDOW)
    red_ball.draw(WINDOW)

    # Update the display
    pygame.display.flip() # this flips the internal buffer with the updated one


pygame.quit()