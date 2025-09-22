# Cluster wrapper for move
## Problem
We want to abstract away cluster submission system, for any command, for hyper parameter sweep. 

## Usage
There are two usages. 
1. submit any single command from CLI.
```
python -m move_utils.move_wrapper [--sl_time 1  --sl_ngpu 1] [YOUR CMD]
```

Toy example

```
python -m move_utils.move_wrapper [--sl_time 1  --sl_ngpu 1] bash 
```


2. hyperparam sweep in python script with the help of hydra

```
inside of your `main.py` 
@hydra.main()
@move_utils.slurm_engine()
def main(cfg)
    # do something
```

In command line:
```
cd examples
python -m hello_no_torch [+engine=move] 
```
