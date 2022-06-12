import configparser
import os

bilibili = {'channel': '14', 'cps': 'bilibili', 'sub_channel': '0'}
mihoyo = {'channel': '1', 'cps': 'mihoyo', 'sub_channel': '1'}
section = 'General'

config = configparser.ConfigParser()
config.read('config.ini')
# 2.8之后，需要b服会比官服多一个PCGameSDK.dll，如果不删除的话，切换官服后，登录会报错
base_path = os.path.dirname(os.path.realpath(__file__))
pcgamesdk_path = os.path.join(base_path, 'YuanShen_Data', 'Plugins')


def modify_values(config, section, values):
    for k, v in values.items():
        config.set('General', k, v)


def rename():
    file_list = os.listdir(pcgamesdk_path)

    for file in file_list:
        if file.startswith('PCGameSDK') and file.endswith('txt'):
            new_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll.txt')
            old_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll')
            os.rename(new_pcgamesdk_name, old_pcgamesdk_name)
        elif file.startswith('PCGameSDK') and file.endswith('dll'):
            new_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll.txt')
            old_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll')
            os.rename(old_pcgamesdk_name, new_pcgamesdk_name)


cps = config.get(section, 'cps')
if cps == 'mihoyo':
    modify_values(config, section, bilibili)
    rename()
    # old_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll.txt')
    # new_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll')
    # os.rename(old_pcgamesdk_name, new_pcgamesdk_name)
else:
    modify_values(config, section, mihoyo)
    rename()
    # new_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll.txt')
    # old_pcgamesdk_name = os.path.join(pcgamesdk_path, 'PCGameSDK.dll')
    # os.rename(old_pcgamesdk_name, new_pcgamesdk_name)

fp = open('config.ini', 'w+')
config.write(fp)
fp.close()
