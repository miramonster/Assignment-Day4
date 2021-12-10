tasks = []

while True:
   print("============================")
   print('Enter 1 to add task: '),
   print('Enter 2 to delete task: '),
   print('Enter 3 to view all tasks: '),
   print('Enter q to quit')
   print("============================")
   print("\n")
   choice = input("Enter choice: ")
   

   if choice == "1": 
    title = input("Enter title: ")
    priority = input("Enter priority: ")
    task = {"Task": title, "Priority": priority}
    tasks.append(task)
    for item in range(len(tasks)):
      task = tasks[item]
      print(f"{item+1}. TASK: {task['Task']} - PRIORITY: {task['Priority']}")
   elif choice == "2":
    title = int(input("Enter number of task you wish to delete: "))
    print(f"{item+1}. TASK: {task['Task']} - PRIORITY: {task['Priority']}") 
    for item in range (0, len(tasks)):
      int(input("Enter number of task you wish to delete: ")) 
      del tasks[title]
   elif choice == "3":
      for index in range(len(tasks)):
          task = tasks[item]
      print(f"{item+1}. TASK: {task['Task']} - PRIORITY: {task['Priority']}")
        
   elif choice == "q": 
     break         
     
     print(tasks)

   