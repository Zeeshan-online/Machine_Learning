
from sklearn.ensemble import RandomForestRegressor
import numpy as np

class HardcoreAICoach:
    
    def __init__(self):
        self.history = []
        self.model_calorie = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model_weight =RandomForestRegressor(n_estimators=100, random_state=42)
        
        # sample training data
        
        x = np.array([
            [25, 1.70, 70, 1],
            [30, 1.75, 80, 2],
            [35, 1.68, 90, 1],
            [40, 1.80, 85, 3]
        ]) 
        # age, height, weight, activity
        
        y_cal = np.array([2200, 2600, 2800, 3000])
        y_weight = np.array([70, 80, 90, 85])
        
        self.model_calorie.fit(x, y_cal)
        self.model_weight.fit(x, y_weight)
        print("🤖 Hardcore AI Coach Ready")
        
     
    def get_user(self):
        age = int(input("Enter your age: "))
        h = float(input("Enter your height (m): "))
        w = float(input("Enter your weight (kg): "))
        act = int(input("Activity (1=low, 2=medium, 3=high): "))
        return age, h, w, act 
    
    def bmi(self, h, w):
        return w / (h * h)
    
    def predict(self, age, h, w, act):
        x = np.array([[age, h, w, act]])
        cal = int(self.model_calorie.predict(x)[0])
        bmi = self.bmi(h, w)
        self.history.append((w))
        
        print(f"\n 🔥 AI calories: {cal}")
        print(f"🧠 BMI: {bmi:.1f}")
        if bmi > 25:
             print("🎯 Goal: Fat Loss | Eat -500 kcal")
       
        elif bmi < 18.5:
            print("🎯 Goal: Muscle Gain | Eat +400 kcal")
        else:
            print("🎯 Goal: Maintain")
            
        self.macro_prediction(cal,)
        
    def predict_weight_future(self,):
        if not self.history:
            print("📉 No enoungh data to predict weight")
            return
        age, h, w, act = self.get_user()
        future_weight = int(self.model_weight.predict([[age, h, w, act]])[0])
        print(f"📈 predict future weight: {future_weight} kg")
        
        
    def plateau_detction(self):
        if len(self.history) < 3:
            return
        if self.history[-1] == self.history[-2] == self.history[-3]:
            print("⚠️ plateau detected! change your routine or diet!")
            
        else:
            print("✅ progress is ongoing")        
                   
     
    def macro_prediction(self, calories):
        protein = int(calories * 0.3 / 4)
        carbs = int(calories * 0.4 / 4)
        fat = int(calories * 0.3 / 9)
        print(f"🥗 marco Recommendation: protein: {protein}g, |🍞 carbs {carbs}g |🧈 Fat {fat}g")    
        
        
    def chat_coach(self):
        print("🗯️ AI Coach: Hey! How do you feel today?")
        msg = input("You: ")
        print("🗯️ AI Coach: Got it! keep consistency and track progress!")               
        
    def menu(self):
        while True:
            print("\n1.Calories 2.Future Weight 3.Plateau Detection 4.Chat with Coach 5.Exit")    
            c = int(input("Choose an option: "))
            if c == 1:
                age, h, w, act, = self.get_user()
                self.predict(age, h, w, act)
            elif c == 2:
                self.predict_weight_future()
            elif c == 3:
                self.plateau_detction()
            elif c == 4:
                self.chat_coach()
            elif c == 5:
                break
            else:
                print("❌ Invalid choice") 
                
                
HardcoreAICoach().menu()                               