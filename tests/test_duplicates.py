#!/usr/bin/env python
# $Copyright:
# ----------------------------------------------------------------
# This confidential and proprietary software may be used only as
# authorised by a licensing agreement from ARM Limited
#  (C) COPYRIGHT 2015 ARM Limited
#       ALL RIGHTS RESERVED
# The entire notice above must be reproduced on all authorised
# copies and copies may only be made to the extent permitted
# by a licensing agreement from ARM Limited.
# ----------------------------------------------------------------
# File:        test_duplicates.py
# ----------------------------------------------------------------
# $
#

import unittest
import matplotlib
import pandas as pd
import utils_tests
import cr2
import shutil

from test_thermal import BaseTestThermal


class TestPlotterDupVals(BaseTestThermal):

    """Test Duplicate Entries in plotter"""

    def __init__(self, *args, **kwargs):
        super(TestPlotterDupVals, self).__init__(*args, **kwargs)

    def test_plotter_duplicates(self):
        """Test that plotter handles duplicates fine"""
        with open("trace.txt", "w") as fout:
            fout.write("""version = 6
cpus=6
       rcuos/2-22 [001] 0000.018510: sched_load_avg_sg: cpus=00000001 load=0 utilization=0
       rcuos/2-22 [001] 6550.018611: sched_load_avg_sg: cpus=00000002 load=1 utilization=1
       rcuos/2-22 [001] 6550.018611: sched_load_avg_sg: cpus=00000004 load=2 utilization=2
       rcuos/2-22 [001] 6550.018612: sched_load_avg_sg: cpus=00000001 load=2 utilization=3
       rcuos/2-22 [001] 6550.018624: sched_load_avg_sg: cpus=00000002 load=1 utilization=4
       rcuos/2-22 [001] 6550.018625: sched_load_avg_sg: cpus=00000002 load=2 utilization=5
       rcuos/2-22 [001] 6550.018626: sched_load_avg_sg: cpus=00000002 load=3 utilization=6
       rcuos/2-22 [001] 6550.018627: sched_load_avg_sg: cpus=00000002 load=1 utilization=7
       rcuos/2-22 [001] 6550.018628: sched_load_avg_sg: cpus=00000004 load=2 utilization=8\n""")
            fout.close()
        run1 = cr2.Run(name="first")
        l = cr2.LinePlot(
            run1,
            cr2.sched.SchedLoadAvgSchedGroup,
            column=['utilization'],
            filters={
                "load": [
                    1,
                    2]},
            pivot="cpus",
            marker='o',
            linestyle='none',
            per_line=3)
        l.view(test=True)

    def test_plotter_triplicates(self):

        """Test that plotter handles triplicates fine"""

        with open("trace.txt", "w") as fout:
            fout.write("""version = 6
cpus=6
       rcuos/2-22 [001] 0000.018510: sched_load_avg_sg: cpus=00000001 load=0 utilization=0
       rcuos/2-22 [001] 6550.018611: sched_load_avg_sg: cpus=00000002 load=1 utilization=1
       rcuos/2-22 [001] 6550.018611: sched_load_avg_sg: cpus=00000004 load=2 utilization=2
       rcuos/2-22 [001] 6550.018611: sched_load_avg_sg: cpus=00000004 load=2 utilization=2
       rcuos/2-22 [001] 6550.018612: sched_load_avg_sg: cpus=00000001 load=2 utilization=3
       rcuos/2-22 [001] 6550.018624: sched_load_avg_sg: cpus=00000002 load=1 utilization=4
       rcuos/2-22 [001] 6550.018625: sched_load_avg_sg: cpus=00000002 load=2 utilization=5
       rcuos/2-22 [001] 6550.018626: sched_load_avg_sg: cpus=00000002 load=3 utilization=6
       rcuos/2-22 [001] 6550.018627: sched_load_avg_sg: cpus=00000002 load=1 utilization=7
       rcuos/2-22 [001] 6550.018628: sched_load_avg_sg: cpus=00000004 load=2 utilization=8\n""")
            fout.close()

        run1 = cr2.Run(name="first")
        l = cr2.LinePlot(
            run1,
            cr2.sched.SchedLoadAvgSchedGroup,
            column=['utilization'],
            filters={
                "load": [
                    1,
                    2]},
            pivot="cpus",
            marker='o',
            linestyle='none',
            per_line=3)
        l.view(test=True)