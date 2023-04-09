import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Rocket here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Rocket extends Actor
{
    public boolean inBounds;
    public boolean mouseOnRocket;
    public int rocketHeight;
    public int rocketWidth;
    
    public boolean mouseBounds(MouseInfo mouseInfo)
    {
        if ((0 < mouseInfo.getX() && mouseInfo.getX() < getWorld().getWidth()) && (0 < mouseInfo.getY() && mouseInfo.getY() < getWorld().getHeight()))
        {
            if (mouseInfo.getX() > getX() || mouseInfo.getX() < getX())
            {
                mouseOnRocket = true;
            }
            return true;
        }
        else 
        {
            return false;
        }
    }

    public void act() 
    {
        rocketHeight = getHeight();
        rocketWidth = getWidth();
        MouseInfo mouseInfo = Greenfoot.getMouseInfo();
        if (mouseInfo != null)
        inBounds = mouseBounds(mouseInfo);
        {
            if (Greenfoot.mouseDragged(null) && (mouseInfo.getX() != getX() && mouseInfo.getY() != getY())) //Checks if the cursor is on the rocket
            {
                move(4);
                turnTowards(mouseInfo.getX(), mouseInfo.getY());
            }
        }
    }    
}
