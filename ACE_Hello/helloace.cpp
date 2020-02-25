#include "ace/OS.h"
#include "ace/Log_Msg.h"
int main(int argc, char **argv){

	ACE_DEBUG((LM_DEBUG,ACE_TEXT("%IMain Entry\n")));
	ACE_DEBUG((LM_DEBUG,ACE_TEXT("%IHello world this is an ACE Log\n")));
	ACE_DEBUG((LM_INFO, ACE_TEXT("%IExitting main\n")));
	return 0;

}
