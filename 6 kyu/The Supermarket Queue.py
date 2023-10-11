"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
"""


# def queue_time(customers, n):
#     result = [0 for _ in range(n)]
#     for idx, val in enumerate(customers):
#         result[idx % n] = result[idx % n] + val
#         print(f'idx % n => {idx % n}', f'res => {val}')
#     return max(result)

def queue_time(customers, n):
    # обработка исключения
    if len(customers) == 0:
        customers.append(0)

    # заполнили кассы
    result = [x for x in customers[:n]]
    # удалили из очереди "первых" покупателей на кассах
    del customers[:n]
    # можно так
    # for x in range(n):
    #     customers.pop(0)

    for idx, val in enumerate(customers):
        result[result.index(min(result))] = min(result) + val
        # print(f'result[result.index(min(result))] => {result[result.index(min(result))]};', f'val => {val}')

    return max(result)


# queue = [2, 3, 10]
# a = 2
# queue = [24, 15, 40, 32, 27, 22, 8, 23, 28, 38, 43, 20, 32, 4, 46]
# a = 4 # 129
queue = []
a = 1
print(queue_time(queue, a))


# result = [x for x in queue[:a]]
# print(max(result))
