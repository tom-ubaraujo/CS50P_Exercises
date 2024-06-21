from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Helvetica", "B", 50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        # self._pdf.image("duck.png", w=self._pdf.epw)
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(0,0,0)
        self._pdf.text(x=65, y=140, text=f"{name} took CS50")

    def save_pdf(self, name):
        self._pdf.output(name)

name = input("What is the name: ")
pdf = PDF(name)
pdf.save_pdf("shirtificate.pdf")