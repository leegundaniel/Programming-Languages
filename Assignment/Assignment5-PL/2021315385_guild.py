### guild.py
### entry point for program

import random
import datetime
import hashlib
import json
import os

# create or load json files
def load(json_file):
    # Create the file if it does not exist
    if not os.path.isfile(json_file):
        with open(json_file, 'w') as file:
            json.dump({}, file, indent = 4)
    # attempt to load the file
    try:
        # load file
        with open(json_file, 'r') as file:
            return json.load(file)
    # handle json decode error
    except json.JSONDecodeError:
        # overwrite file with empty json object
        with open(json_file, 'w') as file:
            json.dump({}, file, indent = 4)
        return {}

# save data to json files
def save(json_file, data):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent = 4)

# Rank class
class Rank:
    def __init__(self, exp):
        self.exp = exp

    # overloading ">=" operator for checking rank up
    def __ge__(self, other):
        return self.exp >= other
    
    # overloading string
    def __str__(self):
        if self.exp >= 500:
            return "DIAMOND"
        elif self.exp >= 300:
            return "PLATINUM"
        elif self.exp >= 150:
            return "GOLD"
        elif self.exp >= 50:
            return "SILVER"
        return "BRONZE"
    
# Inventory class for loots
class Inventory:
    def __init__(self, items):
        # items is a dictionary
        self.items = items

    # overload + operator to merge loot
    def __add__(self, loot):
        # copy the inventory to create a new dictionary
        # used for merging then returning
        inventory = self.items.copy()
        # for every loot received, add its value to the existing inventory
        for key, value in loot.items():
            # if value exists, get it, if not, use 0
            # add the new loot's value and add to dictionary
            inventory[key] = inventory.get(key, 0) + value
        return inventory


# class to define train and resting
# overloading the addition and subtraction operator
class Train:
    # addition will be used for stamina addition (rest)
    def __add__(self, minutes):
        stamina_gain = 0
        # stamina will increase by 5 every 30 minutes
        while minutes > 0:
            stamina_gain += 5
            minutes -= 30
        return stamina_gain
    
    # subtraction will be used for stamina subtraction (train)
    # first 30 minutes = 5
    # every 30 minutes afterwards loses 2 additional stamina
    def __sub__(self, minutes):
        stamina_cost = 5
        # stamina will decrease by 2 every other 30 minutes
        minutes -= 30
        while minutes > 0:
            stamina_cost += 2
            minutes -= 30
        return stamina_cost

# check if a username already exists in the user database
def is_username_taken(username):
    return username in users

# check password
def password_check(password):
    # password must be at least 8 characters
    if len(password) < 8:
        return False
    # password must contain an uppercase letter
    if not any(c.isupper() for c in password):
        return False
    # password must contain a special character
    if not any(c in "!@#$%^&*()" for c in password):
        return False
    # else, return true
    return True

# hashing password / pin
def hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

# generate a random unique 5 digit user ID
def generate_unique_id():
    # to ensure uniqueness, gather existing IDs
    existing_ids = {users[username]["id"] for username in users}
    # while loop to find a unique ID
    while True:
        # generate random 5 digit ID
        user_id = random.randint(10000, 99999)
        # check if ID is unique
        if user_id not in existing_ids:
            # if it is, return it
            return user_id

# create a user profile
def user_profile(username, password, pin):
    # create user profile dictionary
    return {
        username: {
            # generate id
            "id": generate_unique_id(),
            # hash password and pin
            "pwd": hash(password),
            "pin": hash(pin),
            "rank": "BRONZE",
            "exp": 0,
            "fame": 0,
            "stamina": 100,
            "skills": {
                "hunting": 5,
                "herbology": 5,
                "sword": 5,
                "alchemy": 5,
                "craft": 5
            },
            "inventory": {},
            "accepted": [],
            "completed": [],
            "history": []
        }
    }

