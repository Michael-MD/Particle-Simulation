# Particle-Simulation
Simulation of particle motion due to electric and magnetic fields

Simulates particle motion using numerical runge-kutta method, more specifically Euler's method by solving the lorentz force equaiton in all directions and plotting the results.
The initial conditions for the velocity, as well as position can be set. The electric and magnetic fields are set as constants in each direction but this can be changed by defining them as functons. The step size needs to also be manually set, I found that for cyclic motion the step size needs to be much smaller than say cyloid motion.
This was written by myself and is open source for anyone to use, I would appreciate it if you let me know first via email at mdei0001@student.monash.edu.
I have a preloaded example but the parameters can be changed from there to whatever you want. It should also be noted that everything is in cartesian coordinates and will need to be converted to such appropriately when necessary
