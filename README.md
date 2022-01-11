# DLA Algorithm Implementation

 ![DLA simulation](/gifs/DLA60X.gif)

## What is DLA?

DLA stands for diffusion-limited aggregation. It is a technique to build dendritic structures.

There are multiple implementations of this algorithm in many languages. This implementation is written in Python and its operation is detailed below.

### Algorithm operation 
- An initial particle is positioned in the middle of a m x m launching rectangle. This launching rectangle is centered within an n x n grid, where m < n.

- One at a time, the particles are released from random positions within the launching rectangle to start random walks (the particle has the same probability of moving to the right, left, up and down).

- If the particle has contact with another particle, it can be its neighbor in the north, south, east or west, the particle adheres to the neighboring particle which results in the formation of a larger structure.

- If the particle travels too far and reaches the edge of the grid, the simulation removes the particle and launches another particle from the launching rectangle to start a new random walk.

## Instructions for use

### The DLA algorithm is implemented as a method (build_dendritic_structure method) within the DLA class which can be used in two ways

1. The first way is to run the simulation and obtain an image of the final state of the dendrite plus some graphs associated with its growth over time. In this case the GIF parameter of the build_dendritic_structure method is set to False.

    First way to use the DLA class, example:
    ```
    dla = DLA(n_particles=10000)
    dla.build_dendritic_structure()

    plt.imshow(dla.matrix, cmap='Blues', interpolation='none')
    plt.savefig("images/matrix.png", dpi=700)
    plt.close()
    ```
    ![Matrix](/images/matrix.png)

    ```
    plt.figure()
    plt.plot(dla.growth_time, list(range(0, dla.n_particles+1)))
    plt.xlabel("Time (sec)")
    plt.ylabel("# Particles")
    plt.title("Growth of the number of particles over time")
    plt.savefig("images/particles_growth.png", dpi=700)
    plt.close()
    ```

    ![Particles growth](/images/particles_growth.png)

    ```
    plt.figure()
    plt.plot(dla.growth_time , dla.structure_length)
    plt.xlabel("Time (sec)")
    plt.ylabel("Length (# particles)")
    plt.title("Structure length growth over time")
    plt.savefig("images/length_growth.png", dpi=700)
    plt.close()
    ```

    ![Length growth](/images/length_growth.png)


2. The second way is to generate a GIF file of the simulation in which you can see how the dendrite grows as the simulation runs. In this case the GIF parameter of the build_dendritic_structure method is set to True.

    Second way to use the DLA class, example:
    ```
    dla = DLA(n_particles=10000)
    dla.build_dendritic_structure(GIF=True)
    ```

    After executing the above code, two new folders will appear in the project directory, a 'frames' folder and a 'media' folder. The 'frames' folder, as its name indicates, contains all the frames that will be used in the construction of the GIF. The 'media' folder contains the GIF generated with the frames in the 'frames' folder, this GIF needs to be processed. To process the generated GIF it is recommended to use FFmpeg.

    *The 'frames' and 'media' folders are not included in this repository because they contain many preprocessed or 'intermediate' files which together weigh many megabytes and are not relevant. These folders with their files can be easily obtained by running the above code.*

    The following commands were used to process the GIF. (Assuming you are positioned in the project directory change the current directory to 'media' with the command `cd media` or some similar command depending on your system)
    
    1. Convert from .gif to .mp4

        `ffmpeg -i DLA.gif DLA.mp4`
    2. Speed up the video by 60X

        `ffmpeg -i DLA.mp4 -filter:v "setpts=PTS/60" DLA60X.mp4`
    3. Convert from .mp4 to .gif

        `ffmpeg -i DLA60X.mp4 -vf "fps=10,scale=1920:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 DLA60X.gif`
    
    After having processed the .gif file, the following result is obtained:

    ![DLA simulation](/gifs/DLA60X.gif)