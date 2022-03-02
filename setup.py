#!/usr/bin/env python
# coding: utf-8

# In[1]:


from setuptools import setup, find_packages

setup(
    name='bot',
    version='1.0',
    description='A useful module',
    url='https://github.com/artemdou/slack-bot',
    author='artemdou',
    packages=['bot', '*.bot', 'bot.*', '*.bot.*']
    # packages=find_packages(include=['dynamic_data_helper', 'dynamic_data_helper.*', 'bot', 'slack_bot.*']),
)
