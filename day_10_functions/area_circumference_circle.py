import math


def area(radius):
    return math.pi * pow(radius, 2)


def circumference(radius):
    return 2 * math.pi * radius


if __name__ == "__main__":
    input_radius = int(
        input("Enter the radius of circle to find its area and circumference : ")
    )

    print(
        f"Area is : {area(input_radius)} and Circumference is : {circumference(input_radius)}"
    )
