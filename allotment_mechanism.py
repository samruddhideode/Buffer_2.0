import time
from art import *
import pandas as pd



    
comp_allotment=[]
IT_allotment=[]
mech_allotment=[]
elec_allotment=[]
all_allotments=[comp_allotment, IT_allotment, mech_allotment, elec_allotment]
no_allotment = []
    
class Allotment_mechanism:
    
    
    def __init__(self):
        self.allotment_done= False
        self.vacancies={0: 15, 1: 15, 2: 15, 3: 15}
    def run_allotment(self):
        global comp_allotment, IT_allotment, mech_allotment, elec_allotment, all_allotment, no_allotment
        if self.allotment_done== True:
            print("Allotment process done!")
        else:
            print("Running allotment process.. please wait") 
            
            df = pd.read_csv("datasheet.csv")
            allotment = df.sort_values('MARKS', ascending = False)
            print(allotment.to_string(index= False))
            dict1 = {}
            for i in range(len(allotment)):
                #print(allotment.iloc[i][3])
                (surname, marks,pref1,pref2,pref3) = (allotment.iloc[i][1],allotment.iloc[i][3],allotment.iloc[i][4],allotment.iloc[i][5],allotment.iloc[i][6])
                dict1[allotment.iloc[i][0]]= (surname,marks,pref1,pref2,pref3)

            print(dict1)
            for regis in dict1:
                pref1 = dict1[regis][2]
                pref2 = dict1[regis][3]
                pref3 = dict1[regis][4]
                
                if(self.vacancies[pref1]>0):
                    self.vacancies[pref1]-=1
                    all_allotments[pref1].append((regis,dict1[regis][0]))
                elif(self.vacancies[pref2]>0):
                    self.vacancies[pref2]-=1
                    all_allotments[pref2].append((regis,dict1[regis][0]))
                elif(self.vacancies[pref3]>0):
                    self.vacancies[pref3]-=1
                    all_allotments[pref3].append((regis,dict1[regis][0]))
                else:
                    no_allotment.append((regis,dict1[regis][0]))
            
            print("\n\nComp allotment: ", all_allotments[0])
            print("\nIT allotment: ", all_allotments[1])
            print("\nENTC allotment: ", all_allotments[2])
            print("\nMech allotment: ", all_allotments[3])
            print("\nNo allotment: ", no_allotment)
            
            '''dict2={'Computer': all_allotments[0], 'IT': all_allotments[1], 'ENTC': all_allotments[2], 'Mech': all_allotments[3]}
            allot = pd.DataFrame(dict2)
            allot.to_csv('allotment_sheet.csv')'''
            
            #****************Allotment done***********************************
            
            
            
            self.allotment_done= True
            #after 2 secs wait, print the allotment process completed.
            time.sleep(2)
            print("Allotment process completed.") 
            print(tickmark)  