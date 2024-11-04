#START question1

user1_first_name: str = str(input("Enter first name for user 1: "))
user1_last_name: str = str(input("Enter last name for user 1: "))
user1_height: float = float(input("Enter height for user 1: "))
user1_year_of_birth: int = int(input("Enter year of birth for user 1: "))

user2_first_name: str = str(input("Enter first name for user 2: "))
user2_last_name: str = str(input("Enter last name for user 2: "))
user2_height: float = float(input("Enter height for user 2: "))
user2_year_of_birth: int = int(input("Enter year of birth for user 2: "))

user3_first_name: str = str(input("Enter first name for user 3: "))
user3_last_name: str = str(input("Enter last name for user 3: "))
user3_height: float = float(input("Enter height for user 3: "))
user3_year_of_birth: int = int(input("Enter year of birth for user 3: "))

print(f"#id 1 = name: {user1_last_name:<12}, {user1_first_name:<10} height: {user1_height:<5f} year-of-birth: {user1_year_of_birth:<4}")
print(f"#id 2 = name: {user2_last_name:<12}, {user2_first_name:<10} height: {user2_height:<5f} year-of-birth: {user2_year_of_birth:<4}")
print(f"#id 3 = name: {user3_last_name:<12}, {user3_first_name:<10} height: {user3_height:<5f} year-of-birth: {user3_year_of_birth:<4}")

#END

#START question2

grade: int = int(input("Enter your grade: "))

if 0 <= grade <= 40:
    print("try harder next time...")
if 41 <= grade <= 60:
    print("you're getting there, need some more work")
if 61 <= grade <= 80:
    print("good pretty")
if 81 <= grade <= 95:
    print("awesome!")
if 96 <= grade <= 100:
    print("excellent!!! You're a Star!")
if grade < 0 or grade > 100:
    print("grade illegal")

#END

# START question3

volume: int = int(input("Enter volume level (0-9): "))

match volume:
    case 0:
        print("mute")
    case 1 :
        print("very quiet")
    case 2 :
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9:
        print("extremely loud")
    case _:
        print("Invalid volume level")

# END