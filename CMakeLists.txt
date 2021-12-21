cmake_minimum_required(VERSION 3.10)

project(ICPAsm)

set(CMAKE_CXX_STANDARD 17)
#Enable ASM provided by NASM
enable_language(ASM_NASM)

if(APPLE)
	#Add leading underscore when building macho64 object files
	string(APPEND CMAKE_ASM_NASM_FLAGS "--prefix _")
endif(APPLE)

if(WIN32)
	string(APPEND CMAKE_ASM_NASM_FLAGS "-dWIN32=1")
endif(WIN32)

# SET(CMAKE_ASM_FLAGS "${CFLAGS} -x assembler-with-cpp")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32")

add_executable(ex1 src/main.cpp src/asm_extension.asm.h src/asm_extension.asm)