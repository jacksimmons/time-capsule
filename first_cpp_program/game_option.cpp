int play_game() {
  cls();
  cout << "\t\t\n~~~~ Please select a hero type ~~~~\n\n"

  while((KB_code != KB_ESCAPE)) { /* This code is used to change the '> / <' position in the menu and the option the user is 'hovering' over */

    if (kbhit()) {

           KB_code = getch();

           switch (KB_code) {

                 case KB_UP:
                       

                 case KB_DOWN:
                       if (hero_option == 1 && pressed == 1) {
                         hero_option1d();
                       }
                       else if (hero_option == 2 && pressed == 1) {
                         hero_option2d();
                       }
                       else if (hero_option == 3 && pressed == 1) {
                         hero_option3d();
                       }

                 case KB_Y:
                       if (hero_option == 1 && pressed == 1) {
                         hero_option_chosen = "Tank";
                         title_passed = 1;
                         cout << "Tank\n";
                       }
                       else if (hero_option == 2 && pressed == 1) {
                         hero_option_chosen = "Melee";
                         title_passed = 1;
                         cout << "Melee\n";
                       }
                       else if (hero_option == 3 && pressed == 1) {
                         hero_option_chosen = "Ranged";
                         title_passed = 1;
                         cout << "Ranged\n";
                       }

                 default:
                   if (hero_option == 1 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), left_arrow.c_str(), hero_option_1.c_str(), right_arrow.c_str(), fsb.c_str(), hero_option_2.c_str(), fnl.c_str(), fsb.c_str(), hero_option_3.c_str(), fnl.c_str());
                     pressed = 1;
                     break;
                   }
                   else if (hero_option == 2 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), fsb.c_str(), hero_option_1.c_str(), fnl.c_str(), left_arrow.c_str(), hero_option_2.c_str(), right_arrow.c_str(), fsb.c_str(), hero_option_3.c_str(), fnl.c_str());
                     pressed = 1;
                     break;
                   }
                   else if (option == 3 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), fsb.c_str(), option_1.c_str(), fnl.c_str(), fsb.c_str(), option_2.c_str(), fnl.c_str(), left_arrow.c_str(), option_3.c_str(), right_arrow.c_str());
                     pressed = 1;
                     break;
                   }
                 break;
                 }
              }

          }
return 0;
}
