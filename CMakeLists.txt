project (ACELearn)
cmake_minimum_required(VERSION 3.1)

if($ENV{ACE_ROOT})
	set(ACE_ROOT $ENV{ACE_ROOT})
	message(${ACE_ROOT})
endif()


include_directories(${ACE_ROOT})
link_directories(${ACE_ROOT}/lib)

add_subdirectory(ACE_Hello)
add_subdirectory(CommandLineApp)
