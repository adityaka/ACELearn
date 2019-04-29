cmake_minimum_required(VERSION 3.1)
project(helloace)

set(ACE_ROOT $ENV{ACE_ROOT})
message(${ACE_ROOT})
include_directories(${ACE_ROOT})
link_directories(${ACE_ROOT}/lib)

add_executable(helloace helloace.cpp)
target_link_libraries(helloace ACE)
