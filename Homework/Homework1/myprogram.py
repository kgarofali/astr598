"""
Kristen Garofali
ASTR598 Homework 1
"""

import mymath

#initialize particle 1 with mass in kg, position in m
pos1 = mymath.Position(0,0,1)
vel1 = mymath.Velocity(-1,0,0)
mass1 = 5.
p1 = mymath.Particle(mass1, pos1, vel1)
#initialize particle 2 with mass in kg, position in m
pos2 = mymath.Position(0,1,0)
vel2 = mymath.Velocity(0,0,1)
mass2 = 3.
p2 = mymath.Particle(mass2,pos2,vel2)

force = mymath.Particle.force(p1,p2)

print("The force between particles p1 and p2 is {0} Newtons".format(force))
