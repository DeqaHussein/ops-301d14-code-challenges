import psutil

def get_system_info():
    # Time spent by normal processes executing in user mode
    user_time = psutil.cpu_times().user

    # Time spent by processes executing in kernel mode
    system_time = psutil.cpu_times().system

    # Time when the system was idle
    idle_time = psutil.cpu_times().idle

    # Time spent by priority processes executing in user mode
    priority_user_time = psutil.cpu_times().nice

    # Time spent waiting for I/O to complete
    io_wait_time = psutil.cpu_times().iowait

    # Time spent for servicing hardware interrupts
    irq_time = psutil.cpu_times().irq

    # Time spent for servicing software interrupts
    soft_irq_time = psutil.cpu_times().softirq

    # Time spent by other operating systems running in a virtualized environment
    guest_time = psutil.cpu_times().guest

    # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
    guest_nice_time = psutil.cpu_times().guest_nice

    # Print the gathered information
    print(f"User Time: {user_time}")
    print(f"System Time: {system_time}")
    print(f"Idle Time: {idle_time}")
    print(f"Priority User Time: {priority_user_time}")
    print(f"I/O Wait Time: {io_wait_time}")
    print(f"IRQ Time: {irq_time}")
    print(f"Soft IRQ Time: {soft_irq_time}")
    print(f"Guest Time: {guest_time}")
    print(f"Guest Nice Time: {guest_nice_time}")

if __name__ == "__main__":
    get_system_info()


resource-chatgpt
