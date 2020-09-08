import numpy as np
import illustris_python as il
import pickle as pkl
import pandas as pd


sim = 'TNG300-1'
dmo = False
#physical = True
#hless = True


if dmo:
    sim = sim+'-Dark'

basePath = '/hpcdata0/simulations/IllustrisTNG/'+sim+'/output/'

fields_sub = ['SubhaloGrNr', 'SubhaloMass', 'SubhaloParent', 'SubhaloPos']

if dmo == False:
    fields_sub = fields_sub + ['SubhaloFlag', 'SubhaloMassType']

fields_grp = ['GroupFirstSub', 'GroupNsubs', 'Group_M_Crit200']

subhalos = il.groupcat.loadSubhalos(basePath,99,fields=fields_sub)
halos = il.groupcat.loadHalos(basePath,99,fields=fields_grp)

header = il.groupcat.loadHeader(basePath,99)

h = header['HubbleParam']
z = header['Redshift']
a = 1./(1. + z)

SubGroupNumber = np.zeros(len(subhalos['SubhaloMass']))
SubGroupNumber[:] = -99
cent_idx = halos['GroupFirstSub'][halos['GroupFirstSub'] != -1]
SubGroupNumber[cent_idx] = 0
GroupNumber = subhalos['SubhaloGrNr']
COP = subhalos['SubhaloPos'] * a * h**-1/1000.
COP_x, COP_y, COP_z = COP[:,0], COP[:,1], COP[:,2]
GalaxyID = np.arange(0, len(COP), 1)
HaloMass = halos['Group_M_Crit200'][GroupNumber]*h**-1
SubhaloMass = subhalos['SubhaloMass']*h**-1

if dmo == False:
    StellarMass = subhalos['SubhaloMassType'][:,4]*h**-1
    Flags = subhalos['SubhaloFlag']

    df = pd.DataFrame({"SubGroupNumber": SubGroupNumber,
                        "GroupNumber": GroupNumber,
                        "COP_x": COP_x, 
                        "COP_y": COP_y, 
                        "COP_z": COP_z,
                        "GalaxyID": GalaxyID,
                        "Flags": Flags,
                        "StellarMass": StellarMass,
                        "SubhaloMass": SubhaloMass,
                        "HaloMass": HaloMass})

elif dmo:
    df = pd.DataFrame({"SubGroupNumber": SubGroupNumber,
                    "GroupNumber": GroupNumber,
                    "COP_x": COP_x, 
                    "COP_y": COP_y, 
                    "COP_z": COP_z,
                    "GalaxyID": GalaxyID,
                    "SubhaloMass": SubhaloMass,
                    "HaloMass": HaloMass})


df.to_pickle('./'+sim+'_catalogue.pkl')

