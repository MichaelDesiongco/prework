# Write a function to print "hello_USERNAME!"
# Username is the input of the function 

def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name('Michael')

# write a function first_odds
# prints odd numbers from 1-100
# returns nothing

def first_odds():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)

first_odds()

# write a function max_num_in_list
# return the max number of a given list

def max_num_in_list(a_list):
    return max(a_list)

numbers = [12, 4, 5 ,7, 13, 60]
print(max_num_in_list(numbers))

# write a function to return if the given year is a leap year

def is_leap_year(a_year):
    return(a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 ==0)

def main():
    try:
        a_year = int(input("Leap year checker: "))
        
        if is_leap_year(a_year):
            print("True")
        else:
            print("False")
    except ValueError:
        print("Invalid input. Please input a valid year.")

if __name__ == "__main__":
    main()
    
# write a function to check if all numbers are consecutive

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

numbers = [2, 3, 1, 4, 5]
print(is_consecutive(numbers))