import pygame
import random
from constants import BLACK, WHITE, RED, GREEN, BLUE, DEFAULT_WIDTH, DEFAULT_HEIGHT, NUM_TYPE_0, NUM_TYPE_1, NUM_TYPE_2, NUM_TYPE_3, NUM_TYPE_4, NUM_TYPE_5, NUM_TYPE_6

class Grid():
    def __init__(self, rows, cols, width, height, top_padding):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height - top_padding  # Reduce height to accommodate padding for the timer
        self.top_padding = top_padding

        available_width = self.width - 200  # Width for grid minus 100px for each side column (start and end)
        available_height = self.height

        # Set cell size ensuring the tiles are square and fit within the available width and height
        self.cell_size = min(available_height // self.rows, available_width // self.cols)

        # Calculate offsets for centering the grid
        self.x_offset = (self.width - (self.cols * self.cell_size)) // 2
        self.y_offset = self.top_padding  # Calculate offset to center everything horizontally

        # Load assets
        self.tile_images = {
            0: pygame.image.load("assets/images/0.png"),
            1: pygame.image.load("assets/images/1.png"),
            2: pygame.image.load("assets/images/2.png"),
            3: pygame.image.load("assets/images/3.png"),
            4: pygame.image.load("assets/images/4.png"),
            5: pygame.image.load("assets/images/5.png"),
            6: pygame.image.load("assets/images/6.png")
        }

        # Define the distribution of tile types
        self.tile_types = self.generate_tile_types(rows, cols)

        # Initialize each tile with the predefined distribution of types
        self.tiles = [[{"revealed": False, "type": self.tile_types.pop()} for _ in range(cols)] for _ in range(rows)]

        # Randomly set the start (left) and end (right) points
        self.start_pos = self.get_random_position("left")
        self.end_pos = self.get_random_position("right")

        # Initialize inventory with a tile of type 0
        self.current_inventory_tile = {"revealed": True, "type": 0}
        self.inventory_slot = (0, -1)

    def generate_tile_types(self, rows, cols):
        """
        Generate a list of tile types based on the required distribution:
        - 50% of the tiles are type 0 (horizontal wire)
        - 10% each are type 1, 2, 3, 4 (elbows)
        - 10% type 6 (vertical wire)
        - The rest are type 5 (T-junctions)
        """
        total_tiles = rows * cols
        num_type_0 = int(total_tiles * NUM_TYPE_0)
        num_type_1 = int(total_tiles * NUM_TYPE_1)
        num_type_2 = int(total_tiles * NUM_TYPE_2)
        num_type_3 = int(total_tiles * NUM_TYPE_3)
        num_type_4 = int(total_tiles * NUM_TYPE_4)
        num_type_5 = int(total_tiles * NUM_TYPE_5)
        num_type_6 = int(total_tiles * NUM_TYPE_6)
        num_remaining = total_tiles - (num_type_0 + num_type_1 + num_type_2 + num_type_3 + num_type_4 + num_type_5 + num_type_6)

        tile_types = ([0] * num_type_0 +
                      [1] * num_type_1 +
                      [2] * num_type_2 +
                      [3] * num_type_3 +
                      [4] * num_type_4 +
                      [5] * num_type_5 +
                      [6] * num_type_6 +
                      [5] * num_remaining)  # Remaining tiles can be of type 5 (T-junctions)
        random.shuffle(tile_types)
        return tile_types

    def get_random_position(self, side):
        """
        Get a random position on either the left or right edge of the grid.
        """
        row = random.randint(0, self.rows - 1)
        if side == "left":
            return (row, -1)  # Position outside of the grid for the left side
        else:
            return (row, self.cols)  # Position outside of the grid for the right side

    def draw(self, window):
        """
        Draw the grid and start/end points on the provided Pygame window surface.
        """
        # Draw the red start point on the left, aligned with the rows
        start_row, _ = self.start_pos
        start_y = self.y_offset + start_row * self.cell_size
        x_start = self.x_offset - self.cell_size
        pygame.draw.rect(window, RED, (x_start, start_y, self.cell_size, self.cell_size))
        pygame.draw.rect(window, (150, 0, 0), (x_start, start_y, self.cell_size, self.cell_size), 3)  # Dark red border for start tile
        font = pygame.font.Font(None, 24)
        label_surface = font.render("Start", True, WHITE)
        label_rect = label_surface.get_rect(center=(x_start + self.cell_size // 2, start_y + self.cell_size // 2))
        window.blit(label_surface, label_rect)

        # Draw the red end point on the right, aligned with the rows
        end_row, _ = self.end_pos
        end_y = self.y_offset + end_row * self.cell_size
        x_end = self.x_offset + (self.cols * self.cell_size)
        pygame.draw.rect(window, RED, (x_end, end_y, self.cell_size, self.cell_size))
        pygame.draw.rect(window, (150, 0, 0), (x_end, end_y, self.cell_size, self.cell_size), 3)  # Dark red border for end tile
        label_surface = font.render("End", True, WHITE)
        label_rect = label_surface.get_rect(center=(x_end + self.cell_size // 2, end_y + self.cell_size // 2))
        window.blit(label_surface, label_rect)

        # Draw inventory slot on the left, below the start point
        inventory_x = self.width - self.cell_size - 150
        inventory_y = 10
        pygame.draw.rect(window, (180, 255, 180), (inventory_x, inventory_y, self.cell_size, self.cell_size))  # Draw the inventory background
        label_surface = font.render("Spare:", True, BLACK)
        label_rect = label_surface.get_rect(midright=(inventory_x - 10, inventory_y + self.cell_size // 2))
        window.blit(label_surface, label_rect)

        if self.current_inventory_tile:
            if self.current_inventory_tile["type"] in self.tile_images:
                inventory_image = self.tile_images[self.current_inventory_tile["type"]]
                inventory_image = pygame.transform.scale(inventory_image, (self.cell_size, self.cell_size))
                window.blit(inventory_image, (inventory_x, inventory_y))
            else:
                tile_surface = font.render(str(self.current_inventory_tile["type"]), True, WHITE)
                tile_rect = tile_surface.get_rect(center=(inventory_x + self.cell_size // 2, inventory_y + self.cell_size // 2))
                window.blit(tile_surface, tile_rect)

        # Draw the grid tiles in the center
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.x_offset + (col * self.cell_size)
                y = self.y_offset + (row * self.cell_size)

                if self.tiles[row][col]["revealed"]:
                    if self.tiles[row][col]["type"] in self.tile_images:
                        tile_image = self.tile_images[self.tiles[row][col]["type"]]
                        tile_image = pygame.transform.scale(tile_image, (self.cell_size, self.cell_size))
                        window.blit(tile_image, (x, y))
                    else:
                        pygame.draw.rect(window, (255, 255, 150), (x, y, self.cell_size, self.cell_size))
                        tile_surface = font.render(str(self.tiles[row][col]["type"]), True, BLACK)
                        tile_rect = tile_surface.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
                        window.blit(tile_surface, tile_rect)
                else:
                    pygame.draw.rect(window, (50, 50, 50), (x, y, self.cell_size, self.cell_size), 1)

    def check_win_condition(self):
        """
        Check if there is a valid path connecting the start to the end, considering wire types.
        """
        start_row, _ = self.start_pos
        end_row, _ = self.end_pos
        visited = set()
        stack = []

        # Define the sides for each movement direction
        movement_directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # Map movement directions to exit and entry sides
        movement_sides = {
            "up": ("top", "bottom"),
            "down": ("bottom", "top"),
            "left": ("left", "right"),
            "right": ("right", "left")
        }

        # Define connection sides for each tile type
        connection_sides = {
            0: {"left", "right"},             # Horizontal straight wire
            1: {"bottom", "right"},           # Elbow piece 1 (from bottom to right)
            2: {"top", "right"},              # Elbow piece 2 (from top to right)
            3: {"bottom", "left"},            # Elbow piece 3 (from bottom to left)
            4: {"top", "left"},               # Elbow piece 4 (from top to left)
            5: {"left", "right", "top"},      # T-junction (left, right, top)
            6: {"top", "bottom"}              # Vertical straight wire
        }

        # Initialize stack with the tile adjacent to the start tile
        if 0 <= start_row < self.rows:
            # The start tile is at (start_row, -1)
            # Check if the tile at (start_row, 0) allows entry from the left
            start_tile = self.tiles[start_row][0]
            if start_tile["revealed"]:
                stack.append(((start_row, 0), "left"))

        while stack:
            (row, col), entry_side = stack.pop()

            # Skip if already visited
            if (row, col, entry_side) in visited:
                continue
            visited.add((row, col, entry_side))

            current_tile = self.tiles[row][col]

            # Check if the current tile allows entry from the entry_side
            if entry_side not in connection_sides.get(current_tile["type"], set()):
                continue

            # Check if we have reached the last column
            if (row, col) == (end_row, self.cols - 1):
                # Check if this tile allows exit to the "right" (i.e., can reach the end tile)
                if "right" in connection_sides.get(current_tile["type"], set()):
                    return True

            # Explore neighboring tiles
            for direction, (d_row, d_col) in movement_directions.items():
                exit_side, next_entry_side = movement_sides[direction]

                # Check if the current tile allows exit through exit_side
                if exit_side not in connection_sides.get(current_tile["type"], set()):
                    continue

                next_row, next_col = row + d_row, col + d_col

                # Check boundaries
                if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                    next_tile = self.tiles[next_row][next_col]
                    if next_tile["revealed"]:
                        # Add the next tile to the stack with the side we will enter from
                        stack.append(((next_row, next_col), next_entry_side))
                    # Special case: Check if we're moving to the end tile position
                elif next_row == end_row and next_col == self.cols:
                    # We're moving from the tile at (row, col) to the end tile position
                    # Ensure that exit_side is "right" since we're moving off the grid to the right
                    if exit_side == "right" and direction == "right":
                        # We have reached the end tile
                        return True
        # If we exit the loop without finding a path to the last column, return False
        return False

    def is_valid_move(self, current_tile_type, direction, next_tile_type, connection_rules, opposite_directions):
        """
        Check if moving from the current tile to the next tile in the given direction is valid.
        """
        # Check if the current tile allows exit in the movement direction
        if direction not in connection_rules.get(current_tile_type, set()):
            return False
        # Check if the next tile allows entry from the opposite direction
        reverse_direction = opposite_directions[direction]
        if reverse_direction not in connection_rules.get(next_tile_type, set()):
            return False
        return True

    def handle_click(self, position):
        """
        Handle a click event, determining which tile or start/end point was clicked.
        """
        x, y = position

        # Handle clicks within the main grid area
        if self.x_offset <= x < self.x_offset + (self.cols * self.cell_size):
            col = (x - (self.x_offset)) // self.cell_size
            row = (y - self.top_padding) // self.cell_size

            if 0 <= row < self.rows and 0 <= col < self.cols:
                tile = self.tiles[row][col]
                if not tile["revealed"]:
                    # Reveal the tile if it hasn't been revealed yet
                    tile["revealed"] = True
                    print(f"Revealed tile at row {row}, col {col}, type: {tile['type']}")
                elif tile["revealed"] and self.current_inventory_tile is None:
                    # If the tile is already revealed and inventory is empty, pick up the tile
                    self.current_inventory_tile = tile
                    self.tiles[row][col] = {"revealed": False, "type": None}  # Remove tile from grid
                    print(f"Picked up tile from row {row}, col {col}, type: {tile['type']}")
                elif tile["revealed"] and self.current_inventory_tile:
                    # If inventory is not empty, swap the inventory tile with the clicked tile
                    self.tiles[row][col], self.current_inventory_tile = self.current_inventory_tile, self.tiles[row][col]
                    print(f"Swapped inventory tile with tile at row {row}, col {col}")

        else:
            # Handle clicks on the start point (left edge)
            start_row, _ = self.start_pos
            end_row, _ = self.end_pos
            clicked_row = (y - self.top_padding) // self.cell_size

            # Check if clicked on start point (left edge)
            if x < self.x_offset and clicked_row == start_row:
                print("Clicked the red start tile!")

            # Check if clicked on end point (right edge)
            elif x > self.x_offset + (self.cols * self.cell_size) and clicked_row == end_row:
                print("Clicked the red end tile!")