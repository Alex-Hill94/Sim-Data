# Sim-Data
## Repository for the storage of simulation data. Descrition of data arrays below taken from tng-project.org/data/ 

SubGroupNumber: -99 if a satellite, 0 if a central

GroupNumber: Idenifier of the host FOF halo

COP_x: Spatial position within the periodic box of the subhalo's particle with the minium gravitational potential energy. Mpc, physical, h-free coordinates.

GalaxyID: Unique identifier of each subhalo, running 0, 1, 2, ..., n-1, n

Flags: Flag to indicate whether subhalo is likely of comsmological origin. For more information see https://www.tng-project.org/data/docs/background/#subhaloflag. Only in baryonic simulation files.

StellarMass: Sum of stellar particle masses bound to a subhalo. Only in baryonic simulation files. [1e10 solar masses]

HaloMass: Sum of particle masses bound to host FOF halo. [1e10 solar masses]
