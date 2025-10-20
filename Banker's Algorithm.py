class BankersAlgorithm:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.process_ids = [f"P{i+1}" for i in range(num_processes)]
        self.allocation_matrix = []
        self.max_needed_matrix = []
        self.available_matrix = []
        self.need_matrix = []
        self.finish = [False] * num_processes

    def input_matrices(self):
        print("Enter the Allocation Matrix:")
        for i in range(self.num_processes):
            allocation = list(map(int, input(f"Enter Allocation for {self.process_ids[i]}: ").split()))
            self.allocation_matrix.append(allocation)

        print("\nEnter the Max Needed Matrix:")
        for i in range(self.num_processes):
            max_needed = list(map(int, input(f"Enter Max Needed for {self.process_ids[i]}: ").split()))
            self.max_needed_matrix.append(max_needed)

        print("\nEnter the Available Matrix:")
        self.available_matrix = list(map(int, input("Enter Available Resources: ").split()))

        self.calculate_need_matrix()

    def calculate_need_matrix(self):
        self.need_matrix = [[self.max_needed_matrix[i][j] - self.allocation_matrix[i][j]
                              for j in range(self.num_resources)] for i in range(self.num_processes)]

    def is_safe(self):
        work = self.available_matrix[:]
        safe_sequence = []
        while len(safe_sequence) < self.num_processes:
            progress_made = False
            for i in range(self.num_processes):
                if not self.finish[i] and all(self.need_matrix[i][j] <= work[j] for j in range(self.num_resources)):
                    safe_sequence.append(self.process_ids[i])
                    work = [work[j] + self.allocation_matrix[i][j] for j in range(self.num_resources)]
                    self.finish[i] = True
                    progress_made = True
                    break
            if not progress_made:
                return False, []
        return True, safe_sequence

    def detect_deadlock(self):
        is_safe, safe_sequence = self.is_safe()
        if is_safe:
            print("\nThe system is in a safe state.")
            print("Safe Sequence:", " -> ".join(safe_sequence))
        else:
            print("\nThe system is in a deadlock state.")
            print("No Safe Sequence Exists.")

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))

    bankers_algo = BankersAlgorithm(num_processes, num_resources)
    bankers_algo.input_matrices()
    bankers_algo.detect_deadlock()