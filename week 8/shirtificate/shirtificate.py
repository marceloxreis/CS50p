from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Renderiza a imagem (certifique-se de que o caminho está correto)
        self.image("shirtificate.png", x=1, y=50, )

        # Define fonte para o título
        self.set_font("helvetica", style="B", size=40)
        self.ln(20)
        self.cell(0, 10, "CS50 SHIRTIFICATE", align="C")
        self.ln(20)



    def generate_certificate(self, name):
        self.add_page()
        self.set_font("Times", size=40)
        self.set_y(120)
        self.cell(0, 10, f"{name} took CS50", align="C")
        self.output("shirtificate.pdf")

# Entrada do usuário e geração do PDF
name = input("Name: ")
pdf = PDF()
pdf.generate_certificate(name)
