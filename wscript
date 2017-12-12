#! /usr/bin/env python
# encoding: utf-8

import os

VERSION = "1.0"
APPNAME = "Fuzzy"

def options(opt):
	opt.load('compiler_cxx')

def configure(cfg):
	cfg.load('compiler_cxx')
	cfg.env.CXXFLAGS=['-std=c++11','-Wall']
	
	cfg.env.LIB_FUZZY = ['fuzzylite']
	print os.getcwd()
	cfg.env.LIBPATH_FUZZY  = [os.path.join(os.getcwd(), 'fuzzylite/release/bin')]
	print cfg.env.LIBPATH_FUZZY
	cfg.env.INCLUDES_FUZZY  = [os.path.join(os.getcwd(), 'fuzzylite')]
	print cfg.env.INCLUDES_FUZZY

def build(bld):
	bld(includes='fuzzylite')
	bld.recurse('example')

