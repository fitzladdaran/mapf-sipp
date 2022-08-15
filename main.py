from instance.import_instance import import_instance
from solver.solver import Solver
from algorithms.a_star import A_star
import argparse
import glob

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = "Multi-Agent Pathfinding using Safe-Interval Path Finding Algorithms")
    parser.add_argument("--instance", type = str, default = None, help = "File name of instance(s)")
    parser.add_argument("--alg", type = str, default = None, help = "Name of algorithm to use")
    args = parser.parse_args()
    
    for f in sorted(glob.glob(args.instance)):
        my_map, agents = import_instance(f)
        
        if args.alg == "astar":
            print("Running: A* algorithm")
            print(agents)
            Solver(my_map, agents, A_star)
        elif args.alg == "asipp":
            print("Running: Anytime Safe-Interval Path Planning")
        
        
        






