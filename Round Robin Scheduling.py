from collections import deque

def round_robin(processes, burst_times, arrival_times, quantum):
    n = len(processes)
    remaining_burst_times = burst_times[:]
    completion_times = [0] * n
    ready_queue = deque()
    t = 0  # Current time
    completed = 0
    arrived = [False] * n

    while completed < n:
        for i in range(n):
            if arrival_times[i] <= t and not arrived[i]:
                ready_queue.append(i)
                arrived[i] = True

        if ready_queue:
            current_process = ready_queue.popleft()
            if remaining_burst_times[current_process] > quantum:
                t += quantum
                remaining_burst_times[current_process] -= quantum
            else:
                t += remaining_burst_times[current_process]
                completion_times[current_process] = t
                remaining_burst_times[current_process] = 0
                completed += 1

            for i in range(n):
                if arrival_times[i] <= t and not arrived[i]:
                    ready_queue.append(i)
                    arrived[i] = True

            if remaining_burst_times[current_process] > 0:
                ready_queue.append(current_process)
        else:
            t += 1

    turnaround_times = [completion_times[i] - arrival_times[i] for i in range(n)]
    waiting_times = [turnaround_times[i] - burst_times[i] for i in range(n)]

    print("\nP\tBurst Time\tArrival Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_times[i]}\t\t{arrival_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")

def main():
    n = int(input("Enter number of processes: "))
    processes, burst_times, arrival_times = [], [], []
    for i in range(n):
        process_id = int(input(f"Enter process ID for process {i + 1}: "))
        arrival_time = int(input(f"Enter arrival time for process P{process_id}: "))
        burst_time = int(input(f"Enter burst time for process P{process_id}: "))
        processes.append(process_id)
        burst_times.append(burst_time)
        arrival_times.append(arrival_time)
    quantum = int(input("Enter time quantum: "))
    round_robin(processes, burst_times, arrival_times, quantum)

if __name__ == "__main__":
    main()
