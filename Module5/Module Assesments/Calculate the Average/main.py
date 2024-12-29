def calculate_average(ls):
    sum = 0
    for item in ls:
        sum += item
    average = sum / len(ls)
    
    return average

def main():
    user_input = list(map(int, input("Enter numbers separated by space: ").split()))
    avg = calculate_average(user_input)
    print(f"The average of the given numbers is: {avg}")
    return avg
main()
