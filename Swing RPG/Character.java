abstract class Character {
    private int max_health;
    private int current_health;
    private int ATK;
    private int DEF;

    public int getMax_health() {
        return max_health;
    }

    public void setMax_health(int max_health) {
        this.max_health = max_health;
    }

    public int getCurrent_health() {
        return current_health;
    }

    public void setCurrent_health(int current_health) {
        this.current_health = current_health;
    }

    public int getATK() {
        return ATK;
    }

    public void setATK(int ATK) {
        this.ATK = ATK;
    }

    public int getDEF() {
        return DEF;
    }

    public void setDEF(int DEF) {
        this.DEF = DEF;
    }
}

