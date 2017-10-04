import pygame
import numpy as np
import sys


class Board(object):
    # 棋盘类
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0

    def __init__(self, line_width=4, chess_width=5, size=482, background_color=WHITE):
        self.line_width = line_width
        self.chess_width = chess_width
        self.size = size
        self.background_color = background_color
        self.board = pygame.Surface((size, size))
        self.clear()
        self.circle = self.get_chess(typ='circle')
        self.cross = self.get_chess(typ='cross')

    def clear(self):
        self.board.fill(self.background_color)

    def draw_lines(self, line_color=BLACK):
        """
        绘制3x3棋盘
        :return: None
        """
        for x in range(0, self.size + 1, self.size // 3):  # 四条竖线
            pygame.draw.line(self.board, line_color, [x, 0], [x, self.size], self.line_width)
            pygame.draw.line(self.board, line_color, [0, x], [self.size, x], self.line_width)

    def get_chess(self, typ='circle', size=160, line_color=BLACK):
        """
        画圈
        :return: Surface
        """
        chess = pygame.Surface((size, size))
        chess.fill(self.background_color)
        for x in range(0, self.size + 1, self.size):  # 边框
            pygame.draw.line(chess, line_color, [x, 0], [x, self.size], self.line_width)
            pygame.draw.line(chess, line_color, [0, x], [self.size, x], self.line_width)
        if typ == 'circle':
            pygame.draw.circle(chess, line_color, [size // 2, size // 2], size // 2 - 20, self.chess_width)
        else:
            length = size / (2 * np.sin(np.pi / 4)) - 20
            cpx, cpy = size / 2, size / 2
            for alpha in np.arange(np.pi / 4, np.pi * 2, np.pi / 2):
                pygame.draw.aaline(chess, line_color, [cpx + length * np.cos(alpha), cpy + length * np.sin(alpha)], [cpx, cpy])
        return chess

    def get_board(self):
        return self.board


def main():
    pygame.init()
    size = 640, 480

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("井字棋 By Netcan")
    screen.fill((255, 255, 255))

    board = Board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        board.draw_lines()
        screen.blit(board.get_board(), (0, 0))
        # screen.blit(board.circle, (0, 0))
        screen.blit(board.cross, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
