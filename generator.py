from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'THE RELENTLESS PROTOCOL', 0, 1, 'C')
        self.ln(10)

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    body_text = """
    INTERMEDIATE HYPERTROPHY // UPPER-LOWER SPLIT
    OBJECTIVE: BUILD MUSCLE. BREAK PLATEAUS.
    MINDSET: NO SKIMPING. NO SOFT CORNER. ONLY GOALS.
    
    ---------------------------------------------------------
    I. THE NUTRITION MANDATE (The "Egg-etarian" Code)
    Target: 1.6g - 2g of protein per KG of bodyweight.
    
    1. EGGS: The Holy Grail. 3-4 whole eggs, rely on EGG WHITES.
    2. WHEY: Non-negotiable. 1-2 scoops post-workout.
    3. SOYA CHUNKS: Highest protein per gram veg source.
    4. DAIRY: Greek Yogurt, Paneer. Keep fats in check.
    
    ---------------------------------------------------------
    II. THE BATTLE PLAN (3-4 Days/Week)
    
    SESSION A: UPPER BODY (Strength/Power)
    - Barbell Bench Press: 4 sets x 6-8 reps (Heavy compound)
    - Bent-Over Barbell Row: 4 sets x 8-10 reps (Strict form)
    - Overhead Press: 3 sets x 8-10 reps
    - Lat Pulldown (Wide): 3 sets x 10-12 reps
    - Dumbbell Bicep Curl: 3 sets x 12 reps
    - Tricep Rope Pushdown: 3 sets x 12-15 reps
    
    SESSION B: LOWER BODY (Squat Focus)
    - Barbell Back Squat: 4 sets x 6-8 reps (Ass to grass)
    - Romanian Deadlift: 3 sets x 8-10 reps (Feel the stretch)
    - Leg Press: 3 sets x 12-15 reps
    - Walking Lunges: 3 sets x 12/leg
    - Calf Raises: 4 sets x 15-20 reps
    
    SESSION C: UPPER BODY (Hypertrophy)
    - Incline DB Press: 4 sets x 8-12 reps
    - Pull-Ups / Pulldowns: 3 sets x Failure
    - Seated Cable Row: 3 sets x 10-12 reps
    - Lateral Raises: 4 sets x 15 reps
    - Face Pulls: 3 sets x 15 reps
    - Skull Crushers: 3 sets x 10-12 reps
    
    ---------------------------------------------------------
    III. THE TECHNICIAN'S MANUAL (Cues)
    
    BENCH PRESS: Bend the bar in half with your hands.
    SQUAT: Spread the floor with your feet.
    DEADLIFT: Push the earth away. Don't pull.
    ROW: Drive elbows to the ceiling.
    """
    
    # Clean text to prevent encoding errors
    pdf.multi_cell(0, 10, body_text.encode('latin-1', 'replace').decode('latin-1'))
    
    # Ensure the public folder exists
    output_path = "public/Relentless_Protocol.pdf"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    pdf.output(output_path)
    print(f"PDF generated successfully at {output_path}")

if __name__ == "__main__":
    create_pdf()
