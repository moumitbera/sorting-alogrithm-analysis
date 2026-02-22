import matplotlib.pyplot as plt

# -------------------------------
# Data
# -------------------------------

n = [1000, 2000, 5000, 10000, 20000, 50000]

# Comparisons
sorted_comp = [5044, 11088, 32004, 69008, 148016, 401952]
reverse_comp = [4932, 10864, 29804, 64608, 139216, 382512]
random_comp = [8702, 19401, 55231, 120452, 260866, 718186]
dup_comp = [8616, 19196, 54597, 118924, 257324, 707493]
near_comp = [7654, 17252, 50630, 111601, 243420, 673777]

# Writes (same across all inputs)
writes = [19952, 43904, 123616, 267232, 574464, 1568928]

# Runtime (ms)
sorted_time = [0.162, 0.221, 0.841, 1.534, 2.416, 5.021]
reverse_time = [0.157, 0.349, 0.823, 0.878, 2.402, 5.073]
random_time = [0.162, 0.297, 1.227, 2.190, 2.950, 7.713]
dup_time = [0.214, 0.389, 1.087, 1.881, 3.163, 5.637]
near_time = [0.089, 0.371, 0.645, 1.626, 2.533, 5.087]


# =====================================================
# 1️⃣ Comparisons Graph
# =====================================================

plt.figure(figsize=(8,6))

plt.plot(n, sorted_comp, marker='o', label='Sorted')
plt.plot(n, reverse_comp, marker='o', label='Reverse Sorted')
plt.plot(n, random_comp, marker='o', label='Random')
plt.plot(n, dup_comp, marker='o', label='Duplicate Heavy')
plt.plot(n, near_comp, marker='o', label='Nearly Sorted')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('N')
plt.ylabel('Comparisons')
plt.title('N vs Comparisons (Merge Sort)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("merge_comparisons.png", dpi=300)
plt.savefig("graphs/merge sort/output/comparisons.png", dpi=300, bbox_inches="tight")


# =====================================================
# 2️⃣ Writes Graph
# =====================================================

plt.figure(figsize=(8,6))

plt.plot(n, writes, marker='o')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('N')
plt.ylabel('Writes')
plt.title('N vs Writes (Merge Sort)')
plt.grid(True)

plt.tight_layout()
plt.savefig("merge_writes.png", dpi=300)
plt.savefig("graphs/merge sort/output/writes.png", dpi=300, bbox_inches="tight")


# =====================================================
# 3️⃣ Runtime Graph
# =====================================================

plt.figure(figsize=(8,6))

plt.plot(n, sorted_time, marker='o', label='Sorted')
plt.plot(n, reverse_time, marker='o', label='Reverse Sorted')
plt.plot(n, random_time, marker='o', label='Random')
plt.plot(n, dup_time, marker='o', label='Duplicate Heavy')
plt.plot(n, near_time, marker='o', label='Nearly Sorted')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('N')
plt.ylabel('Run Time (ms)')
plt.title('N vs Run Time (Merge Sort)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("merge_runtime.png", dpi=300)
plt.savefig("graphs/merge sort/output/runtime.png", dpi=300, bbox_inches="tight")
