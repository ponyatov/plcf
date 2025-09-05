
cmake_minimum_required(VERSION 3.22)
get_filename_component(CMAKE_PROJECT_NAME ${CMAKE_SOURCE_DIR} NAME_WE)
project(${CMAKE_PROJECT_NAME} VERSION 0.0.1 LANGUAGES C CXX ASM)

file(GLOB S
    RELATIVE ${CMAKE_SOURCE_DIR}
    src/*.s
)

file(GLOB C
    RELATIVE ${CMAKE_SOURCE_DIR}
    src/*.c*
)

file(GLOB H
    RELATIVE ${CMAKE_SOURCE_DIR}
    inc/*.h*
)

add_executable(${CMAKE_PROJECT_NAME} ${C} ${H} ${S})

