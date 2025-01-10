class OnlineVotingSystem:
    def __init__(self):
        self.candidates = {}
        self.voters = {}
        self.logged_in_voter = None

    def register_voter(self, voter_id, password):
        if voter_id in self.voters:
            print("Voter ID already registered.")
        else:
            self.voters[voter_id] = {"password": password, "has_voted": False}
            print("Voter registered successfully!")

    def login_voter(self, voter_id, password):
        if voter_id in self.voters and self.voters[voter_id]["password"] == password:
            if self.voters[voter_id]["has_voted"]:
                print("You have already voted!")
            else:
                self.logged_in_voter = voter_id
                print(f"Welcome, Voter {voter_id}!")
        else:
            print("Invalid credentials.")

    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"{candidate_name} is already a candidate.")
        else:
            self.candidates[candidate_name] = 0
            print(f"Candidate {candidate_name} added successfully!")

    def cast_vote(self, candidate_name):
        if not self.logged_in_voter:
            print("You must log in first to vote.")
            return

        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
            self.voters[self.logged_in_voter]["has_voted"] = True
            self.logged_in_voter = None
            print("Thank you for voting!")
        else:
            print("Invalid candidate name. Please try again.")

    def display_results(self):
        if not self.candidates:
            print("No candidates are registered yet.")
            return

        print("\nVoting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")

        winner = max(self.candidates, key=self.candidates.get, default=None)
        print(f"\nLeading Candidate: {winner} with {self.candidates[winner]} votes" if winner else "No votes yet.")

    def main_menu(self):
        while True:
            print("\nMenu:")
            print("1. Register Voter")
            print("2. Login Voter")
            print("3. Add Candidate")
            print("4. Cast Vote")
            print("5. Display Results")
            print("6. Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    voter_id = input("Enter voter ID: ")
                    password = input("Set a password: ")
                    self.register_voter(voter_id, password)
                elif choice == 2:
                    voter_id = input("Enter voter ID: ")
                    password = input("Enter your password: ")
                    self.login_voter(voter_id, password)
                elif choice == 3:
                    candidate_name = input("Enter candidate name: ")
                    self.add_candidate(candidate_name)
                elif choice == 4:
                    candidate_name = input("Enter candidate name to vote for: ")
                    self.cast_vote(candidate_name)
                elif choice == 5:
                    self.display_results()
                elif choice == 6:
                    print("Exiting the system. Thank you!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    system = OnlineVotingSystem()
    system.main_menu()
