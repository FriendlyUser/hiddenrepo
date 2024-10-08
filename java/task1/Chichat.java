import java.awt.Color;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.*;

public class Chichat {

    public static void main(String[] args) {
        // Initialize the application
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new LoginForm().setVisible(true);
            }
        });
    }
}

class RegisterForm extends JFrame {
    Connection connect = null;
    PreparedStatement preparedStatement = null;
    ResultSet result;

    JTextField fnameText, lnameText, emailText, contactText, unameText;
    JPasswordField upasswordText;
    JButton register, cancel;

    public RegisterForm() {
        initComponents();
    }

    private void initComponents() {
        JPanel panel = new JPanel();
        JLabel fname = new JLabel("First Name");
        fnameText = new JTextField(15);
        JLabel lname = new JLabel("Last Name");
        lnameText = new JTextField(15);
        JLabel email = new JLabel("E-Mail");
        emailText = new JTextField(15);
        JLabel contact = new JLabel("Contact");
        contactText = new JTextField(15);
        JLabel username = new JLabel("Username");
        unameText = new JTextField(15);
        JLabel password = new JLabel("Password");
        upasswordText = new JPasswordField(15);
        register = new JButton("Register");
        cancel = new JButton("Cancel");

        // Add components to panel

        // Add panel to frame
        this.add(panel);
        this.pack();
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
}

class LoginForm extends JFrame {

    Connection cn = null;
    PreparedStatement tex = null;
    ResultSet result;

    JPasswordField passwordText;
    JTextField userText;

    public LoginForm() {
        initComponents();
    }

    private void initComponents() {
        JPanel panel = new JPanel();
        JLabel jLabel6 = new JLabel("Login Form");
        JLabel jLabel1 = new JLabel("Username");
        JLabel jLabel2 = new JLabel("Password");
        passwordText = new JPasswordField(15);
        userText = new JTextField(15);
        JButton loginButton = new JButton("Login");

        // Add components to panel

        // Configure login button
        loginButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Add login logic here
            }
        });

        // Add panel to frame
        this.add(panel);
        this.pack();
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
}

class SQLConnect {

    public static Connection connectDatabase() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection cn = DriverManager.getConnection("jdbc:mysql://localhost:3306/chitchat?" + "user=root");
            Statement st = cn.createStatement();
            // JOptionPane.showMessageDialog(null,"connectedd");
            return cn;

        } catch (ClassNotFoundException | SQLException | HeadlessException e) {
            JOptionPane.showMessageDialog(null, "mysql not connectedd");
            return null;
        }
    }
}

class MainFrame extends JFrame {

    public MainFrame() {
        initComponents();
    }

    private void initComponents() {
        JPanel mainPan = new JPanel();
        JButton join = new JButton("Join");
        JButton create = new JButton("Create");

        // Add components to mainPan

        // Add mainPan to frame
        this.add(mainPan);
        this.pack();
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
}
