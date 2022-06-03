from email import message
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._player_win = False
        self._message = Actor()

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # if bullet.position == food poition:
        #       points = food.get_points()
        #       score.add_points(points)
        #       foodsList.remove(food)
        score = cast.get_first_actor("scores")
        foodsList = cast.get_all_actors_group("foods")
        snake = cast.get_first_actor("snakes")
        bullet = cast.get_first_actor("bullet")
        player2 = cast.get_first_actor("player2")
        player2_head = player2.get_head()
        for food in foodsList:
            if bullet.get_position().equals(food.get_position()):
                points = food.get_points()
                # snake.grow_tail(points)
                score.add_points(points)
                bullet.set_position(player2_head.get_position())
                foodsList.remove(food)
                bullet.set_shot_fired(False)
    #     if player2_head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         player2.grow_tail(points)
    #         food.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        bullet = cast.get_first_actor("bullet")
        score = cast.get_first_actor("scores")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        player2 = cast.get_first_actor("player2")
        player2_head = player2.get_segments()[0]

        
        if player2_head.get_position().equals(head.get_position()):
                self._is_game_over = True
                self._message.set_text("Game Over")
        elif bullet.get_position().equals(head.get_position()):
            if len(snake._segments) == 1:
                self._is_game_over = True
                score.add_points(20)
                bullet.set_position(player2_head.get_position())
                self._message.set_text("You Win!")
                self._player_win = True
            else:
                snake._segments.pop(len(snake._segments)-1)
                constants.SNAKE_LENGTH -= 1
                bullet.set_shot_fired(False)
                score.add_points(20)
                bullet.set_position(player2_head.get_position())
        for segment in segments:
            # if head.get_position().equals(segment.get_position()):
            #     self._is_game_over = True 
            #     self._message.set_text("Blue Wins!")
            if player2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._message.set_text("Game Over")
            if bullet.get_position().equals(segment.get_position()):
                snake._segments.pop(len(snake._segments)-1)
                constants.SNAKE_LENGTH -= 1
                bullet.set_shot_fired(False)
                score.add_points(20)
                bullet.set_position(player2_head.get_position())
            # elif bullet.get_position().equals(head.get_position()):
            #     snake._segments.pop(len(snake._segments)-1)
            #     constants.SNAKE_LENGTH -= 1
            #     bullet.set_shot_fired(False)
            #     score.add_points(20)
            #     bullet.set_position(player2_head.get_position())

            # elif len(snake._segments) == 1 and bullet.get_position().equals(head.get_position()):
            #     snake._segments.pop(len(snake._segments)-1)
            #     constants.SNAKE_LENGTH -= 1
            #     bullet.set_shot_fired(False)
            #     score.add_points(20)
            #     bullet.set_position(player2_head.get_position())

            # if constants.SNAKE_LENGTH <= 0:
            #     self._is_game_over = True
            #     self._message.set_text("You Win!")


            #     print('game')
            #     self._is_game_over = True
            #     self._message.set_text("You Win!")

    
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            player2 = cast.get_first_actor("player2")
            player2_segments = player2.get_segments()
            foodsList = cast.get_all_actors_group("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            self._message.set_position(position)
            cast.add_actor("messages", self._message)
            if self._player_win:
                segments[0].set_text(" ")
            

            for segment in segments:
                segment.set_color(constants.WHITE)
                
            for segment in player2_segments:
                segment.set_color(constants.WHITE)
                
            for food in foodsList:
                food.set_color(constants.WHITE)