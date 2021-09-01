import configparser

bilibili = {'channel': '14', 'cps': 'bilibili', 'sub_channel': '0'}
mihoyo = {'channel': '1', 'cps': 'mihoyo', 'sub_channel': '1'}
section = 'General'

config = configparser.ConfigParser()
config.read('config.ini')


def modify_values(config, section, values):
    for k, v in values.items():
        config.set('General', k, v)


cps = config.get(section, 'cps')
if cps == 'mihoyo':
    modify_values(config, section, bilibili)
else:
    modify_values(config, section, mihoyo)

fp = open('config.ini', 'w+')
config.write(fp)
fp.close()
