# -*- coding: utf-8 -*-
"""
MUSTAFA EREN ISIKTASLI 2020510043
SERHAT OZDEMIR 2020510087
"""
#
import pandas;

def indexReturner(comand,littleIndex,bigIndex):
    operations="!<","!>","!=","=<","=>","<",">","="#necessary operators
    index=-1
    indexlen1=-1
    indexlen2=-1
    index2=-1
    
    if(len(comand)==5 or (len(comand)==9) and comand[0]=="select"):#is it for delete or select 
        for x in operations:
            chr = comand[littleIndex].find(x)#finding the operators index
            if(x==comand[littleIndex][chr] or x==comand[littleIndex][chr:chr+2]):#if it is the operand
                index=comand[littleIndex].find(x)#keeps the index
                indexlen1=len(x)#keeps the length of the operand
                break
    elif (len(comand)==7 or (len(comand)==11 and comand[0]=="select")):#is it for delete or it is for select and length is 11
        for x in operations:
            chr= comand[littleIndex].find(x)#first item's oprend's index
            if(x==comand[littleIndex][chr:chr+len(x)]):
                index=comand[littleIndex].find(x)#keeps the index
                indexlen1=len(x)#keeps the length
                break
        for x in operations:
            chr = comand[bigIndex].find(x)#second item's operand's index
            if(x == comand[bigIndex][chr:chr+len(x)]):
                index2=comand[bigIndex].find(x)#keeps the second operands index and length
                indexlen2=len(x)
                break
    return [index,index2,indexlen1,indexlen2]#returns a list of index'
