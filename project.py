from argparse import ArgumentParser
import logging
import sys
import os

class App(object):
    APPNAME = sys.argv[0]
    APPARGS = {"project-name":{
                                "short":"p",
                                "help":"name of the new project",
                                "type":str,
                                "dest":"project_name",
                                "required":True
                },
                "ace-lib":{
                                "short":"al",
                                "help": "Ace library path",
                                "type":str,
                                "dest":"ace_lib",
                                "required":True
                },
                "ace-include":{ "short":"ai",
                                "help":"ACE include directory",
                                "type":str,
                                "dest":"ace_include",
                                "required":True
                }

    }

    CMAKE_CONTENT = """
cmake_minimum_required(VERSION 3.1)
project({0})
set(ACE_INCLUDE_DIR {1})
set(ACE_LIB_DIR {2})
include_directories(${{ACE_INCLUDE_DIR}})
link_directories(${{ACE_LIB_DIR}})
add_executable({3} {3}.cpp)
target_link_libraries({3} ACE)
"""

    MAINFILE_CONTENT = """
#include <ace/OS.h>
#include <ace/Log_Msg.h>
int main(int argc, char **argv){
    // your code goes here
    return 0;
}
"""

    def __init__(self, **kwargs):
       #setup the commandline parser using the APPARGS
        self.__setupParser()
        self.__args = self.__parser.parse_args()
        self.__logger = logging.getLogger(App.APPNAME)
        self.__logger.setLevel(logging.INFO)
        
    

    def __call__(self):
        self.main()
    

    def __setupParser(self):
        self.__parser = ArgumentParser()
        for argEntry in App.APPARGS.items():
            longName = argEntry[0]
            shortName = argEntry[1]["short"] if "short" in argEntry[1] else None
            helpText = argEntry[1]["help"] if "help" in argEntry[1] else None
            argType = argEntry[1]["type"] if "type" in argEntry[1] else str
            argRequired = argEntry[1]["required"] if  "required" in argEntry[1] else False
            argDefault = None
            argDest = argEntry[1]["dest"] if "dest" in argEntry[1] else None
            self.__parser.add_argument("--"+longName, "-" + shortName, help=helpText, type=argType, required=argRequired, dest=argDest)

    def main(self):
        args = self.__args
        cmakeFileContent = App.CMAKE_CONTENT.format(args.project_name, args.ace_include, args.ace_lib, args.project_name)
        currPath = os.path.abspath(os.getcwd())
        projectDir = os.path.join(currPath, args.project_name)
        os.makedirs(projectDir)
        cmakeFilePath = os.path.join(projectDir, "CMakeLists.txt")
        cmakeFile = open(cmakeFilePath, "w+")
        cmakeFile.writelines(cmakeFileContent)
        cmakeFile.close()
        cppFilePath = os.path.join(projectDir, args.project_name + ".cpp")
        cppFile = open(cppFilePath,"w+")
        cppFile.writelines(App.MAINFILE_CONTENT)
        cppFile.close()




if __name__ == "__main__":
    app = App()
    app()