# registration process
def registration():
    # while loop for receiving all inputs
    while True:
        print("\n--- Register ---")
        # get username
        username = input("Username (0 to cancel): ").strip()
        # if user inputs '0', cancel registration
        if username == '0':
            print("Registration cancelled.\n")
            return
         # if username is blank or taken, restart loop
        if not username:
            print("Username cannot be blank.")
            continue
        if is_username_taken(username):
            print("Username already taken. Please choose another.")
            continue

        # get password
        password = input("Password (>=8, 1 uppercase, 1 special) (0 to cancel): ").strip()
        # if user inputs '0', cancel registration
        if password == '0':
            print("Registration cancelled.\n")
            return
        # check password validity
        if not password_check(password):
            print("Password must be at least 8 characters, contain an uppercase letter, and a special character.")
            continue
        
        # get 4-digit pin
        pin = input("4-digit PIN (0 to cancel): ").strip()
        # if user inputs '0', cancel registration
        if pin == '0':
            print("Registration cancelled.\n")
            return
        # check pin validity
        if not (pin.isdigit() and len(pin) == 4):
            print("PIN must be exactly 4 digits.")
            continue

        # if all inputs are valid, create user profile
        user = user_profile(username, password, pin)
        # update users dictionary
        users.update(user)
        # save users to json file
        save('adventurers.json', users)
        
        # registration successful, break loop
        print(f"Registration successful! Welcome, {username}. Your Adventurer ID is {users[username]['id']}.\n")
        break

# login
def login():
    # while loop for login attempts
    while True: 
        print("\n--- Login ---")
        # get username and password
        username = input("Username (0 to cancel): ").strip()

        # if user inputs '0', cancel login
        if username == '0':
            print("Login cancelled.\n")
            return None

        password = input("Password: ").strip()

        # validate credentials
        if username not in users:
            print("Username not found. Please try again.")
            continue

        if users[username]['pwd'] != hash(password):
            print("Incorrect password. Please try again.")
            continue
        
        # login successful
        print(f"Login successful! Welcome back, {username}.\n")
        return username

# log history
# using kwargs to allow flexible additional details
def log_history(username, action_type="", **kwargs):
    # prepare history entry
    entry = {
        "type": action_type,
        "date": datetime.datetime.now().isoformat()
    }

    for bad_binding in ['type', 'date']:
        if bad_binding in kwargs:
            print(f"Binding error: '{bad_binding}' is a reserved key and cannot be used in history logging.")
            return

    # update entry with kwarg values
    entry.update(kwargs)
    users[username]['history'].append(entry)


# view history
def history(username):
    # get user profile
    profile = users[username]
    print("\n--- History (latest first) ---")
    # iterate through history list in reverse order
    for quest in reversed(profile['history']):
        # display based on action type
        if quest["type"] == "Train":
            print(f"[{quest['date']}] {quest['type']}\t{quest['skill']} +{quest['exp']} ({quest['time']})")
        elif quest["type"] == "Submit":
            print(f"[{quest['date']}] {quest['type']}\t{quest['quest_id']} EXP:{quest['exp']} Fame:{quest['fame']} Loot:{quest['loot']}")
        elif quest["type"] == "Accept":
            print(f"[{quest['date']}] {quest['type']}\t{quest['quest_id']} difficulty={quest['difficulty']} priority={quest['priority']}")
        elif quest["type"] == "Rest":
            print(f"[{quest['date']}] {quest['type']}\tStamina: +{quest['stamina']} ({quest['time']})")

