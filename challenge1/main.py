
def file_to_list(file):
    with open(file) as f:
        lines = f.read()

    elves = [[int(y) for y in x.split('\n')] for x in lines.split("\n\n")]
    most_cal(elves)
    top_three(elves)


def most_cal(elves):
    largest = 0
    for elf in elves:
        cal = sum(elf)
        if cal > largest:
            largest = cal
    print(f"Largest amount of Calories: {largest}")

def top_three(elves):
    sum_list = []
    for elf in elves:
        sum_list.append(sum(elf))
    sum_list.sort(reverse=True)
    top_three = sum_list[0:3]
    print(f"Sum of top 3 largest calories: {sum(top_three)}")

def main():
    file_to_list('input.txt')

main()