project (ACELearn)
cmake_minimum_required(VERSION 3.1)

if(DEFINED ENV{ACE_ROOT})
	set(PROJECT_ACE_ROOT $ENV{ACE_ROOT})
	include_directories(${PROJECT_ACE_ROOT})
	link_directories(${PROJECT_ACE_ROOT}/lib)
	message(${PROJECT_ACE_ROOT} " is set as ACE_ROOT")
else()
	message("ACE_ROOT is not set build will fail.")
endif()

add_subdirectory(ACE_Hello)
add_subdirectory(CommandLineApp)