def inputTaker(columns):
    str = input("please Enter an input: ")#getting the input
    comand = str.lower().split(" ")#arrenging the input to valid format to check
    flag= False;
    if(comand[0]=="exit"):#if user exits
        return comand[0]
    
    
    
    
    
    if(comand[0]=="select"):#select operation
        values=comand[1].split(",")#the values will be printed to the consol
        
        indexList= indexReturner(comand, 5, 7)#returns the index' of operations like '<'
        index=indexList[0]#keeps the index of first operations
        index2=indexList[1]#keep the index of second operations
        indexlen1=indexList[2]#keeps the length of the operation for example if =< the length is 2
        indexlen2=indexList[3]
        if(comand[1].lower()=="all"):#if user wants to see all
            values=["id","name","lastname","email","grade"]
        
        
        for x in columns:#loop to check if values is valid
            for y in values:
                if(x==y):
                    flag=True
                    break
                elif(y==values[len(values)-1]):
                    break
            
        if(flag==False):
            print("ERROR! INVALID COLUMN NAME!")
            return 0
        elif((comand[2]=="from" and comand[3]=="students" and comand[4]=="where" )):#format validation
            flag=False
            if((len(comand)==11)):#if there are 2 conditions
                if((">" in comand[5]==-1)and ("<" in comand[5]==-1) and ("=" in comand[5]==-1) and ("!>" in comand[5]==-1)and ("!<" in comand[5]==-1)and ("!=" in comand[5]==-1)):
                    print("ERROR! PROCESS EXPECTED")#comparision control
                    return 0
                elif(comand[6]!="and" and comand[6]!="or"):#and-or control
                    print("ERROR! 'and' or 'or' EXPECTED")
                elif((">" in comand[7]==-1)and ("<" in comand[7]==-1) and ("=" in comand[7]==-1) and ("!>" in comand[7]==-1)and ("!<" in comand[7]==-1)and ("!=" in comand[7]==-1)):
                    print("ERROR! PROCESS EXPECTED")#second comparission control
                    return 0
                elif(comand[8]!="order" or comand[9]!="by" or (comand[10]!="asc" and comand[10]!="dsc")):
                    print("ERROR! ORDER TYPE EXPECTED")#order type control
                    return 0
                elif(comand[5][0:index] not in columns or (comand[7][:index2] not in columns)):
                    print("ERROR! Compare column is False1")#is conditions valid
                    return 0
                else:
                    flag=True
            elif(len(comand)==9):#if there is a single condition
                if((">" in comand[5]==-1)and ("<" in comand[5]==-1) and ("=" in comand[5]==-1) and ("!>" in comand[5]==-1)and ("!<" in comand[5]==-1)and ("!=" in comand[5]==-1)):
                    print("ERROR! PROCESS EXPECTED")#comparision control
                    return 0
                elif(comand[6]!="order" or comand[7]!="by" or (comand[8]!="asc" and comand[8]!="dsc")):
                    print("ERROR! ORDER TYPE EXPECTED")#order type control
                    return 0
                elif(comand[5][0:index] not in columns):#is condition valid
                    print("ERROR! Compare column is False2")
                    return 0
                else:
                    flag=True
            else:
                print("ERROR! INVALID SYNTAX")
                return 0
            if(len(comand)==9) and (comand[5][0:index]!="id" and comand[5][0:index]!="grade") and (comand[5][index:index+indexlen1] != "=" and comand[5][index:index+indexlen1] != "!="):
                print("ERROR! string operations can have '=' or '!=' ")#if comparing the strings operator must be "=" or "!="
                return 0
            elif((len(comand)==11) and (comand[5][0:index]!="id" and comand[5][0:index]!="grade") and (comand[5][index:index+indexlen1] != "=" and comand[5][index:index+indexlen1] != "!=")) or (len(comand)==11 and (comand[7][0:index2]!="id" and comand[7][0:index2]!="grade") and (comand[7][index2:index2+indexlen2] != "=" and comand[7][index2:index2+indexlen2] != "!=")):
                print("ERROR! string operations can have '=' or '!=' ")#if comparing the strings operator must be "=" or "!="
                return 0
            
            if(len(comand)==9):#arrenging the lists to return
                list=(comand[0],values,comand[5][0:index],comand[5][index:index+indexlen1],comand[5][index+indexlen1:],"0","0","0","0",comand[8])
                return list
            elif(len(comand)==11):
                list=(comand[0],values,comand[5][0:index],comand[5][index:index+indexlen1],comand[5][index+indexlen1:],comand[6],comand[7][:index2],comand[7][index2:index2+indexlen2],comand[7][index2+indexlen2:],comand[10])
                return list
            return list
        else:
            print("ERROR! SYNTAX ERROR")
            return 0            
            

            
        
    elif(comand[0]=="insert"):#insert operation
        flag=True
        if(comand[1]!="into" or comand[2]!="students"):#syntax check
            print("ERROR! INVALID SYNTAX")
            flag=False
            return 0
        elif("values(" in comand[3]==-1 or ")" in comand[3]==-1):#syntax check
            print("ERROR! INVALID SYNTAX")
            flag=False
            return 0
        elif(len(comand[3][7:-1].split(","))!=len(columns)):#attributes check 
            print("ERROR! There must be ",len(columns)," attributes")
            flag=False
            return 0
        elif(len(comand[3][7:-1].split(","))==len(columns)):
            temp =comand[3][7:-1].split(",")
            if((temp[0]).isdigit()==False or (temp[1]).isdigit()or (temp[2]).isdigit() or (temp[3]).isdigit() or (temp[4]).isdigit()==False):# string integer check
                flag=False
                print("ERROR! type of the values are not fit, VALUES MUST BE LIKE (ID,NAME,SURNAME,MAIL,GRADE)")
                return 0
        list=(comand[0],temp)
        return list
    elif(comand[0]=="delete"):#delete operation
        flag=True
       
        indexList= indexReturner(comand, 4, 6)#returns the operants index'
        index=indexList[0]
        index2=indexList[1]
        indexlen1=indexList[2]
        indexlen2=indexList[3]
       
        if(comand[1]!="from" or comand[2]!="students" or comand[3]!="where") or index==-1:
            print("ERROR! INVALID SYNTAX")#syntax control
            flag=False
            return 0
        elif(comand[4][:index] not in columns):#attribute check
            flag=False
            print("ERROR! Attribute is not valid")
            return 0
        elif(len(comand)== 7 and comand[6][:index2] not in columns):#second attributes check
            print("ERROR! Attribute2 is not valid")
            flag=False
            return 0
        elif(len(comand)==7 and (comand[5]!= "and" and comand[5]!="or")):#and or check
             print("ERROR! Comperission is not valid")
             return 0
        elif(len(comand)==5) and (comand[4][0:index]!="id" and comand[4][0:index]!="grade") and (comand[4][index:index+indexlen1] != "=" and comand[4][index:index+indexlen1] != "!="):
             print("ERROR! string operations can have '=' or '!=' ")#if comparing the strings operator must be "=" or "!="
             return 0
        elif((len(comand)==7) and (comand[4][0:index]!="id" and comand[4][0:index]!="grade") and (comand[4][index:index+indexlen1] != "=" and comand[4][index:index+indexlen1] != "!=")) or (len(comand)==7 and (comand[6][0:index2]!="id" and comand[6][0:index2]!="grade") and (comand[6][index2:index2+indexlen2] != "=" and comand[6][index2:index2+indexlen2] != "!=")):
             print("ERROR! string operations can have '=' or '!=' ")#if comparing the strings operator must be "=" or "!="
             return 0
         
        if(len(comand)==5):#returning the lists
            list=(comand[0],comand[4][:index],comand[4][index:index+indexlen1],comand[4][index+indexlen1:],"0","0","0","0")
            return list
        elif(len(comand)==7):
            list=(comand[0],comand[4][:index],comand[4][index:index+indexlen1],comand[4][index+indexlen1:],comand[5],comand[6][:index2],comand[6][index2:index2+indexlen2],comand[6][index2+indexlen2:])
            return list
    else:
        print()

    return comand
