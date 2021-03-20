import time
from art import *
import pandas as pd



    
comp_allotment=[]
IT_allotment=[]
mech_allotment=[]
elec_allotment=[]
all_allotments=[comp_allotment, IT_allotment, mech_allotment, elec_allotment]
no_allotment = []
    
class Allotment_machanism:
    
    
    def __init__(self):
        self.allotment_done= False
        self.vacancies={0: 120, 1: 60, 2: 60, 3: 120}
    def run_allotment(self):
        global comp_allotment, IT_allotment, mech_allotment, elec_allotment, all_allotment, no_allotment
        if self.allotment_done== True:
            print("Allotment process done!")
        else:
            print("Running allotment process.. please wait") 
            
            df = pd.read_csv("datasheet.csv")
            allotment = df.sort_values('MARKS', ascending = False)
            print(allotment.to_string(index= False))
            
            for i in range(len(allotment)):
                
                pref =  allotment.loc[i,"PREF1"]
                if(self.vacancies[pref]>0):
                    self.vacancies[pref]-=1
                    all_allotments[pref].append(allotment.iloc[i,:].to_string(header = False, index = False)) 
                else:
                    pref =  allotment.loc[i,"PREF2"]
                    if(self.vacancies[pref]>0):
                        self.vacancies[pref]-=1
                        all_allotments[pref].append(allotment.iloc[i,:].to_string(header = False, index = False))
                    else:
                        pref =  allotment.loc[i,"PREF3"]
                        if(self.vacancies[pref]>0):
                            self.vacancies[pref]-=1
                            all_allotments[pref].append(allotment.iloc[i,:].to_string(header = False, index = False))
                        else:
                            no_allotment.append(allotment.iloc[i,:].to_string(header = False, index = False))
            
            print(all_allotments[0])
            print(len(all_allotments[0]))
            self.allotment_done= True
            #after 2 secs wait, print the allotment process completed.
            time.sleep(2)
            print("Allotment process completed.") 
            print(tickmark)  