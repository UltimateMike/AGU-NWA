# Error Handling

# numbers = [10, 5, 6, 8, 0, 12, 9]
# for num in numbers: 
#     try:
#        result = 100/num
#        print(f"100 divided by {num} is {result}")
#     except ZeroDivisionError:
#         print("100 is not divisiable by 0") 
    
    
        
# numbers = ["10", "5","6","8","Faith","12","9"]
# for item in numbers:
#     try:
#        num = int(item)
#        print(f"Successfully Converted {num}")
#     except ValueError:
#         print(f"{item} is a text not a number")
#     finally:
#         print("Everthing worked")



# Dictionaries and lists in Error Handling

# studentData = {"Ultimate": "90", "Chioma": "50", "Uche": "60"}
# studentNames = ["Ultimate", "Chioma", "Faith", "Uche"]
# for name in studentNames:
#     try:
#          print(f"found {name}'s name and their score is {studentData[name]}")
#     except KeyError:
#         print("Faith not found")
#     finally:
#         print(f"I am done going through {studentNames} and i found the above") 
        
        
        
# studentData = {"Ultimate": "90", "Chioma": "50", "Uche": "60"}
# studentNames = ["Ultimate", "Chioma", "Faith", "Uche"]
# for name in studentNames:
#     try:
#         print(f"found {name}'s name and their score is {studentData[name]}")
#     except KeyError:
#         print("Faith not found")        


# attempts = 0
# while attempts <2:
#    try:
#         choice = int(input("Please enter a lucky number:\n"))
#         print(f"Congratulations! You choosed {choice}")
#         break
#    except ValueError:
#        print("Please enter a valid number")
#        attempts +=1  
       
       
# attempts = 0
# while attempts <2:
#    try:
#         choice = int(input("Please enter a lucky number:\n"))
#         print(f"Congratulations! You choosed {choice}")
        
#    except ValueError:
#        print("Please enter a valid number")
#        attempts +=1





# colors = ["red", "blue","green"]
# positionIndex = [0,1,5]
# for col in positionIndex:
#     try:
#         print(f"found {col} in colors and their position in {colors[col]}")
#     except IndexError:
#         print("5 not found")


# colors = ["red", "blue","green"]       
# attempts = 2

# while attempts >= 0:
#     try:
#         print(f"for colors in attempts is {colors[attempts]}")
#         attempts -=1 
#     except IndexError:
#         print("No more colors at the index\n attempts error reached")
        
        