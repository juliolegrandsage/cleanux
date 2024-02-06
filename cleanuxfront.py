import tkinter as tk
from tkinter import StringVar, ttk
import subprocess

# Déclaration des variables globales
root = None
clean_temp_var = None
clean_linux_temp_var = None
clean_prefetch_var = None
clean_update_cache_var = None
clean_logs_var = None
status_label = None
browser_var = None
progress_bar = None

# Chemins vers les fichiers des scripts bash
clean_system_script_path = "cleanux.sh"
clean_browser_cache_script_path = "browser_cleaners/browser_clean.sh"


def execute_bash_script(script_path, progress_bar, *args):
    try:
        # Démarrer la barre de progression
        progress_bar.start()

        # Exécuter le script bash avec les arguments
        process = subprocess.Popen(["bash", script_path] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Lire les sorties standard et d'erreur en temps réel pour surveiller l'état du processus
        for line in process.stdout:
            # Mettre à jour la barre de progression (vous devrez peut-être ajuster cette logique en fonction du comportement réel de votre script bash)
            progress_bar.step(1)
            root.update_idletasks()

        # Attendre que le processus se termine
        output, error = process.communicate()

        # Arrêter la barre de progression
        progress_bar.stop()

        # Afficher la sortie du script bash dans la console Python
        print(output.decode())
        print(error.decode())

        # Vérifier si une erreur s'est produite dans le processus
        if process.returncode != 0:
            raise Exception("Error occurred")

        # Exemple de message de succès (à remplacer par votre logique réelle)
        status_label.config(text="The cleaning was executed successfully.", fg="green")

    except Exception as e:
        # Afficher un message d'erreur dans l'étiquette de statut
        status_label.config(text=f"The cleaning failed successfully : {str(e)}", fg="red")

    finally:
        # Arrêter la barre de progression si elle est encore en cours
        progress_bar.stop()

        # Mettre à jour l'étiquette pour indiquer que le nettoyage est terminé
        root.after(3000, clear_status_label)


def clear_status_label():
    # Effacer le texte de l'étiquette de statut après un certain délai
    status_label.config(text="", fg="black")


def create_settings_frame(parent_frame):
    # Création du cadre de paramètres
    menu_frame = tk.Frame(parent_frame, bg="#f8f9fa", padx=10, pady=10)

    global clean_temp_var, clean_windows_temp_var, clean_prefetch_var, clean_update_cache_var, clean_logs_var, browser_var, progress_bar
    clean_temp_var = StringVar(value="1")
    clean_windows_temp_var = StringVar(value="1")
    clean_prefetch_var = StringVar(value="1")
    clean_update_cache_var = StringVar(value="1")
    clean_logs_var = StringVar(value="1")

    clean_temp_checkbox = ttk.Checkbutton(menu_frame, text="Clean Temp folder", variable=clean_temp_var)
    clean_temp_checkbox.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    clean_windows_temp_checkbox = ttk.Checkbutton(menu_frame, text="Clean Linux Temp folder", variable=clean_windows_temp_var)
    clean_windows_temp_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    clean_prefetch_checkbox = ttk.Checkbutton(menu_frame, text="Clean Prefetch folder", variable=clean_prefetch_var)
    clean_prefetch_checkbox.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    clean_update_cache_checkbox = ttk.Checkbutton(menu_frame, text="Clean Update Cache", variable=clean_update_cache_var)
    clean_update_cache_checkbox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    clean_logs_checkbox = ttk.Checkbutton(menu_frame, text="Clean Logs", variable=clean_logs_var)
    clean_logs_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    browser_label = ttk.Label(menu_frame, text="Choose Browser:", font=("Helvetica", 10))
    browser_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    browser_options = ["firefox", "brave", "opera", "chromium"]
    browser_var = tk.StringVar(value=browser_options[0])
    browser_combobox = ttk.Combobox(menu_frame, textvariable=browser_var, values=browser_options, state="readonly", width=20)
    browser_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # Ajout de la barre de progression
    global progress_bar
    progress_bar = ttk.Progressbar(menu_frame, orient="horizontal", mode="indeterminate", length=200)
    progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    return menu_frame


def main():
    global root, status_label

    root = tk.Tk()
    root.title("Cleanux")

    # Couleur de fond pour la fenêtre principale
    root.configure(bg="#f8f9fa")

    # Ajout d'un en-tête stylisé
    header_label = tk.Label(root, text="Welcome to Cleanux", font=("Helvetica", 18), bg="#007BFF", fg="white", padx=10, pady=10)
    header_label.grid(row=0, column=0, columnspan=2, sticky="ew")

    # Ajout d'une description
    description_label = tk.Label(root, text="Linux cleaning tool", font=("Helvetica", 12), bg="#f8f9fa", padx=10, pady=10)
    description_label.grid(row=1, column=0, columnspan=2, sticky="ew")

    # Ajout d'un cadre pour les options de nettoyage
    settings_frame = create_settings_frame(root)
    settings_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Ajout d'un bouton "Clean Linux"
    clean_button = tk.Button(root, text="Clean Linux", font=("Helvetica", 14), bg="#007BFF", fg="white", padx=20, pady=10, relief="flat",
                             command=lambda: execute_bash_script(clean_system_script_path, progress_bar,
                                                                 clean_temp_var.get(),
                                                                 clean_windows_temp_var.get(),
                                                                 clean_prefetch_var.get(),
                                                                 clean_update_cache_var.get(),
                                                                 clean_logs_var.get()))
    clean_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Ajout d'une étiquette pour afficher l'état du nettoyage
    status_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f8f9fa")
    status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Ajout d'un pied de page
    footer_label = tk.Label(root, text="by foreach", font=("Helvetica", 10), bg="#007BFF", fg="white", padx=10, pady=5)
    footer_label.grid(row=5, column=0, columnspan=2, sticky="ew")

    # Configurer les poids des lignes et des colonnes pour le redimensionnement
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
