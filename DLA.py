import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
import time
import os

matplotlib.use("Agg")

class DLA:
    def __init__(self, n_particles, N = 400) -> None:
        self.n_particles = n_particles
        self.N = N

    def build_dendritic_structure(self, GIF=False):
        start_time = time.time()

        if GIF:
            import imageio

        if GIF and not os.path.isdir("frames"):
            os.mkdir("frames")
        
        if GIF and not os.path.isdir("media"):
            os.mkdir("media")

        # M < N
        self.M = int(self.N * 0.8)

        self.matrix = np.zeros((self.N, self.N))

        launching_reactangle_x_start = launching_reactangle_y_start = (self.N-self.M) // 2
        launching_reactangle_x_end = launching_reactangle_y_end = (self.N-self.M)//2 + self.M - 1

        seed_x = seed_y = self.N // 2
        self.matrix[seed_y, seed_x] = 1
        self.structure_length = [0, 1]
        structure_x_start = structure_x_end = seed_x

        particles_added = 1

        self.growth_time = [0, round(time.time()-start_time, 3)]

        if GIF:
            plt.imshow(self.matrix, cmap='Blues', interpolation='none')
            plt.savefig("frames/frame1.png", dpi=300)
            plt.close()

        while particles_added < self.n_particles:
            walker_x = random.randint(launching_reactangle_x_start, launching_reactangle_x_end)
            walker_y = random.randint(launching_reactangle_y_start, launching_reactangle_y_end)

            found_neighbor = False
            near_grid_boundary = False

            while not found_neighbor and not near_grid_boundary:
                if walker_x == 0 or walker_x == self.N-1 or walker_y == 0 or walker_y == self.N-1:
                    near_grid_boundary = True

                if not near_grid_boundary:
                    # Left neighbor
                    if self.matrix[walker_y, walker_x-1] == 1:
                        found_neighbor = True
                        self.matrix[walker_y, walker_x] = 1
                        particles_added += 1
                        self.growth_time.append(round(time.time()-start_time, 3))
                        if walker_x > structure_x_end:
                            structure_x_end = walker_x
                        self.structure_length.append(structure_x_end-structure_x_start+1)

                    # Right neighbor
                    elif self.matrix[walker_y, walker_x+1] == 1:
                        found_neighbor = True
                        self.matrix[walker_y, walker_x] = 1
                        particles_added += 1
                        self.growth_time.append(round(time.time()-start_time, 3))
                        if walker_x < structure_x_start:
                            structure_x_start = walker_x
                        self.structure_length.append(structure_x_end-structure_x_start+1)
                    
                    # Top neighbor
                    elif self.matrix[walker_y-1, walker_x] == 1:
                        found_neighbor = True
                        self.matrix[walker_y, walker_x] = 1
                        particles_added += 1
                        self.growth_time.append(round(time.time()-start_time, 3))
                        self.structure_length.append(structure_x_end-structure_x_start+1)

                    # Bottom neighbor
                    elif self.matrix[walker_y+1, walker_x] == 1:
                        found_neighbor = True
                        self.matrix[walker_y, walker_x] = 1
                        particles_added += 1
                        self.growth_time.append(round(time.time()-start_time, 3))
                        self.structure_length.append(structure_x_end-structure_x_start+1)

                if not found_neighbor and not near_grid_boundary:
                    rand = random.randint(1, 4)
                    # Left neighbor
                    if rand == 1:
                        walker_x -= 1
                    # Right neighbor
                    if rand == 2:
                        walker_x += 1
                    # Top neighbor
                    if rand == 3:
                        walker_y -= 1
                    # Bottom neighbor
                    if rand == 4:
                        walker_y += 1

            if GIF and found_neighbor:
                plt.imshow(self.matrix, cmap='Blues', interpolation='none')
                plt.savefig(f"frames/frame{particles_added}.png", dpi=300)
                plt.close()

        if GIF:
            with imageio.get_writer("media/DLA.gif", mode="I") as writer:
                for i in range(1, particles_added+1):
                    frame = imageio.imread(f"frames/frame{i}.png")
                    writer.append_data(frame)

        end_time = time.time()

        self.execution_time = end_time-start_time

        # The growth times will be distorted if the GIF option is activated because
        # to create the GIF the frames must be saved, which in other words corresponds
        # to doing operations in the file system which takes a lot of time.
        # Due to the above-mentioned, the growth_time list is discarded if the GIF option is activated.
        if GIF:
            self.growth_time = None