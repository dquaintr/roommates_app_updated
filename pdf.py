import webbrowser

from fpdf import FPDF


class Pdf:
    """
    creates pdf file that contains data about flatmates, such as names, due amount and period of bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, bill):
        flatmate1_pays = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pays = str(flatmate2.pays(bill, flatmate1))
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        #add icon

        pdf.image("house.png", w=30, h=30)

        #title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Rechnung WG", border=1, align="C", ln=1)

        # period lable and value
        pdf.set_font(family="Times", size = 20, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #name and amount
        pdf.set_font(family="Times", size=18)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0, ln=1)

        return(pdf.output(self.filename))
        webbrowser.open(self.filename)
