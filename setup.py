#!/usr/bin/env python
# coding: utf-8

# In[1]:


from setuptools import setup, find_packages

setup(
    name='slack-bot',
    version='1.0',
    description='A useful module',
    author='artemdou',
    packages=['bot']
    # packages=find_packages(include=['dynamic_data_helper', 'dynamic_data_helper.*', 'bot', 'slack_bot.*']),
)