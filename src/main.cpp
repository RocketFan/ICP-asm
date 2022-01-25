#include <iostream>
#include "asm_extension.asm.h"

int main() {
    const int N = 10;
    float point[2] = {10, 15};
    float point_list[N] = {1, 3, 1, 2, 10, 15, 8, 10, 7, 8};

    std::cout << "Ptr 1: " << point << std::endl;
    std::cout << "Ptr 2: " << point_list << std::endl;

    float* result = _find_closest_point(point, point_list, N);

    std::cout << "Result ptr: " << result << std::endl;

    std::cout << "Result: ";
    for (int i = 0; i < 2; i++)
        std::cout << " " << result[i];
    std::cout << "\n";

    std::cout << "Point list: ";
    for (int i = 0; i < N; i++)
        std::cout << " " << point_list[i];
    std::cout << "\n";

    std::cout << "Point: " << point[0] << " " << point[1] << "\n";
    
    return 0;
}