
def priority_scheduling(processes, burst_times, priorities, arrival_times):
    n = len(processes)
    waiting_times, turnaround_times, completion_times = [0] * n, [0] * n, [0] * n
    remaining_processes = sorted(zip(processes, burst_times, priorities, arrival_times), key=lambda x: x[3])

    current_time, completed = 0, 0
    while completed < n:
        ready_queue = [p for p in remaining_processes if p[3] <= current_time]
        if ready_queue:
            process, burst_time, priority, arrival_time = min(ready_queue, key=lambda x: x[2])
            remaining_processes.remove((process, burst_time, priority, arrival_time))
            current_time = max(current_time, arrival_time) + burst_time
            idx = processes.index(process)
            completion_times[idx] = current_time
            turnaround_times[idx] = current_time - arrival_time
            waiting_times[idx] = turnaround_times[idx] - burst_time
            completed += 1
        else:
            current_time = remaining_processes[0][3]

    print("\nProcess\tAT\tPriority\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_times[i]}\t{priorities[i]}\t\t{burst_times[i]}\t{completion_times[i]}\t{turnaround_times[i]}\t{waiting_times[i]}")
    
    print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")

def main():
    n = int(input("Enter the number of processes: "))
    processes, burst_times, priorities, arrival_times = [], [], [], []

    for i in range(n):
        processes.append(int(input(f"Enter process ID for P{i + 1}: ")))
        arrival_times.append(int(input(f"Enter arrival time for P{i + 1}: ")))
        burst_times.append(int(input(f"Enter burst time for P{i + 1}: ")))
        priorities.append(int(input(f"Enter priority for P{i + 1} (lower number = higher priority): ")))

    priority_scheduling(processes, burst_times, priorities, arrival_times)

if __name__ == "__main__":
    main()
