from game import Game
import arcade
import numpy as np










SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Platformer"




class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.game = Game()


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.game.step(None)

        self.clear()
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,2*self.game.width,2*self.game.height,arcade.color.DARK_BROWN)

        for obj in self.game.objects:

            arcade.draw_circle_filled(SCREEN_WIDTH//2+obj.x,SCREEN_HEIGHT//2+obj.y, obj.radius, arcade.color.PINK, 0)
        # Code to draw the screen goes here


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


    arcade.draw_rectangle_filled(0,0,2*window.game.width,2*window.game.height,arcade.color.DARK_BROWN)



if __name__ == "__main__":
    main()