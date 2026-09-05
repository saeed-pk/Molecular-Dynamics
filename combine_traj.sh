#!/bin/tcsh
#SBATCH --job-name combine_trajectories
#SBATCH --exclude=born,gibbs # can add one or more nodes like kelvin,joule,gibbs,zeus,planck
#SBATCH --nodes=1
##SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=2
#SBATCH --ntasks-per-node=1
#SBATCH --output job.out
#SBATCH --error job.err

source /data/software/amber24/amber24.sh


#/data/software/amber24/bin/cpptraj -i sasa.in
/data/software/amber24/bin/cpptraj -i cluster.traj
#/data/software/amber24/bin/cpptraj -i BDP-RFP-distance.traj
#/data/software/amber24/bin/cpptraj -i H-Bond.traj
#/data/software/amber24/bin/cpptraj -i pi_pi_Stacking.traj
#/data/software/amber24/bin/cpptraj -i rmsd.in
#/data/software/amber24/bin/cpptraj -i Dihedral_Angle.traj
