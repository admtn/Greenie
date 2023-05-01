cpu_power_consumption = 50  # Watts
memory_power_consumption = 10  # Watts
gpu_power_consumption = 80  # Watts

cpu_usage = 0.7  # 70% CPU usage
memory_usage = 0.5  # 50% memory usage
gpu_usage = 0.8  # 80% GPU usage

estimated_cpu_power = cpu_power_consumption * cpu_usage
estimated_memory_power = memory_power_consumption * memory_usage
estimated_gpu_power = gpu_power_consumption * gpu_usage

total_power_consumption = estimated_cpu_power + estimated_memory_power + estimated_gpu_power

print(f"Estimated CPU Power Consumption: {estimated_cpu_power} Watts")
print(f"Estimated Memory Power Consumption: {estimated_memory_power} Watts")
print(f"Estimated GPU Power Consumption: {estimated_gpu_power} Watts")
print(f"Total Estimated Power Consumption: {total_power_consumption} Watts")
