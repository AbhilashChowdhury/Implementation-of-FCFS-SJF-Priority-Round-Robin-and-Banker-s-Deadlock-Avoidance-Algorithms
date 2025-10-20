def fcfs(processes, burst_times, arrival_times):
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    completion_times = [0] * n  

    data = list(zip(processes, arrival_times, burst_times))
    data.sort(key=lambda x: x[1])  

    processes, arrival_times, burst_times = zip(*data)

    completion_times[0] = arrival_times[0] + burst_times[0]
    for i in range(1, n):
        completion_times[i] = max(arrival_times[i], completion_times[i - 1]) + burst_times[i]

    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    print("\nProcess\t\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"P{processes[i]}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}\t\t{completion_times[i]}")

    # Calculate and print average times
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")

def main():
    n = int(input("Enter the number of processes: "))

    processes = []
    burst_times = []
    arrival_times = []

    for i in range(n):
        process_id = int(input(f"Enter process ID for process {i + 1}: "))
        arrival_time = int(input(f"Enter arrival time for process P{process_id}: "))
        burst_time = int(input(f"Enter burst time for process P{process_id}: "))
        processes.append(process_id)
        burst_times.append(burst_time)
        arrival_times.append(arrival_time)

    fcfs(processes, burst_times, arrival_times)

if __name__ == "__main__":
    main()
