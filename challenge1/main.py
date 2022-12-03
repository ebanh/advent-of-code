
def get_from_file(file):
    with open(file) as f:
        lines = f.read()
    return lines

def prep_data(file):
    lines = get_from_file(file)
    elves = [[int(y) for y in x.split('\n')] for x in lines.split("\n\n")]
    
    sum_list = []
    for elf in elves:
        sum_list.append(sum(elf))

    sum_list.sort(reverse=True)
    return sum_list

def most_cal(elves):
    print(f"Largest amount of Calories: {elves[0]}")

def top_three(elves):
    print(f"Sum of top 3 largest calories: {sum(elves[0:3])}")

def main():
    list = prep_data('input.txt')
    most_cal(list)
    top_three(list)

main()