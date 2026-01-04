from app.assets.loader_assets import load_logo, load_icon
from app.ui.settings_window import SettingsWindow
import customtkinter as ctk



class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 5), columnspan=2)

        self.grid_propagate(False)

        self.configure(height=68)

        self.grid_columnconfigure(0, weight=0)  # logo
        self.grid_columnconfigure(1, weight=1)  # título (cresce)
        self.grid_columnconfigure(2, weight=0)  # ações
        self.grid_rowconfigure(1, weight=1)

        self.logo_image = load_logo(size=(60, 60))
        self.icon_settings = load_icon("settings", size=(30, 30))

        self.build_frame()

    def build_frame(self):
        # Logo
        ctk.CTkLabel(
            self,
            image=self.logo_image,
            text=""
        ).grid(
            row=0,
            column=0,
            padx=(15, 10),
            sticky="w",
            rowspan=2
        )

        # Título
        ctk.CTkLabel(
            self,
            text="CheetahPy",
            font=ctk.CTkFont(size=20, weight="bold")
        ).grid(
            row=0,
            column=1,
            sticky="w",
            pady=(12, 0)
        )

        # Subtítulo
        ctk.CTkLabel(
            self,
            text="Aprenda lógica de programação com Python",
            font=ctk.CTkFont(size=13),
            text_color="gray"
        ).grid(
            row=1,
            column=1,
            sticky="w",
            pady=(0, 12)
        )

        ctk.CTkButton(
            self,
            image=self.icon_settings,
            text="",
            width=30,
            height=30,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#363636",
            command=self.open_settings
        ).grid(
            row=0,
            column=2,
            rowspan=2,
            padx=(10, 15)
        )

    def open_settings(self):
        SettingsWindow(self.master)