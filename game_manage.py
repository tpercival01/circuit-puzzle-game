import pygame
import time
from grid import Grid
from constants import START_TIME, WHITE, BLACK, GREEN, RED, MAIN_MENU, GAMEPLAY, LOSE_SCREEN, WIN_SCREEN

class GameManager:
    def __init__(self, window, total_points=0):
        self.window = window
        x, y = window.get_size()
        self.top_padding = 100 # Define padding for timer display
        self.running = True
        self.current_level = 1
        self.session_points = 0
        self.total_points = 0
        self.start_level()
        self.return_to_menu = False
    
    def start_game(self):
        while self.running:
            self.update_timer()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.return_to_menu = False
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.current_state == GAMEPLAY:
                            self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if self.current_state == WIN_SCREEN:
                        if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                            self.start_level()
                            self.current_level += 1
                            self.session_points += 100
                        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                            self.total_points += self.session_points
                            self.session_points = 0
                            print(f"Total points: {self.total_points}")
                            self.return_to_menu = True
                            self.running = False
                    elif self.current_state == LOSE_SCREEN:
                        if event.key == pygame.K_r:
                            self.session_points = 0
                            self.start_level()
                        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                            self.session_points = 0
                            self.current_level = 1
                            self.return_to_menu = True
                            self.running = False
            
             # Check game state
            if self.current_state == GAMEPLAY:
                if self.remaining_time == 0:
                    self.game_over()
                elif self.grid.check_win_condition():
                    self.win()
                else:
                    # Continue game
                    self.window.fill((230, 230, 230))  # Clear the screen before each draw
                    self.draw_timer()  # Draw the timer at the top
                    self.grid.draw(self.window)  # Draw the grid below the timer
            elif self.current_state == WIN_SCREEN:
                self.draw_win_screen()
            elif self.current_state == LOSE_SCREEN:
                # Draw lose screen
                self.draw_lose_screen()
            pygame.display.flip()  # Update the display
        
    def update_timer(self):
        if self.current_state == GAMEPLAY:
            elapsed_time = time.time() - self.start_time
            self.remaining_time = max(0, START_TIME - int(elapsed_time))
            if self.remaining_time == 0:
                self.game_over()
    
    def draw_timer(self):
        font = pygame.font.Font(None, 48)
        timer_surface = font.render(f"Time: {self.remaining_time}", True, (50,50,50))
        timer_rect = timer_surface.get_rect(center=(self.window.get_width() // 2, self.top_padding // 2))
        self.window.blit(timer_surface, timer_rect)

        info_font = pygame.font.Font(None, 36)
        level_surface = info_font.render(f"Level: {self.current_level}", True, BLACK)
        self.window.blit(level_surface, (10, 10))
        points_surface = info_font.render(f"Session Points: {self.session_points}", True, BLACK)
        self.window.blit(points_surface, (10,50))    
    
    def game_over(self):
        print("Game Over")
        self.current_state = LOSE_SCREEN
        self.session_points = 0

    def handle_click(self, position):
        if self.current_state == GAMEPLAY:
            self.grid.handle_click(position)
    
    def win(self):
        print("You Win!")
        self.current_state = WIN_SCREEN
        self.session_points += 100

    def start_level(self):
        x, y = self.window.get_size()
        self.grid = Grid(6, 6, x, y, top_padding=self.top_padding)
        self.start_time = time.time()
        self.remaining_time = START_TIME
        self.current_state = GAMEPLAY
    
    def draw_lose_screen(self):
        self.window.fill(RED)
        font = pygame.font.Font(None, 74)
        message_surface = font.render("GAME OVER - You Lose!", True, WHITE)
        message_rect = message_surface.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 - 50)
        )
        self.window.blit(message_surface, message_rect)
        prompt_font = pygame.font.Font(None, 48)
        prompt_surface = prompt_font.render("Press R to Retry or Q to Quit", True, WHITE)
        prompt_rect = prompt_surface.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 + 50)
        )
        self.window.blit(prompt_surface, prompt_rect)
        # Display current level
        info_font = pygame.font.Font(None, 36)
        level_surface = info_font.render(f"Level: {self.current_level}", True, WHITE)
        level_rect = level_surface.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 + 100)
        )
        self.window.blit(level_surface, level_rect)

    def draw_win_screen(self):
        self.window.fill(GREEN)
        font = pygame.font.Font(None, 74)
        message_surface = font.render("You Win!", True, WHITE)
        message_rect = message_surface.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 - 50)
        )
        self.window.blit(message_surface, message_rect)
        prompt_font = pygame.font.Font(None, 48)
        prompt_surface = prompt_font.render("Press ENTER to Continue or Q to Quit", True, WHITE)
        prompt_rect = prompt_surface.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 + 50)
        )
        self.window.blit(prompt_surface, prompt_rect)
        # Display current session points
        info_font = pygame.font.Font(None, 36)
        points_surface = info_font.render(f"Session Points: {self.session_points}", True, WHITE)
        points_rect = points_surface.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 + 100)
        )
        self.window.blit(points_surface, points_rect)