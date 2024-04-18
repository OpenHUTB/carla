
from __future__ import print_function

from . import SmokeTest
import argparse
import glob
import math
import os
import sys
import time
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/carla')
except IndexError:
    pass

import carla

def WalkersSpawnTest():

    client = carla.Client()
    world = client.load_world('Town10HD_Opt')
    bp_lib = world.get_blueprint_library()
    spectator = world.get_spectator()
    spectator.set_transform(carla.Transform(carla.Location(-27.8, -63.28, 10.6), carla.Rotation(pitch=-29, yaw=135)))

    walkers_bp_to_spawn = bp_lib.filter("*walker*")
    # Spawn the actor
    walkers = []
    counter = 0
    for bp in walkers_bp_to_spawn:
        location = carla.Location(-27.8 + counter , -61.28, 10.6)
        walker = world.spawn_actor(bp, carla.Transform(location, carla.Rotation()))
        walkers.append(walker)
        counter += 1
        if walker is None:
            print("Error spawning Walker", walker)
    
    world.tick()
    actors = world.get_actors().filter('*walker*')
    gotactors = actors.__len__()

    for _ in range(400):
        world.tick()
    
    #This MUST Become an assert
    print("Spected actors: ", counter, " Got Actors: ", gotactors)

    for walker in walkers:
        walker.destroy()

    world.tick()
    actors = world.get_actors().filter('*walker*')
    gotactors = actors.__len__()

    #This MUST Become an assert
    print("Spected actors: 0 Got Actors: ", gotactors)

if __name__ == '__main__':
    WalkersSpawnTest()
