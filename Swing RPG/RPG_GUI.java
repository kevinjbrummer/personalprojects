import javax.swing.*;



public class RPG_GUI {
    private static Player player;
    private static JFrame main_menu;

    public RPG_GUI(Player player){
        main_menu = new JFrame("Let's Adventure");
        main_menu.setSize(1000, 600);
        main_menu.setLayout(null);
        main_menu.setVisible(true);
        main_menu.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        RPG_GUI.player = player;
        startGUI();
    }
    public void startGUI(){
        JLabel opening_label = new JLabel("Let's Adventure");
        opening_label.setBounds(450, 0, 500, 400);

        JButton start_button = new JButton("Start ");
        start_button.setBounds(450, 500, 100, 50);
        start_button.addActionListener(e -> {
            main_menu.getContentPane().removeAll();
            main_menu.revalidate();
            main_menu.repaint();
            encounterGUI();
        });

        main_menu.add(start_button);
        main_menu.add(opening_label);


    }
    public void updateStats_GUI(){

        final int[] stat_points = {10};

        JButton up_health = new JButton("↑");
        up_health.setBounds(700, 110, 50, 50);

        JButton down_health = new JButton("↓");
        down_health.setBounds(700, 160, 50, 50);

        JButton up_attack = new JButton("↑");
        up_attack.setBounds(700, 220, 50, 50);

        JButton down_attack = new JButton("↓");
        down_attack.setBounds(700, 270, 50, 50);

        JButton up_defense = new JButton("↑");
        up_defense.setBounds(700, 330, 50, 50);

        JButton down_defense = new JButton("↓");
        down_defense.setBounds(700, 380, 50, 50);

        JLabel health_label = new JLabel("Health: " + player.getMax_health());
        health_label.setBounds(600, 130, 100, 50);

        JLabel attack_label = new JLabel("Attack: " + player.getATK());
        attack_label.setBounds(600, 240, 100, 50);

        JLabel defense_label = new JLabel("Defense: " + player.getDEF());
        defense_label.setBounds(600, 350, 100, 50);

        JButton confirm_button = new JButton("Confirm");
        confirm_button.setBounds(450, 500, 100, 50);

        JLabel remaining_stats = new JLabel("Remaining Points: " + stat_points[0]);
        remaining_stats.setBounds(450, 0, 150, 50);


        main_menu.add(up_health);
        main_menu.add(down_health);
        main_menu.add(up_attack);
        main_menu.add(down_attack);
        main_menu.add(up_defense);
        main_menu.add(down_defense);
        main_menu.add(health_label);
        main_menu.add(attack_label);
        main_menu.add(defense_label);
        main_menu.add(confirm_button);
        main_menu.add(remaining_stats);


        up_health.addActionListener(e -> {
            if (stat_points[0] > 0) {
                player.setMax_health(player.getMax_health() + 1);
                player.setCurrent_health(player.getCurrent_health() + 1);
                stat_points[0] = stat_points[0] - 1;
                health_label.setText("Health: " + player.getMax_health());
                remaining_stats.setText("Remaining Points: " + stat_points[0]);

            }
        });
        down_health.addActionListener(e -> {
            if (stat_points[0] < 12 && player.getMax_health() > 0) {
                player.setMax_health(player.getMax_health() - 1);
                player.setCurrent_health(player.getCurrent_health() - 1);
                stat_points[0] = stat_points[0] + 1;
                health_label.setText("Health: " + player.getMax_health());
                remaining_stats.setText("Remaining Points: " + stat_points[0]);

            }
        });
        up_attack.addActionListener(e -> {
            if (stat_points[0] > 0) {
                player.setATK(player.getATK() + 1);
                stat_points[0] = stat_points[0] - 1;
                attack_label.setText("Attack: " + player.getATK());
                remaining_stats.setText("Remaining Points: " + stat_points[0]);
            }
        });
        down_attack.addActionListener(e -> {
            if (stat_points[0] < 12 && player.getATK() > 0) {
                player.setATK(player.getATK() - 1);
                stat_points[0] = stat_points[0] + 1;
                attack_label.setText("Attack: " + player.getATK());
                remaining_stats.setText("Remaining Points: " + stat_points[0]);
            }
        });
        up_defense.addActionListener(e -> {
            if (stat_points[0] > 0) {
                player.setDEF(player.getDEF() + 1);
                stat_points[0] = stat_points[0] - 1;
                defense_label.setText("Defense: " + player.getDEF());
                remaining_stats.setText("Remaining Points: " + stat_points[0]);
            }
        });
        down_defense.addActionListener(e -> {
            if (stat_points[0] < 12 && player.getDEF() > 0) {
                player.setDEF(player.getDEF() - 1);
                stat_points[0] = stat_points[0] + 1;
                defense_label.setText("Defense: " + player.getDEF());
                remaining_stats.setText("Remaining Points: " + stat_points[0]);
            }
        });

        confirm_button.addActionListener(e -> {
            player.setCurrent_health(player.getMax_health());
            main_menu.getContentPane().removeAll();
            main_menu.revalidate();
            main_menu.repaint();
            encounterGUI();
        });


    }

