#  This program uses accompanying 'emails.txt' file to store and retrieve emails.


class Email(object):
    #  Class constructor method with prescribed instance variables, including default attribute settings.
    def __init__(self, from_address, email_contents):
          self.has_been_read = False
          self.email_contents = email_contents
          self.is_spam = False
          self.from_address = from_address
          self.sender_address = "jonnie_depro@darkshadows.com"

    #  Class method returns a string representation of an object - sender e-mail address and message contents.
    def __str__(self):
        output =   "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n"
        output +=  "\n"
        output +=  f"From: \033[94m{self.from_address}\033[0m\n\n"
        output +=  f"Msg: \033[94m{self.email_contents}\033[0m\n"
        output +=  "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n"
        return output
      
    #  Class method, marks e-mail as read.
    def mark_as_read(self):
        self.has_been_read = True
    #  Class method, marks e-mail as spam.
    def mark_as_spam(self):
        self.mark_as_spam = True

#  Promts user to enter an e-mail address and message to add new object to 'inbox' list of Email class objects.
def add_email():  
  sender_email = input("\n\033[94mPlease enter the senders E-mail address: \033[0m")
  sender_msg = input("\033[94mPlease enter the E-mail message: \033[0m")
  print("")
  inbox.append(Email(sender_email, sender_msg))
  #  Appends new e-mail address and message to 'emails.txt'.
  with open('emails.txt', 'a') as f:
    f.write(sender_email + ': ' + sender_msg)

#  Displays selected e-mail message using format in __str__ method.
def get_mail(msg_num):
  inbox[msg_num].mark_as_read()
  return (inbox[msg_num].__str__())

#  Counts the number of unread messages in 'emails.txt' initially available to user. 
def get_count():
  f = open('emails.txt', 'r')
  for msg_cnt, line in enumerate(f):  #  Counts each line of 'emails.txt'.
    pass
  f.close()
  return (msg_cnt + 1)

#  Prints out a numbered list of sender e-mails addresses. 
def get_unread_emails():
  list.clear(select_list)  
  for msg_cnt, obj in enumerate(inbox):
    if obj.has_been_read != True and obj.is_spam == False:
      select_list.append(msg_cnt)  #  If Email object unread and not spam, index is stored in 'selet_list'.
      print(f"({select_list.index(msg_cnt)}) {obj.from_address}")  #  Displayed e-mail to user as a selection option.
    else:
      pass

#  Prints out sender address of e-mails marked as spam.
def get_spam_emails():
  for obj in inbox:
    if obj.mark_as_spam == True:
      print(obj.from_address)
    else:
      pass
  
#  Deletes an object from 'inbox' list and removes data from 'emails.txt'.
def delete(msg_num):
  del inbox[msg_num]
  with open('emails.txt', 'w') as f:
    for obj in inbox:
      f.write(obj.from_address + ': ' + obj.email_contents)

#================================================START OF PROGRAM================================================#
  
import copy
import os
inbox = []
select_list = []
spam_mail = []
user_choice = ""

#  Opens 'emails.txt' then splits data and stores as an Email class object in 'inbox' list using list comprehension.
f = open('emails.txt', 'r')
for count, line in enumerate(f):
  fdata = line.split(": ")
  inbox += [Email(from_address, email_contents) for from_address, email_contents in [(fdata[0], fdata[1])]]
f.close() 

#  Displays user e-mail address and total messages in inbox to user.
print(f"\nWelcome \033[94m{inbox[0].sender_address}\033[0m, you have (\033[94m{get_count()}\033[0m) new messages waiting for you. \n")

#  Repeats menu selection until user quits.
while user_choice != "quit":
  user_choice = input("\nWhat would you like to do - read/mark spam/send/quit? ")

  #  If user selects 'read' from main menu.
  if user_choice == "read":
    get_unread_emails()
    if len(select_list) != 0:  #  Continues displaying messages until no more unread messages.
      os.system('clear')
      get_unread_emails()
      
      try:  #  Executes if index for 'selection_list' in range and corresponding integer entered.
        msg_num = int(input("\nSelect the message you want to read: "))
        print(get_mail(select_list[msg_num]))
        #  Executes until user chooses to delete slected message or not.
        while user_choice.lower() != 'no' and user_choice.lower() != 'yes':
          user_choice = input("\nWould you like to delete this message yes/no? ")
          if user_choice.lower() == 'yes':
            delete(select_list[msg_num])  #  Calls function to delete selected message.
            print("\n\033[94m--- Message Deleted ---\033[0m")
          elif user_choice.lower() == 'no':
            pass
          else:
            print("\nPlease enter yes or no:")
      except Exception:
        print("\n\033[94m--- Not a valid selection ---\033[0m")
        
    else:
      print("\n\033[94m--- You have no more messages ---\033[0m")


  #  If user selects 'mark spam' from main menu.     
  elif user_choice == "mark spam":
    get_unread_emails()
    if len(select_list) != 0:  #  Continues displaying messages until no more unread or spam messages.
      os.system('clear')
      get_unread_emails()
      try:
        msg_num = int(input("\nSelect the message you want to mark as spam: "))
        print(get_mail(select_list[msg_num]))
        inbox[select_list[msg_num]].mark_as_spam()  #  Email class object held in 'inbox' list marked as spam.
        print("\n--- SPAM E-MAILS ---\n")
        get_spam_emails()  #  Displays 'spam_mail' list.
        pause = input("\n--- Press Enter ---")
      except Exception:
        print("\n\033[94m--- Not a valid selection ---\033[0m")
    else:
      print("\n\033[94m--- You have no more messages ---\033[0m")
    

  #  If user selects 'send' from main menu.  
  elif user_choice == "send":
    add_email()
    
    
  #  If user selects 'quit' from main menu. 
  elif user_choice == "quit":
      print("\n\033[92m--- Live long and prosper! ---\033[0m")
  else:  
      print("\n\033[94m--- Oops! - incorrect input ---\033[0m")  #  Prompts user for a correct menu selection.
