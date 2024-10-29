import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String file = "Data.txt";
        List<PlayerData> playerDataList = new ArrayList<>();

        // Reading existing data from the file
        try {
            FileInputStream input = new FileInputStream(file);
            ObjectInputStream ois = new ObjectInputStream(input);
            while (true) {
                try {
                    playerDataList.add((PlayerData) ois.readObject());
                } catch (EOFException e) {
                    break;
                }
            }
            ois.close();
            input.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found. Creating a new file.");
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        // Adding new data
        PlayerData newData1 = new PlayerData("NEW2", 1050);
        playerDataList.add(newData1);

        // Sorting the list in descending order based on the score
        Collections.sort(playerDataList, new Comparator<PlayerData>() {
            @Override
            public int compare(PlayerData p1, PlayerData p2) {
                return Integer.compare(p2.score, p1.score);
            }
        });

        // Keeping only the top 5 scorers
        if (playerDataList.size() > 5) {
            playerDataList = playerDataList.subList(0, 5);
        }

        // Saving the updated list back to the file
        try {
            FileOutputStream output = new FileOutputStream(file);
            ObjectOutputStream oos = new ObjectOutputStream(output);
            for (PlayerData playerData : playerDataList) {
                oos.writeObject(playerData);
            }
            oos.close();
            output.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Displaying the updated data
        for (PlayerData playerData : playerDataList) {
            System.out.println(playerData);
        }
    }
}

class PlayerData implements Serializable {
    String name;
    int score;

    public PlayerData(String name, int score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public String toString() {
        return "PlayerData{name='" + name + "', score=" + score + "}";
    }
}