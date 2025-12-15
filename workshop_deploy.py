import boa

def main():
    workshop = boa.load("workshop.vy")
    starting_boolean = workshop.retrieve()
    print(f"Our starting boolean is {starting_boolean}")

    workshop.set_bool(False)

    ending_boolean = workshop.retrieve()
    print(f"Our ending boolean is {ending_boolean}")

if __name__ == "__main__":
    main()