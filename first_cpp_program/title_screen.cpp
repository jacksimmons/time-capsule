int title_screen() {
  startup();
  while((KB_code != KB_ESCAPE)) { /* This code is used to change the '> / <' position in the menu and the option the user is 'hovering' over */

    if (kbhit()) {

           KB_code = getch();

           switch (KB_code) {

                 case KB_UP:
                       if (option == 1 && pressed == 1) {
                         option1u();
                       }
                       else if (option == 2 && pressed == 1) {
                         option2u();
                       }
                       else if (option == 3 && pressed == 1) {
                         option3u();
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

                 case KB_Y:
                    if (title_passed < 1) {
                       if (option == 1 && pressed == 1) {
                         option_chosen = "Play";
                         title_passed = 1;
                         play_chosen();
                       }
                       else if (option == 2 && pressed == 1) {
                         option_chosen = "Settings";
                         title_passed = 1;
                         settings_chosen();
                       }
                       else if (option == 3 && pressed == 1) {
                         exit(0);
                       }
                    }
                    else if (title_passed = 1) {
                       if (option == 1 && pressed == 1) {
                         option_chosen = "Video";
                         title_passed = 2;
                         video_chosen();
                       }
                       else if (option == 2 && pressed == 1) {
                         option_chosen = "Game";
                         title_passed = 2;
                         game_chosen();
                       }
                       else if (option == 3 && pressed == 1) {
                         option_chosen = "Back";
                         title_passed = 0;
                         restart();
                         break;
                       }
                    }
                    else if (title_passed = 2) {
                       if (option == 1 && pressed == 1) {
                         option_chosen = "Text Colour";
                         title_passed = 3;
                         first_option();
                         break;
                       }
                       // else if (option == 2 && pressed == 1) {
                       //   option_chosen = "Text Shadow";
                       //   title_passed = 3;
                       //   background_chosen();
                       //   break;
                       //}
                       else if (option == 3 && pressed == 1) {
                         option_chosen = "Back";
                         title_passed = 1;
                         restart();
                         break;
                       }
                    }

                 default:
                   option_1 = first_option();
                   option_2 = second_option();
                   option_3 = third_option();
                   current_menu = c_menu_option();
                   if (option == 1 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), left_arrow.c_str(), option_1.c_str(), right_arrow.c_str(), fsb.c_str(), option_2.c_str(), fnl.c_str(), fsb.c_str(), option_3.c_str(), fnl.c_str());
                     pressed = 1;
                     break;
                   }
                   else if (option == 2 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), fsb.c_str(), option_1.c_str(), fnl.c_str(), left_arrow.c_str(), option_2.c_str(), right_arrow.c_str(), fsb.c_str(), option_3.c_str(), fnl.c_str());
                     pressed = 1;
                     break;
                   }
                   else if (option == 3 && pressed == 0) {
                     cls();
                     printf("%s %s %s %s %s %s %s %s %s %s \n\n", current_menu.c_str(), fsb.c_str(), option_1.c_str(), fnl.c_str(), fsb.c_str(), option_2.c_str(), fnl.c_str(), left_arrow.c_str(), option_3.c_str(), right_arrow.c_str());
                     pressed = 1;
                     break;
                   }
           }
    }
}
return 0;
}
