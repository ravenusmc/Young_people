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
