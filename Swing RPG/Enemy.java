import javax.swing.*;
import java.util.Random;

abstract class Enemy extends Character {
    public int experience_to_player;
    public ImageIcon icon;

    public Enemy(int player_level){
        Random random = new Random();
        this.setMax_health((random.nextInt(5)+1)*player_level);
        this.setCurrent_health(this.getMax_health());
        this.setATK((random.nextInt(5)+1)*player_level);
        this.setDEF((random.nextInt(5)+1)*player_level);
        this.experience_to_player
                = ((this.getMax_health() + this.getATK() + this.getDEF())*3)*player_level;
    }

    public int getExperience_to_player() {
        return this.experience_to_player;
    }

    public ImageIcon getIcon(){
        return this.icon;
    }


    public static class Dragon extends Enemy{

        public Dragon( int player_level) {
            super(player_level);
            this.icon = new ImageIcon("C:\\Users\\kjbru\\IdeaProjects\\RPG\\src\\Dragon_Icon_2.PNG");
        }



    }

    public static class Goblin extends Enemy{


        public Goblin(int player_level) {

            super(player_level);
            this.icon = new ImageIcon("C:\\Users\\kjbru\\IdeaProjects\\RPG\\src\\Goblin_Icon.PNG");
        }

    }

    public static class Bandit extends Enemy{
        public Bandit(int player_level) {

            super(player_level);
            this.icon = new ImageIcon("C:\\Users\\kjbru\\IdeaProjects\\RPG\\src\\Bandit_Icon.PNG");
        }
    }

    public static class Demon extends Enemy {


        public Demon(int player_level) {
            super(player_level);
            this.icon = new ImageIcon("C:\\Users\\kjbru\\IdeaProjects\\RPG\\src\\Demon_Icon.PNG");

        }
    }

    public static class Bear extends Enemy{
        public Bear(int player_level) {

            super(player_level);
            this.icon = new ImageIcon("C:\\Users\\kjbru\\IdeaProjects\\RPG\\src\\Bear_Icon.PNG");
        }
    }
}
