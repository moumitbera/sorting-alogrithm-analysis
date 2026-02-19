import matplotlib.pyplot as plt

# --------------------- DATA ---------------------

N = [1000, 2000, 5000, 10000, 20000, 50000]

# ---------------- Comparisons ----------------
sorted_comp = [999, 1999, 4999, 9999, 19999, 49999]
reverse_comp = [499500, 1999000, 12497500, 49995000, 199990000, 1249975000]
random_comp = [248288, 1004094, 6242496, 25077297, 100175744, 624949001]
duplicate_comp = [237236, 952758, 5942234, 23774823, 95014971, 593828027]
nearly_comp = [34132, 122705, 764749, 3109850, 12459258, 77414619]

# ---------------- Shifts ----------------
sorted_shift = [0, 0, 0, 0, 0, 0]
reverse_shift = [499500, 1999000, 12497500, 49995000, 199990000, 1249975000]
random_shift = [247295, 1002101, 6237505, 25067305, 100155575, 624899012]
duplicate_shift = [236239, 950761, 5937238, 23764827, 94994975, 593778030]
nearly_shift = [33133, 120706, 759750, 3099851, 12439259, 77364620]

# ---------------- Runtime (ms) ----------------
sorted_time = [0.016, 0.015, 0.016, 0.074, 0.150, 0.374]
reverse_time = [1.304, 4.337, 18.097, 69.263, 272.022, 1700.455]
random_time = [1.040, 2.727, 10.000, 34.422, 136.546, 849.583]
duplicate_time = [0.992, 2.561, 9.565, 33.194, 129.383, 806.148]
nearly_time = [0.173, 0.602, 2.324, 5.880, 18.295, 105.793]

# ================= GRAPH 1 =================
plt.figure()
plt.plot(N, sorted_comp, marker='o', label="Sorted")
plt.plot(N, reverse_comp, marker='o', label="Reverse Sorted")
plt.plot(N, random_comp, marker='o', label="Random")
plt.plot(N, duplicate_comp, marker='o', label="Duplicate Heavy")
plt.plot(N, nearly_comp, marker='o', label="Nearly Sorted")

plt.yscale("log")
plt.xlabel("N")
plt.ylabel("Comparisons")
plt.title("N vs Comparisons")
plt.legend()
plt.grid(True)
plt.show()

# ================= GRAPH 2 =================
plt.figure()
plt.plot(N, sorted_shift, marker='o', label="Sorted")
plt.plot(N, reverse_shift, marker='o', label="Reverse Sorted")
plt.plot(N, random_shift, marker='o', label="Random")
plt.plot(N, duplicate_shift, marker='o', label="Duplicate Heavy")
plt.plot(N, nearly_shift, marker='o', label="Nearly Sorted")

plt.yscale("log")
plt.xlabel("N")
plt.ylabel("Shifts")
plt.title("N vs Shifts")
plt.legend()
plt.grid(True)
plt.show()

# ================= GRAPH 3 =================
plt.figure()
plt.plot(N, sorted_time, marker='o', label="Sorted")
plt.plot(N, reverse_time, marker='o', label="Reverse Sorted")
plt.plot(N, random_time, marker='o', label="Random")
plt.plot(N, duplicate_time, marker='o', label="Duplicate Heavy")
plt.plot(N, nearly_time, marker='o', label="Nearly Sorted")

plt.yscale("log")
plt.xlabel("N")
plt.ylabel("Run Time (ms)")
plt.title("N vs Run Time")
plt.legend()
plt.grid(True)
plt.savefig("graphs/comparisons.png", dpi=300, bbox_inches="tight")
plt.savefig("graphs/shifts.png", dpi=300, bbox_inches="tight")
plt.savefig("graphs/runtime.png", dpi=300, bbox_inches="tight")

