print("Welcome to Bhavith's Kinematic Equations Solver!")
print("First Kinematic Equation: vF = v0 + at")
print("Second Kinematic Equation: xF = x0 + v0t + 2at^2")
print("Third Kinematic Equation: vF^2 = v0^2 + 2a(xF-x0)")
user_input = input("What Kinematic Equation do you want to use?: (1st, 2nd, 3rd) ")
if user_input == "1st":
    print("The First Kinematic Equation is vF = v0 + at")
    print("You can use this equation to solve for final velocity (vF), initial velocity (v0), time (t), or acceleration (a).")
    first_kinematic_input = input("Which value are you solving for? (vF, v0, a, t): ")
    if first_kinematic_input == "vF":
        print("Please provide the numerical values for these variables: ")
        first_v0 = float(input("v0 (initial velocity)= "))
        first_a = float(input("a (acceleration)= "))
        first_t = float(input("t (time in seconds)= "))
        first_vF = first_v0 + first_a * first_t
        print(f"Answer: vF = {first_vF} m/s\n"
        f"Explanation: Using vF = v0 + a*t, multiply acceleration {first_a} by time {first_t} and add the initial velocity {first_v0}. "
        f"vF = {first_v0} + {first_a} * {first_t} = {first_vF} m/s.")
        print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
    if first_kinematic_input == "v0":
        print("Please provide the numerical values for these variables: ")
        first_vF = float(input("vF (final velocity) = "))
        first_a = float(input("a (acceleration) = "))
        first_t = float(input("t (time in seconds) = "))
        first_v0 = first_vF - first_a * first_t
        print(f"Answer: v0 = {first_v0} m/s\n"
        f"Explanation: Starting from vF = v0 + a*t, subtract a*t from both sides to isolate v0: v0 = vF - a*t. "
        f"Substitute the values: vF = {first_vF}, a = {first_a}, t = {first_t}. "
        f"After calculating: v0 = {first_vF} - {first_a} * {first_t} = {first_v0} m/s.")
        print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
    if first_kinematic_input == "a":
        print("Please provide the numerical values for these variables: ")
        first_vF = float(input("vF (final velocity) = "))
        first_v0 = float(input("v0 (initial velocity)= "))
        first_t = float(input("t (time in seconds) = "))
        first_a = (first_vF - first_v0) / first_t
        print(f"Answer: a = {first_a} m/s²\n"
        f"Explanation: Starting from vF = v0 + a*t, we subtract v0 from both sides to get vF - v0 = a*t. "
        f"Then divide both sides by t, so a = (vF - v0)/t. "
        f"Substituting the values: vF = {first_vF}, v0 = {first_v0}, t = {first_t}. "
        f"After calculating, we get a = ({first_vF} - {first_v0}) / {first_t} = {first_a} m/s².")
        print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")        
    if first_kinematic_input == "t":
        print("Please provide the numerical values for these variables: ")
        first_vF = float(input("vF (final velocity) = "))
        first_v0 = float(input("v0 (initial velocity) = "))
        first_a = float(input("a (acceleration) = "))
        first_t = (first_vF - first_v0)/ first_a
        print(f"Answer: t = {first_t} s\n"
        f"Explanation: Starting from vF = v0 + a*t, subtract v0 from both sides: vF - v0 = a*t. "
        f"Divide both sides by a to isolate t: t = (vF - v0)/a. "
        f"Substitute values: vF = {first_vF}, v0 = {first_v0}, a = {first_a}. "
        f"After calculating: t = ({first_vF} - {first_v0}) / {first_a} = {first_t} s.")
        print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")