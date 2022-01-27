#include "asm_extension.asm.h"

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <iostream>

namespace py = pybind11;

py::array_t<float> find_closest_point(py::array_t<float, py::array::c_style | py::array::forcecast> point,
                                      py::array_t<float, py::array::c_style | py::array::forcecast> point_list)
{
    auto buf_point = point.mutable_unchecked<1>();
    float* ptr_point = buf_point.mutable_data(0);

    auto buf_point_list = point_list.mutable_unchecked<2>();
    float* ptr_point_list = point_list.mutable_data(0);

    auto closest_point = _find_closest_point(ptr_point, ptr_point_list, buf_point_list.size());

    return py::array_t<float>({2}, closest_point);
}

PYBIND11_MODULE(asm_extension, m)
{
    m.doc() = "This is doc file for this module";
    m.def("find_closest_point", &find_closest_point);
}