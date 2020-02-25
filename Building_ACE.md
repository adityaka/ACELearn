# Building ACE from github source

## Dependencies 
1. Linux VM ubuntu (any version) 
1. ACE Source clone the github repo 
	1. ```mkdir -p $HOME/src```
	1. ```git clone git clone https://github.com/DOCGroup/ACE_TAO  $HOME/src```
1. MPC ACE project configurator , clone github repo
	1. ```git clone https://github.com/DOCGroup/MPC $HOME/src```
1. g++ (any version)
	1. sudo apt-get install g++-8
1. perl for MPC to configure the ACE Project 
1. make (any version)

## Manual Build procedure 
1. Set ```MPC_ROOT=$HOME/src/MPC```
1. Use MPC to generate the project files
	1.  ```$ACE_ROOT/bin/mwc.pl --type gnuace ACE.mwc``` 
1. Setup the ACE_ROOT environment variable *$HOME/src/ACE_TAO/ACE*
	1. ACE_TAO repo has ACE+TAO
	1. ACE exists under ACE subdirectory 
	1. Original build instructions (optional) available @ http://www.dre.vanderbilt.edu/~schmidt/DOC_ROOT/ACE/ACE-INSTALL.html#unix
1. Setup the platform specific includes
	1. open ```$ACE_ROOT/ace/config.h```
	1. add ```#include "ace/config-linux.h"```
1. Setup macros 
	1. Open/Create ```$ACE_ROOT/include/makeinclude/platform_macros.GNU```
	2. Add 'include ```$(ACE_ROOT)/include/makeinclude/platform_linux.GNU```
1. Make ACE 
	1. make -j 4 (use the number of CPUs I used 2 instead of 4)
	2. if make -j 4 fails you can try make clean and make
1. Install ACE
	1. ```export INSTALL_PREFIX=<path to install>```
	2. sudo make install

## Automated Build
[TODO : ]