# accept quest
def accept_quest(username):
    profile = users[username]
    print("\n=== Quest Board ===")
    # display available quests
    for quest_id, quest in quests.items():
        require = quest['require']
        print(f"- {quest_id}:\t'{quest['title']}'    Difficulty: {quest['difficulty']}   Req: {require['skill']}>={require['level']} Due: {quest['due_date']}")
    # get quest id to accept
    qid = input("Enter Quest ID to accept (0 to cancel): ").strip()
    # if user inputs '0', cancel
    if qid == '0':
        print("Quest acceptance cancelled.\n")
        return
    # check if quest id is valid
    if qid not in quests:
        print("Invalid Quest ID. Please try again.")
        return
    # check if anyone has already accepted the quest
    quest = quests[qid]
    if quest['accepted'] is not None:
        print("This quest has already been accepted by another adventurer.")
        return
    
    # get pin for verification
    pin = input("Enter your 4-digit PIN for verification: ").strip()
    if profile['pin'] != hash(pin):
        print("Incorrect PIN. Quest acceptance cancelled.")
        return
    
    req = quest['require']
    user_skill = profile['skills'].get(req['skill'], 0)
    # check if user meets skill requirement
    if user_skill < req['level']:
        print(f"You do not meet the skill requirement for this quest. Required: {req['skill']} >= {req['level']}, Your level: {user_skill}.")
        return
    
    # check if due date has not passed
    due_date = datetime.datetime.strptime(quest['due_date'], "%Y-%m-%d").date()
    if due_date < datetime.date.today():
        print("The due date for this quest has already passed.")
        return
    
    # receive priority input, default NORMAL
    priority = input("Priority (NORMAL / HIGH) [default: NORMAL]: ").strip().upper()
    if priority not in ['NORMAL', 'HIGH']:
        priority = 'NORMAL'
    
    # accept quest
    quest['accepted'] = username

    users[username]['accepted'].append(qid)
    # for history tracking
    log_history(username, action_type="Accept", quest_id=qid, difficulty=quest['difficulty'], priority=priority)

    # save changes to json file
    save('adventurers.json', users)
    save('quests.json', quests)

#  validate proof
def validate_proofs(*proofs, required=None):
    if required is None:
        print("Binding error: There must be a 'required' proof list to validate user's submission")
        return False
    
    # if proofs list is empty
    if not proofs:
        print("Binding error: No proof parameter. Provide at least one proof.")
        return False
    
    # Binding errors: no duplicate proof names allowed
    if len(proofs) != len(set(proofs)):
        print("Binding error: Duplicate proof names detected.")
        return False
    
    # check if all proofs are in req_proofs
    if not all(p in proofs for p in required):
        print("You have not provided all required proof items.")
        return False
    return True

# submit quest
def submit_quest(username):
    profile = users[username]
    # get quest ID input
    qid = input("Quest to submit (0 to cancel): ").strip()
    # if user inputs '0', cancel
    if qid == '0':
        print("Quest submission cancelled.\n")
        return
    # check if quest is accepted by user
    if qid not in profile['accepted']:
        print("You have not accepted this quest.")
        return

    # get pin for verification
    pin = input("Enter your 4-digit PIN for verification: ").strip()
    if users[username]['pin'] != hash(pin):
        print("Incorrect PIN. Quest submission cancelled.")
        return
    
    # ensure due date has not passed
    quest = quests[qid]
    due_date = datetime.datetime.strptime(quest['due_date'], "%Y-%m-%d").date()
    if due_date < datetime.date.today():
        print("The due date for this quest has already passed. You cannot submit it.")
        return
    
    # check for required proofs in inventory
    req_proofs = quest['required_proofs']
    # print required proofs
    print("Provide proof item: ", ", ".join(req_proofs))
    user_proof = []
    # get proof items from user
    while True:
        proof = input("Add proof item (blank to stop): ").strip()
        if proof == "":
            break
        user_proof.append(proof)
    
    # validation using *args
    if not validate_proofs(*user_proof, required=req_proofs):
        return
    
    # check if user has enough stamina to submit quest (10 stamina)
    if profile['stamina'] < 10:
        print("You do not have enough stamina to submit this quest. Minimum 10 stamina required.")
        return
    
    # submit quest
    profile['accepted'].remove(qid)
    # submit dictionary for history logging
    profile['completed'].append(quest)
    profile['stamina'] -= 10
    profile['exp'] += quest['rewards']['exp']
    # use overloaded str() in Rank class to check new rank
    rank = str(Rank(profile['exp']))
    # if rank changed, update rank
    rankChange = False
    if profile['rank'] != rank:
        profile['rank'] = rank
        rankChange = True
    profile['fame'] += quest['rewards']['fame']
    # use Inventory class for the loots
    current_inventory = Inventory(profile['inventory'])
    # add loot to user
    profile['inventory'] = current_inventory + quest['rewards']['loot']

    # for history tracking
    log_history(username, action_type="Submit", quest_id=qid, exp=quest['rewards']['exp'], fame=quest['rewards']['fame'], loot=quest['rewards']['loot'])
    # add quest to quests.json as unaccepted
    quest['accepted'] = None
    # update due date to tomorrow
    quest['due_date'] = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    # save changes to json files
    save('adventurers.json', users)
    save('quests.json', quests)
    print(f"Submit OK. You gained EXP: {quest['rewards']['exp']}, Fame: {quest['rewards']['fame']}, Loot: {quest['rewards']['loot']}")
    # if rank changed, announce it
    if rankChange:
        print(f"Congratulations!!! You have been promoted to the rank {rank}")
