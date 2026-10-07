import random


lotto_starting_numbers = []

statistics = {}


def set_lotto_starting_numbers():
    for i in range(1, 46):
        lotto_starting_numbers.append(i)

def set_statistics():
    for i in range(1, 46):
        statistics[i] = 0

def lotto_draw():
    size = len(lotto_starting_numbers) - 1
    drawn_numbers = []
    for i in range(6):
        rand_index = random.randint(0, size)
        drawn_number = lotto_starting_numbers[rand_index]
        lotto_starting_numbers[rand_index] = lotto_starting_numbers[size]
        lotto_starting_numbers[size] = drawn_number
        drawn_numbers.append(drawn_number)
        statistics[drawn_number] += 1
        size -= 1
    

if __name__ == "__main__":
    set_lotto_starting_numbers()
    set_statistics()
    pulls = int(input("How many lotto games do you want to simulate?: "))
    for i in range(0, pulls):
        lotto_draw()
    for key, value in statistics.items(): 
        print(str(key) + ": " + str(value))
        