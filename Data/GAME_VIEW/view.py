from abc import *


class View(metaclass=ABCMeta):
    @abstractmethod
    def set_size(self):
        pass

    def update(self, view, screen):
        screen.blit(view, (self.x_pos, self.y_pos))


def init_view(screen, list):
    for view in list:
        temp = view.set_size()
        view.update(temp, screen)
