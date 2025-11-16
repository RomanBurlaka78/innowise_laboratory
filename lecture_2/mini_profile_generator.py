from datetime import datetime

user_name = input("Enter your full name?: ")
birth_year_str = input("Enter your birth year?: ")
birth_year = int(birth_year_str)
current_age = datetime.now().year - birth_year
hobbies = list()

while (True):
    hobby = input("Enter a favorite hobby: or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)

def generate_profile(age: int):
    if 0 <= age <= 12:
        life_stage = "Child"
    elif 13 <= age <= 19:
        life_stage = "Teenager"
    elif age >= 20:
        life_stage = "Adult"

    return life_stage


generate_profile(current_age)

user_profile = {
    "Name": user_name,
    "Age": current_age,
    "Life Stage": generate_profile(current_age),
    "Favorite Hobbies": hobbies

}
print("------------------------")
print("Profile Summary :")
print(f"Name:  {user_profile['Name']}")
print(f"Age: {user_profile['Age']}")
print(f"Life stage: {user_profile['Life Stage']}")

if len(hobbies) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies({len(hobbies)}): ")
    for key, value in user_profile.items():
        if key == "Favorite Hobbies":
            for hobby in value:
                print(f"- {hobby}")
print("------------------------")
