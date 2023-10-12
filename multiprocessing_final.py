import multiprocessing

from files_to_load import file_loader

if __name__ == "__main__":
    # Create a list of processes
    processes = []

    # Number of processes to create
    num_processes = 4

    for i in range(num_processes):
        process = multiprocessing.Process(target=file_loader, args=(i,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All processes are done.")

