#pragma once

extern "C"
{
    // Find closest point in point_list of size N in 2D space
    float* _find_closest_point(float *point, float *point_list, int N);
}