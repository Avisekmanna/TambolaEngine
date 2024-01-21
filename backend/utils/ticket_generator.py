import random
from tabulate import tabulate
from loguru import logger

@logger.catch
def generate_tickets(used_numbers):
    # Initialize a 3x9 array for the ticket
    ticket_array= [[0] * 9 for _ in range(3)]

    # # Create a list of numbers from 1 to 90
    # total_numbers = [num for num in range(1, 91)]
    # Generate a list of sublists, each containing a range of 10 consecutive numbers
    total_numbers = [list(range(start, start + 10)) for start in range(1, 91, 10)]

    # # Remove the item specified in the used_numbers from the total numbers array
    # total_numbers = [[item for item in sublist if item not in used_numbers] for sublist in total_numbers]otal_numbers)
    

    # Create a list of indices in a 3x9 array
    total_indices = [[i,j] for i in range(3) for j in range(9)]

    # Randomly select 5 indices from the first, second, and third row
    first_row = random.sample(total_indices[:9], 5)
    second_row = random.sample(total_indices[9:18], 5)
    third_row = random.sample(total_indices[-9:], 5)

    random_indices = first_row + second_row + third_row

    # Finding missing coloumn and add them to the 15 randomly chosen indices
    missing_cols = [col for col in range(9) if col not in [i[1] for i in random_indices]]
    while missing_cols:
        column_counts = {}
        for idx, pair in enumerate(random_indices):
            column = pair[1]
            if column in column_counts:
                column_counts[column].append(idx)
            else:
                column_counts[column] = [idx]

        # Finding the column with the maximum occurrences
        max_column = max(column_counts, key=lambda k: len(column_counts[k]))
        # Get the indexes of elements with the most occurring column
        randomly_chosen_index = random.choice(column_counts[max_column])
        random_indices[randomly_chosen_index][1] = missing_cols[0]
        missing_cols.pop(0)
    
    # # Populate values in the 15 randomly chosen indices
    for num in random_indices:
        if num[1] == 0:
            # number = random.choice(total_numbers[:10])
            number = random.choice(total_numbers[0])
            while (number == 0):
                number = random.choice(total_numbers[0])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[0].pop(total_numbers[0].index(number))
        elif num[1] == 1:
            # number = random.choice(total_numbers[10:20])
            number = random.choice(total_numbers[1])
            while (number == 0):
                number = random.choice(total_numbers[1])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[1].pop(total_numbers[1].index(number))
        elif num[1] == 2:
            # number = random.choice(total_numbers[20:30])
            number = random.choice(total_numbers[2])
            while (number == 0):
                number = random.choice(total_numbers[2])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[2].pop(total_numbers[2].index(number))
        elif num[1] == 3:
            # number = random.choice(total_numbers[30:40])
            number = random.choice(total_numbers[3])
            while (number == 0):
                number = random.choice(total_numbers[3])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[3].pop(total_numbers[3].index(number))
        elif num[1] == 4:
            # number = random.choice(total_numbers[40:50])
            number = random.choice(total_numbers[4])
            while (number == 0):
                number = random.choice(total_numbers[4])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[4].pop(total_numbers[4].index(number))
        elif num[1] == 5:
            # number = random.choice(total_numbers[50:60])
            number = random.choice(total_numbers[5])
            while (number == 0):
                number = random.choice(total_numbers[5])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[5].pop(total_numbers[5].index(number))
        elif num[1] == 6:
            # number = random.choice(total_numbers[60:70])
            number = random.choice(total_numbers[6])
            while (number == 0):
                number = random.choice(total_numbers[6])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[6].pop(total_numbers[6].index(number))
        elif num[1] == 7:
            # number = random.choice(total_numbers[70:80])
            number = random.choice(total_numbers[7])
            while (number == 0):
                number = random.choice(total_numbers[7])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[7].pop(total_numbers[7].index(number))
        elif num[1] == 8:
            # number = random.choice(total_numbers[80:90])
            number = random.choice(total_numbers[8])
            while (number == 0):
                number = random.choice(total_numbers[8])
            ticket_array[num[0]][num[1]] = number
            # total_numbers[total_numbers.index(number)] = 0
            total_numbers[8].pop(total_numbers[8].index(number))


    # Sort each column in ascending order
    for col in range(9):
        if(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            for row in range(2):
                if ticket_array[row][col] > ticket_array[row+1][col]:
                    temp = ticket_array[row][col]
                    ticket_array[row][col] = ticket_array[row+1][col]
                    ticket_array[row+1][col] = temp

        elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
            if ticket_array[0][col] > ticket_array[1][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[1][col]
                ticket_array[1][col] = temp

        elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
            if ticket_array[0][col] > ticket_array[2][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

        elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            if ticket_array[1][col] > ticket_array[2][col]:
                temp = ticket_array[1][col]
                ticket_array[1][col] = ticket_array[2][col]
                ticket_array[2][col] = temp
    return ticket_array

@logger.catch
def get_ticket(used_numbers):
    ticket = generate_tickets(used_numbers)
    logger.info(tabulate(ticket, tablefmt="fancy_grid", numalign="center"))
    return ticket



