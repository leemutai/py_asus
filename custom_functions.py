def say_my_name():
    print("Hey, I am June")


def say_my_name(name):
    print("Hey, My name is" + name)


def calculate_volume_cylinder(radius, height):
    vol = 22 / 7 * radius ** 2 * height
    print(vol)


calculate_volume_cylinder(7, 16)
calculate_volume_cylinder(17, 54)
calculate_volume_cylinder(87, 345.22)


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    return total

#
# v1 = calculate_volume_cylinder(10, 18)
#
# print(round(v1))
# print(v1 * 5)

add_numbers(10, 20)
# add_numbers(10.55, 65.1, 32.22, 11, 25, 71,)
# say_my_name("June)
# say_my_name("Walid)
# say_my_name("Job)
