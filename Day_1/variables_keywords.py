"""DAY 1 - VARIABLES & KEYWORDS"""
import keyword

"""VARIABLES"""
print("Day 1    | Variables ")
# Variables
"""Rule 1 - Starts with a character or underscore"""
_1Var = "Pass"
Var = "Pass"

print("Rule 1   | Starts with underscore : ", _1Var)
print("Rule 1   | Starts with character : ", Var)

"""Rule 1  - Invalid Identifier"""
# 1Var = "Test"
# @Var = "Test"


"""Rule 2 - Combination of character, digits & underscore"""
Var123_ = "Pass"

print("Rule 2   | Combination of character, digits & underscore : ", Var123_)

"""Rule 2  - Invalid Identifier"""
# Var123# = "Test"
# Var 123 = "Test"

"""Rule 3 - Case sensitive"""
Var = "Quality"
var = "Check"
VAR = "OK"

print("Rule 3   | Case sensitive : ", Var, var, VAR)

"""Rule 4 - Keywords cannot be used"""
# if = "test"
class1 = "test"

print("Rule 4   | [IF] is it a keyword  : ", keyword.iskeyword("if"))
print("Rule 4   | [CLASS1] is it a valid identifier  : ", class1.isidentifier())

"""KEYWORDS"""
print("\n\nDay 1    | Keywords")
print("Available keywords : ", keyword.kwlist)

"""Usage of TRUE | FALSE | AND | OR | NOT"""
print("Usage of TRUE | FALSE | AND | OR | NOT")
print("TRUE OR FALSE : ", True or False)
print("TRUE AND FALSE : ", True and False)
print("NOT TRUE : ", not True)

"""Usage of Break and Continue"""
"""Usage of FOR | IN | IF | ELIF | ELSE"""
print("Usage of BREAK | CONTINUE")
print("Usage of FOR | IN | IF | ELIF | ELSE")
for i in range(1, 11):
    # Check the value of i is less than 5 - continue else break
    if i < 5:
        # Continue & Print the value of i
        print("Hit Continue at : ", i)
        continue
    elif i == 5:
        # Continue & Print the value of i
        print("Hit Continue at : ", i)
        continue
    else:
        # Break & Print the value of i
        print("Hit Break at : ", i)
        break

"""Usage of def | try | except | raise"""
print("Usage of DEF | TRY | EXCEPT | RAISE")


def check_min_age(age):
    if age < 18:
        raise ValueError("Age should be greater than or equal to 18")
    else:
        print("Permission Granted !")


try:
    check_min_age(10)
except ValueError as e:
    print("Permission Denied : ", e)
finally:
    print("Check Minimum Age - Completed!")


