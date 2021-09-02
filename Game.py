import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, QUIT
from pygame.locals import *
import time
import snake as sk
import Snake_food as sf

screen_x, screen_y = 1300, 600
SIZE = 40


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")

        pygame.mixer.init()
        self.play_background_music()
        self.lnth = 0
        self.surface = pygame.display.set_mode((screen_x, screen_y))
        self.snake = sk.Snake(self.surface, 2)
        self.snake.draw()
        self.apple = sf.Apple(self.surface)
        self.apple.draw()

    def play_background_music(self):
        pygame.mixer.music.load('Python39/Snake Game/resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound(
                "Python39/Snake Game/resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound(
                "Python39/Snake Game/resources/ding.mp3")

        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load("Python39/Snake Game/resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def score(self):
        score_font = pygame.font.SysFont('arial', 30)
        score_render = score_font.render(
            f"Score:{self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score_render, (1150, 20))

    def reset(self):
        self.snake = sk.Snake(self.surface, 2)
        self.apple = sf.Apple(self.surface)

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(
            f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (400, 225))
        line2 = font.render(
            "To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (400, 300))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.score()
        pygame.display.flip()
        for i in range(self.snake.length):
            if self.isCollision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.play_sound('ding')
                self.snake.increaseLength()
                self.apple.move()

        for i in range(2, self.snake.length):
            if self.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Collision Occurred"

        if not (0 <= self.snake.x[0] <= screen_x and 0 <= self.snake.y[0] <= screen_y):
            self.play_sound('crash')
            raise "Hit the boundry error"

    def timeIncrease(self):
        time.sleep(0.01)

    def isCollision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2:
            if y1 >= y2 and y1 <= y2:
                return True
        return False

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif(event.type == QUIT):
                    running = False
            try:
                if not pause:
                    self.play()
            except:
                self.show_game_over()
                pause = True
                self.reset()

            self.timeIncrease()


if __name__ == "__main__":
    game = Game()
    game.run()
