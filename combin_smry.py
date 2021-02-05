#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   combin_smry.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021-02-05 14:42   tangyubao      1.0         None
'''

# import lib
import json

smry_path = 'val_wiki_entity_smry.json'
data_path = 'val_wiki.json'
out_path = 'val_wiki_smry.json'

with open(smry_path,'r',encoding='utf-8') as f:
    smry = json.load(f)
    smry_len = len(smry)
i = 0

one_type_ins = []
data = {}
with open(data_path,'r',encoding='utf-8') as f:
    content = json.load(f)
    for key in content.keys():
        for ins in content[key]:
            if ins['h'][1] == smry[i][0]:
                ins['h'].append(str(smry[i][2]).split(' '))
            else: print('head error!!')
            i += 1

            if ins['t'][1] == smry[i][0]:
                ins['t'].append(str(smry[i][2]).split(' '))
            else: print('tail error!!')
            i += 1

            one_type_ins.append(ins)
        data[key] = one_type_ins

with open(out_path,'w',encoding='utf-8') as f:
    json.dump(data,f)
