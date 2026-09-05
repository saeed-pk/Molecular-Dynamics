#!/bin/bash
########################################################
#SBATCH -J D1Cl1_aMD  # job name
#SBATCH -o stdout.%j.txt
#SBATCH -e stderr.%j.txt
#SBATCH -A $ACCOUNT
#SBATCH -q gp_resa            # Priority queue for GPP nodes
#SBATCH --ntasks=112          # number of total cores
#SBATCH --tasks-per-node=112  #number of cores per node max 112/node
#SBATCH --mail-user=saeed.ahmed@upc.edu
#SBATCH --mail-type=end
##SBATCH --get-user-env
#SBATCH -t 72:00:00  # WALLTIME
########################################################

export SRUN CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

module load amber/24
######################
cd $TMPDIR

mkdir run.${SLURM_JOBID}
cd run.${SLURM_JOBID}

  # Directories and binaries definition
  DIR=/gpfs/projects/upc31/ahmed/D-Series/R6/D1Cl1/aMD/run03
  EXE=/apps/GPP/AMBER/24/INTEL/IMPI/bin/pmemd.MPI
  name="D1Cl1_R6_TIP3P"

# Copy initial files
cp $DIR/$name.prmtop .
cp $DIR/$name.inpcrd .
#cp $DIR/restrt restrt
cp $DIR/amd_$name.rst7 restrt
cp $DIR/amd.in .

############ start job###########
# Run aMD simulation
echo "Starting aMD simulation..."
srun ${EXE} -O -i amd.in -c restrt -p $name.prmtop -x $name.nc -o amd_${name}.mdout -r amd_${name}.rst7

if [ $? -eq 0 ]; then
    echo "aMD simulation completed successfully."
else
    echo "Error: aMD simulation failed."
    exit 1
fi

gzip ${name}.nc

# Recovering files
cd ..
tar cvzf run.${SLURM_JOBID}.tar.gz run.${SLURM_JOBID}
cp run.${SLURM_JOBID}.tar.gz ${DIR}

exit 0

