import psutil

# Get the list of running processes
def g(n):
    processes = psutil.process_iter()

    # Iterate over the processes
    for process in processes:
        if n == process.name().lower() or n in process.name().lower():
            try:
                # Get the process name and ID
                process_name = process.name()
                process_id = process.pid

                # Get the CPU and memory usage of the process
                cpu_percent = process.cpu_percent(interval=0.1)
                memory_info = process.memory_info()

                print(f"Process Name: {process_name}")
                print(f"Process ID: {process_id}")
                print(f"CPU Percent: {cpu_percent}%")
                print(f"Memory Info: {memory_info}")

                print("------------------------------")
            
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle exceptions for processes that are no longer available or accessible
                pass

g("cloudflare")