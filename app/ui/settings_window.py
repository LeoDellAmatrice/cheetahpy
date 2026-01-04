import customtkinter as ctk


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Configurações")
        self.geometry("420x500")
        self.minsize(380, 420)

        # Mantém a janela "ligada" à principal
        self.transient(master)
        self.grab_set()  # modal (bloqueia a principal)

        self.protocol("WM_DELETE_WINDOW", self.close)

        self.build_ui()

    def build_ui(self):
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            container,
            text="Configurações",
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(anchor="w", pady=(0, 20))

        # Placeholder
        ctk.CTkLabel(
            container,
            text="️Em breve...",
            text_color="gray"
        ).pack(anchor="w")

    def close(self):
        self.grab_release()
        self.destroy()
