import pygame
from menu import Menu
from game_manage import GameManager

class GameWindow:
    def __init__(self, width=800, height=600, title="Circuit Connect"):
        """
        Initializes the game window with the given width, height, and title.
        """
        # Initialize Pygame
        pygame.init()

        # Set the window size
        self.width = width
        self.height = height

        # Set the window title
        self.title = title

        # Create the game window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Set the title for the window
        pygame.display.set_caption(self.title)

        # Set a flag to indicate if the game is running
        self.running = True

        self.total_points = 0

    def run(self):
        """
        Main loop to keep the window open.
        """
        while self.running:
            # Show the main menu first
            main_menu = Menu(self.window, ["Start", "Settings", "Exit"], self.total_points, "Main Menu")
            action = main_menu.show()

            if action == "Exit":
                self.running = False
            elif action == "Settings":
                while True:
                    settings_menu = Menu(self.window, ["Audio", "Video", "Back"], self.total_points, "Settings Menu")
                    settings_action = settings_menu.show()

                    if settings_action == "Back":
                        break
                    elif settings_action == "Video":
                        while True:
                            video_menu = Menu(self.window, ["1024 x 768", "800 x 600", "Back"], self.total_points, "Video Menu")
                            video_action = video_menu.show()

                            if video_action == "Back":
                                break
                            elif video_action == "1024 x 768":
                                self.width, self.height = 1024, 768
                                self.window = pygame.display.set_mode((self.width, self.height))
                            elif video_action == "800 x 600":
                                self.width, self.height = 800, 600
                                self.window = pygame.display.set_mode((self.width, self.height))

            elif action == "Start":
                game_manager = GameManager(self.window, total_points=self.total_points)
                game_manager.start_game()
                
                if game_manager.return_to_menu:
                    self.total_points = game_manager.total_points
                    pass
                else:
                    self.running = False

        # Quit Pygame after the loop ends
        pygame.quit()