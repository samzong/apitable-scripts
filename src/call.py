import yaml
import json
from apitable import Apitable

with open('config.yaml', mode='r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

TOKEN = config['apitable']['token']
HOST = config['apitable']['host']

task_table = config['apitable']['task_table']
dce5model_table = config['apitable']['dce5model_table']

apitable = Apitable(TOKEN, api_base=HOST, debug=True)


def get_dce5model(model_key):
    datasheet = apitable.datasheet(dce5model_table, field_key="id")
    models = datasheet.records.all()
    
    for model in models:
        print(model.json())


datasheet = apitable.datasheet(task_table, field_key="name")

# 返回所有记录的集合
records = datasheet.records.all()
for record in records:
    if '状态' in record.json() and record.json()['状态'] == "未处理":
        data = json.dumps(record.json(), ensure_ascii=False, indent=4)
        print(record.json()['产品模块'][0])
        model_key = record.json()['产品模块'][0]
        get_dce5model(model_key)

        break
