def isValid(password):
  hasValidLength = len(password) >= 10
  hasValidDigits = len([x for x in password if x.isdigit()]) >= 2
  return hasValidLength and hasValidDigits

print(isValid('AVs1aasdf3gkop['))
