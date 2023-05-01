import psutil
import py3nvml

# Initialize NVML
def estimatePower(application):
    py3nvml.py3nvml.nvmlInit()

    # Get the number of available GPUs
    num_gpus = py3nvml.py3nvml.nvmlDeviceGetCount()

    # Get the list of running processes
    processes = psutil.process_iter()

    # Iterate over the processes
    for process in processes:
        if application in process.name().lower():
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

                # Iterate over the available GPUs
                gpu_power = 0.0
                for gpu_index in range(num_gpus):
                    handle = py3nvml.py3nvml.nvmlDeviceGetHandleByIndex(gpu_index)
                    utilization = py3nvml.py3nvml.nvmlDeviceGetUtilizationRates(handle)
                    gpu_utilization = utilization.gpu

                    # Assuming the GPU power consumption is linearly related to GPU utilization
                    gpu_power += gpu_utilization

                    print(f"GPU {gpu_index} Usage: {gpu_utilization}%")

                # Estimate power consumption based on CPU, memory, and GPU usage
                power_consumption = cpu_percent + (memory_info.rss / (1024 * 1024)) + gpu_power
                print(f"Estimated Power Consumption: {power_consumption}W")

                print("------------------------------")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle exceptions for processes that are no longer available or accessible
                pass

    # Clean up NVML
    py3nvml.py3nvml.nvmlShutdown()

estimatePower("discord")