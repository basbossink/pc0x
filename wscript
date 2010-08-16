#! /usr/bin/env python
# encoding: utf-8

# pc0x a command line podcatcher
# Copyright (C) 2010 Bas Bossink <bas.bossink@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# the following two variables are used by the target "waf dist"
VERSION='0.0.1'
APPNAME='pc0x'

# these variables are mandatory ('/' are converted automatically)
top = '.'
out = 'build'

gppflags = ['-ansi', '-std=c++0x',
    '-Wall', '-Werror', '-Weffc++', '-Wextra', '-Wformat-security',
    '-Wredundant-decls', '-pedantic-errors', '-g']

def set_options(opt):
    opt.tool_options('compiler_cxx')

def configure(conf):
    conf.check_tool('compiler_cxx')
    conf.check(header_name='gtest/gtest.h', features='cxx', mandatory=True)
    conf.check(header_name='gmock/gmock.h', features='cxx', mandatory=True)
    conf.check_cxx(lib='pthread', cxxflags='-Wall')
    conf.check_cxx(staticlib='gtest', cxxflags='-Wall')
    conf.check_cxx(staticlib='gtest_main', cxxflags='-Wall')
    conf.check_cxx(staticlib='gmock', cxxflags='-Wall')
    conf.write_config_header('src/inc/config.h')

def build(bld):
    staticlib = bld(
        features=['cxx', 'cstaticlib' ],
        target='libpc0x',
        source=bld.path.ant_glob("src/lib/**/*.cc"),
        includes="src/inc",
        export_incdirs = 'src/inc',
        cxxflags=gppflags)

    main = bld(
            features=['cxx', 'cprogram' ],
            source='src/pc0x/main.cc',
            target='pc0x',
            includes="src/inc",
            cxxflags=gppflags,
            uselib_local='libpc0x')

    testrunner = bld(
            features=['cxx', 'cprogram' ],
            source=bld.path.ant_glob("src/test/**/*.cc"),
            target='testrunner',
            lib=['gtest', 'gtest_main', 'gmock', 'pthread'],
            cxxflags=gppflags,
            uselib_local='libpc0x')