# training logic closure
def training():
    # define base experience and diminishing factor
    base_exp = 10
    diminishing_factor = 0.8
    
    def train(username, skill, minutes=30, stamina_cost=5):
        nonlocal base_exp
        exp = 0
        # calculate exp with diminishing returns
        # for every 20 minutes
        for _ in range(minutes // 30):
            exp += base_exp
            base_exp *= diminishing_factor

        # retrieve profile
        profile = users[username]
        # increase skill experience
        profile['skills'][skill] += int(exp)
        # reduce stamina by fixed amount
        profile['stamina'] -= stamina_cost

        # log training in history and update user information in json
        log_history(username, action_type="Train", skill=skill, exp=int(exp), time=f"{minutes}m")
        save('adventurers.json', users)
        
        print(f"Trained {skill} for {minutes} minutes. Gained {int(exp)} EXP.")
    return train
        

# training skill
def train_skill(username):
    # get user profile
    profile = users[username]
    global active

    # get skill to train
    skill = input("Skill to train [e.g., hunting, herbology, sword, alchemy, craft, rest] (0 to cancel): ").strip().lower()
    # if user inputs '0', cancel
    if skill == '0':
        print("Training cancelled.\n")
        return
    
    # check if skill is valid
    if skill not in profile['skills'] and skill != 'rest':
        print("Invalid skill name. Please try again.")
        return
    
    # get training time in minutes
    train_time = input("Minutes [default 30]:").strip()
    # process training time input
    # default to 30 if blank
    if train_time == '':
        train_time = 30
    # if input is digit and greater than 0, convert to int
    elif train_time.isdigit() and int(train_time) > 0:
        train_time = int(train_time)
    # wrong input
    else:
        print("Invalid time input. Minutes must be a number greater than 0.")
        return
    
    # if skill is resting, use the Rest class's + operator
    if skill == 'rest':
        # using Train class to overload the '+' operator
        resting = Train()
        # using overloaded operator to get recovered stamina
        stamina_gain = resting + train_time
        # add stamina back
        profile['stamina'] += stamina_gain
        # log into history and update user information in json
        log_history(username, action_type="Rest", stamina=int(stamina_gain), time=f"{train_time}m")
        save('adventurers.json', users)
        print(f"Rested for {train_time} minutes. Stamina + {int(stamina_gain)}")
        return


    # calculate additional stamina cost (2 stamina for every 30 min)
    # use the Train class to get the cost
    trainer = Train()
    stamina_cost = trainer - train_time

    # check if user has enough stamina
    if profile['stamina'] < stamina_cost:
        print("Not enough stamina. Training requires at least 5 stamina.")
        return
    
    # input pin for verification
    pin = input("Enter your 4-digit PIN for verification: ").strip()
    if profile['pin'] != hash(pin):
        print("Incorrect PIN. Training cancelled.")
        return
    
    # call closure to apply training
    if username not in active:
        # once per user session
        active[username] = training()
    current = active[username]

    # use the closure function with or without defaults
    if train_time == 30:
        current(username, skill)
    else:
        current(username, skill, minutes=train_time, stamina_cost=stamina_cost)
    return

# main menu after login
def main_menu(username):
    # get user profile
    profile = users[username]
    # main menu loop
    while True:
        print("\n=== Main ===")
        # display user info
        print(f"User: {username}\tID: {profile['id']}\tRank: {profile['rank']}\tStamina: {profile['stamina']}")
        print("[1] History\t[2] Accept Quest\t[3] Submit Quest\t[4] Train Skill\t[9] Logout")
        choice = input("Select: ").strip()
        # choice 1: view history
        if choice == '1':
            # display history
            history(username)
        # choice 2: accept quest
        elif choice == '2':
            accept_quest(username)
        # choice 3: submit quest
        elif choice == '3':
            submit_quest(username)
        # choice 4: train skill
        elif choice == '4':
            train_skill(username)
        # choice 9: logout
        elif choice == '9':
            print("Logging out...\n")
            break
        # invalid choice
        else:
            print("Invalid selection. Please try again.")

# main function
def main():
    while True:
        print("=== Adventurer's Guild ===")
        print("[1] Register\t[2] Login\t[0] Exit")
        choice = input("Select: ").strip()
        # choice 1: register
        if choice == '1':
            registration()
        # choice 2: login
        elif choice == '2':
            user = login()
            if user:
                main_menu(user)
        # choice 0: exit program
        elif choice == '0':
            print("Bye!")
            break
        # invalid choice
        else:
            print("Invalid selection. Please try again.\n")


# load or initialize guild data from json file
users = load('adventurers.json')
quests = load('quests.json')

# Global scope for active trainers (to reduce the constant calling of the closure function during training)
active = {}

# if quests data is empty, initialize with default quests
if quests == {}:
    quests = {
        "Q007": {
            "title": "Herb Gathering",
            "difficulty": "EASY",
            "require": {"skill": "herbology", "level": 5},
            "due_date": datetime.date.today().strftime("%Y-%m-%d"),
            "rewards": {"exp": 12, "fame": 1, "loot": {"coin_pouch": 3}},
            "required_proofs": ["herb_bundle"],
            "accepted": None
        },
        "Q027": {
            "title": "Boar Hunting",
            "difficulty": "EASY",
            "require": {"skill": "hunting", "level": 10},
            "due_date": (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
            "rewards": {"exp": 20, "fame": 2, "loot": {"coin_pouch": 5}},
            "required_proofs": ["boar_hide"],
            "accepted": None
        },
        "Q030": {
            "title": "Escort Caravan",
            "difficulty": "HARD",
            "require": {"skill": "sword", "level": 15},
            "due_date": (datetime.date.today() + datetime.timedelta(days=2)).strftime("%Y-%m-%d"),
            "rewards": {"exp": 55, "fame": 8, "loot": {"coin_pouch": 10}},
            "required_proofs": ["caravan_badge", "caravan_safe"],
            "accepted": None
        },
        "Q033": {
            "title": "Slime Nest Cleanup",
            "difficulty": "EASY",
            "require": {"skill": "alchemy", "level": 2},
            "due_date": (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"),
            "rewards": {"exp": 18, "fame": 1, "loot": {"coin_pouch": 2}},
            "required_proofs": ["slime_remains"],
            "accepted": None
        },
        "Q010": {
            "title": "Bridge Repair",
            "difficulty": "MEDIUM",
            "require": {"skill": "craft", "level": 10},
            "due_date": datetime.date.today().strftime("%Y-%m-%d"),
            "rewards": {"exp": 28, "fame": 3, "loot": {"coin_pouch": 3}},
            "required_proofs": ["repaired_bridge"],
            "accepted": None
        }
    }

    save('quests.json', quests)

main()
# attempt to show binding error
# log_history("test_user", type="Broken", date="2025-01-01")
# log_history("test_user", date="2025-01-01")
# validate_proofs("hello", "hello", required="hello")
