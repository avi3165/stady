#q1
# def jump_rope():
#     print("1...2...3...jump!")
# jump_rope()
#q2
# def wake_up():
#     print("get out from bed")
# def eat_breakfast():
#     print("eat breakfast")
# def go_to_school():
#     print("live home")
# wake_up()
# eat_breakfast()
# go_to_school()
#q3
# mission_complete=False
# def drive():
#     print("The paramedic drive in ambulance to save somebody")
# def save_people():
#     print("The paramedic is saving someone")
#     global mission_complete
#     mission_complete=True
# def return_to_base():
#     print("The paramedic return to base")
# drive()
# save_people()
# return_to_base()
# if mission_complete==True:
#     print("The mission was successful")
# else:
#     print("The mission failed")
#q4
coffee_ready=False
def boil_water():
    print("Boiling water on the gas.")
def brew_coffee():
    print("Making coffee")
def add_sugar():
    print("Adding sugar")
def serve_coffee():
    print("Serving coffee")
    global coffee_ready
    coffee_ready=True
boil_water()
brew_coffee()
add_sugar()
serve_coffee()
if coffee_ready==True:
    print("The coffee is ready!!!")
elif coffee_ready==False:
    print("Something went wrong with the coffee.")
