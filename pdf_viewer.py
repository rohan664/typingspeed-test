from fpdf import FPDF
import mysql.connector


def create_pdf() :
    conn = mysql.connector.connect(host="Localhost", user="root", password="rohandesai664",
                                   database="typing_speed")
    my_cursor = conn.cursor()
    query = (
        "SELECT name,wpm,accuracy FROM register ORDER BY personid DESC LIMIT 1;")

    my_cursor.execute(query)
    row = my_cursor.fetchone()
    name, wpm, accuracy = row
    my_pdf = FPDF()
    my_pdf.add_page()
    image = "ribbon.jpg"
    my_pdf.image(image, x=15, y=7)
    cet_name = "Certificate-Geographics-WordArt-1-L (2).jpg"
    my_pdf.image(cet_name, x=70, y=10)
    my_pdf.set_font("Arial", size=30)
    head = "TYPING SPEED TEST"
    my_pdf.cell(60)
    my_pdf.cell(1, 60, txt=head)
    my_pdf.set_font("Arial", size=20)
    text1 = "This certificate is awarded to Mr/Ms : "
    my_pdf.cell(-10)
    my_pdf.cell(1, 100, txt=text1)
    my_pdf.set_font("Arial", size=25)
    my_pdf.cell(20)
    my_pdf.cell(1, 120, txt=name)
    my_pdf.set_font("Arial", size=20)
    line = "___________________________"
    my_pdf.cell(-15)
    my_pdf.cell(1, 125, txt=line)
    my_pdf.set_font("Arial", size=20)
    text2 = "Candidate has successfully Completed our Typing test with below "
    my_pdf.cell(-60)
    my_pdf.cell(10, 160, txt=text2)
    my_pdf.set_font("Arial", size=20)
    text3 = "SPPED(WPM)"
    my_pdf.cell(20)
    my_pdf.cell(10, 200, txt=text3)
    my_pdf.set_font("Arial", size=30)
    my_pdf.cell(8)
    my_pdf.cell(10, 225,txt=wpm)
    my_pdf.set_font("Arial", size=20)
    text4 = "SCORE"
    my_pdf.cell(80)
    my_pdf.cell(10, 200, txt=text4)
    my_pdf.set_font("Arial", size=30)
    my_pdf.cell(2)
    my_pdf.cell(10, 225, txt=accuracy)
    stamp = "certificate_stamp (1).jpg"
    my_pdf.image(stamp, x=135, y=130)
    conn.commit()
    conn.close()
    my_pdf.output("mypdf.pdf")




