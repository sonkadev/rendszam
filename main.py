import random

file = open('szar.txt', 'w')

for x in range(10):

    B1 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    B2 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    B3 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])


    S1 = random.randint(0, 9)
    S2 = random.randint(0, 9)
    S3 = random.randint(0, 9)

    if S1 == S2 == S3:
        S3 = 1  # mivel nem lehet AAA-000

    print(f"{B1}{B2}{B3} - {S1}{S2}{S3}")
    # file.write(f"{B1}{B2}{B3} - {S1}{S2}{S3} \n")

file.close()
