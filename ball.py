from pico2d import load_image
import game_world

class Ball:
    image = None
    def __init__(self, x, y, velocity):
        if not Ball.image:
            Ball.image = load_image('ball21x21.png')
        self.x = x
        self.y = y
        self.velocity = velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x < 25 or self.x > 800-25:
            game_world.remove_object(self)
