from fpdf import FPDF

FONT_DIR = "/System/Library/Fonts/Supplemental/"

class StyledPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Register Unicode fonts
        self.add_font("Arial", "", FONT_DIR + "Arial.ttf", uni=True)
        self.add_font("Arial", "B", FONT_DIR + "Arial Bold.ttf", uni=True)
        self.add_font("Arial", "I", FONT_DIR + "Arial Italic.ttf", uni=True)
        self.add_font("Arial", "BI", FONT_DIR + "Arial Bold Italic.ttf", uni=True)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"SCU | Season 2: Career Blueprint Challenge | Page {self.page_no()}", align="C")

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(26, 26, 46)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(255, 215, 0)
        self.set_line_width(0.8)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def sub_title(self, title):
        self.set_font("Arial", "B", 11)
        self.set_text_color(26, 26, 78)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def body_text(self, text):
        self.set_font("Arial", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bold_text(self, text):
        self.set_font("Arial", "B", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Arial", "", 10)
        self.set_text_color(30, 30, 30)
        self.cell(6, 5.5, "\u2022")
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def quote_block(self, text):
        self.set_fill_color(255, 253, 240)
        x = self.get_x()
        y = self.get_y()
        self.set_font("Arial", "I", 10)
        self.set_text_color(60, 60, 60)
        self.set_draw_color(255, 215, 0)
        self.set_line_width(1.2)
        # Calculate height first
        w = self.w - self.l_margin - self.r_margin - 8
        lines = self.multi_cell(w, 5.5, text, dry_run=True, output="LINES")
        h = len(lines) * 5.5 + 8
        # Draw background
        self.rect(x, y, self.w - self.l_margin - self.r_margin, h, "F")
        # Draw gold border
        self.line(x, y, x, y + h)
        # Write text
        self.set_xy(x + 8, y + 4)
        self.multi_cell(w, 5.5, text)
        self.set_y(y + h + 4)

    def table_row(self, cols, widths, header=False, alt=False):
        h = 7
        if header:
            self.set_font("Arial", "B", 9)
            self.set_fill_color(26, 26, 46)
            self.set_text_color(255, 255, 255)
        else:
            self.set_font("Arial", "", 9)
            if alt:
                self.set_fill_color(245, 245, 245)
            else:
                self.set_fill_color(255, 255, 255)
            self.set_text_color(30, 30, 30)

        for i, col in enumerate(cols):
            self.cell(widths[i], h, str(col), border=0, fill=True)
        self.ln(h)


pdf = StyledPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 24)
pdf.set_text_color(26, 26, 46)
pdf.cell(0, 14, "Season 2: Read. Reflect. Express.", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_draw_color(255, 215, 0)
pdf.set_line_width(1.2)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(8)

# Intro
pdf.body_text("Hey team,")
pdf.body_text('You\'ve just finished reading Season 2 \u2014 "Build Career, Not Just Get Job." Six episodes. Six universes. One truth.')
pdf.bold_text("Now comes the part that matters: what do YOU do with it?")

# The Career Blueprint Challenge
pdf.section_title("The Career Blueprint Challenge")
pdf.body_text("Attached is a markdown template with 29 questions across 6 phases. Each phase maps to one episode from Season 2. But this isn\'t a quiz about the story \u2014 it\'s about YOUR career.")
pdf.body_text("The same questions Coulson asked Daisy, you\'ll answer about yourself.")

# Schedule
pdf.section_title("The Schedule: One Phase Per Day")
pdf.body_text("This isn\'t a fill-it-all-on-Sunday-night exercise. You\'ll submit one phase per day, starting Tuesday. Each phase takes 10-15 minutes of honest reflection.")
pdf.ln(2)

w = [22, 55, 55, 40]
pdf.table_row(["Day", "Phase", "Episode Connection", "Submit By EOD"], w, header=True)
pdf.table_row(["Tue", "Phase 1: Foundation Audit", "S2E1 \u2014 THE FOUNDATION", "Q1-Q4"], w, alt=False)
pdf.table_row(["Wed", "Phase 2: Loop Map", "S2E2 \u2014 THE BUILDER", "Q5-Q8"], w, alt=True)
pdf.table_row(["Thu", "Phase 3: Self-Test", "S2E3 \u2014 THE BLUEPRINT", "Q9-Q12"], w, alt=False)
pdf.table_row(["Fri", "Phase 4: Mentor Map", "S2E4 \u2014 THE PIPELINE", "Q13-Q16"], w, alt=True)
pdf.table_row(["Mon", "Phase 5: Prevention Audit", "S2E5 \u2014 THE UPTIME", "Q17-Q20"], w, alt=False)
pdf.table_row(["Tue", "Phase 6: Architecture + Final", "S2E6 \u2014 THE ARCHITECT", "Q21-Q29"], w, alt=True)
pdf.ln(4)

pdf.bold_text("Why daily? Because building a career blueprint in one sitting is the same as cramming for a test \u2014 you complete it but you don\'t build anything. One phase per day gives you time to actually sit with each question.")
pdf.ln(2)
pdf.quote_block("Re-read the episode for that day\'s phase before answering. 10 minutes of re-reading, 10-15 minutes of writing. That\'s it.")

# How Submission Works
pdf.section_title("How Submission Works")
pdf.bullet("Submit your updated file by end of day \u2014 each day\'s phase added to your blueprint.")
pdf.bullet("You\'ll receive feedback the same day or next morning \u2014 a score and 1-2 lines on your phase before you start the next one.")
pdf.bullet("This is a conversation, not a test. The daily feedback helps you build a better blueprint. Day 2\'s answers should be sharper than Day 1\'s.")

# Miss a Day
pdf.section_title("What If You Miss a Day?")
pdf.body_text("Life happens. But the daily rhythm matters.")
pdf.ln(2)

w2 = [45, 127]
pdf.table_row(["Missed Submissions", "What Happens"], w2, header=True)
pdf.table_row(["First miss", "You get a reminder. No penalty. Catch up."], w2, alt=False)
pdf.table_row(["Second miss", "That phase loses 20% of its score."], w2, alt=True)
pdf.table_row(["Third miss or more", "That phase scores zero."], w2, alt=False)
pdf.ln(4)

pdf.body_text("If you submit two phases crammed together on the same day, both phases take the penalty \u2014 cramming is completing, not building. That\'s literally the Season 2 lesson.")
pdf.body_text("The weekend (Sat-Sun) is a natural break between Phase 4 (Fri) and Phase 5 (Mon). Use it to sit with what you\'ve written so far.")

# What's Expected
pdf.section_title("What\'s Expected")
pdf.bullet("Be specific. Names, dates, actions \u2014 not aspirations.")
pdf.bullet("If a question is hard to answer, that IS the answer. Write that.")
pdf.bullet("Don\'t polish. Don\'t perform. Just be honest.")

# What Happens After
pdf.section_title("What Happens After All 6 Phases")
pdf.bullet("Your written blueprints will be graded on depth, honesty, and specificity \u2014 not on having impressive answers.")
pdf.bullet("You will then present your Phase 6 (Your Architecture) to the team in a live session. 3-5 minutes each.")
pdf.bullet("The team will ask you questions. You\'ll score each other.")
pdf.bullet("Your final grade combines both: written depth + verbal defense.")
pdf.ln(2)
pdf.body_text("The Peer Defense Guide will be shared before the session so you know how scoring works.")

# AI Tools
pdf.section_title("A Note on Using AI Tools")
pdf.body_text("You\'re welcome to use LLMs to structure your thoughts \u2014 organize your notes, clean up your writing, improve clarity.")
pdf.body_text("But if the LLM is doing the thinking for you, you\'ll know. And so will we \u2014 both in the grading and the moment your team asks you a follow-up question in the defense session.")
pdf.bold_text("The whole point of Season 2 is the difference between completing and building. Don\'t complete this exercise. Build something real with it.")

# One More Thing
pdf.section_title("One More Thing")
pdf.body_text("There are no \"right\" answers. The best blueprints won\'t sound polished. They\'ll sound honest. If your biggest realization is \"I\'ve been firefighting for 2 years and I don\'t know how to stop\" \u2014 that\'s more valuable than a perfect architecture diagram.")
pdf.bold_text("The questions that make you uncomfortable are the ones that matter most.")
pdf.ln(3)

pdf.body_text("Good luck. Build something. One brick per day.")
pdf.ln(2)

# Signature — keep on same page
pdf.set_font("Arial", "B", 12)
pdf.set_text_color(26, 26, 46)
pdf.cell(0, 8, "\u2014 Swami", new_x="LMARGIN", new_y="NEXT")

# Output
output = "S2_Team_Communication.pdf"
pdf.output(output)
print(f"PDF generated: {output}")
