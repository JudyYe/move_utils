import os
from hydra import main
# from jutils import slurm_utils
# import sys

from move_utils.slurm_utils import slurm_engine


@main(config_path="configs", config_name="hello", version_base=None)
@slurm_engine()
def hello(cfg):
    
    print(f"hello world! a={cfg.a} b={cfg.b}")
    print('cwd',os.getcwd())
    #touch file test_{cfg.a}_{cfg.b}.txt
    os.system(f"touch test_{cfg.a}_{cfg.b}.txt")


if __name__ == "__main__":
    print('outside', hello)
    hello()