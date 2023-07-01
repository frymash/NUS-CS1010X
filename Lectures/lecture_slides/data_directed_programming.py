##################################################################################
############################## data-dircted programming ##########################

import math

proc = {}

def attach_tag(tag, content):
    return (tag, ) + content


def type_tag(datum):
    if type(datum) == tuple and len(datum) == 3:
        return datum[0]
    raise Exception('Bad tagged datum -- type_tag' + datum)


def content(datum):
    if type(datum) == tuple and len(datum) == 3:
        return datum[1:]
    raise Exception('Bad tagged datum -- content' + datum)


def put(op, types, value):
    if op not in proc:
        proc[op] = {}
    proc[op][types] = value
    
    
def get(op, types):
    return proc[op][types]


def install_ben_package():
    def make_from_real_imag(x, y):
        return attach_tag('rectangular', (x, y))
    def real_part(z):
        return z[1]
    def imag_part(z):
        return z[2]
    def magnitude(z):
        return math.hypot(real_part(z), imag_part(z))
    def angle(z):
        return math.atan(image_part(z) / real_part(z))
    def make_from_mag_ang(r, a):
        return (r * math.cos(a), r * math.sin(a))

    put('real_part', ('rectangular', ), real_part)
    put('imag_part', ('rectangular', ), imag_part)
    put('magnitude', ('rectangular', ), magnitude)
    put('angle', ('rectangular', ), angle)
    put('make_from_real_imag', 'rectangular', make_from_real_imag)
    put('make_from_mag_ang', 'rectangular', make_from_mag_ang)
    return 'done'


def install_alyssa_package():
    def make_from_mag_ang(r, a):
        return attach_tag('polar', (r, a))
    def magnitude(z):
        return z[1]
    def angle(z):
        return z[2]
    def real_part(z):
        return magnitude(z) * math.cos(angle(z))
    def imag_part(z):
        return magnitude(z) * math.sin(angle(z))
    def make_from_real_imag(x, y):
        return (math.hypot(x, y), math.atan(y / x))

    put('real_part', ('polar', ), real_part)
    put('imag_part', ('polar', ), imag_part)
    put('magnitude', ('polar', ), magnitude)
    put('angle', ('polar', ), angle)
    put('make_from_real_imag', 'polar', make_from_real_imag)
    put('make_from_mag_ang', 'polar', make_from_mag_ang)
    return 'done'

def apply_generic(op, *args):
    type_tags = tuple(map(type_tag, args))
    proc = get(op, type_tags)
    return proc(*args)

def make_from_real_imag_rectangular(x, y):
    return get('make_from_real_imag', 'rectangular')(x, y)

def make_from_mag_ang_rectangular(x, y):
    return get('make_from_mag_ang', 'rectangular')(x, y)

def make_from_real_imag_polar(x, y):
    return get('make_from_real_imag', 'polar')(x, y)

def make_from_mag_ang_polar(x, y):
    return get('make_from_mag_ang', 'polar')(x, y)

def real_part(z):
    return apply_generic('real_part', z)

def imag_part(z):
    return apply_generic('imag_part', z)

def magnitude(z):
    return apply_generic('magnitude', z)

def angle(z):
    return apply_generic('angle', z)


install_ben_package()
install_alyssa_package()
