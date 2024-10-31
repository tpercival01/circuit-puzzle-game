# Circuit Connect

Welcome to Circuit Connect!

Circuit Connect is a puzzle game built with Python and Pygame. The objective is to connect the circuit from the start point to the end point by arranging the tiles on the grid. As you progress through the levels, the difficulty increases, challenging your problem-solving skills.

## Table of Contents
- [Features](#features)
- [Gameplay](#gameplay)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [How to Run](#how-to-run)
- [Controls](#controls)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- **Engaging Puzzle Mechanics**: Connect the circuit by arranging tiles with different connections.
- **Multiple Levels**: Progress through levels with increasing difficulty.
- **Scoring System**: Earn points by completing levels; risk losing them if you lose in subsequent levels.
- **Time Challenge**: Complete each level within the time limit.
- **Main Menu and Settings**: Navigate through the main menu and adjust settings like resolution.
- **Restart and Quit Options**: Restart levels or return to the main menu at any time.
- **Persistent Scoring**: Total points are displayed in the main menu and accumulated across sessions.

## Gameplay
- **Objective**: Connect the start point to the end point by arranging the tiles on the grid.
- **Tiles**: Various tile types represent different circuit connections.
- **Timer**: Complete the level before the timer runs out.
- **Points**: Earn points for each level completed; choose to risk them by continuing or save them by quitting to the main menu.
- **Levels**: Advance through levels that increase in difficulty.

## Installation
### Prerequisites
- **Python 3.x**: Download and install from [python.org](https://www.python.org/).
- **Pygame**: Install the Pygame library.

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/circuit-connect.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd circuit-connect
   ```

3. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   **Note**: If `requirements.txt` is not available, install Pygame manually:
   ```bash
   pip install pygame
   ```

## How to Run
After installing the dependencies, you can run the game using:
```bash
python main.py
```
Make sure you are in the project directory where `main.py` is located.

## Controls
- **Mouse Click**: Interact with the tiles to reveal or swap them.
- **Keyboard**:
  - **Enter**: Continue to the next level on the win screen.
  - **R**: Restart the level on the lose screen.
  - **Q or Escape**: Quit to the main menu.

## Screenshots
- Main Menu displaying total points.
- In-game screenshot showing the grid and timer.
- Win screen with options to continue or quit.

## Roadmap
Planned features for future releases:
- **Tile Rotation Mechanic**: Allow players to rotate tiles to connect circuits.
- **New Levels and Difficulty Modes**: Introduce varying difficulty settings and more levels.
- **Power-Ups and Obstacles**: Add power-ups like extra time or hints, and obstacles like locked tiles.
- **Multiplayer Mode**: Implement local and online multiplayer options.
- **Enhanced Graphics and Sound**: Upgrade visuals and add background music and sound effects.
- **Leaderboard Integration**: Implement a global leaderboard to track high scores.
- **Story Mode**: Develop a storyline that unfolds as the player progresses.

## Contributing
Contributions are welcome! To contribute:
1. **Fork the Project**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Pygame**: For providing the game development framework.
- **OpenAI's ChatGPT**: For assistance and suggestions during development.

