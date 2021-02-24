# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Tell me a name and how to greet you
def greet(name, greeting='Hello, <name>!'):
    return greeting.replace('<name>', name)  # find is also possible


# How much force is needed on a specific planet
def force(mass: float, body='earth'):
    gravity = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6}
    return mass * gravity[body]


# How much do two objects pull to each other
def pull(m1: float, m2: float, d: float):
    G = 6.674 * 10 ** -11  # gravitational constante
    return G * ((m1 * m2) / d ** 2)
