#include <stdio.h>
#include <conio.h>
#include <windows.h>
#include <iostream>
#include <sstream>
#include <string>
#include <windows.h>

#define KB_UP 72
#define KB_DOWN 80
#define KB_LEFT 75
#define KB_RIGHT 77
#define KB_ENTER 13
#define KB_ESCAPE 27

int option = 1;
int pressed = 1;

using namespace std;

string option_chosen = "None";

// Copied, makes a window
void cls()
  {
  HANDLE                     hStdOut;
  CONSOLE_SCREEN_BUFFER_INFO csbi;
  DWORD                      count;
  DWORD                      cellCount;
  COORD                      homeCoords = { 0, 0 };

  hStdOut = GetStdHandle( STD_OUTPUT_HANDLE );
  if (hStdOut == INVALID_HANDLE_VALUE) return;

  /* Get the number of cells in the current buffer */
  if (!GetConsoleScreenBufferInfo( hStdOut, &csbi )) return;
  cellCount = csbi.dwSize.X *csbi.dwSize.Y;

  /* Fill the entire buffer with spaces */
  if (!FillConsoleOutputCharacter(
    hStdOut,
    (TCHAR) ' ',
    cellCount,
    homeCoords,
    &count
    )) return;

  /* Fill the entire buffer with the current colors and attributes */
  if (!FillConsoleOutputAttribute(
    hStdOut,
    csbi.wAttributes,
    cellCount,
    homeCoords,
    &count
    )) return;

  /* Move the cursor home */
  SetConsoleCursorPosition( hStdOut, homeCoords );
  }

string option_1 = "Play";
string option_2 = "Settings";
string option_3 = "Quit";
string left_arrow = "> ";
string right_arrow = " <\n";
string current_menu = "Welcome to {game}!\n\n";
string fnl = "\n"; /*Adds a new line*/
string fsb = "  "; /*Filling spacebar*/

option1u() { /* When the user pressses [Up-arrow] on option [Play] */
  cls();
  option = 3;
  pressed = 0;
  return 0;
}

option1d() { /* When the user pressses [Down-arrow] on option [Play] */
  cls();
  option = 2;
  pressed = 0;
  return 0;
}

option2u() { /* When the user pressses [Up-arrow] on option [Settings] */
  cls();
  option = 1;
  pressed = 0;
  return 0;
}

option2d() { /* When the user pressses [Down-arrow] on option [Settings] */
  cls();
  option = 3;
  pressed = 0;
  return 0;
}

option3u() { /* When the user pressses [Up-arrow] on option 3 */
  cls();
  option = 2;
  pressed = 0;
  return 0;
}

option3d() { /* When the user pressses [Down-arrow] on option 3 */
  cls();
  option = 1;
  pressed = 0;
  return 0;
}


int main() {
  cls();
  cout << "Welcome to {game}!\n\n >  Play  <\n    Settings\n    Quit\n";

  int KB_code = 0;
  int title_passed = 0;

  while((KB_code != KB_ESCAPE) && (option_chosen == "None")) { /* This code is used to change the '> / <' position in the menu and the option the user is 'hovering' over */

    if (kbhit()) {

           KB_code = getch();

           switch (KB_code)
           {
                 case KB_UP:
					 if (option == 1)
					 {
						 option = 3
					 }
					 else
					 {
						 option = option - 1;
					 }

                 case KB_DOWN:
                       if (option == 1 && pressed == 1) {
                         option1d();
                       }
                       else if (option == 2 && pressed == 1) {
                         option2d();
                       }
                       else if (option == 3 && pressed == 1) {
                         option3d();
                       }

                 case KB_ENTER:
                       if (option == 1) {
                         option_chosen = "Play";
                         title_passed = 1;
                         cout << "Play";
                         break;
                       }
                       else if (option == 2) {
                         option_chosen = "Settings";
                         title_passed = 1;
                         cout << "Settings";
                         break;
                       }
                       else if (option == 3) {
                         option_chosen = "Quit";
                         title_passed = 1;
                         cout << "Quit";
                         break;
                       }

                 default:
                   if (option == 1 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), left_arrow.c_str(), option_1.c_str(), right_arrow.c_str(), fsb.c_str(), option_2.c_str(), fnl.c_str(), fsb.c_str(), option_3.c_str(), fnl.c_str());
                     break;
                   }
                   else if (option == 2 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), fsb.c_str(), option_1.c_str(), fnl.c_str(), left_arrow.c_str(), option_2.c_str(), right_arrow.c_str(), fsb.c_str(), option_3.c_str(), fnl.c_str());
                     break;
                   }
                   else if (option == 3 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), fsb.c_str(), option_1.c_str(), fnl.c_str(), fsb.c_str(), option_2.c_str(), fnl.c_str(), left_arrow.c_str(), option_3.c_str(), right_arrow.c_str());
                     break;
                   }
                 break;
           }
	}

  }
	return 0;
}
