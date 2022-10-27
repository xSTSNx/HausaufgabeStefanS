# # # ############################
# FizzBuzz
# # # ############################


# # # ############################
# Example 1: Fizzbuzz as function
# # # ############################
def run_fizzbuzz():
    count = 0

    while True:
        # Increment counter
        count += 1

        # Get the users input
        user_input = input(f"{count}\t: ")

        # If count can be devided by 3 and 5, await "fizzbuzz"
        if count % 3 == 0 and count % 5 == 0:
            if user_input == "fizzbuzz":
                continue

        # If count can be devided by 3, await "fizz"
        if count % 3 == 0:
            if user_input == "fizz":
                continue

        # If count can be devided by 5, await "buzz"
        if count % 5 == 0:
            if user_input == "buzz":
                continue

        # If count can either be devided by 3 or 5, await ""
        if count % 3 != 0 and count % 5 != 0:
            if user_input == "":
                continue

        break

    print(f"Du hast insgesamt {count - 1} Runden geschafft.")


# # # ############################
# Example: 2
# # # ############################
class FizzBuzzGame():
    count = 0
    user_input = None

    def get_user_input(self):
        self.user_input = input(f"{self.count}\t: ")

    def print_end_text(self):
        print(f"Du hast insgesamt {self.count - 1} Runden geschafft.")

    def increment_count(self):
        self.count += 1
    
    def check_user_input(self):
        # If count can be devided by 3 and 5, await "fizzbuzz"
        if self.count % 3 == 0 and self.count % 5 == 0:
            if self.user_input == "fizzbuzz":
                return True

        # If count can be devided by 3, await "fizz"
        if self.count % 3 == 0:
            if self.user_input == "fizz":
                return True

        # If count can be devided by 5, await "buzz"
        if self.count % 5 == 0:
            if self.user_input == "buzz":
                return True

        # If count can either be devided by 3 or 5, await ""
        if self.count % 3 != 0 and self.count % 5 != 0:
            if self.user_input == "":
                return True

        return False

    def start_game(self):
        while True:
            self.increment_count()
            self.get_user_input()
            if self.check_user_input():
                continue
            break
        self.print_end_text()
            


if __name__ == "__main__":
    # Run game as function
    run_fizzbuzz()

    # Run game as class
    game = FizzBuzzGame()
    game.start_game()