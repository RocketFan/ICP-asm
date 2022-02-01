from icp import ICP

from build.src.asm_extension import find_closest_point

class ICPAsm(ICP):
    def find_closest_point(self, point, points_list):
        p_closest = find_closest_point(point, points_list)
        
        return p_closest