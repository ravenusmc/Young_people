#All of the functions for validation will be kept in this file.
def valid_three(option):
    if option == 1 or option == 2 or option == 3:
        return True
    else:
        return False

def age_validation(age):
  if age <= 0 or age >= 75:
    return False
  else:
    return True

def valid_choice(option):
    if option > 6 or option < 1:
        return False
    else:
        return True

def music_valid(choice):
  if choice > 10 or choice < 1:
    return False
  else:
    return True

def movie_valid(choice):
    if choice > 11 or choice < 1:
        return False
    else:
        return True

def subjects_valid(choice):
    if choice > 12 or choice < 1:
        return False
    else:
        return True

def fear_valid(choice):
    if choice > 11 or choice < 1:
        return False
    else:
        return True

def activity_valid(choice):
    if choice > 11 or choice < 1:
        return False
    else:
        return True

def other_valid(choice):
    if choice > 9 or choice < 1:
        return False
    else:
        return True
