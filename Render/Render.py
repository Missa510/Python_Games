import pygame as pg

class SoftwareRenderer:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1260, 685
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRenderer()
    app.run()