"""
What is class?
Think it as a way of creating an object.

Why class?
If you create a big project in C you will know that managing many functions and data structure is very hard
and confusing. And that's where class come in by categorizing the func and data to a set of data that can
be easier to develop, debug, and manage.

For this revision lets try to create a class of 2D shapes.
"""
# Square
# Properties:
# - Size
#   + Side
class Square:  # Define a class named Square
    # Telling what does this class info contain.
    def __init__(self, side):
        # Use the parameter to turn it into a data called self.side which can be accessed in the class itself
        self.side = side
# Lets try to use this class
square1 = Square(2)
square2 = Square(4)
print(f"sq1 = side:{square1.side}")
print(f"sq2 = side:{square2.side}")
# What if we don't use class?
square1_side = 2
square2_side = 4
print(f"sq1 = side:{square1_side}")
print(f"sq2 = side:{square2_side}")

# The same?
# That's the case because our class have only one properties
# But what if the class more than 1 properties?
# Lets try that again with a Box
# Box
# Properties:
# - size
#   + width
#   + length
#   + height
# - weight
# - color
# - Status of the box (Opened or closed)
class Box: #define a class named box
    # Telling what does this class info contain.
    def __init__(self, width, length, height, weight, color, box_opened):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.box_opened = box_opened
box1 = Box(2,3,4,2,"Black",False)
box2 = Box(4,3,2,4,"White",True)
print(f"box1 = size:{box1.width}x{box1.length}x{box1.height} Weight:{box1.weight} kg Color:{box1.color}")
print("Box closed") if not box1.box_opened else print("Box opened")
print(f"box2 = size:{box2.width}x{box2.length}x{box2.height} Weight:{box2.weight} kg Color:{box2.color}")
print("Box closed") if not box2.box_opened else print("Box opened")

# Now if you write it without class?
#Let's try with box1 and box2
box1_width = 2
box1_length = 3
box1_height = 4
box1_weight = 2
box1_color = "Black"
box1_box_opened = False
box2_width = 4
box2_length = 3
box2_height = 2
box2_weight = 4
box2_color = "Black"
box2_box_opened = True

# If we compare between Class and Non-class
# Class 45-55 = 10 line
# Non-class 63-74 = 11 line
# If you add more object
# Class += 1 (Use only one line to declare all data)
# Non-class += 6 (You need to declare 6 variable)

"""
Exercise1:
Write Car class that contains the following properties
Assign to 2 different Car object
And display both object using the display format example as a guideline
Properties:
1. Owner
2. Brand
3. Color
4. License plate ID
5. Year
Display format example:
Owner:Kris Brand:BMW Color:Black ID:PYQT5 Year:2012
Owner:Jack Brand:Nissan Color:White ID:COVID-19 Year:2019
"""

"""
Now you've understand how initializing and why class are made and what is it good for.
Let's continue with the next part
The class we created can only store data but it can't use any of its data yet.
Lets upgrade our Square class
"""
class Square:  # Define a class named Square
    # Telling what does this class info contain.
    def __init__(self, side):
        self.side = side
    def get_area(self): # A func in class are called Method
        # What is self.?
        # Did see what u defined in the init?
        # That's the value that this func use.
        return self.side**2
    def change_side(self, side):
        # Why self.__init__ when your __init__ is also an func
        # Please memorize that if u r going to use a func in class within the same class
        # U must use self.(Func name) to use that specific(func)
        self.__init__(side)
    def dis_all_info(self):
        print(f"This sq-> Side:{self.side} Area:{self.get_area()}")

sq = Square(3)
print(sq.get_area())
sq.dis_all_info()
sq.change_side(4)
print(sq.get_area())
sq.dis_all_info()

"""
Exercise2:
Write a Box class which contain these properties and methods
Properties:
1. size (Ex.[w,l,h])
2. weight
3. color 
4. box_lock
5. things (Ex.[Watch, Pen, Dog, Wifi router])
Methods:
1. disp_info_box -> a method that will show the box info as follows
Ex. Box: 
Size: w x l x h 
Weight: (weight) kg
Color: (Color)
2. open -> a method that will unlock the lock
3. lock -> a method that will lock the lock
4. add_item -> Add an item to your box
5. rem_item -> Remove an item to your box
6. disp_item -> check first if the lock is still on then display a message that the box is locked
if the box doesn't lock then display all item in the box
"""
