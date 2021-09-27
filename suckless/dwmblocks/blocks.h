//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		                               /*Update Interval*/	/*Update Signal*/

    {"",        "$HOME/suckless/dwmblocks/statusbar/wlan",   1,               0},    

    {"",        "$HOME/suckless/dwmblocks/statusbar/brightness",   1,               0},

    {"",        "$HOME/suckless/dwmblocks/statusbar/volume",   1,                   0},
    
    {"",        "$HOME/suckless/dwmblocks/statusbar/cputemp",  5,                   0},

    {"",        "$HOME/suckless/dwmblocks/statusbar/battery",  5,                   0},
	
    {"",        "$HOME/suckless/dwmblocks/statusbar/date_time",5,		            0},

    {"",        "$HOME/suckless/dwmblocks/statusbar/record",   1,                   0},
    
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = "  ";
static unsigned int delimLen = 5;
