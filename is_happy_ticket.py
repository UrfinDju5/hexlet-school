def is_happy_ticket(number_of_ticket : int) -> bool:
    first_half = number_of_ticket[0:int(len(number_of_ticket)/2)]
    second_half = number_of_ticket[int(len(number_of_ticket)/2):]
    summ_of_first_half = 0
    for i in first_half:
        i = int(i)
        summ_of_first_half += i
    summ_of_second_half = 0
    for i in second_half:
        i = int(i)
        summ_of_second_half += i
    if summ_of_first_half == summ_of_second_half:
        return True
    else:
        return False



print(is_happy_ticket('123123')) # True
print(is_happy_ticket('341800')) # True

print(is_happy_ticket('42')) # False
print(is_happy_ticket('12345678')) # False


# красивое решение: 
def is_happy_ticket(ticket):
    balance = 0
    middle = len(ticket) // 2
    for i in range(middle):
        balance += int(ticket[i]) - int(ticket[i + middle])
    return balance == 0