def insertStudent(studentsDict, idNum, name, lastName, mail, grade):#Insert Function to insert new infos
    newStudent = {'id': idNum,'name':name, 'lastname': lastName, 'email':mail, 'grade':grade}
    studentsDict[len(studentsDict)] = newStudent#appending to the dictionary
    return studentsDict

def selectStudents(studentsDict, col1, cond1, colVal1, statment, col2, cond2, colVal2):#select function to get info
    
    tempDict = conditions(studentsDict, col1, cond1, colVal1)#a temporary dictionary to hold first part of the process
    if statment == "and":
        tempDict = conditions(tempDict, col2, cond2, colVal2)#if the process is and finds the common parts of both dictionaries
    elif statment == "or":
        tempDict2 = conditions(studentsDict, col2, cond2, colVal2)#if the process is or merges the dictionaries
        for key in tempDict2.keys():#a loop for merge
            tempDict[key] = tempDict2[key]
    
    return tempDict


def deleteStudent(studentsDict,col1, cond1, colVal1, statment, col2, cond2, colVal2):#delete operation
    dictToDelete = selectStudents(studentsDict,col1, cond1, colVal1, statment, col2, cond2, colVal2)#determines the dictionary which will be deleted
    for key in dictToDelete:#deletes the choosen parts
        del studentsDict[key]
    

    return studentsDict

def conditions(studentsDict, columnName, cond, inputName):#a function which keeps the conditions by this function we did not have to check over 40 conditions
    if('"' not in inputName):#determines whether the data is string or integer
        inputName=int (inputName)
    else:
        inputName=inputName[1:-1].title()#if it is string ignorse the'"' parts
   
    tempDict = {}#initiallize a new empty dictionary
    for key1 in studentsDict.keys():#loop for datas
        for key2 in studentsDict[key1].keys():#loop for attributes
            if key2 == columnName:
                if cond == "=" and studentsDict[key1][key2] == inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == "!=" and studentsDict[key1][key2] != inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == "<" and studentsDict[key1][key2] < inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == "!<" and studentsDict[key1][key2] >= inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == "<=" and studentsDict[key1][key2] <= inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == ">" and studentsDict[key1][key2] > inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == "!>" and studentsDict[key1][key2] <= inputName:
                    tempDict[key1] = studentsDict[key1]
                elif cond == ">=" and studentsDict[key1][key2] >= inputName:
                    tempDict[key1] = studentsDict[key1] 
            
    
    

    return tempDict

