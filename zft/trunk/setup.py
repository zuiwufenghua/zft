#!/usr/bin/python
# Copyright (c) 2010-2011 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
from setuptools.command.sdist import sdist
import os
import subprocess

from zft import __version__ as version


class local_sdist(sdist):
    """Customized sdist hook - builds the ChangeLog file from VC first"""

    def run(self):
        if os.path.isdir('.bzr'):
            # We're in a bzr branch

            log_cmd = subprocess.Popen(["bzr", "log", "--gnu"],
                                       stdout=subprocess.PIPE)
            changelog = log_cmd.communicate()[0]
            with open("ChangeLog", "w") as changelog_file:
                changelog_file.write(changelog)
        sdist.run(self)


name = 'zft'

setup(
    name=name,
    version=version,
    description='Zft',
    license='Apache License (2.0)',
    author='zz.',
    author_email='zjfhappy@gmail.com',
    url='',
    packages=find_packages(exclude=['bin']),
    test_suite='nose.collector',
    cmdclass={'sdist': local_sdist},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[],  # removed for better compat
    scripts=[
        ''
        ],
    entry_points={
        'paste.app_factory': [
            'proxy=zft.proxy:app_factory',
            'object=zf.object:app_factory',
#            'container=swift.container.server:app_factory',
#            'account=swift.account.server:app_factory',
#            'auth=swift.auth.server:app_factory',
            ],
        'paste.filter_factory': [
            'auth=zft.auth:filter_factory',
#            'swauth=swift.common.middleware.swauth:filter_factory',
#            'healthcheck=swift.common.middleware.healthcheck:filter_factory',
#            'memcache=swift.common.middleware.memcache:filter_factory',
#            'ratelimit=swift.common.middleware.ratelimit:filter_factory',
#            'cname_lookup=swift.common.middleware.cname_lookup:filter_factory',
#            'catch_errors=swift.common.middleware.catch_errors:filter_factory',
#            'domain_remap=swift.common.middleware.domain_remap:filter_factory',
#            'swift3=swift.common.middleware.swift3:filter_factory',
            ],
        },
    )
