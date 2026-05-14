import argparse
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfolder", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    return parser.parse_args()

def plot():
    args = parse_args()
    n = os.path.basename(args.inputfolder)
    files = sorted(
    [f for f in os.listdir(args.inputfolder) if f.endswith('.txt')],
    key=lambda x: int(x.split('.')[0])
    )
    data = [
        np.loadtxt(os.path.join(args.inputfolder, file))
        for file in files
    ]

    plt.figure(figsize=(10, 6))

    labels = [f"k={file.split('.')[0]}" for file in files]

    plt.boxplot(
        data,
        tick_labels=labels,
        medianprops=dict(color='black', linewidth=2)
    )

    
    plt.ylabel("Mean")
    plt.title(f"Testing Draws for {n}")

    plt.savefig(args.output, dpi=300, bbox_inches='tight')

plot()