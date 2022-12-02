
def most_cal(file):
    with open(file) as f:
        lines = f.read()

    elves = [[int(y) for y in x.split('\n')] for x in lines.split("\n\n")]
    largest = 0

    for elf in elves:
        cal = sum(elf)
        if cal > largest:
            largest = cal

    print(largest)

def main():
    most_cal('input.txt')

main()