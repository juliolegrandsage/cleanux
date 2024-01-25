import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess

def execute_bash_script(output_text):
    print("Début de l'exécution du script Bash")
    try:
        process = subprocess.Popen(["bash", "cleanux.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, bufsize=1)

        def read_output():
            output_line = process.stdout.readline()
            if output_line:
                print(output_line, end='')  # Pour débogage
                output_text.insert(tk.END, output_line)
                output_text.see(tk.END)
                output_text.update()

                # Continue de surveiller la sortie du processus
                root.after(1, read_output)
            elif process.poll() is None:
                # Si le processus n'est pas encore terminé, continue de surveiller
                root.after(100, read_output)
            else:
                # Le processus est terminé
                finalize_output_text()

        # Démarre la surveillance de la sortie du processus
        root.after(1, read_output)

    except Exception as e:
        print(f"Erreur lors de l'exécution du script Bash : {str(e)}")
        messagebox.showerror("Erreur", f"Erreur lors de l'exécution du script Bash : {str(e)}")

def finalize_output_text():
    output_text.insert(tk.END, "Nettoyage terminé\n")
    output_text.see(tk.END)
    output_text.update()
    print("Fin de l'exécution du script Bash")
    messagebox.showinfo("Succès", "Le script Bash a été exécuté avec succès.")

def main():
    global root  # Déclarer root en tant que variable globale
    root = tk.Tk()
    root.title("Cleanux")

    # Couleur de fond pour la fenêtre principale
    root.configure(bg="#f8f9fa")

    # Ajout d'un en-tête stylisé
    header_label = tk.Label(root, text="Bienvenue dans Cleanux", font=("Helvetica", 18), bg="#007BFF", fg="white", padx=10, pady=10)
    header_label.pack(fill="x")

    # Ajout d'un espace
    space_label = tk.Label(root, text="", bg="#f8f9fa")
    space_label.pack()

    # Ajout d'une description
    description_label = tk.Label(root, text="Cliquez sur le bouton ci-dessous pour exécuter le nettoyage du système.", font=("Helvetica", 12), bg="#f8f9fa", padx=10, pady=10)
    description_label.pack()

    # Ajout d'un panneau pour la sortie du terminal
    global output_text  # Déclarer output_text en tant que variable globale
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
    output_text.pack(padx=10, pady=10)

    # Ajout d'un bouton
    button = tk.Button(root, text="Nettoyer le système", command=lambda: execute_bash_script(output_text), font=("Helvetica", 14), bg="#007BFF", fg="white", padx=20, pady=10, relief="flat")
    button.pack()

    # Ajout d'un pied de page
    footer_label = tk.Label(root, text="pour La Capsule", font=("Helvetica", 10), bg="#007BFF", fg="white", padx=10, pady=5)
    footer_label.pack(fill="x", side="bottom")

    # Ajout d'un pied de page
    footer_label = tk.Label(root, text="foreach en personne", font=("Helvetica", 10), bg="#007BFF", fg="white", padx=10, pady=5)
    footer_label.pack(fill="x", side="bottom")

    root.mainloop()

if __name__ == "__main__":
    main()
