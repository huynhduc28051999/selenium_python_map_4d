from selenium import webdriver
import unittest
import time
import os
from package.html_test_runner import HTMLTestRunner

from common.logger import Log

log = Log('run').get_log()
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName='case', rule='test*.py'):
    case_path = os.path.join(os.getcwd(), caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    # Define the parameters of the discover method
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover

def run_case(all_case, reportName='reports'):
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_path = os.path.join(cur_path, reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + 'result.html')
    with open(report_abspath, 'w') as fp:
        runner = HTMLTestRunner(stream=fp, title='Test case auto report', description='use case execution')
        runner.run(all_case)

if __name__ == '__main__':
    # add test case for prepare run
    all_case = add_case()
    # run test case
    run_case(all_case)