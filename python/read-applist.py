import pickle
from pathlib import Path
import os

checkpoint_folder = Path("checkpoints")

apps_dict_filename_prefix = 'apps_dict'
exc_apps_filename_prefix = 'excluded_apps_list'
error_apps_filename_prefix = 'error_apps_list'

apps_dict = {}
excluded_apps_list = []
error_apps_list = []


def check_latest_checkpoints(checkpoint_folder, apps_dict_filename_prefix, exc_apps_filename_prefix, error_apps_filename_prefix):
    # app_dict
    all_pkl = []
    
    for root, dirs, files in os.walk(checkpoint_folder):
        all_pkl = list(map(lambda f: Path(root, f), files))
        all_pkl = [p for p in all_pkl if p.suffix == '.p']
        break
            
    apps_dict_ckpt_files = [f for f in all_pkl if apps_dict_filename_prefix in f.name and "ckpt" in f.name]
    exc_apps_list_ckpt_files = [f for f in all_pkl if exc_apps_filename_prefix in f.name and "ckpt" in f.name]
    error_apps_ckpt_files = [f for f in all_pkl if error_apps_filename_prefix in f.name and 'ckpt' in f.name]

    apps_dict_ckpt_files.sort()
    exc_apps_list_ckpt_files.sort()
    error_apps_ckpt_files.sort()

    latest_apps_dict_ckpt_path = apps_dict_ckpt_files[-1] if apps_dict_ckpt_files else None
    latest_exc_apps_list_ckpt_path = exc_apps_list_ckpt_files[-1] if exc_apps_list_ckpt_files else None
    latest_error_apps_list_ckpt_path = error_apps_ckpt_files[-1] if error_apps_ckpt_files else None

    return latest_apps_dict_ckpt_path, latest_exc_apps_list_ckpt_path, latest_error_apps_list_ckpt_path


def load_pickle(path_to_load:Path) -> dict:
    obj = pickle.load(open(path_to_load, "rb"))
    # print(f'Successfully loaded {str(path_to_load)}')
    
    return obj

if not checkpoint_folder.exists():
    print(f'Fail to find checkpoint folder: {checkpoint_folder}')
    print(f'Start at blank.')


latest_apps_dict_ckpt_path, latest_exc_apps_list_ckpt_path, latest_error_apps_list_ckpt_path = check_latest_checkpoints(checkpoint_folder, apps_dict_filename_prefix, exc_apps_filename_prefix, error_apps_filename_prefix)

if latest_apps_dict_ckpt_path:
    apps_dict = load_pickle(latest_apps_dict_ckpt_path)
    print('Successfully load apps_dict checkpoint:', latest_apps_dict_ckpt_path)
    print(f'Number of apps in apps_dict: {len(apps_dict)}')

if latest_exc_apps_list_ckpt_path:
    excluded_apps_list = load_pickle(latest_exc_apps_list_ckpt_path)
    print("Successfully load excluded_apps_list checkpoint:", latest_exc_apps_list_ckpt_path)
    print(f'Number of apps in excluded_apps_list: {len(excluded_apps_list)}')

if latest_error_apps_list_ckpt_path:
    error_apps_list = load_pickle(latest_error_apps_list_ckpt_path)
    print("Successfully load error_apps_list checkpoint:", latest_error_apps_list_ckpt_path)
    print(f'Number of apps in error_apps_list: {len(error_apps_list)}')








