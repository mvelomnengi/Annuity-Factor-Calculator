# This program serves as a financial math calculator
# It computes actuarial factors that go beyond standard actuarial tables,

# Implement error handling
try:

  # Import necessary libraries
  import math as m

  # Define a function to display the main menu
  def display_menu():

    # Display menu
    print("\nFinancial Math Calculator")
    print("1. Level annuities")
    print("2. Increasing annuities")
    print("3. Exit")

  # Define a function to get user choice
  def get_choice():

    # Prompt user to make selection
    choice = input("\nSelect option (1-3): ")

    # Validate user input
    while choice not in ["1", "2", "3"]:
      print("Invalid choice. Please select a valid option.")
      choice = input("\nSelect option (1-3): ")

    return choice

  # Define a function to get the interest rate and number of periods
  def get_rate_and_time():

    # Prompt user for rate and time
    rate = float(input("Enter the interest rate (as a decimal): "))
    time = float(input("Enter the number of periods (n): "))

    return rate, time

  # Define a function for a_n (PV, annuity-immediate)
  def a_n(i, n):
    return (1 - (1 + i) ** (-n)) / i

  # Define a function for a-due_n (PV, annuity-due)
  def a_due_n(i, n):
    return a_n(i, n) * (1 + i)

  # Define a function for s_n (AV, annuity-immediate)
  def s_n(i, n):
    return ((1 + i) ** n - 1) / i

  # Define a function for s-due_n (AV, annuity-due)
  def s_due_n(i, n):
    return s_n(i, n) * (1 + i)

  # Define a function for a-bar_n (PV, continuous annuity)
  def a_bar_n(i, n):
    return a_n(i, n) * i / m.log(1 + i)

  # Define a function for s-bar_n (AV, continuous annuity)
  def s_bar_n(i, n):
    return s_n(i, n) * i / m.log(1 + i)

  # Define a function for the level annuities sub menu
  def level_annuity_menu():

    # Display sub menu
    print("\nLevel Annuities:")
    print("1. a_n     (PV, annuity-immediate)")
    print("2. a-due_n (PV, annuity-due)")
    print("3. s_n     (AV, annuity-immediate)")
    print("4. s-due_n (AV, annuity-due)")
    print("5. a-bar_n (PV, continuous)")
    print("6. s-bar_n (AV, continuous)")

    # Prompt user to make selection
    sub_choice = input("\nSelect option (1-6): ")

    # Validate user input
    while sub_choice not in ["1", "2", "3", "4", "5", "6"]:
      print("Invalid choice. Please select a valid option.")
      sub_choice = input("\nSelect option (1-6): ")

    # Get rate and time, allowing non-integer n unlike printed tables
    rate, time = get_rate_and_time()

    # Calculate and display the chosen factor
    if sub_choice == "1":
      print(f"\na_{time} = {a_n(rate, time):.6f}")

    elif sub_choice == "2":
      print(f"\na-due_{time} = {a_due_n(rate, time):.6f}")

    elif sub_choice == "3":
      print(f"\ns_{time} = {s_n(rate, time):.6f}")

    elif sub_choice == "4":
      print(f"\ns-due_{time} = {s_due_n(rate, time):.6f}")

    elif sub_choice == "5":
      print(f"\na-bar_{time} = {a_bar_n(rate, time):.6f}")

    else:
      print(f"\ns-bar_{time} = {s_bar_n(rate, time):.6f}")

  # Define a function for (Ia)_n (PV, increasing annuity-immediate)
  def Ia_n(i, n):
    return (a_n(i, n) - n * (1 + i) ** (-n)) / i

  # Define a function for (Ia-due)_n (PV, increasing annuity-due)
  def Ia_due_n(i, n):
    return Ia_n(i, n) * (1 + i)

  # Define a function for (Is)_n (AV, increasing annuity-immediate)
  def Is_n(i, n):
    return (s_n(i, n) - n) / i

  # Define a function for (Is-due)_n (AV, increasing annuity-due)
  def Is_due_n(i, n):
    return Is_n(i, n) * (1 + i)

  # Define a function for (I-bar a-bar)_n (PV, continuous increasing annuity)
  def Ia_bar_n(i, n):
    return (a_bar_n(i, n) - n * (1 + i) ** (-n)) / m.log(1 + i)

  # Define a function for (I-bar s-bar)_n (AV, continuous increasing annuity)
  def Is_bar_n(i, n):
    return Ia_bar_n(i, n) * (1 + i) ** n

  # Define a function for the increasing annuities sub menu
  def increasing_annuity_menu():

    # Display sub menu
    print("\nIncreasing Annuities:")
    print("1. (Ia)_n     (PV, increasing annuity-immediate)")
    print("2. (Ia-due)_n (PV, increasing annuity-due)")
    print("3. (Is)_n     (AV, increasing annuity-immediate)")
    print("4. (Is-due)_n (AV, increasing annuity-due)")
    print("5. (I-bar a-bar)_n (PV, continuous)")
    print("6. (I-bar s-bar)_n (AV, continuous)")

    # Prompt user to make selection
    sub_choice = input("\nSelect option (1-6): ")

    # Validate user input
    while sub_choice not in ["1", "2", "3", "4", "5", "6"]:
      print("Invalid choice. Please select a valid option.")
      sub_choice = input("\nSelect option (1-6): ")

    # Get rate and time, allowing non-integer n unlike printed tables
    rate, time = get_rate_and_time()

    # Calculate and display the chosen factor
    if sub_choice == "1":
      print(f"\n(Ia)_{time} = {Ia_n(rate, time):.6f}")

    elif sub_choice == "2":
      print(f"\n(Ia-due)_{time} = {Ia_due_n(rate, time):.6f}")

    elif sub_choice == "3":
      print(f"\n(Is)_{time} = {Is_n(rate, time):.6f}")

    elif sub_choice == "4":
      print(f"\n(Is-due)_{time} = {Is_due_n(rate, time):.6f}")

    elif sub_choice == "5":
      print(f"\n(I-bar a-bar)_{time} = {Ia_bar_n(rate, time):.6f}")

    else:
      print(f"\n(I-bar s-bar)_{time} = {Is_bar_n(rate, time):.6f}")

  # Main program loop, controlled by a boolean flag
  running = True

  while running:
    display_menu()
    choice = get_choice()

    if choice == "1":
      level_annuity_menu()

    elif choice == "2":
      increasing_annuity_menu()

    else:
      print("\nGoodbye!")
      running = False

# Display error messages
except ImportError as e:
  print(f"Error importing libraries: {e}")
except Exception as e:
  print(f"An error occurred: {e}")