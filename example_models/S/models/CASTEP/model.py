import os
from distutils import spawn
from ase.calculators.castep import Castep

model_abs_dir = os.path.abspath(os.path.dirname(__file__))

mpirun = "srun"
mpirun_args = "srun --distribution=block:block --hint=nomultithread"
castep = "castep.mpi"

os.environ['CASTEP_COMMAND'] = '{0} {1} {2}'.format(mpirun, mpirun_args, castep)

no_checkpoint = True

def start(test_name):
    global calculator
    calculator = Castep(directory=test_name,
                        cut_off_energy=300,
                        spin_polarized=False,
                        opt_strategy='speed',
                        xc_functional='PBEsol',
                        max_scf_cycles=250,
                        calculate_stress=True,
                        smearing_width='0.04',
                        mixing_scheme='pulay',
                        kpoints_list='0 0 0 1',
                        species_pot = ("Si","{}/S_C19_PBESOL_OTF-FromArcher2-Castep20P11.usp".format(model_abs_dir)),
                        perc_extra_bands=100)
