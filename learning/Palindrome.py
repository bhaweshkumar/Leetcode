# is input a palindrome
user_input = ""
while user_input != "XX":
    user_input = input("Please enter a string to test for palindrome\n")
    middle = len(user_input) // 2
    count = 0
    palindrome = True

    while count <= middle:
        if user_input[count] != user_input[(count + 1) * -1]:
            palindrome = False
            break
        count += 1

    print("Palindrome:", palindrome)
