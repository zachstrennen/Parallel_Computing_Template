from trial_division import trial_division
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Print cpu count
    print(mp.cpu_count())

    mp.set_start_method('spawn')

    integers = []
    f = open("./integers.dat", "r")
    for line in f:
        integers.append(int(line.rstrip("\n")))
    f.close()
    k_list = [1, 2, 3, 4, 5, 6, 7, 8]
    factors = []
    primes = []
    time_list = []
    # Find prime numbers
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

    f = open("factors.dat", "w")
    for factor_list in factors:
        f.write(str(factor_list) + "\n")
    f.close()

    f = open("primes.dat", "w")
    for prime in primes:
        f.write(str(prime) + "\n")
    f.close()

    # Calculate speedup
    s_list = [time_list[0] / x for x in time_list]

    # Plot k against speedup
    plt.plot(k_list, s_list)
    plt.xlabel('k')
    plt.ylabel('Speedup')
    plt.show()
