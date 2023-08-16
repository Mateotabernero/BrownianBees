import numpy as np 
import matplotlib.pyplot as plt 
import math  
from sklearn.cluster import KMeans
from collections import Counter 



# I can separate the function that does one simulation and in this function only make a call to that function for each simulation 
def bees_2(num_particles, num_steps, num_simulations):
    all_particles = [0 for _ in range(num_simulations)]
    for l in range(num_simulations): 
        t = 0 
        times = [0 for _ in range(num_particles)]
        times_to = np.random.exponential(scale = 1, size = num_particles)
        for i in range(num_particles):
            times[i] = times_to[i]
        particles =  [[0,0] for _ in range(num_particles)]
        barycenter = [0.0] 
        dist_from_barycenter = [0 for _ in range(num_particles)]
        
        for w in range(num_steps): 
            j = np.argmin(times) 
            new_t = times[j]
            
            for i in range(len(particles)):
                particles[i] = sum_2(particles[i], step(new_t-t)) 
            
            barycenter = calc_barycenter(particles) 
            dist_from_barycenter = np.zeros(len(particles)) 
            for i in range(len(particles)):
                dist_from_barycenter[i] = dist(particles[i], barycenter) 
            
            new_particle = particles[j] 
            
            k = np.argmin(dist_from_barycenter)
            new_time = new_t + np.random.exponential(scale = 1) 
            times[k] =  new_t + np.random.exponential(scale = 1) 
            
            particles.append(new_particle) 
            times.append(new_time) 
            
            k = np.argmin(dist_from_barycenter) 
            del times[k]
            del particles[k]
        all_particles[l] = particles 
    return all_particles 
  
