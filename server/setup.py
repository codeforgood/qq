#!/usr/bin/env python

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["-r"]
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name="QQ",
    version="0.1",
    author="Sadish Ravi",
    description="Query queue and scheduler",
    keywords="query queue scheduler",
    url="https://github.com/codeforgood/qq",
    license="TBD",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    scripts=[],
    cmdclass={'test': Tox},
)
