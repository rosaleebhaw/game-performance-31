class GamePerformanceError(Exception):
    """Custom exception for game performance issues."""
    def __init__(self, message):
        super().__init__(message)

class Game:
    def __init__(self, name, fps_limit=60):
        self.name = name
        self.fps_limit = fps_limit
        self.current_fps = 0

    def update_performance(self, new_fps):
        """Update the current FPS and check against limit."""
        self.current_fps = new_fps
        if self.current_fps > self.fps_limit:
            raise GamePerformanceError(f"FPS limit exceeded: {self.current_fps} > {self.fps_limit}")

    def display_performance(self):
        """Display current FPS and game name."""
        performance_info = f"Game: {self.name}, Current FPS: {self.current_fps}"
        return performance_info

if __name__ == '__main__':
    game = Game("Epic Adventure")
    try:
        game.update_performance(75)  # Simulate FPS update
    except GamePerformanceError as e:
        print(e)
    print(game.display_performance())