#start of the main

df = pandas.read_csv('students.csv', sep = ';')#reading the file
df = df.sort_values(by = ['id']).reset_index(drop=True)#sorting the file by id 
studentsDict = df.to_dict('index')#a new main dictionary which will keep the whole data

while(True):#the main loop for the program
    try:
        list = inputTaker(df.columns)
        if(list[0]=="select"):#if select is the operation
            dictSelect = selectStudents(studentsDict, list[2], list[3], list[4], list[5], list[6], list[7], list[8]);#call the function with neccessary operations
            dfSelect = pandas.DataFrame.from_dict(dictSelect, orient="index")#turn into pandas to sort
            if(list[len(list)-1]=="asc"):#orders by ascending 
                dfSelect = dfSelect.sort_values(by = [list[1][0]], ascending = True)
            elif(list[len(list)-1]=="dsc"):#orders by descending
                 dfSelect = dfSelect.sort_values(by = [list[1][0]], ascending = False)
            dfSelect = dfSelect.reset_index(drop=True)
            dictSelect = dfSelect.to_dict('index')
            if(len(studentsDict)==0):
                print("NO DATA TO SHOW")
            for key1 in list[1]:
                print(key1, end='\t')
            print()       
                
                
            for key in dictSelect.keys():#a loop for type selected values to the consol
                for x in list[1]:
                    print(dictSelect[key][x], end='\t')#printing
                print()
                        
        elif(list[0]=="insert"):#insert operation
            studentsDict=insertStudent(studentsDict,int(list[1][0]), list[1][1][1:-1].title(), list[1][2][1:-1].title(), list[1][3][1:-1],  int(list[1][4]))#calls insert function to insert the new values to the dictionary
            if(len(studentsDict)==0):
                print("NO DATA TO SHOW")
            for key1 in studentsDict:
                for key2 in studentsDict[key1]:
                    print(key2, end='\t')
                print()
                break
            for key in studentsDict.keys():#a loop for type the values from dictionary to consol
                for x in studentsDict[key].keys():
                    print(studentsDict[key][x], end='\t')
                print()
        elif(list[0]=="delete"):#delete operation
            studentsDict=deleteStudent(studentsDict,list[1], list[2], list[3], list[4], list[5], list[6], list[7])#call delete function with neccessary varibles to delete 
            if(len(studentsDict)==0):
                print("NO DATA TO SHOW")
            for key1 in studentsDict:
                for key2 in studentsDict[key1]:
                    print(key2, end='\t')
                print()
                break
            for key in studentsDict.keys():#a loop for type the values without deleted ones from dictionary to consol
                for x in studentsDict[key].keys():
                    print(studentsDict[key][x], end='\t')
            
                print()
        elif(list =="exit"):#exits if the user types to exit
            print("EXIT THE PROGRAM")
            if(len(studentsDict) == 0):#if the dictionary is not null creates a json file which includes all data in it.
                print("there is no data to write into json!!")
                break
            df = pandas.DataFrame.from_dict(studentsDict, orient="index")#calling pandas library to sort 
            df = df.sort_values(by = ['id']).reset_index(drop=True)
            jsonVersion = df.to_json(r'dataframe.json', orient='records')#create the json file
            break
                
        else:
            print("ERROR! WRONG SYNTAX TRY AGAIN")
    except:
        print("ERROR! TRY AGAIN (AN ERROR COULD BE OR THERE IS NO DATA TO SHOW)")
    
    


