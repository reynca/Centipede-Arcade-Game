from shutil import move
from tokenize import group
import pyray
import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.actor import Actor


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._directionPlayer1 = Point(constants.CELL_SIZE, 0)
        self._directionPlayer2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player2 = cast.get_first_actor("player2")
        player2.turn_head(Point(0,0))
        player2Head = player2.get_head()
        player2_p = player2Head.get_position()
        bullet = cast.get_first_actor("bullet")
        bullet_p = bullet.get_position()
        # # left
        # if self._keyboard_service.is_key_down('a'):
        #     self._directionPlayer1 = Point(-constants.CELL_SIZE, 0)
        
        # # right
        # if self._keyboard_service.is_key_down('d'):
        #     self._directionPlayer1 = Point(constants.CELL_SIZE, 0)
        
        # # up
        # if self._keyboard_service.is_key_down('w'):
        #     self._directionPlayer1 = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service.is_key_down('s'):
        #     self._directionPlayer1 = Point(0, constants.CELL_SIZE)
        
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()
        foodsList = cast.get_all_actors_group("foods")
        
        # snake.turn_head(Point(0,0))

        newPoint = head.get_position()
        newPointX = newPoint.add(Point(15,0))
        newPointY = newPoint.add(Point(0,15))
        newPointXneg = newPoint.add(Point(-15,0))
        newPointYneg = newPoint.add(Point(0, -15))

        for food in foodsList:
            if newPointX.equals(food.get_position()):
                snake.turn_head(snake._snakeDirection)
                snake._movesR += 1
            elif newPointXneg.equals(food.get_position()):
                snake.turn_head(snake._snakeDirection)
                snake._movesL += 1
        # Wall Collision        
        if newPointX.equals(Point(constants.MAX_X, newPoint.get_y())):
            snake.turn_head(snake._snakeDirection)
            snake._movesR += 1
        elif newPoint.equals(Point(0, newPoint.get_y())):
            snake.turn_head(snake._snakeDirection)
            snake._movesL += 1
        
        # Floor Collision
        if newPointY.equals(Point(newPoint.get_x(), constants.MAX_Y)):
            snake._snakeDirection = Point(0, -constants.CELL_SIZE)
            # snake.turn_head(snake._snakeDirection)
            snake._movesR += 1
        elif newPointYneg.equals(Point(newPoint.get_x(), (constants.COLUMNS- 6) * 15)):
            snake._snakeDirection = Point(0, constants.CELL_SIZE)
            # snake.turn_head(snake._snakeDirection)
            snake._movesR += 1
        # 3 frame rule
        if snake._movesR == 1:
            snake._movesR += 1
        elif snake._movesR >= 2:
            snake.turn_head(Point(-constants.CELL_SIZE, 0))
            snake._movesR = 0
        
        if snake._movesL == 1:
            snake._movesL += 1
        elif snake._movesL >= 2:
            snake.turn_head(Point(constants.CELL_SIZE, 0))
            snake._movesL = 0
        
        

        
        
        
        
        
        
        
        # left
        if pyray.is_key_down(pyray.KEY_LEFT):
            self._directionPlayer2 = Point(-constants.CELL_SIZE, 0)
            player2.turn_head(self._directionPlayer2)
        
        # right
        if pyray.is_key_down(pyray.KEY_RIGHT):
            self._directionPlayer2 = Point(constants.CELL_SIZE, 0)
            player2.turn_head(self._directionPlayer2)
        
        # up
        if pyray.is_key_down(pyray.KEY_UP):
            self._directionPlayer2 = Point(0, -constants.CELL_SIZE)
            player2.turn_head(self._directionPlayer2)
        
        # down
        if pyray.is_key_down(pyray.KEY_DOWN):
            self._directionPlayer2 = Point(0, constants.CELL_SIZE)
            player2.turn_head(self._directionPlayer2)
        # player2 = cast.get_first_actor("player2")
        # player2.turn_head(self._directionPlayer2)
        
        if bullet_p.equals(Point(bullet_p.get_x(), 0)):
            bullet.set_shot_fired(False)
            # player2_p = player2_p.add(Point(0, 0))

        elif self._keyboard_service.is_key_down('space'):
            self._directionPlayer1 = Point(0, -constants.CELL_SIZE)
            bullet.shoot(self._directionPlayer1)
            bullet.set_shot_fired(True)
            
        if bullet.get_shot_fired() == False:
            bullet.set_position(player2_p)
    