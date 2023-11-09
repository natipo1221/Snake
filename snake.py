import random
import pygame


speed = 0
colors = []
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)


def menu():
    global speed, screen
    pygame.display.set_caption("Snake")
    font = pygame.font.Font(None, 36)
    button_easy = pygame.Rect(200, 200, 300, 50)
    button_medium = pygame.Rect(200, 300, 300, 50)
    button_hard = pygame.Rect(200, 400, 300, 50)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint(event.pos):
                    speed = 70
                    done = True
                elif button_medium.collidepoint(event.pos):
                    speed = 50
                    done = True
                elif button_hard.collidepoint(event.pos):
                    speed = 30
                    done = True

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), button_easy)
        pygame.draw.rect(screen, (255, 255, 255), button_medium)
        pygame.draw.rect(screen, (255, 255, 255), button_hard)

        welcome_1 = font.render("Welcome to the snake game, Please choose a level", True, (255, 0, 0))
        text_easy = font.render("Easy", True, (0, 0, 0))
        text_medium = font.render("Medium", True, (0, 0, 0))
        text_hard = font.render("Hard", True, (0, 0, 0))
        screen.blit(welcome_1, (70, 70))
        screen.blit(text_easy, (250, 210))
        screen.blit(text_medium, (250, 310))
        screen.blit(text_hard, (250, 410))

        pygame.display.flip()


menu()


def menu2():
    global colors
    pygame.display.set_caption("Snake")
    font = pygame.font.Font(None, 36)
    welcome = pygame.Rect(200, 100, 300, 50)
    button_red = pygame.Rect(200, 200, 150, 50)
    button_blue = pygame.Rect(200, 300, 150, 50)
    button_colors = pygame.Rect(200, 400, 150, 50)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_red.collidepoint(event.pos):
                    colors = ["red"]
                    done = True
                elif button_blue.collidepoint(event.pos):
                    colors = ["blue"]
                    done = True
                elif button_colors.collidepoint(event.pos):
                    colors = ["green", "blue", "yellow", "pink"]
                    done = True

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (0, 0, 0), welcome)
        pygame.draw.rect(screen, (255, 255, 255), button_red)
        pygame.draw.rect(screen, (255, 255, 255), button_blue)
        pygame.draw.rect(screen, (255, 255, 255), button_colors)

        text_welcome = font.render("Choose a color for the snake", True, (255, 0, 0))
        text_easy = font.render("Red", True, (255, 0, 0))
        text_medium = font.render("Blue", True, (0, 0, 255))
        text_hard = font.render("Colors", True, (180, 120, 180))
        screen.blit(text_welcome, (200, 110))
        screen.blit(text_easy, (250, 210))
        screen.blit(text_medium, (250, 310))
        screen.blit(text_hard, (250, 410))

        pygame.display.flip()

menu2()