    public void encounterGUI(){

        final Enemy[] encounter_enemy = {get_enemy(player)};
        JButton attack_button = new JButton("Attack");
        attack_button.setBounds(300, 500, 100, 50);

        JButton use_potion_button = new JButton("Use Potion");
        use_potion_button.setBounds(400, 500, 100, 50);

        JButton run_button = new JButton("Run Away");
        run_button.setBounds(500, 500, 100, 50);

        JLabel level_label = new JLabel("Level " + player.getLevel());
        level_label.setBounds(20, 0, 100, 50);

        JLabel health_label = new JLabel("Health");
        health_label.setBounds(20, 20, 100, 50);

        JProgressBar health_progress = new JProgressBar(0, player.getMax_health());
        health_progress.setString(player.getCurrent_health() + "/" + player.getMax_health());
        health_progress.setStringPainted(true);
        health_progress.setValue(player.getMax_health());
        health_progress.setBounds(110, 35, 100, 20);

        JLabel attack_label = new JLabel("Attack " + player.getATK());
        attack_label.setBounds(20, 40, 100, 50);

        JLabel defense_label = new JLabel("Defense " + player.getDEF());
        defense_label.setBounds(20, 60, 100, 50);

        JLabel potions_label = new JLabel("Potions " + player.getPotionNumber());
        potions_label.setBounds(20, 80, 100, 50);

        JLabel experience_label = new JLabel("XP");
        experience_label.setBounds(20, 100, 100, 50);

        JProgressBar experience_progress = new JProgressBar(0, player.getExperience_to_level_up());
        experience_progress.setString(player.getExperience() + "/" + player.getExperience_to_level_up());
        experience_progress.setStringPainted(true);
        experience_progress.setBounds(110, 115, 100, 20);

        JLabel enemy_art = new JLabel(encounter_enemy[0].getIcon());
        enemy_art.setBounds(300, 10, 500, 500);

        main_menu.add(attack_button);
        main_menu.add(use_potion_button);
        main_menu.add(run_button);
        main_menu.add(level_label);
        main_menu.add(health_label);
        main_menu.add(health_progress);
        main_menu.add(attack_label);
        main_menu.add(defense_label);
        main_menu.add(potions_label);
        main_menu.add(experience_label);
        main_menu.add(experience_progress);
        main_menu.add(enemy_art);

        attack_button.addActionListener(e -> {
            attack_sequence(player, encounter_enemy[0]);
            health_progress.setString(player.getCurrent_health() + "/" + player.getMax_health());
            health_progress.setValue(player.getCurrent_health());
            if (encounter_enemy[0].getCurrent_health() <= 0){
                player.setExperience(player.getExperience() + encounter_enemy[0].getExperience_to_player());
                if(player.getExperience() >= player.getExperience_to_level_up()){
                    player.levelUp();
                    main_menu.getContentPane().removeAll();
                    main_menu.revalidate();
                    main_menu.repaint();
                    updateStats_GUI();
                }
                else {
                    experience_progress.setString(player.getExperience() + "/" + player.getExperience_to_level_up());
                    experience_progress.setValue(player.getExperience());
                    encounter_enemy[0] = get_enemy(player);
                    enemy_art.setIcon(encounter_enemy[0].getIcon());
                }
                int roll = player.rollD20();
                if (roll >= 10) {
                    player.addPotion();
                    potions_label.setText("Potions " + player.getPotionNumber());
                }
            }
        });

        use_potion_button.addActionListener(e -> {
            player.usePotion();
            health_progress.setString(player.getCurrent_health() + "/" + player.getMax_health());
            health_progress.setValue(player.getCurrent_health());
            potions_label.setText("Potions " + player.getPotionNumber());
        });

        run_button.addActionListener(e -> encounter_enemy[0] = get_enemy(player));

    }

    public void attack_sequence(Player player, Enemy encounter_enemy){
        int roll = player.rollD20();
        int dmg_to_player = Math.max(encounter_enemy.getATK() - player.getDEF(), 0);
        int dmg_to_enemy = Math.max(player.getATK() - encounter_enemy.getDEF(), 0);
        if (roll == 1){
            encounter_enemy.setCurrent_health(encounter_enemy.getCurrent_health() - dmg_to_enemy);
            if(encounter_enemy.getCurrent_health() > 0) {
                player.setCurrent_health(player.getCurrent_health() - encounter_enemy.getATK());
            }
        }
        else if (roll == 20){
            encounter_enemy.setCurrent_health(encounter_enemy.getCurrent_health() - player.getATK());
            if(encounter_enemy.getCurrent_health() > 0) {
                player.setCurrent_health(player.getCurrent_health() - dmg_to_player);
            }
        }
        else{
            encounter_enemy.setCurrent_health(encounter_enemy.getCurrent_health() - dmg_to_enemy);
            if(encounter_enemy.getCurrent_health() > 0) {
                player.setCurrent_health(player.getCurrent_health() - dmg_to_player);
            }
        }
    }
    public static Enemy get_enemy(Player player){
        int roll = player.rollD20();
        Enemy encounter_enemy;
        if (roll <= 3){
            encounter_enemy = new Enemy.Demon(player.getLevel());
        }
        else if (roll <= 6){
            encounter_enemy = new Enemy.Dragon(player.getLevel());
        }
        else if (roll <= 10){
            encounter_enemy = new Enemy.Bear(player.getLevel());
        }
        else if (roll <= 15){
            encounter_enemy = new Enemy.Bandit(player.getLevel());
        }
        else{
            encounter_enemy = new Enemy.Goblin(player.getLevel());
        }
        return encounter_enemy;
    }


}
