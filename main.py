import pygame
import numpy as np
import sys


class Board(object):
    # 棋盘类
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0

    def __init__(self, line_width=4, chess_width=5, board_size=482, background_color=WHITE):
        self.line_width = line_width
        self.chess_width = chess_width
        self.board_size = board_size
        self.chess_size = board_size // 3
        self.background_color = background_color
        self.board = pygame.Surface((board_size, board_size))
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
        for x in range(0, self.board_size + 1, self.board_size // 3):  # 四条竖线
            pygame.draw.line(self.board, line_color, [x, 0], [x, self.board_size], self.line_width)
            pygame.draw.line(self.board, line_color, [0, x], [self.board_size, x], self.line_width)

    def get_chess(self, typ='circle', line_color=BLACK):
        """
        画圈
        :return: Surface
        """
        chess = pygame.Surface((self.chess_size, self.chess_size))
        chess.fill(self.background_color)
        for x in range(0, self.board_size + 1, self.board_size):  # 边框
            pygame.draw.line(chess, line_color, [x, 0], [x, self.board_size], self.line_width)
            pygame.draw.line(chess, line_color, [0, x], [self.board_size, x], self.line_width)
        if typ == 'circle':
            pygame.draw.circle(chess, line_color, [self.chess_size // 2, self.chess_size // 2],
                               self.chess_size // 2 - 20, self.chess_width)
        else:
            length = self.chess_size / (2 * np.sin(np.pi / 4)) - 20
            cpx, cpy = self.chess_size / 2, self.chess_size / 2
            for alpha in np.arange(np.pi / 4, np.pi * 2, np.pi / 2):
                pygame.draw.line(chess, line_color, [cpx + length * np.cos(alpha), cpy + length * np.sin(alpha)],
                                 [cpx, cpy], self.chess_width)
        return chess

    def get_board(self, input_stat=np.array([])):
        """
        :param input_stat: 输入的状态，np二维矩阵，0表示圈，1表示叉
        :return:
        """
        self.clear()
        self.draw_lines()
        for y in range(3):
            for x in range(3):
                if input_stat[y][x] is not None:
                    self.board.blit(self.cross if input_stat[y][x] else self.circle,
                                    (x * self.chess_size, y * self.chess_size))

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
        stat = np.array([
            [False, None, False],
            [True, False, True],
            [False, True, False],
        ])
        screen.blit(board.get_board(stat), (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