def end_game():
    pygame.mixer_music.load("no.wav")
    pygame.mixer_music.play(5, 0, 0)
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    font = pygame.font.SysFont(None, 50)

    button_width, button_height = 200, 50
    button_spacing = 20
    button_x = (screen_width - button_width) // 2
    button_y = (screen_height - (button_height + button_spacing) * 3) // 2
    play_button = pygame.Rect(button_x, button_y, button_width, button_height)
    game_text = font.render("You lost! Do you want to play again?", True, (255, 255, 255))
    text_game = pygame.Rect(button_x, button_y - button_height - button_spacing, button_width, button_height)
    text_game_1 = game_text.get_rect(center=text_game.center)
    play_text = font.render("Play", True, (255, 255, 255))
    play_text_rect = play_text.get_rect(center=play_button.center)
    quit_button = pygame.Rect(button_x, button_y + button_height + button_spacing, button_width, button_height)
    menu_button = pygame.Rect(button_x, button_y + button_height * 2 + button_spacing * 2, button_width, button_height)
    quit_text = font.render("Quit", True, (255, 255, 255))
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    menu_text = font.render("Menu", True, (255, 255, 255))
    menu_text_rect = menu_text.get_rect(center=menu_button.center)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    running = False
                elif menu_button.collidepoint(mouse_pos):
                    pygame.mixer_music.stop()
                    menu()
                elif quit_button.collidepoint(mouse_pos):
                    quit()

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (0, 0, 0), text_game)
        screen.blit(game_text, text_game_1)
        pygame.draw.rect(screen, (0, 255, 0), play_button)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)
        screen.blit(quit_text, quit_text_rect)
        pygame.draw.rect(screen, (0, 0, 255), menu_button)
        screen.blit(menu_text, menu_text_rect)

        pygame.display.update()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, length, size):
        global speed
        self.speed = speed
        self.score = 0
        self.length = length
        self.points = []
        self.size = size
        self.size2 = int(self.size)
        for i in range(length):
            self.points.append(Point(screen.get_width() // 2 + (i * self.size2), screen.get_height() // 2))
        self.direction = "left"

    def Move(self):
        i = len(self.points) - 1
        while i > 0:
            self.points[i] = Point(self.points[i - 1].x, self.points[i - 1].y)
            i -= 1
        if self.direction == "right":
            self.points[0].x += self.size
        elif self.direction == "left":
            self.points[0].x -= self.size
        elif self.direction == "down":
            self.points[0].y += self.size
        elif self.direction == "up":
            self.points[0].y -= self.size
        if self.points[0].x >= screen.get_width() and self.direction == "right":
            self.points[0].x = 0
        if self.points[0].x + self.size <= 0 and self.direction == "left":
            self.points[0].x = screen.get_width() - self.size
        if self.points[0].y >= screen.get_height() and self.direction == "down":
            self.points[0].y = 0
        if self.points[0].y + self.size <= 0 and self.direction == "up":
            self.points[0].y = screen.get_height() - self.size

    def draw_food(self, food_location):
        global food_location_3
        food_rect = pygame.Rect(food_location, (self.size2, self.size2))
        pygame.draw.rect(screen, "blue", food_rect)
        if self.score % 7 == 0 and self.score != 0:
            food_rect = pygame.Rect(food_location_3, (self.size2, self.size2))
            pygame.draw.rect(screen, "green", food_rect)
        # font = pygame.font.Font("NotoSansSymbols2-Regular.ttf", 64)
        # text2 = font.render(u'\U0001F34E', True, (255, 0, 0))
        # text_rect2 = text2.get_rect(center=food_location)
        # screen.blit(text2, text_rect2)

    def Draw(self):
        for i in range(len(self.points)):
            pygame.draw.rect(screen, colors[i % len(colors)], rect=(self.points[i].x, self.points[i].y, self.size2, self.size2))
        pygame.draw.rect(screen, "red", rect=(self.points[0].x, self.points[0].y, self.size2, self.size2))
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(f"Score: {self.score}", True, (255, 0, 0))
        text_rect = text.get_rect(center=(100, 30))
        screen.blit(text, text_rect)

    def big(self):
        global food_location_1, food_location_3
        if self.points[0].x + self.size2 > food_location_1[0] and self.points[0].x < food_location_1[0] + self.size2 and self.points[0].y + self.size2 > food_location_1[1] and self.points[0].y < food_location_1[1] + self.size2:
            self.points.append(Point(self.points[-1].x, self.points[-1].y))
            food_location_1 = (random.randint(1, screen.get_width() // 10) * 10 - my_snake.size2 * 2,
                               random.randint(1, screen.get_height() // 10) * 10 - my_snake.size2 * 2)
            self.score += 1
            print(food_location_1)

        if self.points[0].x + self.size2 > food_location_3[0] and self.points[0].x < food_location_3[0] + self.size2 and self.points[0].y + self.size2 > food_location_3[1] and self.points[0].y < food_location_3[1] + self.size2:
                for i in range(3):
                    self.points.append(Point(self.points[-1].x, self.points[-1].y))
                    self.score += 1
                food_location_3 = (random.randint(1, int(screen.get_width() // self.size)) * self.size - my_snake.size2 * 2,
                                   random.randint(1, int(screen.get_height() // self.size)) * self.size - my_snake.size2 * 2)


my_snake = Snake(5, 10)
my_snake.Draw()
pygame.display.flip()
food_location_3 = (random.randint(1, int(screen.get_width() // my_snake.size)) * my_snake.size - my_snake.size2 * 2, random.randint(1, int(screen.get_height() // my_snake.size)) * my_snake.size - my_snake.size2 * 2)
food_location_1 = (random.randint(1, int(screen.get_width() // my_snake.size)) * my_snake.size - my_snake.size2 * 2, random.randint(1, int(screen.get_height() // my_snake.size)) * my_snake.size - my_snake.size2 * 2)
print(food_location_1)
while True:
    screen.fill((0, 0, 0))
    my_snake.draw_food(food_location_1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if my_snake.direction != "left":
                    my_snake.direction = "right"
            elif event.key == pygame.K_LEFT:
                if my_snake.direction != "right":
                    my_snake.direction = "left"
            elif event.key == pygame.K_UP:
                if my_snake.direction != "down":
                    my_snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                if my_snake.direction != "up":
                    my_snake.direction = 'down'
    my_snake.big()
    my_snake.Draw()
    pygame.display.flip()
    my_snake.Move()
    pygame.time.delay(my_snake.speed)
    print(my_snake.points[0].x, my_snake.points[0].y)
    for i in range(1, len(my_snake.points)):
        if my_snake.points[0].x == my_snake.points[i].x and my_snake.points[0].y == my_snake.points[i].y:
            end_game()
            menu()
            menu2()
            screen.fill((0, 0, 0))
            my_snake = Snake(5, 10)
            my_snake.Draw()
            pygame.display.flip()
            food_location_1 = (random.randint(1, int(screen.get_width() // my_snake.size)) * my_snake.size - my_snake.size2 * 2,
                               random.randint(1, int(screen.get_height() // my_snake.size)) * my_snake.size - my_snake.size2 * 2)
            print(food_location_1)

            my_snake.draw_food(food_location_1)
            break




