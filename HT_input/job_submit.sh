#!/bin/bash
#SBATCH -J job_submitter        # Job name
#SBATCH -o job_submission.log       # Name of stdout output file
#SBATCH -e job.e%j       # Name of stderr error file
#SBATCH -p normal     # Queue (partition) name
#SBATCH -N 1               # Total # of nodes
#SBATCH -n 1              # Total # of mpi tasks
#SBATCH -t 24:00:00        # Run time (hh:mm:ss)
#SBATCH -A TG-DMR150099       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...
# Launch MPI code...


my_array=()
for folder in */; do my_array+=($folder); done
echo "${my_array[*]}"

max_job=50

for i in ${my_array[@]:117:119}  ; do
    cd $i;
    cp ../INCAR ./INCAR;
    cp ../jobvasp_pbe .;
    echo $PWD;
    
    num_row=$(expr $(squeue -u tg833140 | wc -l) - 1);
    echo $num_row
    while [ $num_row -ge $max_job ]; 
        do sleep 360; 
        num_row=$(expr $(squeue -u tg833140 | wc -l) - 1);
    done
    sbatch jobvasp_pbe;
    cd ..;
    echo "current: $i";
done
