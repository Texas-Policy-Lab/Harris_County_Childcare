import yaml

def read_yaml(fl = "config.yaml"):
    with open(fl, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return exc