from matplotlib import pyplot as plt
import os
from DLA import DLA

def save_dendrite_and_charts():
    dla = DLA(n_particles=10000)
    dla.build_dendritic_structure()
    
    print(f"Execution time: {dla.execution_time/60:.2f} minutes")

    if not os.path.isdir("images"):
        os.mkdir("images")

    plt.imshow(dla.matrix, cmap='Blues', interpolation='none')
    plt.savefig("images/matrix.png", dpi=700)
    plt.close()

    plt.figure()
    plt.plot(dla.growth_time, list(range(0, dla.n_particles+1)))
    plt.xlabel("Time (sec)")
    plt.ylabel("# Particles")
    plt.title("Growth of the number of particles over time")
    plt.savefig("images/particles_growth.png", dpi=700)
    plt.close()

    plt.figure()
    plt.plot(dla.growth_time , dla.structure_length)
    plt.xlabel("Time (sec)")
    plt.ylabel("Length (# particles)")
    plt.title("Structure length growth over time")
    plt.savefig("images/length_growth.png", dpi=700)
    plt.close()

def save_gif():
    dla = DLA(n_particles=10000)
    dla.build_dendritic_structure(GIF=True)
    
    print(f"Execution time: {dla.execution_time/60:.2f} minutes")

def main():
    save_gif()

if __name__ == '__main__':
    main()