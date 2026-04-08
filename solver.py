import math
import cmath

print("Welcome to Bhavith the Physics Tutor AI!")
choice = input("Would you like to solve Kinematic Equations, or do you want to know which Kinematic Equation to use?: (1 or 2) ")
if choice == "1":
    print("Welcome to Bhavith's Kinematic Equations Solver!")
    print("First Kinematic Equation: vF = v0 + at")
    print("Second Kinematic Equation: xF = x0 + v0t + 1/2at^2")
    print("Third Kinematic Equation: vF^2 = v0^2 + 2a(xF-x0)")
    user_input = input("What Kinematic Equation do you want to use?: (1st, 2nd, 3rd) ")
    if user_input == "1st" or user_input == "1":
        print("The First Kinematic Equation is vF = v0 + at")
        print("You can use this equation to solve for final velocity (vF), initial velocity (v0), time (t), or acceleration (a).")
        first_kinematic_input = input("Which value are you solving for? (vF, v0, a, t): ")
        if first_kinematic_input == "vF" or first_kinematic_input == "vf":
            print("Please provide the numerical values for these variables: ")
            first_v0 = float(input("v0 (initial velocity)= "))
            first_a = float(input("a (acceleration)= "))
            first_t = float(input("t (time in seconds)= "))
            first_vF = first_v0 + first_a * first_t
            print(f"Answer: vF = {first_vF} m/s\n"
            f"Explanation: Using vF = v0 + a*t, multiply acceleration {first_a} by time {first_t} and add the initial velocity {first_v0}. "
            f"vF = {first_v0} + {first_a} * {first_t} = {first_vF} m/s.")
            print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
        if first_kinematic_input == "v0" or first_kinematic_input == "vi":
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
    if user_input == "2nd" or user_input == "2":
        print("The Second Kinematic Equation is xF = x0 + v0t + 1/2at^2")
        second_kinematic_input = input("Which value are you solving for? (xF, x0, v0, a, t): ")
        if second_kinematic_input == "xF" or second_kinematic_input == "xf":
            print("Please provide the numerical values for these variables: ")
            second_x0 = float(input("x0 (initial position) = "))
            second_v0 = float(input("v0 (initial velocity) = "))
            second_a = float(input("a (acceleration) = "))
            second_t = float(input("t (time) = "))
            second_xF = second_x0 + (second_v0 + second_t) + 0.5*(second_a*second_t**2)
            print(f"Answer: xF = {second_xF} m\n"
            f"Explanation: We use the second kinematic equation xF = x0 + v0*t + 0.5*a*t^2. "
            f"First, multiply the initial velocity {second_v0} m/s by time {second_t} s to get {second_v0 * second_t}. "
            f"Then calculate the acceleration term: 0.5 * {second_a} * {second_t}^2 = {0.5 * second_a * second_t**2}. "
            f"Finally, add everything together with the initial position {second_x0}: "
            f"xF = {second_x0} + {second_v0 * second_t} + {0.5 * second_a * second_t**2} = {second_xF} m.")
            print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
        if second_kinematic_input == "x0" or second_kinematic_input == "xi":
            print("Please provide the numerical values for these variables: ")
            second_xF = float(input("xF (final position / displacement) = "))
            second_v0 = float(input("v0 (initial velocity) = "))
            second_a = float(input("a (acceleration) = "))
            second_t = float(input("t (time) = "))
            second_x0 = second_xF - second_v0 * second_t - 0.5(second_a * second_t**2)
            print(f"Answer: x0 = {second_x0} m\n"
            f"Explanation: We start with the second kinematic equation xF = x0 + v0*t + 0.5*a*t^2. "
            f"To solve for x0, we move the other terms to the other side by subtracting them: "
            f"x0 = xF - v0*t - 0.5*a*t^2. "
            f"Now substitute the values: xF = {second_xF}, v0 = {second_v0}, t = {second_t}, a = {second_a}. "
            f"Calculate each term: v0*t = {second_v0 * second_t}, and 0.5*a*t^2 = {0.5 * second_a * second_t**2}. "
            f"Finally, subtract both from xF: x0 = {second_xF} - {second_v0 * second_t} - {0.5 * second_a * second_t**2} = {second_x0} m.")
            print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
        if second_kinematic_input == "v0" or second_kinematic_input == "vi":
            print("Please provide the numerical values for these variables: ")
            second_xF = float(input("xF (final position / displacement) = "))
            second_x0 = float(input("x0 (initial position) = "))        
            second_a = float(input("a (acceleration) = "))
            second_t = float(input("t (time) = "))
            second_v0 = (second_xF - second_x0 - 0.5 * second_a * second_t **2) / second_t
            print(f"Answer: v0 = {second_v0} m/s\n"
            f"Explanation: We start with the second kinematic equation xF = x0 + v0*t + 0.5*a*t^2. "
            f"To solve for v0, we first subtract x0 from both sides: xF - x0 = v0*t + 0.5*a*t^2. "
            f"Then subtract the acceleration term: xF - x0 - 0.5*a*t^2 = v0*t. "
            f"Finally, divide both sides by t to isolate v0: v0 = (xF - x0 - 0.5*a*t^2) / t. "
            f"Substitute the values: xF = {second_xF}, x0 = {second_x0}, a = {second_a}, t = {second_t}. "
            f"Calculate step by step: v0 = ({second_xF} - {second_x0} - {0.5 * second_a * second_t**2}) / {second_t} = {second_v0} m/s.")
            print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")        
        if second_kinematic_input == "a":
            second_xF = float(input("xF (final position / displacement) = "))
            second_x0 = float(input("x0 (initial position) = "))               
            second_v0 = float(input("v0 (initial velocity) = "))
            second_t = float(input("t (time) = "))
            second_a = 2*((second_xF - second_x0) - (second_v0 * second_t)) / second_t **2 
            print(f"Answer: a = {second_a} m/s²\n"
            f"Explanation: We start with the second kinematic equation xF = x0 + v0*t + 0.5*a*t^2. "
            f"To solve for a, we first subtract x0 and v0*t from both sides: xF - x0 - v0*t = 0.5*a*t^2. "
            f"Then we divide both sides by 0.5*t^2. Dividing by 0.5 is the same as multiplying by 2, so we get: "
            f"a = 2 * (xF - x0 - v0*t) / t^2. "
            f"Now substitute the values: xF = {second_xF}, x0 = {second_x0}, v0 = {second_v0}, t = {second_t}. "
            f"Calculate step by step: a = 2 * ({second_xF} - {second_x0} - {second_v0 * second_t}) / {second_t**2} = {second_a} m/s².") 
            print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)") 
        if second_kinematic_input == "t":
            second_xF = float(input("xF (final position / displacement) = "))
            second_x0 = float(input("x0 (initial position) = "))               
            second_v0 = float(input("v0 (initial velocity) = "))
            second_a = float(input("a (acceleration) = "))
            second_t = (0-second_v0 + math.sqrt((second_v0 **2 + (2 * second_a) * (second_xF - second_x0)))) / second_a
            second_t2 = (0-second_v0 - math.sqrt((second_v0 **2 + (2 * second_a) * (second_xF - second_x0)))) / second_a
            if second_t > 0:
                print(f"Answer: t = {second_t} s\n"
                f"Explanation: We start with the third kinematic equation: vF^2 = v0^2 + 2a(xF - x0). "
                f"However, to solve for time, we instead use the second equation in quadratic form: "
                f"xF = x0 + v0*t + 0.5*a*t^2.\n\n"         
                f"Step 1: Move all terms to one side to form a quadratic equation:\n"
                f"0 = 0.5*a*t^2 + v0*t + (x0 - xF)\n\n"       
                f"Step 2: Identify the coefficients:\n"
                f"a = 0.5*{second_a}, b = {second_v0}, c = {second_x0 - second_xF}\n\n"       
                f"Step 3: Use the quadratic formula:\n"
                f"t = (-b ± sqrt(b^2 - 4ac)) / (2a)\n\n"    
                f"Step 4: Substitute the values:\n"
                f"t = (-{second_v0} ± sqrt({second_v0}^2 + 2*{second_a}*({second_xF} - {second_x0}))) / {second_a}\n\n" 
                f"This gives two possible solutions. The first solution is t = {second_t}s, which is positive, but the second solution is t = {second_t2}s so we accept the first one as the physically meaningful time, because time cannot be negative. Negative time doesn't make sense right?")
                print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
            elif second_t2 > 0:
                print(f"Answer: t = {second_t2} s\n"
                f"Explanation: Solving the quadratic equation gives two solutions because motion equations "
                f"can mathematically describe motion forward and backward in time.\n\n"
                f"The first solution was not valid, so we check the second one:\n"
                f"t = {second_t2}\n\n"
                f"Since this value is positive, it represents a valid physical time, so we accept it.")
                print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
            else:
                print(f"No valid solution.\n"
                f"Explanation: After solving the quadratic equation, both values of time were negative or invalid. "
                f"In physics, time cannot be negative in this context, so the given values do not represent a realistic motion.")
                print("Does this make sense? If you need extra help in Physics, please feel free to have a chat with Bhavith or Mr. Smith. We would be glad to help you! :)")
    if user_input == "3rd" or user_input == "3":
        print("The Thrid Kinematic Equation (Timeless Equation) is vF^2 = v0^2 + 2a(xF-x0)")
        print("You can use this equation to solve for final velocity (vF), initial velocity (v0), displacement (xF), initial position(x0), or acceleration (a).")
        third_kinematic_input = input("Which value are you solving for? (vF, v0, a, xF, x0, dx): ")

    if third_kinematic_input == "vF" or third_kinematic_input == "vf":
        print("Please provide the numerical values for these variables: ")
        third_v0 = float(input("v0 (initial velocity) = "))
        third_a = float(input("a (acceleration) = "))
        third_xF = float(input("xF (final position) = "))
        third_x0 = float(input("x0 (initial position) = "))
        third_vF = math.sqrt(third_v0**2 + 2 * third_a * (third_xF - third_x0))

        print(f"Answer: vF = {third_vF} m/s\n"
        f"Explanation: We use the third kinematic equation vF^2 = v0^2 + 2a(xF - x0). "
        f"First, calculate the displacement: xF - x0 = {third_xF} - {third_x0} = {third_xF - third_x0}. "
        f"Then multiply by 2a: 2 * {third_a} * {third_xF - third_x0} = {2 * third_a * (third_xF - third_x0)}. "
        f"Next, add v0^2: {third_v0}^2 = {third_v0**2}. "
        f"So vF^2 = {third_v0**2} + {2 * third_a * (third_xF - third_x0)} = {third_v0**2 + 2 * third_a * (third_xF - third_x0)}. "
        f"Finally, take the square root to solve for vF: vF = {third_vF} m/s.")

    elif third_kinematic_input == "v0" or third_kinematic_input == "vi":
        print("Please provide the numerical values for these variables: ")
        third_vF = float(input("vF (final velocity) = "))
        third_a = float(input("a (acceleration) = "))
        third_xF = float(input("xF (final position) = "))
        third_x0 = float(input("x0 (initial position) = "))
        third_v0 = math.sqrt(third_vF**2 - 2 * third_a * (third_xF - third_x0))

        print(f"Answer: v0 = {third_v0} m/s\n"
        f"Explanation: Starting from vF^2 = v0^2 + 2a(xF - x0), subtract 2a(xF - x0) from both sides: "
        f"v0^2 = vF^2 - 2a(xF - x0). "
        f"Substitute values: vF = {third_vF}, a = {third_a}, xF = {third_xF}, x0 = {third_x0}. "
        f"Compute: v0^2 = {third_vF**2} - {2 * third_a * (third_xF - third_x0)} = {third_vF**2 - 2 * third_a * (third_xF - third_x0)}. "
        f"Finally, take the square root: v0 = {third_v0} m/s.")

    elif third_kinematic_input == "a":
        print("Please provide the numerical values for these variables: ")
        third_vF = float(input("vF (final velocity) = "))
        third_v0 = float(input("v0 (initial velocity) = "))
        third_xF = float(input("xF (final position) = "))
        third_x0 = float(input("x0 (initial position) = "))
        third_a = (third_vF**2 - third_v0**2) / (2 * (third_xF - third_x0))

        print(f"Answer: a = {third_a} m/s²\n"
        f"Explanation: Starting from vF^2 = v0^2 + 2a(xF - x0), subtract v0^2 from both sides: "
        f"vF^2 - v0^2 = 2a(xF - x0). "
        f"Then divide both sides by 2(xF - x0): a = (vF^2 - v0^2) / (2(xF - x0)). "
        f"Substitute values: vF = {third_vF}, v0 = {third_v0}, xF = {third_xF}, x0 = {third_x0}. "
        f"Compute: a = ({third_vF**2} - {third_v0**2}) / (2 * {third_xF - third_x0}) = {third_a} m/s².")

    elif third_kinematic_input == "dx":
        print("Please provide the numerical values for these variables: ")
        third_vF = float(input("vF (final velocity) = "))
        third_v0 = float(input("v0 (initial velocity) = "))
        third_a = float(input("a (acceleration) = "))
        third_dx = (third_vF**2 - third_v0**2) / (2 * third_a)

        print(f"Answer: displacement (xF - x0) = {third_dx} m\n"
        f"Explanation: Starting from vF^2 = v0^2 + 2a(xF - x0), subtract v0^2 from both sides: "
        f"vF^2 - v0^2 = 2a(xF - x0). "
        f"Then divide both sides by 2a: (xF - x0) = (vF^2 - v0^2) / (2a). "
        f"Substitute values: vF = {third_vF}, v0 = {third_v0}, a = {third_a}. "
        f"Compute: ({third_vF**2} - {third_v0**2}) / (2 * {third_a}) = {third_dx} m.")

    elif third_kinematic_input == "xF" or third_kinematic_input == "xf":
        print("Please provide the numerical values for these variables: ")
        third_vF = float(input("vF (final velocity) = "))
        third_v0 = float(input("v0 (initial velocity) = "))
        third_a = float(input("a (acceleration) = "))
        third_x0 = float(input("x0 (initial position) = "))
        third_xF = ((third_vF**2 - third_v0**2) / (2 * third_a)) + third_x0

        print(f"Answer: xF = {third_xF} m\n"
        f"Explanation: Starting from vF^2 = v0^2 + 2a(xF - x0), subtract v0^2: "
        f"vF^2 - v0^2 = 2a(xF - x0). "
        f"Divide by 2a: (xF - x0) = (vF^2 - v0^2) / (2a). "
        f"Then add x0 to both sides: xF = (vF^2 - v0^2)/(2a) + x0. "
        f"Substitute values: xF = ({third_vF**2} - {third_v0**2})/(2 * {third_a}) + {third_x0} = {third_xF} m.")

    elif third_kinematic_input == "x0" or third_kinematic_input == "xi":
        print("Please provide the numerical values for these variables: ")
        third_vF = float(input("vF (final velocity) = "))
        third_v0 = float(input("v0 (initial velocity) = "))
        third_a = float(input("a (acceleration) = "))
        third_xF = float(input("xF (final position) = "))
        third_x0 = third_xF - ((third_vF**2 - third_v0**2) / (2 * third_a))

        print(f"Answer: x0 = {third_x0} m\n"
        f"Explanation: Starting from vF^2 = v0^2 + 2a(xF - x0), subtract v0^2: "
        f"vF^2 - v0^2 = 2a(xF - x0). "
        f"Divide by 2a: (xF - x0) = (vF^2 - v0^2)/(2a). "
        f"Then subtract this from xF to isolate x0: "
        "x0 = xF - (vF^2 - v0^2)/(2a). "
        f"Substitute values: x0 = {third_xF} - ({third_vF**2} - {third_v0**2})/(2 * {third_a}) = {third_x0} m.")
        
if choice == "2":
    print("Under Construction")        