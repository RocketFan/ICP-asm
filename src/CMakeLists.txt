cmake_minimum_required(VERSION 3.10)

pybind11_add_module(asm_extension SHARED asm_extension.cpp asm_extension.asm.h asm_extension.asm)