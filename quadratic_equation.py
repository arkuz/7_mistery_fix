from math import sqrt


def calc_root1(a, b, discriminant):
    root = (-b - sqrt(discriminant)) / (2 * a)
    return root


def calc_root2(a, b, discriminant):
    root = (-b + sqrt(discriminant)) / (2 * a)
    return root


def get_roots(a, b, c):

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None, None

    elif discriminant == 0:
        root1 = calc_root1(a, b, discriminant)
        return root1, None

    else:
        root1 = calc_root1(a, b, discriminant)
        root2 = calc_root2(a, b, discriminant)
        return root1, root2
