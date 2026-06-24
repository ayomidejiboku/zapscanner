# bad.py
import subprocess
import yaml
import pickle

def run_command(cmd):
    return subprocess.getoutput(cmd)

def load_yaml(data):
    return yaml.load(data, Loader=yaml.Loader)

def load_pickle(data):
    return pickle.loads(data)
