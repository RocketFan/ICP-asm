#include <iostream>
#include "asm_extension.asm.h"

int main() {
    int result = add42(40);
    std::cout << "Result: " << result << std::endl;
    return 0;
}