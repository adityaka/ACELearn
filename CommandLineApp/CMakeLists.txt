cmake_minimum_required(VERSION 3.1)
project(CommandLineApp)

set(ACE_ROOT $ENV{ACE_ROOT})
include_directories(${ACE_ROOT})
link_directories(${ACE_ROOT}/lib)
add_executable(CommandLineApp CommandLineApp.cpp)
target_link_libraries(CommandLineApp ACE)

