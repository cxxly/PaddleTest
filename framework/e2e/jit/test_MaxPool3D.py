#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test jit cases
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "utils"))

from utils.yaml_loader import YamlLoader
from jittrans import JitTrans

yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "yaml", "nn.yml")
yml = YamlLoader(yaml_path)


def test_AdaptiveMaxPool3D_base():
    """test AdaptiveMaxPool3D_base"""
    jit_case = JitTrans(case=yml.get_case_info("AdaptiveMaxPool3D_base"))
    jit_case.jit_run()


def test_AdaptiveMaxPool3D_1():
    """test AdaptiveMaxPool3D_1"""
    jit_case = JitTrans(case=yml.get_case_info("AdaptiveMaxPool3D_1"))
    jit_case.jit_run()


def test_AdaptiveMaxPool3D_2():
    """test AdaptiveMaxPool3D_2"""
    jit_case = JitTrans(case=yml.get_case_info("AdaptiveMaxPool3D_2"))
    jit_case.jit_run()


def test_MaxPool3D_base():
    """test MaxPool3D_base"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_base"))
    jit_case.jit_run()


def test_MaxPool3D_0():
    """test MaxPool3D_0"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_0"))
    jit_case.jit_run()


def test_MaxPool3D_1():
    """test MaxPool3D_1"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_1"))
    jit_case.jit_run()


def test_MaxPool3D_2():
    """test MaxPool3D_2"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_2"))
    jit_case.jit_run()


def test_MaxPool3D_3():
    """test MaxPool3D_3"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_3"))
    jit_case.jit_run()


def test_MaxPool3D_4():
    """test MaxPool3D_4"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_4"))
    jit_case.jit_run()


def test_MaxPool3D_5():
    """test MaxPool3D_5"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_5"))
    jit_case.jit_run()


def test_MaxPool3D_6():
    """test MaxPool3D_6"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_6"))
    jit_case.jit_run()


def test_MaxPool3D_7():
    """test MaxPool3D_7"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_7"))
    jit_case.jit_run()


def test_MaxPool3D_8():
    """test MaxPool3D_8"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_8"))
    jit_case.jit_run()


def test_MaxPool3D_9():
    """test MaxPool3D_9"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_9"))
    jit_case.jit_run()


def test_MaxPool3D_10():
    """test MaxPool3D_10"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_10"))
    jit_case.jit_run()


def test_MaxPool3D_11():
    """test MaxPool3D_11"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_11"))
    jit_case.jit_run()


def test_MaxPool3D_12():
    """test MaxPool3D_12"""
    jit_case = JitTrans(case=yml.get_case_info("MaxPool3D_12"))
    jit_case.jit_run()