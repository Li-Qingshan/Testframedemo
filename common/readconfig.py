#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser
from config.conf import cm

HOST = 'HOST'
LOGCONFIG = 'LOGCONFIG'

class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)
    def _add(self,section):
        self.config.add_section(section)

    @property
    def url(self):
        return self._get(HOST, HOST)
    @property
    def loglevel(self):
        return  self._get(LOGCONFIG,'loglevel')


ini = ReadConfig()

if __name__ == '__main__':
    ini._set(LOGCONFIG,'loglevel','debug')
    print(ini.loglevel)
    # print(ini.url)