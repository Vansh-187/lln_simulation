import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--repeats", type=int, required=True)
    parser.add_argument("--output", type=str, required=True)
    return parser.parse_args()

def lln_sim():
    args = parse_args()
    means = []
    for _ in range(args.repeats):
        samples = np.random.randint(1,args.n + 1, size=args.k)
        means.append(samples.mean())
    
    with open(args.output,"w") as f:
        for m in means:
            f.write(f"{m}\n")


lln_sim()