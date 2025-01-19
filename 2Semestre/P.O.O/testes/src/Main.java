import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.*;

public class Main {
    public static void main(String[] args) {
            String file = "Data.txt";
            List<Player> playerDataList = new ArrayList<>();

            try (FileInputStream input = new FileInputStream(file);
                 ObjectInputStream ois = new ObjectInputStream(input)) {
                while (true) {
                    try {
                        playerDataList.add((Player) ois.readObject());
                    } catch (EOFException e) {
                        break;
                    }
                }
            } catch (FileNotFoundException e) {
                System.out.println("File not found. Creating a new file.");
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }

            playerDataList.add(new Player("NEW0", 0));
            playerDataList.add(new Player("NEW1", 0));
            playerDataList.add(new Player("NEW2", 0));
            playerDataList.add(new Player("NEW3", 0));
            playerDataList.add(new Player("NEW4", 0));

            playerDataList.sort(Comparator.comparingInt(p -> -p.highscore));

            if (playerDataList.size() > 5) {
                playerDataList = playerDataList.subList(0, 5);
            }

            try (FileOutputStream output = new FileOutputStream(file);
                 ObjectOutputStream oos = new ObjectOutputStream(output)) {
                for (Player playerData : playerDataList) {
                    oos.writeObject(playerData);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

            playerDataList.forEach(System.out::println);
        }
    }
    



class PlayerData {
    public static void main(String[] args) {
        String file = "Data.txt";
        List<Player> playerDataList = new ArrayList<>();

        try (FileInputStream input = new FileInputStream(file);
             ObjectInputStream ois = new ObjectInputStream(input)) {
            while (true) {
                try {
                    playerDataList.add((Player) ois.readObject());
                } catch (EOFException e) {
                    break;
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found. Creating a new file.");
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        playerDataList.add(new Player("NEW0", 0));
        playerDataList.add(new Player("NEW1", 0));
        playerDataList.add(new Player("NEW2", 0));
        playerDataList.add(new Player("NEW3", 0));
        playerDataList.add(new Player("NEW4", 0));

        playerDataList.sort(Comparator.comparingInt(p -> -p.highscore));

        if (playerDataList.size() > 5) {
            playerDataList = playerDataList.subList(0, 5);
        }

        try (FileOutputStream output = new FileOutputStream(file);
             ObjectOutputStream oos = new ObjectOutputStream(output)) {
            for (Player playerData : playerDataList) {
                oos.writeObject(playerData);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        playerDataList.forEach(System.out::println);
    }
}



class Player implements Serializable {
    String name;
    int highscore;

    public Player(String name, int highscore) {
        this.name = name;
        this.highscore = highscore;
    }

    @Override
    public String toString() {
        return "Player{name='" + name + "', highscore=" + highscore + "}";
    }
}