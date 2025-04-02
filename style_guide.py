# style_guide.py

# -------------------------------------
# 1. Naming Conventions (İsimlendirme)
# -------------------------------------

# ✅ Correct: descriptive and uses snake_case
user_name = "Alice"

# ❌ Wrong: uses PascalCase (PascalCase sınıflar içindir)
UserName = "Alice"  # wrong

# ✅ Correct: function name in snake_case
def calculate_total_price():
    pass

# ❌ Wrong: function name too short and unclear
def calcTP():  # wrong
    pass

# -------------------------------------
# 2. Constants
# -------------------------------------

# ✅ Correct: uses UPPER_CASE_WITH_UNDERSCORES
MAX_CONNECTIONS = 10

# ❌ Wrong: lowercase used
maxconnections = 10  # wrong

# -------------------------------------
# 3. Classes
# -------------------------------------

# ✅ Correct: class name in PascalCase
class BankAccount:
    pass

# ❌ Wrong: uses snake_case instead of PascalCase
class bank_account:  # wrong
    pass

# -------------------------------------
# 4. Methods
# -------------------------------------

class User:
    # ✅ Correct
    def get_balance(self):
        pass

    # ❌ Wrong: uses PascalCase
    def GetBalance(self):  # wrong
        pass

# -------------------------------------
# 5. Indentation (Girintileme)
# -------------------------------------

# ✅ Correct indentation (4 spaces)
if True:
    print("This is indented correctly.")

# ❌ Wrong indentation
if True:
print("This will cause an IndentationError.")  # wrong

# ✅ Correct: inside a loop
for i in range(3):
    print("Inside loop")
print("Outside loop")

# ❌ Wrong: inconsistent indentation
for i in range(3):
  print("Bad indent")  # wrong

# -------------------------------------
# 6. Booleans
# -------------------------------------

# ✅ Correct: uses is_/has_ prefix
is_valid = True
has_permission = False

# ❌ Wrong: not descriptive
valid = True  # wrong

# -------------------------------------
# 7. Exceptions
# -------------------------------------

# ✅ Correct: class ends with Error and uses PascalCase
class InvalidUserError(Exception):
    pass

# ❌ Wrong: all lowercase
class invaliduser(Exception):  # wrong
    pass

# -------------------------------------
# 8. Type Hints
# -------------------------------------

# ✅ Correct: uses type hints
def add(x: int, y: int) -> int:
    return x + y
