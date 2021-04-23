# Importerer nødvendige bibliotek
from matplotlib import pyplot as plt
import math
# import numpy as np

# Konstanter
gravitational_const = 6.67408E-11  # m^3 kg^-1 s^-2
earth_mass = 5.972E24  # Mass/kg
earth_radius = 6371000
rocket_mass = 8E4  # Mass/kg


# Variabler
fuel_mass = 2.66E5  # Mass/kg
total_mass = fuel_mass + rocket_mass


# Lager lister
altitude = []
field_strength = []


class Rocket():
    def __init__(self, position, velocity, acceleration, mass, fuel):
        self.time = [0]
        self.mass = mass  # Masse/kg
        self.fuel = fuel  # Masse/kg
        self.pitch = math.pi/2  # Vinkel/rad
        self.throttle = 1
        self.max_thrust = 3.1E6

    @property
    def thrust(cls):
        return cls.throttle * cls.max_thrust  # Kraft av motorene / Newton

    @property
    def total_mass(cls):
        return cls.mass + cls.fuel  # Totale massen til raketten

    # @property
    # def position(cls):
    #     position[-1]

    @property
    def altitude(cls):
        return position[-1]

    # @property
    # def velocity(cls):
    #     return velocity[-1]

    @property
    def acceleration(cls):
        if cls.altitude == earth_radius:
            if abs(cls.thrust) < abs(cls.gravity):
                return 0
        return (cls.gravity + cls.thrust) / cls.mass

    @property
    def gravity(cls):
        """
        Beregner gravitasjonskraften mellom raketten og jorden ved hjelp av
        Newtons universelle gravitasjonslov (k*m1*m2/r^2). Tar inn h som høyde
        over bakken, r blir da jordas radius pluss h.
        """
        return -gravitational_const*cls.total_mass*earth_mass/(cls.altitude)**2


lifty = Rocket([0, earth_radius], [0, 0], [0, 0], rocket_mass,
               fuel_mass,)


time = [0]
position = [earth_radius]
velocity = [0]
acceleration = [0]
fuel = [fuel_mass]
throttle = [1]


for i in range(3000):
    if lifty.fuel < 500*lifty.throttle:
        lifty.throttle = 0
    lifty.fuel -= 500*lifty.throttle

    if i > 500:
        lifty.throttle = 0

    time.append(i)
    throttle.append(lifty.throttle)
    fuel.append(lifty.fuel)
    acceleration.append(lifty.acceleration)
    velocity.append(velocity[i] + (acceleration[i] + acceleration[i-1])/2)
    position.append(position[i] + (velocity[i] + velocity[i-1])/2)

    # if position[-1] > 4000000:
    #     break


fig, axs = plt.subplots(2, 3)
axs[0, 0].plot(time, acceleration)
axs[0, 0].set_title('Akselerasjon')
axs[0, 1].plot(time, velocity, 'tab:orange')
axs[0, 1].set_title('Hastighet')
axs[0, 2].plot(time, position, 'tab:orange')
axs[0, 2].set_title('Posisjon')
axs[1, 0].plot(time, throttle, 'tab:green')
axs[1, 0].set_title('throttle')
axs[1, 1].plot(time, fuel, 'tab:red')
axs[1, 1].set_title('Drivstoff')

for ax in axs.flat:
    ax.set(xlabel='Tid/s')
plt.show()

print(acceleration)


# class Engine():
#     def __init__(self, angle):
#         self.throttle = 0
#         self.angle = angle
#
#     def thrust(cls):
#         return cls.throttle * 2.21E6  # Kraft av motorene / Newton
#
#
# raptor1 = Engine(math.pi/2)
# raptor2 = Engine()
# raptor3 = Engine()
