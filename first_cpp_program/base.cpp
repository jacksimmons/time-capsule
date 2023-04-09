#include <stdio.h>
  #include <conio.h>
  #include <windows.h>
  #include <stdlib.h>
  #include <iostream>
  #include <sstream>
  #include <string>
  #include <windows.h>

using namespace std;

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

#define KB_UP 72
  #define KB_DOWN 80
  #define KB_LEFT 75
  #define KB_RIGHT 77
  #define KB_Y 'y'
  #define KB_ESCAPE 27

int option = 1;
  int pressed = 1;
  int KB_code = 0;
  int title_passed = 0;
  int option_1_type = 0;
  int option_2_type = 0;
  int option_3_type = 0;
  int menu_type = 0;
  int colour_choice = 4;
  int stored_colour_choice = 0;
  int old_colour_choice = 0;

string option_chosen = "None";
  string left_arrow = "> ";
  string right_arrow = " <\n";
  string fnl = "\n"; /*Adds a new line*/
  string fsb = "  "; /*Filling spacebar*/
  string executed = "";
  string option_1 = "";
  string option_2 = "";
  string option_3 = "";
  string current_menu = "";
  string input = "";

void restart() {
  option_1_type = 0;
  option_2_type = 0;
  option_3_type = 0;
  menu_type = 0;
  }

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

game() {
  cout << "11";
  return 0;
}

video_settings() {
  pressed = 0;
  executed = "Video";
  return 0;
}

game_settings() {
  pressed = 0;
  executed = "Game";
  return 0;
}

play_chosen() {
  cout << "Coming soon...";
  pressed = 0;
  game();
}

settings_chosen() {
  option_1_type = 1;
  option_2_type = 1;
  option_3_type = 1;
  menu_type = 1;
  pressed = 0;
  option = 1;
  return 0;
}

video_chosen() {
  option_1_type = 2;
  option_2_type = 2;
  option_3_type = 2;
  menu_type = 2;
  pressed = 1;
  option = 1;
  return 0;
}

game_chosen() {
  option_1_type = 3;
  option_2_type = 3;
  option_3_type = 3;
  menu_type = 3;
  pressed = 1;
  option = 1;
  return 0;
}

int colours( void ) {
  HANDLE h = GetStdHandle ( STD_OUTPUT_HANDLE );
  WORD wOldColorAttrs;
  CONSOLE_SCREEN_BUFFER_INFO csbiInfo;

  /*
   * First save the current color information
   */
  GetConsoleScreenBufferInfo(h, &csbiInfo);
  wOldColorAttrs = csbiInfo.wAttributes;

  /*
   * Set the new color information
   */
  SetConsoleTextAttribute ( h, colour_choice );
  /*
  0   BLACK
  1   BLUE
  2   GREEN
  3   CYAN
  4   RED
  5   MAGENTA
  6   BROWN
  7   LIGHTGRAY
  8   DARKGRAY
  9   LIGHTBLUE
  10  LIGHTGREEN
  11  LIGHTCYAN
  12  LIGHTRED
  13  LIGHTMAGENTA
  14  YELLOW
  15  WHITE
  */
}

startup() {
  cls();
  colour_choice = 12;
  colours();
  cout << "\n> Use the Arrow Keys to navigate through the menus and 'y' to select an option.\n\n";
  Sleep(3500);
  cls();
  colour_choice = 11;
  colours();
  cout << "----Welcome to {game}! ('y' to confirm)----\n\n >    Play    <\n    Settings\n      Quit  \n";
}

char const*first_option() {

  if (option_1_type == 1) {
    return "Video Settings";
  }

  else if (option_1_type == 2) {
    old_colour_choice = colour_choice;
    colour_choice = 0;
    KB_code = 0;
    cls();
    cout << "Use the Up and Down arrows to change in-game text colour ('y' to confirm).\n\n";
    while((KB_code != KB_ESCAPE)) { /* This code is used to change the '> / <' position in the menu and the option the user is 'hovering' over */

      if (kbhit()) {
             KB_code = getch();

             while (KB_code == KB_UP) {
                   if (colour_choice < 15) {
                     colour_choice = colour_choice + 1;
                     cout << "Hi";
                     Sleep(5000);
                     break;
                   }
                   else {
                     colour_choice = 0;
                     break;
                   }
            }
            while (KB_code == KB_DOWN) {
                  if (colour_choice > 0) {
                    colour_choice = colour_choice - 1;
                    cout << "Hi";
                    break;
                  }
                  else {
                    colour_choice = 15;
                    break;
                  }
            }
            while (KB_code == KB_Y) {
                   return "Video Settings";
                   break;
            }
            cls();
            Sleep(2500);
            printf("Your current colour is: %s", colour_choice);
            colours();
            cout << "Sample text";
            }
      }
    }

  else {
    return "  Play  ";
  }
}

char const*second_option() {
  if (option_2_type == 1) {
    return "Game Settings";
  }
  else {
    return "Settings";
  }
}

char const*third_option() {
  if (option_3_type == 1) {
    return "\tBack\t";
  }
  else {
    return "  Quit  ";
  }
}

char const*c_menu_option() {
  if (menu_type == 1) {
    return "----Settings ('y' to select)----\n\n";
  }
  else {
    return "----Welcome to {game}! ('y' to confirm)----\n\n";
  }
}
