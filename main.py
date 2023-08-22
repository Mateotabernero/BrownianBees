import numpy as np 
import matplotlib.pyplot as plt 
import math  

def bees(num_particles, num_steps):
    t = 0 
    times = np.random.exponential(scale = 1, size = num_particles)
    particles  =  np.zeros((num_particles, 2))
    barycenter =  np.zeros(2) 

    for w in range(num_steps): 
        j = np.argmin(times) 
        new_t = times[j]
        
        particles = [p + step(new_t-t) for p in particles]  
        

        barycenter = np.mean(particles, axis = 0) 
        dist_from_barycenter = np.linalg.norm(particles - barycenter) 

        new_particle = particles[j] 
        
        j = np.argmin(dist_from_barycenter)
        new_time = new_t + np.random.exponential(scale = 1) 
        times[j] =  new_t + np.random.exponential(scale = 1) 

        particles= np.vstack((particles, new_particle[np.newaxis, :])) 
        times = np.append(times, new_time) 

        j = np.argmin(dist_from_barycenter) 
        times = np.delete(times, j, axis = 0) 
        
        particles = np.delete(particles, j, axis = 0 ) 

        
    return particles 


# I can separate the function that does one simulation and in this function only make a call to that function for each simulation 
def bees(num_particles, num_steps, num_simulations):
    all_particles = [0 for _ in range(num_simulations)]
    for l in range(num_simulations): 
        all_particles[l] = one_bees(num_particles, num_steps) 
    return all_particles 
  
