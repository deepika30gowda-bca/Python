def check_leap_year():
    try:
  
        year = int(input("Enter a year: "))
        
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
            
    except ValueError:
        print("Invalid input! Please enter a whole number for the year.")

check_leap_year()
