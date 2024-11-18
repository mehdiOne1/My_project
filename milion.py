import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



Sports_questions = [
    ("من يُعرف بلقب 'الأعظم' في رياضة الملاكمة؟", "أ) مايك تايسون", "ب) محمد علي", "ج) فلويد مايويذر", "د) جو فريزر",
     "ب"),
    ("أي فريق فاز بآخر نسخة من دوري أبطال أوروبا؟", "أ) ريال مدريد", "ب) مانشستر سيتي", "ج) بايرن ميونيخ", "د) تشيلسي",
     "أ"),
    ("أي رياضة تستخدم فيها كرة الريشة؟", "أ) الإسكواش", "ب) التنس", "ج) الريشة الطائرة", "د) تنس الطاولة", "ج"),
    ("كم عدد اللاعبين في فريق كرة السلة الأساسي؟", "أ) 4 لاعبين", "ب) 5 لاعبين", "ج) 6 لاعبين", "د) 7 لاعبين", "ب"),
    ("من فاز بجائزة الكرة الذهبية لعام 2022؟", "أ) كريم بنزيما", "ب) محمد صلاح", "ج) كيليان مبابي",
     "د) روبرت ليفاندوفسكي", "أ"),
    ("أي دولة حصدت أكبر عدد من الميداليات الذهبية في أولمبياد طوكيو 2020؟", "أ) الصين", "ب) اليابان",
     "ج) الولايات المتحدة", "د) روسيا", "أ"),
    ("كم عدد الجولات في مباراة الملاكمة الاحترافية الكاملة؟", "أ) 8 جولات", "ب) 10 جولات", "ج) 12 جولة", "د) 15 جولة",
     "ج"),
    ("من هو اللاعب الذي يُعتبر أسطورة في رياضة الفورمولا 1 وحصد 7 ألقاب عالمية؟", "أ) مايكل شوماخر", "ب) لويس هاميلتون","ج) فرناندو ألونسو", "د) سيباستيان فيتيل","أ"),
    ("ما اسم ملعب ليفربول الذي يُعتبر من أشهر الملاعب في إنجلترا؟", "أ) ستامفورد بريدج", "ب) أولد ترافورد", "ج) أنفيلد",
     "د) الإمارات", "ج")
]

Technology_questions = [
    ("من هو مؤسس شركة 'مايكروسوفت'؟", "أ) بيل غيتس", "ب) ستيف جوبز", "ج) مارك زوكربيرغ", "د) إيلون ماسك", "أ"),
    ("ما هو أول هاتف ذكي أطلقته شركة 'آبل'؟", "أ) آيفون 3G", "ب) آيفون 4", "ج) آيفون 6", "د) آيفون الأصلي", "د"),
    ("ما هو نظام التشغيل الذي يقدمه شركة 'غوغل' للأجهزة المحمولة؟", "أ) ويندوز", "ب) iOS", "ج) أندرويد", "د) لينكس",
     "ج"),
    ("من هو مخترع الإنترنت؟", "أ) تيم برنرز لي", "ب) مارك زوكربيرغ", "ج) بيل غيتس", "د) ستيف جوبز", "أ"),
    ("ما هي شركة التكنولوجيا التي أسسها ستيف جوبز؟", "أ) مايكروسوفت", "ب) أبل", "ج) جوجل", "د) تسلا", "ب"),
    ("ما هي أول لغة برمجة تم تطويرها؟", "أ) جافا", "ب) C++", "ج) بايثون", "د) فورتران", "د"),
    ("ما هي لغة البرمجة المستخدمة بشكل رئيسي في تطوير تطبيقات أندرويد؟", "أ) جافا", "ب) بايثون", "ج) سي شارب",
     "د) جافا سكريبت", "أ"),
    ("ما هي لغة البرمجة التي تم تطويرها بواسطة شركة 'آبل' لتطوير تطبيقات iOS؟", "أ) بايثون", "ب) جافا", "ج) سويفت",
     "د) C++", "ج"),
    ("ما هو البروتوكول المستخدم لتحويل النصوص إلى روابط في صفحات الإنترنت؟", "أ) HTML", "ب) HTTP", "ج) FTP", "د) URI",
     "أ")
]

