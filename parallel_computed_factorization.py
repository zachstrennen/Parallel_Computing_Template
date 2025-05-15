from trial_division import trial_division
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Store and print cpu count
    cpu_count = mp.cpu_count()
    print("Your CPU count is :", cpu_count)

    # Set start method
    mp.set_start_method('spawn')

    # Read in integers from data file
    integers = []
    f = open("data/integers.dat", "r")
    for line in f:
        integers.append(int(line.rstrip("\n")))
    f.close()

    # List of integers from 1 to cpu_count
    k_list = list(range(1, cpu_count + 1))

    # Lists to store factors, primes, and runtime for each cpu count
    factors = []
    primes = []
    time_list = []

    # Find prime numbers and factors
    for k in k_list:
        with mp.Pool(k) as pool:
            # Start timing
            start_time = time.time()
            for res in pool.map(trial_division, integers):
                factors.append(res)
                if len(res) == 1:
                    primes.append(res[0])
            # Store time
            time_list.append(time.time() - start_time)

    # Write factors to data file
    f = open("data/factors.dat", "w")
    for factor_list in factors:
        f.write(str(factor_list) + "\n")
    f.close()

    # Write primes to data file
    f = open("data/primes.dat", "w")
    for prime in primes:
        f.write(str(prime) + "\n")
    f.close()

    # Calculate speedup (how many times faster)
    s_list = [time_list[0] / x for x in time_list]

    # Plot cpu count against speedup
    plt.plot(k_list, s_list)
    plt.xlabel('cpu Count')
    plt.ylabel('Speedup')
    plt.show()
