from typing import Literal

import customtkinter as ctk

from app.ui.frames import desafio_frame, editor_frame, output_frame

from app.domain.desafio import Desafio
from app.services.desafio_service import DesafioService

desafios_gerenciador = DesafioService()


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SnakePy")
        self.minsize(1000, 500)
        self.geometry("1000x500")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)

        self.frame_desafio = desafio_frame.DesafioFrame(master=self, desafio_service=desafios_gerenciador)
        self.frame_output = output_frame.OutputFrame(master=self)
        self.frame_editor = editor_frame.EditorFrame(master=self, desafio_service=desafios_gerenciador, on_output=self.frame_output.set_output)

