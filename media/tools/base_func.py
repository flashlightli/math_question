import os
import json


def get_config():
    try:
        config_path = os.path.split(os.path.realpath(__file__))[0].replace("tools", "media") + os.sep + 'config.json'
        if not os.path.isfile(config_path):
            raise Exception("当前路径不存在配置文件")
        with open(config_path) as f:
            config = json.loads(f.read())
    except:
        raise Exception("加载配置文件失败")

    return config
