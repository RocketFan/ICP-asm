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

    ptr_point[0] = 0;

    std::cout << "Size 1: " << buf_point.size() << std::endl;
    std::cout << "Size 2: " << buf_point_list.size() << std::endl;

    std::cout << "C++: ";

    for (int i = 0; i < buf_point.size(); i++)
        std::cout << " " << ptr_point[i];

    std::cout << "\n";

    std::cout << "C++ 2: ";

    for (int i = 0; i < buf_point_list.size(); i += buf_point_list.shape(1))
    {
        for (int j = 0; j < buf_point_list.shape(1); j++)
            std::cout << " " << ptr_point_list[i + j];

        std::cout << "\n";
    }


    std::cout << "\n";

    return py::array_t<float>();
}

PYBIND11_MODULE(asm_extension, m)
{
    m.doc() = "This is doc file for this module";
    m.def("find_closest_point", &find_closest_point);
}