**Power Consumption Estimation Tool**

This is a simple Python program that allows you to measure the power consumption of a specific application running on your computer. The program utilizes the **psutil** and **py3nvml** libraries to retrieve information about running processes, CPU usage, memory usage, and GPU utilization. It then estimates the power consumption based on these metrics. Note that this might be limited to NVIDIA GPU cores.

**Prerequisites**

1. **Python and Libraries:** Ensure that you have Python installed on your system. This application uses the following Python libraries:
  - **psutil** : Used for retrieving system and process information. Install it by running **pip install psutil.**
  - **py3nvml** : Used for interacting with NVIDIA GPU metrics. Install it by running **pip install py3nvml.**
  - **tkinter** : Used for building the graphical user interface (GUI) and table display. It is typically included with Python installations
2. **System Requirements:**
  - Windows operating system
  - NVIDIA GPU (optional) - If you have an NVIDIA GPU, the application can provide additional GPU power consumption information which may improve the accuracy of the results.

**Code Structure**

The code is divided into two main parts:

1. **Estimate Power Consumption** : This part contains the **estimatePower** function, which is responsible for estimating the power consumption of the specified application. It initializes the NVML library, retrieves the list of running processes using **psutil** , and iterates over each process to collect relevant information such as CPU usage, memory usage, and GPU utilization. The power consumption is estimated based on these metrics and added to the table for display.
2. **Graphical User Interface** : This part creates a graphical window using **tkinter**. It provides a search bar and a table to display the search results. The user can enter the name of a process in the search bar, and the program will search for processes with matching names using the **perform\_search** function. The search results are then displayed in the table using the **taskMgr** Treeview widget.

**Usage**

1. Run the program by executing the "Table.py" script.
2. A graphical window will open, showing a search bar and a table initially displaying zero processes.
3. Enter the name of the process you want to search for in the search bar. The program will search for processes that are supersets of the entered name. Note that these are the names of the processes, and not the applications. E.g (Google Chrome will be chrome.exe, VSCode will be code.exe, Microsoft Edge will be msedge.exe)
4. Press the "Search" button or hit the "Enter" key to perform the search.
5. The table will be updated with the matching processes and their corresponding CPU usage, memory usage, GPU utilization, and estimated power consumption, the table is a snapshot of these values upon searching, and needs to be re-queried for an updated value.
6. The total power consumption of all the displayed processes is shown at the bottom of the table as "TOTAL".
7. You can display all processes running on the system by leaving the search bar empty and hitting enter. However, note that System Idle Process(PID = 0) will skew the results leading to an inaccurate total power consumption.

**Estimation Formula**

The power consumption estimation formula used in the program is as follows:

power\_consumption = ( (cpu\_percent / 100) \* cpu\_power + (memory\_info.rss / (1024 \* 1024 \* 1024)) \* memory\_power + (gpu\_power / 100) \* gpu\_power\_consumption )

- **cpu\_percent** : CPU utilization percentage obtained from psutil.
- **cpu\_power** : The power consumption of the CPU under full load. This value is typically provided by the CPU manufacturer or can be estimated based on the CPU model.
- **memory\_info.rss** : The resident set size of the process, representing the physical memory occupied by the process.
- **memory\_power** : The power consumption per unit of memory usage. This value can vary depending on the specific memory type and configuration.
- **gpu\_power** : GPU utilization percentage obtained from psutil.
- **gpu\_power\_consumption** : The power consumption of the GPU under full load. This value is typically provided by the GPU manufacturer or can be estimated based on the GPU model.

**Rationale**

The power consumption estimation formula takes into account multiple factors that contribute to the overall power consumption of a process, namely CPU usage, memory usage, and GPU usage. By considering these factors, the formula provides a more comprehensive and accurate estimation of the power consumed by a process.

