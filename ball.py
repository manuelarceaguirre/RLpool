
import pygame
#Ball colors
YELLOW = (250, 215, 4)
BLUE   = (37, 83, 217)
RED    = (231, 0, 15)
PURPLE = (123, 0, 170)
ORANGE = (255, 131, 0)
GREEN  = (0, 147, 68)
BROWN  = (138, 28, 30)  
BLACK  = (0, 0, 0)
FONT = pygame.font.SysFont('Arial', 9, bold=True)  # Small, bold font
#colors 
DARK_GREEN = (1, 50, 32)
WHITE = (255,255,255,)
# Window stuff
WIDTH, HEIGHT = 800, 400
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
        if self.stripe == True:
            pygame.draw.circle(window, WHITE, (self.x, self.y), self.radius)
            band_height = int(self.radius * 0.99)
            pygame.draw.rect(window, self.color,
            (int(self.x - self.radius), int(self.y - band_height // 2), self.radius * 2, band_height))
        else:
            pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

            
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