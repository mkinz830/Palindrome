def is_palindrome(num):
    is_pal = False

    num_string = str(num)
    reversed_string = reversed(num_string)

    is_pal = num_string == reversed_string


    if(is_pal):
        print("The given number is a palindrome")
    else:
        print("The given number is not a palindrome")

    test_num = 7
    print(is_palindrome(test_num))