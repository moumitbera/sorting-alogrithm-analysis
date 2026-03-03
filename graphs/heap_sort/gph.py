import matplotlib.pyplot as plt


# Input sizes
n = [1000, 2000, 5000, 10000, 20000, 50000]

# All the comparisons

sorted_comp = [17583, 39159, 112126, 244460, 529074, 1455438]
reverse_comp = [15965, 35964, 103227, 226682, 493307, 1366047]
random_comp = [16834, 37713, 107679, 235392, 510769, 1409872]
duplicate_comp = [16447, 36610, 104328, 227573, 492690, 1357730]
nearly_comp = [17484, 39065, 111705, 243495, 527166, 1451360]

plt.figure()
plt.plot(n, sorted_comp, marker='o', label='Sorted')
plt.plot(n, reverse_comp, marker='o', label='Reverse Sorted')
plt.plot(n, random_comp, marker='o', label='Random')
plt.plot(n, duplicate_comp, marker='o', label='Duplicate Heavy')
plt.plot(n, nearly_comp, marker='o', label='Nearly Sorted')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Comparisons')
plt.title('Heap Sort - Comparisons (Log-Log Scale)')
plt.legend()
plt.grid(True)

plt.savefig("comparisons.png", dpi=300)
plt.close()


# For swaps

sorted_swaps = [9708, 21300, 60932, 131956, 282878, 773304]
reverse_swaps = [8316, 18708, 53436, 116696, 254334, 698892]
random_swaps = [9061, 20156, 57110, 124211, 268426, 737469]
duplicate_swaps = [8724, 19299, 54640, 118732, 256236, 703605]
nearly_swaps = [9647, 21348, 60388, 130821, 281754, 771193]

plt.figure()
plt.plot(n, sorted_swaps, marker='o', label='Sorted')
plt.plot(n, reverse_swaps, marker='o', label='Reverse Sorted')
plt.plot(n, random_swaps, marker='o', label='Random')
plt.plot(n, duplicate_swaps, marker='o', label='Duplicate Heavy')
plt.plot(n, nearly_swaps, marker='o', label='Nearly Sorted')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Swaps')
plt.title('Heap Sort - Swaps (Log-Log Scale)')
plt.legend()
plt.grid(True)

plt.savefig("swaps.png", dpi=300)
plt.close()


# for runtime

sorted_rt = [0.097, 0.441, 1.241, 2.035, 3.748, 6.988]
reverse_rt = [0.111, 0.334, 1.233, 2.208, 3.514, 6.431]
random_rt = [0.176, 0.320, 0.952, 2.429, 3.170, 8.692]
duplicate_rt = [0.219, 0.551, 1.320, 2.209, 3.849, 7.617]
nearly_rt = [0.289, 0.292, 1.289, 1.622, 3.853, 7.403]

plt.figure()
plt.plot(n, sorted_rt, marker='o', label='Sorted')
plt.plot(n, reverse_rt, marker='o', label='Reverse Sorted')
plt.plot(n, random_rt, marker='o', label='Random')
plt.plot(n, duplicate_rt, marker='o', label='Duplicate Heavy')
plt.plot(n, nearly_rt, marker='o', label='Nearly Sorted')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Runtime (ms)')
plt.title('Heap Sort - Runtime (Log-Log Scale)')
plt.legend()
plt.grid(True)

plt.savefig("runtime.png", dpi=300)
plt.close()

print("All Heap Sort graphs generated successfully.")