1. **CPU Usage:** The CPU is one of the primary components responsible for power consumption in a computer system. The formula incorporates the CPU percentage ( **cpu\_percent** ) as a proportion of the maximum CPU power ( **cpu\_power** ). This reflects the direct correlation between CPU utilization and power consumption. A process with higher CPU usage will consume more power.
2. **Memory Usage:** Memory usage also contributes to power consumption, although to a lesser extent compared to the CPU. The formula includes the Resident Set Size ( **memory\_info.rss** ) of the process, which represents the amount of physical memory used by the process. This value is converted to gigabytes ( **GB** ) and multiplied by a memory power factor ( **memory\_power** ). This accounts for the additional power consumed by memory operations.
3. **GPU Usage:** If the system has an NVIDIA GPU, the formula considers the GPU usage ( **gpu\_power** ) as a proportion of the maximum GPU power consumption ( **gpu\_power\_consumption** ). Modern GPUs have their power consumption related to their utilization. By including GPU utilization, the formula incorporates the power consumed by graphics-related tasks, such as rendering or GPU computing.

By combining the contributions from CPU, memory, and GPU usage, the formula provides a more accurate estimation of the power consumption of a process. It considers the varying impact of each factor on power consumption and reflects the real-world behavior of processes running on the system. However, it's important to note that the formula provides an estimation and may have inherent limitations based on hardware variations and the specific workload characteristics of the process.

Overall, the formula aims to provide a reasonable approximation of the power consumption of a process based on the available system metrics.

**Assumptions and Estimations, and placeholder values**

**cpu\_power :** The average power consumption of CPUs can vary significantly depending on the specific model, architecture, and manufacturing process. Generally, lower-power CPUs designed for laptops and mobile devices have average power consumption in the range of 5 to 25 watts. Mid-range desktop CPUs typically consume around 35 to 100 watts, while high-end CPUs used in gaming rigs and workstations can consume 100 watts or more.

It's important to note that these are rough average values, and the actual power consumption of a CPU can vary based on factors such as workload, clock speed, voltage, and efficiency optimizations. Thus, our placeholder value used will be 50 watts.

**Memory\_power** : The power consumption per unit of memory usage can vary within a range depending on the specific memory type and configuration. Here is a rough range for memory power consumption:

For DDR3 memory: Approximately 0.5 to 1.5 watts per gigabyte (W/GB) of memory usage.

For DDR4 memory: Approximately 0.3 to 1.2 W/GB of memory usage.

For GDDR5 memory (graphics memory): Approximately 1.5 to 3.5 W/GB of memory usage.

For HBM (High-Bandwidth Memory): Approximately 3 to 8 W/GB of memory usage.

The most common memory types used today are DDR4 for system memory and GDDR5 for graphics memory. As such, we will be using 1.2 watts as our placeholder value.

**gpu\_power** : The average power consumption of a GPU under full load can vary greatly depending on the GPU model, architecture, manufacturing process, and other factors.

However, as a rough estimate, mid-range and high-end desktop GPUs typically have power consumption ranging from 150 watts to 300 watts under full load. More power-hungry GPUs, such as those designed for gaming or specialized tasks like deep learning, can consume even higher power, exceeding 300 watts. Therefore, our placeholder value will be 150W.

**Limitations**

- The estimation of power consumption is based on general assumptions and average values. The actual power consumption can vary depending on the specific hardware, configuration, and workload characteristics.
- The power consumption values for CPU, memory, and GPU used in the estimation formula are placeholders. It is recommended to replace them with accurate values specific to your hardware and components.
- The program provides an estimate of the power consumption but does not measure it directly. It relies on system metrics and assumptions to calculate the power consumption.
- Since the estimations are calculated and displayed on the table as snapshots, the table is not updated live. Therefore when the information is captured during an instance of intensive system resource utilisation which may occur over an extremely short timespan, it may display a very high value which is not representative of the average power consumption.

**Disclaimer**

Refer to official specifications, documentation, or power measurement tools provided by the hardware manufacturers for accurate power consumption information.

Use this program responsibly and be aware of the limitations and assumptions involved in the power consumption estimation process.