from game.scripting.action import Action
import constants


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):

    def execute(self, cast, script):
        actors = cast.get_all_actors()
        snakes = cast.get_actors("snakes")
        player2 = cast.get_actors("player2")
        for actor in actors:
            actor.move_next()
        # for part in snakes:
        #     part.grow_tail(1)
        # for part in player2:
        #     part.grow_tail(1)
            