import psutil
import py3nvml
from tkinter import *
from tkinter import ttk


# this function will not be used although it increases accuracy, it drastically increases search time
def get_cpu_percent(p):
    list_of_percentages = []
    for i in range(5):
        p_cpu = p.cpu_percent(interval=0.1)
        list_of_percentages.append(p_cpu)

    # pop the first index for better accuracy, this is because with interval value greater than 0, 
    # cpu_percent() will block the current process. During the blocking period, the cpu percent is 0,
    # and so 0.0 will be always be appended into the first index.
    list_of_percentages.pop(0)

    # return the average
    return float(sum(list_of_percentages))/len(list_of_percentages)

# Initialize NVML
def estimatePower(application, gui=None):
    if gui is None:
        gui = ttk.Treeview()
    py3nvml.py3nvml.nvmlInit()

    # Get the number of available GPUs
    num_gpus = py3nvml.py3nvml.nvmlDeviceGetCount()

    # Get the list of running processes
    processes = psutil.process_iter()

    # Iterate over the processes
    i = 0
    totalPower = 0.0
    totalCPU = 0.0
    totalGPU = 0.0
    totalMem = 0.0
    for process in processes:

        if application in process.name().lower():
            try:
                # Get the process name and ID
                process_name = process.name()
                process_id = process.pid

                # Get the CPU and memory usage of the process
                mem_percent = process.memory_percent()
                cpu_percent = process.cpu_percent(interval=0.1)


                memory_info = process.memory_info()
                i += 1

                # Iterate over the available GPUs
                gpu_power = 0.0
                for gpu_index in range(num_gpus):
                    handle = py3nvml.py3nvml.nvmlDeviceGetHandleByIndex(gpu_index)
                    utilization = py3nvml.py3nvml.nvmlDeviceGetUtilizationRates(handle)
                    gpu_utilization = utilization.gpu

                    # Assuming the GPU power consumption is linearly related to GPU utilization
                    gpu_power += gpu_utilization

                # Estimate power consumption based on CPU, memory, and GPU usage
                # Generally, computers use between 30 and 70 watts (W) of electricity, depending on the model. 
                # Computers usually use between 3 and 5 amps, and connect to a 120-volt outlet. 
                # Larger desktop and gaming computers can use up to 500 W

                # power_consumption = (cpu_percent / 100) * cpu_power 
                # + (memory_info.rss / (1024 * 1024)) * memory_power 
                # + (gpu_power / 100) * gpu_power_consumption

                # rss is in bytes
                power_consumption = ( (cpu_percent / 100) * 100 
                                     + (memory_info.rss / (1024 * 1024 * 1024)) * 3.5
                                     + (gpu_power / 100) * 200 )
                # Convert power consumption to watts
                power_consumption_watts = power_consumption

                gui.insert(parent='', index='end', iid=i, text='',
                           values=(process_id, process_name, cpu_percent, mem_percent, gpu_utilization,
                                   power_consumption_watts))

                totalPower += power_consumption_watts
                totalCPU += cpu_percent
                totalGPU += gpu_utilization
                totalMem += mem_percent

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle exceptions for processes that are no longer available or accessible
                pass

    gui.insert(parent='', index='end', iid=i+1, text='',
               values=("N.A", "TOTAL", totalCPU, totalMem, totalGPU, totalPower))

    # Clean up NVML
    py3nvml.py3nvml.nvmlShutdown()

