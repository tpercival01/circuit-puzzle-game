import pygame
from constants import WHITE, BLACK, GREEN, RED, BLUE  # Add button colors to constants.py

class Menu:
    def __init__(self, window, buttons, total_points, title):
        self.window = window
        self.buttons = buttons
        self.title = title
        self.total_points = total_points
        self.button_rects = []
        self.top_padding = 150  # Consistent with the top padding used in Grid/GameManager

    def draw_button(self, text, rect, color, text_color=WHITE):
        pygame.draw.rect(self.window, color, rect, border_radius=10)
        font = pygame.font.Font(None, 36)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.window.blit(text_surf, text_rect)

    def show(self):
        menu_running = True
        self.create_button_rects()

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i, button_rect in enumerate(self.button_rects):
                        if button_rect.collidepoint(mouse_pos):
                            print(f"{self.buttons[i]} button clicked")
                            menu_running = False
                            return self.buttons[i]

            self.window.fill(BLACK)
            self.draw_title()
            self.draw_buttons()
            pygame.display.flip()

    def create_button_rects(self):
        button_width = 200
        button_height = 50
        spacing = 20
        total_height = len(self.buttons) * button_height + (len(self.buttons) - 1) * spacing
        start_y = self.top_padding

        self.button_rects = [
            pygame.Rect(
                (self.window.get_width() - button_width) // 2, 
                start_y + i * (button_height + spacing), 
                button_width, 
                button_height
            ) for i in range(len(self.buttons))
        ]

    def draw_title(self):
        font = pygame.font.Font(None, 48)
        title_surface = font.render(self.title, True, WHITE)
        title_rect = title_surface.get_rect(center=(self.window.get_width() // 2, self.top_padding // 2))
        self.window.blit(title_surface, title_rect)

        points_font = pygame.font.Font(None, 36)
        points_text = f"Total Points: {self.total_points}"
        points_surface = points_font.render(points_text, True, WHITE)
        points_y = title_rect.bottom + 10  # Position 10 pixels below the title
        points_rect = points_surface.get_rect(center=(self.window.get_width() // 2, points_y + points_surface.get_height() // 2))
        self.window.blit(points_surface, points_rect)

    def draw_buttons(self):
        for i, button_rect in enumerate(self.button_rects):
            button_label = self.buttons[i]
            color = GREEN if button_label == "Start" else RED if button_label == "Exit" else BLUE
            self.draw_button(button_label, button_rect, color)
