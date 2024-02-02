import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class helloworld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("irlinique");


        String pythonScriptPath = "cleanuxfront.py"; // Remplacez par le chemin réel de votre script Python

        // Spécifiez le chemin vers l'interpréteur Python
        String pythonInterpreter = "python";

        // Ajoutez l'option -i pour permettre l'affichage de l'interface graphique
        ProcessBuilder processBuilder = new ProcessBuilder(pythonInterpreter, "-i", pythonScriptPath);

        try {
            // Lancez le processus
            Process process = processBuilder.start();

            // Lisez la sortie du processus
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Attendez que le processus se termine
            int exitCode = process.waitFor();
            System.out.println("Le script Python s'est terminé avec le code de sortie : " + exitCode);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
