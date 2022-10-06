# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns an integer

def square_every_digit(num):
    nums_list = [x for x in str(num)]
    answer_list = [str(int(x) * int(x)) for x in nums_list]
    answer = int(''.join(answer_list))
    return answer

num = 9119
print(square_every_digit(num))
