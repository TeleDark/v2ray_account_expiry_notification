import os
import yaml
real_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(real_dir,"accounts_info.json")
login_file = os.path.join(real_dir,"login.py")
config_yaml_file = os.path.join(real_dir, "./config.yaml")
pickle_file = os.path.join(real_dir, "cookies.pkl")
inactives_file = os.path.join(real_dir, "inactives.pkl")


# load yaml config
with open(config_yaml_file, 'r') as f:
    config_yaml = yaml.safe_load(f)

token_bot = config_yaml["token_bot"]
chat_id = config_yaml["chat_id"]
panels = config_yaml["panels"]
