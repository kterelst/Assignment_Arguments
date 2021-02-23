# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting=None):
    if greeting is None:
        return f'Hello, {name}!'
    else:
        return greeting.replace('<name>', name)  # find had ook gekund


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


def pull(m1: float, m2: float, d: float):
    G = 6.674 * 10 ** -11  # gravitational constante
    return G * ((m1 * m2) / d ** 2)
