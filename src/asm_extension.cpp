#include "asm_extension.asm.h"

#include <pybind11/pybind11.h>
#include <iostream>

namespace py = pybind11;

PYBIND11_MODULE(asm_extension, m) {
    m.doc() = "This is doc file for this module";
    m.def("add42", &add42);
}