print("Welcome to Bhavith's Kinematic Equations Solver!")
print("First Kinematic Equation: vF = v0 + at")
print("Second Kinematic Equation: xF = x0 + v0t + 2at^2")
print("Third Kinematic Equation: vF^2 = v0^2 + 2a(xF-x0)")
user_input = input("What Kinematic Equation do you want to use?: (1st, 2nd, 3rd) ")
if user_input == "1st":
    print("The First Kinematic Equation is vF = v0 + at")
    print("You can use this equation to solve for final velocity (vF), initial velocity (v0), time (t), or acceleration (a).")
    first_kinematic_input = print("Which value are you solving for? (vF, v0, a, t): ")
    if first_kinematic_input == "vF":
        print("Please provide the numerical values for these variables: ")
        first_v0 = input("v0 (initial velocity)= ")
        first_a = input("a (acceleration)= ")
        first_t = input("t (time)= ")
        