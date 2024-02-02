import tkinter as tk
from tkinter import messagebox
import subprocess

def execute_bash_script():
    try:
        process = subprocess.Popen(["bash", "cleanux.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        while True:
            output_line = process.stdout.readline()
            if output_line == '' and process.poll() is not None:
                break

        process.communicate()  # Attend la fin du processus
        messagebox.showinfo("Succès", "Le script Bash a été exécuté avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'exécution du script Bash : {str(e)}")

def main():
    root = tk.Tk()
    root.title("Cleanux")

    # Couleur de fond pour la fenêtre principale
    root.configure(bg="#f8f9fa")

    # Ajout d'un en-tête stylisé
    header_label = tk.Label(root, text="Welcome to Cleanux", font=("Helvetica", 18), bg="#007BFF", fg="white", padx=10, pady=10)
    header_label.pack(fill="x")

    # Ajout d'un espace
    space_label = tk.Label(root, text="", bg="#f8f9fa")
    space_label.pack()

    # Ajout d'une description
    description_label = tk.Label(root, text="Linux cleaning tool", font=("Helvetica", 12), bg="#f8f9fa", padx=10, pady=10)
    description_label.pack()

    # Ajout d'un bouton
    button = tk.Button(root, text="Clean Linux", font=("Helvetica", 14), bg="#007BFF", fg="white", padx=20, pady=10, relief="flat", command=execute_bash_script)
    button.pack()

    # Ajout d'un pied de page
    footer_label = tk.Label(root, text="for La Capsule", font=("Helvetica", 10), bg="#007BFF", fg="white", padx=10, pady=5)
    footer_label.pack(fill="x", side="bottom")

    # Ajout d'un pied de page
    footer_label = tk.Label(root, text=" by foreach herself", font=("Helvetica", 10), bg="#007BFF", fg="white", padx=10, pady=5)
    footer_label.pack(fill="x", side="bottom")

    root.mainloop()

if __name__ == "__main__":
    main()
