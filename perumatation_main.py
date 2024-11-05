from graph_data import graph_data
import permutation

if __name__ == "__main__":
    permutations = permutation.sjt(graph_data[0])
    hamiltonians = permutation.check_hamiltonian(graph_data[0], permutation.sjt(graph_data[0]))
    optimals = permutation.optimal_cycles(graph_data[0], permutation.sjt(graph_data[0]))
    largest_clique = permutation.get_largest_clique(graph_data[0])

    print(f"Permutations: {permutations}", f"Hamiltonian Cycles: {hamiltonians}", f"Optimal Cycles {optimals}",f"Largest Clique {largest_clique}" )
    