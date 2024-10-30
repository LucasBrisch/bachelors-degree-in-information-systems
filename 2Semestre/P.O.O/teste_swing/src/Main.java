import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import javax.swing.*;

public class Main extends JPanel implements ActionListener, KeyListener {
    private int x = 0, y = 0, diameter = 30;
    private int xSpeed, ySpeed;
    private Timer timer;
    private int paddleX = 50, paddleY = 350, paddleWidth = 10, paddleHeight = 100; 
    private boolean gameRunning = true;
    private Random random;

    public Main() {
        random = new Random(); 
        xSpeed = random.nextInt(5) + 1;
        ySpeed = random.nextInt(5) + 1;
        timer = new Timer(30, this);
        timer.start();
        addKeyListener(this);
        setFocusable(true);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (gameRunning) {
            g.setColor(Color.RED);
            g.fillOval(x, y, diameter, diameter);
            g.setColor(Color.BLACK);
            g.fillRect(paddleX, paddleY, paddleWidth, paddleHeight);
        } else {
            g.setColor(Color.BLACK);
            g.drawString("Game Over", getWidth() / 2 - 30, getHeight() / 2);
        }
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(800, 800); 
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (gameRunning) {
            moveBall();
            repaint();
        }
    }

    private void moveBall() {
        x += xSpeed;
        y += ySpeed;

        if (x <= 0 || x >= getWidth() - diameter) {
            xSpeed = -xSpeed;
        }
        if (y <= 0 || y >= getHeight() - diameter) {
            ySpeed = -ySpeed;
        }
        if (x <= paddleX + paddleWidth && y + diameter >= paddleY && y <= paddleY + paddleHeight) {
            xSpeed = -xSpeed;
        } else if (x <= 0) {
            gameRunning = false;
            timer.stop();
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        if (key == KeyEvent.VK_UP && paddleY > 0) {
            paddleY -= 20;
        }
        if (key == KeyEvent.VK_DOWN && paddleY < getHeight() - paddleHeight) {
            paddleY += 20;
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        // Não utilizado
    }

    @Override
    public void keyTyped(KeyEvent e) {
        // Não utilizado
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Ball Game");
        Main game = new Main();
        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}