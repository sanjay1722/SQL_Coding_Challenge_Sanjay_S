'''3. Write Python Program to do the following :
1. Display Area of
Circle
Parallelogram'''

radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14 * radius ** 2  
print(f"Area of the circle: {area_circle:.2f}")

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
area_parallelogram = base * height  
print(f"Area of the parallelogram: {area_parallelogram:.2f}")