Cultuarl_questions = [
    ("ما هي اللغة الرسمية في البرازيل؟", "أ) الإسبانية", "ب) الإنجليزية", "ج) البرتغالية", "د) الفرنسية", "ج"),
    ("ما هي العملة المستخدمة في اليابان؟", "أ) الين", "ب) اليوان", "ج) الوون", "د) الروبية", "أ"),
    ("ما هو أكبر محيط في العالم؟", "أ) المحيط الأطلسي", "ب) المحيط الهندي", "ج) المحيط الهادئ", "د) المحيط المتجمد الشمالي", "ج",),
    ("ما هي أكبر قارة من حيث المساحة؟", "أ) آسيا", "ب) أفريقيا", "ج) أمريكا الشمالية", "د) أوروبا", "أ"),
    ("ما هو الحيوان الذي يُعتبر رمزًا وطنيًا في أستراليا؟", "أ) الكانغارو", "ب) الكوالا", "ج) الإيمو", "د) الكلب الدنغو", "أ"),
    ("ما هي عاصمة كندا؟", "أ) تورونتو", "ب) فانكوفر", "ج) أوتاوا", "د) مونتريال", "ج"),
    ("ما هي أقدم جامعة في العالم؟", "أ) جامعة هارفارد", "ب) جامعة الأزهر", "ج) جامعة القرويين", "د) جامعة بولونيا", "ج"),
    ("ما هي عاصمة الأرجنتين؟", "أ) بوينس آيرس", "ب) ليما", "ج) سانتياغو", "د) برازيليا", "أ"),
    ("من هو مكتشف قارة أمريكا؟", "أ) فاسكو دا غاما", "ب) كريستوفر كولومبوس", "ج) فرديناند ماجلان", "د) ماركو بولو", "ب")
]

Religious_questions = [
    ("ما هو عدد سور القرآن الكريم؟","أ) 110","ب) 112","ج) 114","د) 116","ج"),
    (" ما هي آخر سورة في القرآن الكريم؟","أ) الفاتحة","ب) الإخلاص","ج) الناس","د) النصر","ج"),
    ("من هو أول خليفة في الإسلام؟","أ) عثمان بن عفان","ب) علي بن أبي طالب","ج) أبو بكر الصديق","د) عمر بن الخطاب","ج"),
    ("من هو النبي الذي ابتلعه الحوت؟","أ) موسى","ب) عيسى","ج) يونس","د) إبراهيم","ج"),
    ("من هو النبي الذي كان يلقب بـ 'خليل الله'؟","أ) عيسى بن مريم","ب) محمد صلى الله عليه وسلم","ج) إبراهيم عليه السلام","د) موسى عليه السلام","ج"),
    ("ما هو أول شيء خلقه الله تعالى؟","أ) الماء","ب) القلم","ج) النور","د) السماء","ب"),
    ("ما هو عدد السجدات في القرآن الكريم؟","أ) 12","ب) 13","ج) 14","د) 15","ب"),
    ("ما هي أطول سورة في القرآن الكريم؟","أ) البقرة","ب) آل عمران","ج) النساء","د) الفاتحة","أ")


]

prizes = [1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000]



class MillionaireGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("من سيربح المليون")
        self.geometry("800x600")
        self.configure(bg="#000000")

        self.bg_image = None
        self.bg_photo = None
        self.load_background("C:\\Users\\MAHDI\\Downloads\\MY_game\\background.jpg")

        self.current_question = 0
        self.current_prize = 0
        self.questions = []
        self.create_category_selection()

    def load_background(self, image_path):

        self.bg_image = Image.open(image_path).resize((1500, 700),  Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self,image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

    def create_category_selection(self):

        self.category_label = tk.Label(self, text="ما نوع الأسئلة التي تريدها؟ ", font=("Arial", 25), bg="#000000", fg="#87CEEB")
        self.category_label.pack(pady=1)

        self.sports_button = tk.Button(self, text="أسئلة رياضية", font=("Arial", 15),width=20, command=self.select_sports,bg="#07293d",fg="#87CEEB")
        self.sports_button.pack(pady=40)

        self.technology_button = tk.Button(self, text="أسئلة تكنولوجية", font=("Arial", 15),width=20, command=self.select_technology,bg="#07293d",fg="#87CEEB")
        self.technology_button.pack(pady=35)

        self.cultural_button = tk.Button(self, text="أسئلة ثقافية", font=("Arial", 15),width=20, command=self.select_cultural,bg="#07293d",fg="#87CEEB")
        self.cultural_button.pack(pady=30)

        self.religious_button = tk.Button(self, text="أسئلة دينية", font=("Arial", 15),width=20, command=self.select_religious,bg="#07293d",fg="#87CEEB")
        self.religious_button.pack(pady=25)
    def select_sports(self):
        self.questions = Sports_questions
        self.start_game()

    def select_technology(self):
        self.questions = Technology_questions
        self.start_game()

    def select_cultural(self):
        self.questions = Cultuarl_questions
        self.start_game()

    def select_religious(self):
        self.questions = Religious_questions
        self.start_game()

    def start_game(self):

        self.category_label.pack_forget()
        self.sports_button.pack_forget()
        self.technology_button.pack_forget()
        self.cultural_button.pack_forget()
        self.religious_button.pack_forget()
        self.create_widgets()

    def create_widgets(self):

        self.question_label = tk.Label(self, text=self.questions[self.current_question][0], font=("Arial", 20), wraplength=550, bg="#000000", fg="#87CEEB")
        self.question_label.pack(pady=1)

        self.option_a_button = tk.Button(self, text=self.questions[self.current_question][1], font=("Arial", 14),
                                         width=30,command=lambda: self.check_answer("أ"), bg="#07293d",fg="#87CEEB")
        self.option_a_button.pack(pady=50)

        self.option_b_button = tk.Button(self, text=self.questions[self.current_question][2], font=("Arial", 14),
                                         width=30, command=lambda: self.check_answer("ب"), bg="#07293d",fg="#87CEEB")
        self.option_b_button.pack(pady=40)

        self.option_c_button = tk.Button(self, text=self.questions[self.current_question][3], font=("Arial", 14),
                                         width=30, command=lambda: self.check_answer("ج"), bg="#07293d",fg="#87CEEB")
        self.option_c_button.pack(pady=40)

        self.option_d_button = tk.Button(self, text=self.questions[self.current_question][4], font=("Arial", 14),
                                         width=30, command=lambda: self.check_answer("د"), bg="#07293d",fg="#87CEEB")
        self.option_d_button.pack(pady=40)

    def check_answer(self, answer):

        correct_answer = self.questions[self.current_question][5]
        if answer == correct_answer:
            self.current_prize = prizes[self.current_question]
            messagebox.showinfo("إجابة صحيحة", f"لقد فزت بـ {self.current_prize} درهم!")
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.update_question()
            else:
                self.end_game("تهانينا! لقد فزت بمليون درهم!")
        else:
            self.end_game("إجابة خاطئة! انتهت اللعبة.")

    def update_question(self):

        self.question_label.config(text=self.questions[self.current_question][0])
        self.option_a_button.config(text=self.questions[self.current_question][1])
        self.option_b_button.config(text=self.questions[self.current_question][2])
        self.option_c_button.config(text=self.questions[self.current_question][3])
        self.option_d_button.config(text=self.questions[self.current_question][4])

    def end_game(self, message):

        messagebox.showinfo("نهاية اللعبة", message)
        self.destroy()


if __name__ == "__main__":
    game = MillionaireGame()
    game.mainloop()
