def main():
    positive_sum = 0
    positive_count = 0
    negative_sum = 0
    negative_count = 0

    while True:
        num = float(input("Enter a number (-1 to stop): "))
        if num == -1:
            break
        elif num >= 0:
            positive_sum += num
            positive_count += 1
        else:
            negative_sum += num
            negative_count += 1

    if positive_count > 0:
        positive_average = positive_sum / positive_count
        print("Average of positive numbers:", positive_average)
    else:
        print("No positive numbers were entered.")

    if negative_count > 0:
        negative_average = negative_sum / negative_count
        print("Average of negative numbers:", negative_average)
    else:
        print("No negative numbers were entered.")

if __name__ == "__main__":
    main()

