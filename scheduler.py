def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    results = []

    for p in processes:
        start_time = max(time, p['arrival'])
        completion_time = start_time + p['burst']
        turnaround_time = completion_time - p['arrival']
        waiting_time = turnaround_time - p['burst']

        results.append({
            'pid': p['pid'],
            'arrival': p['arrival'],
            'burst': p['burst'],
            'completion': completion_time,
            'turnaround': turnaround_time,
            'waiting': waiting_time
        })
        time = completion_time

    return results

