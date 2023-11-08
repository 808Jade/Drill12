import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie


# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global grass
    global boy

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    game_world.add_collision_pair('boy:ball', boy, None) #소년은 과 볼 충돌을 비교해야돼 a: boy 넣어주고 b: 아직몰라
    game_world.add_collision_pair('boy:zombie', boy, None) #소년은 과 볼 충돌을 비교해야돼 a: boy 넣어주고 b: 아직몰라

    # fill here
    balls = [Ball(random.randint(100, 1600 - 100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)


    for ball in balls:  # 모든 ball에 대해서..
        game_world.add_collision_pair('boy:ball', None, ball) # a 그룹엔 이미 boy가 들어가 있다.
        game_world.add_collision_pair('zombie:ball', None, ball) #소년은 과 볼 충돌을 비교해야돼 a: boy 넣어주고 b: 아직몰라

    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie', None, zombie)
        game_world.add_collision_pair('zombie:ball', zombie, None) #소년은 과 볼 충돌을 비교해야돼 a: boy 넣어주고 b: 아직몰라



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
