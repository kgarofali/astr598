import numpy as np

class Position:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

class Velocity:
    def __init__(self, vx=0.0, vy=0.0, vz=0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    @staticmethod
    def force(particle_one, particle_two):
        G = 6.67e-11 #gravitational constant in m^3 kg^-1 s^-2
        p1 = Particle(particle_one.mass, particle_one.position, particle_one.velocity)
        p2 = Particle(particle_two.mass, particle_two.position, particle_two.velocity)
        r = np.sqrt((p2.position.x-p1.position.x)**2 + (p2.position.y-p1.position.y)**2 + (p2.position.z-p1.position.z)**2)
        return (G*p1.mass*p2.mass)/r**2
