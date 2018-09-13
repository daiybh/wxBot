#!/usr/bin/env python
# -*- coding: utf-8 -*-



with open('config.json', 'r') as f:
    import json
    config = json.loads(f.read())

nxx="kkkllff"
result = f'你的名字设置为: {nxx}, 以后需要修改，请发送 \\name_<你的新名字>'
print(result)
if __name__=="__main__":
    print(config)

