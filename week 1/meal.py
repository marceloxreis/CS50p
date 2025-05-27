def main():
    time = input("time: ")
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    if 12 <= converted_time <= 13:
        print("lunch time")
    if 18 <= converted_time <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    time = hours + minutes
    return time


if __name__ == "__main__":
    main()
