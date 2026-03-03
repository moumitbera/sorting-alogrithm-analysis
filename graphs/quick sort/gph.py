import matplotlib.pyplot as plt
import numpy as np
import os

# folder making

folders = [
    "graphs/quick_sort/last",
    "graphs/quick_sort/random",
    "graphs/quick_sort/median",
    "graphs/quick_sort/three_way",
    "graphs/quick_sort/comparison"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# data set / array size

n = np.array([1000, 2000, 5000, 10000, 20000, 50000])

# store data

quick_data = {

"last": {
    "Sorted":        {"comp":[499500,1999000,12497500,49995000,199990000,1249975000],
                      "swap":[500499,2000999,12502499,50004999,200009999,1250024999],
                      "time":[2.612,6.116,31.379,123.657,487.679,3042.939]},
    "Reverse":       {"comp":[499500,1999000,12497500,49995000,199990000,1249975000],
                      "swap":[250499,1000999,6252499,25004999,100009999,625024999],
                      "time":[2.365,6.002,27.811,111.774,434.212,2736.875]},
    "Random":        {"comp":[11093,24606,70462,154872,335646,939010],
                      "swap":[6602,13972,40539,86768,186663,519042],
                      "time":[0.113,0.198,0.857,1.042,2.132,5.480]},
    "Duplicate":     {"comp":[29860,110470,650148,2552856,10108304,62747071],
                      "swap":[28294,106745,642472,2537276,10079031,62672281],
                      "time":[0.329,0.798,2.523,7.282,26.917,159.106]},
    "Nearly":        {"comp":[35060,87712,232756,528747,1141526,3275758],
                      "swap":[18768,54296,147878,322017,684700,1868302],
                      "time":[0.278,0.339,1.384,2.260,2.916,9.345]}
},

"random": {
    "Sorted":        {"comp":[11005,24798,71099,152395,340851,949808],
                      "swap":[6915,15260,42925,90054,199013,558023],
                      "time":[0.125,0.253,0.654,0.972,1.916,4.324]},
    "Reverse":       {"comp":[10965,24880,70841,154477,338505,931313],
                      "swap":[7006,14724,41206,90018,194880,530666],
                      "time":[0.129,0.268,0.691,1.058,2.254,3.726]},
    "Random":        {"comp":[11067,24965,70637,155077,335635,944695],
                      "swap":[7060,15700,43158,92753,199184,551320],
                      "time":[0.080,0.225,0.638,1.321,2.942,5.335]},
    "Duplicate":     {"comp":[30179,109882,649842,2552566,10105662,62757000],
                      "swap":[29653,109006,647505,2546928,10091429,62737197],
                      "time":[0.176,0.977,3.147,8.248,27.216,158.370]},
    "Nearly":        {"comp":[29928,25127,71853,152985,338681,929037],
                      "swap":[29147,15291,42085,90537,196585,522281],
                      "time":[0.294,0.289,0.347,1.424,2.370,4.204]}
},

"median": {
    "Sorted":        {"comp":[9520,21033,60678,131343,282672,782782],
                      "swap":[4960,10916,30713,66421,142837,398052],
                      "time":[0.038,0.171,0.372,0.465,1.583,3.198]},
    "Reverse":       {"comp":[15849,36177,106182,234923,518623,1433133],
                      "swap":[9583,21655,63403,139308,306792,837620],
                      "time":[0.111,0.299,0.654,0.858,2.505,3.895]},
    "Random":        {"comp":[11359,25132,70679,152315,329516,898486],
                      "swap":[6730,14563,40710,85888,184615,505524],
                      "time":[0.145,0.335,0.894,1.436,2.865,4.807]},
    "Duplicate":     {"comp":[32293,114788,661839,2576089,10150915,62872424],
                      "swap":[29055,108243,645353,2543247,10083102,62704376],
                      "time":[0.174,0.937,2.989,8.087,27.452,158.825]},
    "Nearly":        {"comp":[14592,33803,91932,211518,460362,1276004],
                      "swap":[5147,11482,33384,70675,150710,414648],
                      "time":[0.079,0.270,0.431,1.403,2.420,4.817]}
},

"three_way": {
    "Sorted":        {"comp":[21665,57882,215416,588191,1618052,6216650],
                      "swap":[19930,54427,206937,571450,1585041,6133788],
                      "time":[0.168,0.370,1.588,3.120,5.247,18.236]},
    "Reverse":       {"comp":[17401,45284,164131,440765,1196249,4537390],
                      "swap":[15651,41811,155575,423844,1162817,4454857],
                      "time":[0.150,0.457,0.677,1.915,5.085,14.248]},
    "Random":        {"comp":[10369,23190,65506,144977,313527,848999],
                      "swap":[8705,19869,57232,128402,280328,766018],
                      "time":[0.163,0.342,0.916,1.596,2.999,5.281]},
    "Duplicate":     {"comp":[4212,8117,20539,41634,80272,205335],
                      "swap":[3166,6070,15491,31587,60224,155287],
                      "time":[0.062,0.060,0.287,0.560,0.832,1.797]},
    "Nearly":        {"comp":[12178,27444,77100,163694,351928,968784],
                      "swap":[10510,24087,68644,146736,351928,883585],
                      "time":[0.122,0.292,0.810,1.340,1.569,4.925]}
}
}

# plotting func

def plot_metric(pivot_name, metric_key, ylabel, save_path):
    plt.figure(figsize=(8,6))
    
    for input_type in quick_data[pivot_name]:
        plt.plot(n,
                 quick_data[pivot_name][input_type][metric_key],
                 marker='o',
                 label=input_type)
    
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Array Size (n)")
    plt.ylabel(ylabel)
    plt.title(f"Quick Sort - {pivot_name.replace('_',' ').title()} ({ylabel})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

# the 12 different graphs

for pivot in quick_data:
    plot_metric(pivot, "comp", "Comparisons",
                f"graphs/quick_sort/{pivot}/comparisons.png")
    plot_metric(pivot, "swap", "Swaps",
                f"graphs/quick_sort/{pivot}/swaps.png")
    plot_metric(pivot, "time", "Runtime (ms)",
                f"graphs/quick_sort/{pivot}/runtime.png")

# the 3 comparisions graphs

def comparison_graph(input_type, metric_key, ylabel, filename):
    plt.figure(figsize=(8,6))
    
    for pivot in quick_data:
        plt.plot(n,
                 quick_data[pivot][input_type][metric_key],
                 marker='o',
                 label=pivot.replace("_"," ").title())
    
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Array Size (n)")
    plt.ylabel(ylabel)
    plt.title(f"Quick Sort Comparison - {input_type} ({ylabel})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"graphs/quick_sort/comparison/{filename}", dpi=300)
    plt.close()

comparison_graph("Sorted", "time", "Runtime (ms)", "runtime_sorted.png")
comparison_graph("Random", "time", "Runtime (ms)", "runtime_random.png")
comparison_graph("Duplicate", "time", "Runtime (ms)", "runtime_duplicate.png")

print("All 15 graphs generated successfully.")
