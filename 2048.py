# 2048 game and graphics - pygame

from logic import *
import pygame
import sys

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

class Game2048:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('2048')
        self.font = pygame.font.Font(None, 55)
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.board = generate(self.board)
        self.board = generate(self.board)

    def draw_board(self):
        self.screen.fill(WHITE)
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                value = self.board[row][col]
                color = COLORS.get(value, GRAY) if value != 0 else GRAY
                pygame.draw.rect(self.screen, color, (col * 200, row * 200, 200, 200))
                if value != 0:
                    text = self.font.render(str(value), True, BLACK)
                    text_rect = text.get_rect(center=(col * 200 + 100, row * 200 + 100))
                    self.screen.blit(text, text_rect)
        pygame.display.update()

    def game_over(self):
        self.screen.fill(WHITE)
        text = self.font.render("Game Over", True, BLACK)
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)

        max_score = max(max(row) for row in self.board)
        score_text = self.font.render(f"Max Score: {max_score}", True, BLACK)
        score_text_rect = score_text.get_rect(center=(400, 400))
        self.screen.blit(score_text, score_text_rect)

        play_again_text = self.font.render("Press Enter to Play Again", True, BLACK)
        play_again_text_rect = play_again_text.get_rect(center=(400, 500))
        self.screen.blit(play_again_text, play_again_text_rect)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.__init__()
                        self.run()

    def action(self, function):
        self.board = function(self.board)
        self.board = generate(self.board)
        self.draw_board()

    def run(self):
        self.draw_board()
        while True:
            if not can_move(self.board):
                self.game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.action(up)
                    elif event.key == pygame.K_DOWN:
                        self.action(down)
                    elif event.key == pygame.K_LEFT:
                        self.action(left)
                    elif event.key == pygame.K_RIGHT:
                        self.action(right)

if __name__ == "__main__":
    game = Game2048()
    game.run()
