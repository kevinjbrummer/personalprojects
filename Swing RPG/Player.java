import java.util.Random;

public class Player extends Character{
    private int level;
    private int experience;
    private int experience_to_level_up;
    private int potion;

    public Player(){
        this.setLevel(1);
        this.setATK(10);
        this.setDEF(5);
        this.setMax_health(10);
        this.setCurrent_health(10);
        this.setExperience(0);
        this.setExperience_to_level_up(1000);
        this.potion = 5;

    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }

    public int getExperience_to_level_up() {
        return experience_to_level_up;
    }

    public void setExperience_to_level_up(int experience_to_level_up) {
        this.experience_to_level_up = experience_to_level_up;
    }

    public void addPotion(){

        this.potion = potion + 1;
    }

    public int getPotionNumber(){
        return this.potion;
    }

    public void usePotion(){
        this.setCurrent_health(Math.min(getCurrent_health() + 5, getMax_health()));
        this.potion = this.potion - 1;
    }

    public void levelUp(){
        this.setExperience(this.getExperience() - this.getExperience_to_level_up());
        this.setLevel(this.getLevel() + 1);
        this.setExperience_to_level_up(1000 * this.getLevel());

    }

    public int rollD20(){
        Random random = new Random();
        return random.nextInt(20) + 1;
    }



}
