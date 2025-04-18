import colorama
import re
# from IPython.display import Image
from colorama import Fore, Back, Style
def print_course_details():
    print(Fore.LIGHTRED_EX + "\nChoose a course you want to enroll:")
    print(Fore.BLUE + "\n1. C/C++")
    print(Fore.LIGHTGREEN_EX + "\n2. Core / Advance Java")
    print(Fore.LIGHTMAGENTA_EX + "\n3. Python")
    print(Fore.LIGHTRED_EX + "\n4. Golang")
    print(Fore.BLUE + "\n5. HTML/CSS/JavaScript")
    print(Fore.LIGHTGREEN_EX + "\n6. DotNet")
    print(Fore.LIGHTMAGENTA_EX + "\n7. C#")
    print(Fore.LIGHTRED_EX + "\n8. Ethical Hacking")
    print(Fore.BLUE + "\n9. Computer Hacking Forensic Investigator (CHFI)")
    print(Fore.LIGHTGREEN_EX + "\n10. Networking")
    print(Fore.LIGHTMAGENTA_EX + "\n11. Cyber Law")
    print(Fore.LIGHTRED_EX + "\n12. Exit")

def admission_chatbot():
    print(Style.BRIGHT + Fore.BLUE + "Welcome to Connectinwhizttech ChatBot")
    name = input("\nEnter your name: ")

    while True:
        user_input = input("\nEnter your contact number: ")
        if not user_input.isdigit():
            print("Please enter a valid contact number. It should only contain digits.")
        else:
            contact_number = int(user_input)
            break

    email = input("Enter your email: ")
    city = input("\nEnter your city: ")
    qualification = input("\nEnter your qualification: ")

    print(Style.BRIGHT + Fore.GREEN + f"\nHello {name}")

    while True:
        print_course_details()

        user_input = input("Enter the course number: ")

        if user_input == "1":
            print(Fore.LIGHTGREEN_EX + "\n1. C/C++")
            print(Fore.BLUE + "\nCareer Options: 1. C/C++ Developer \n2. Analyst.")
            print(Fore.LIGHTGREEN_EX + "\nAdmission Fees: â‚¹ 5000")
            print(Fore.BLUE + "\nLast Date to Apply: 30th June")
            print(Fore.RED + "\nOnline Offline Classes Available From 1st July")
            print(Fore.LIGHTGREEN_EX + "\nProjects and Internship Available")

        elif user_input == "2":
            print(Fore.LIGHTBLUE_EX + "\n2. Core / Advance Java:")
            print("\nCareer Options:\n1. Java Developer,\n2. DevOps Engineer,\n3. Solutions Architect,\n4. Project Manager.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "3":
            print(Fore.BLUE + "\nPython:")
            print("\nCareer Options:\n1. Data Analyst,\n2. Cyber Security Expert,\n3. Machine Learning Engineer,\n4. Database Administrator.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "4":
            print(Fore.RED + "\nGolang:")
            print("\nCareer Options:\n1. Golang Developer,\n2. Backend Developer,\n3. Open Source Contributor,\n4. Technical Lead.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "5":
            print(Fore.BLUE + "\nHTML/CSS/JavaScript:")
            print("\nCareer Options:\n1. Web Developer,\n2. Front-end Developer,\n3. JavaScript Developer,\n4. Content Editor,\n5. HTML Email Developer,\n6. SEO Specialist,\n7. UI Designer.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "6":
            print(Fore.GREEN + "\nDotNet:")
            print("\nCareer Options:\n1. .NET Software Developer,\n2. .NET Engineer,\n3. .NET Architect or .NET Applications Architect.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "7":
            print(Fore.RED + "\nC#:")
            print("\nCareer Options:\n1. C# Developer,\n2. Software Engineer,\n3. Application Developer,\n4. Web Developer,\n5. Systems Analyst,\n6. Solution Architect,\n7. Technical Lead,\n8. Backend Developer.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "8":
            print(Fore.GREEN + "\nEthical Hacking:")
            print("\nCareer Options:\n1. Network Support,\n2. Network Engineering,\n3. Various positions related to information security.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "9":
            print(Fore.BLUE + Back.WHITE + "\nComputer Hacking Forensic Investigator (CHFI):")
            print("\nCareer Options:\n1. Forensic Analyst,\n2. Security Consultant,\n3. Incident Responder,\n4. IT Auditor.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "10":
            print(Fore.RED + Back.WHITE + "\nNetworking:")
            print("\nCareer Options:\n1. Network Administrator,\n2. Network Analyst,\n3. IT Help Desk Technician,\n4. Network Specialist,\n5. Network Architect,\n6. Database Administrator.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "11":
            print(Style.BRIGHT + "\nCyber Law:")
            print("\nCareer Options:\n1. Cyber Lawyer,\n2. Cyber Assistant,\n3. Cyber Advisor,\n4. Information Security Auditor,\n5. Research Assistant,\n6. Specialist in Cyber Arbitration.")
            print("\nAdmission Fees: â‚¹ 20000")
            print("\nLast Date to Apply: 30th June")
            print("\nOnline Offline Classes Available From 1st July")
            print("\nProjects and Internship Available")

        elif user_input == "12":
            print("Thank you for using Connectinwhizttech ChatBot. Goodbye!")
            break

        else:
            print(Back.MAGENTA + Fore.WHITE + "Sorry, I didn't get you. Please choose a number between 1 and 12.")

        further_question = input("\nDo you have any other questions? (yes/no): ").strip().lower()
        if further_question == "no":
            print(Style.BRIGHT + Fore.BLUE + "\nThank you for using Connectinwhizttech ChatBot. Goodbye!")
            print(Style.BRIGHT + Fore.RED + "\nFor more details contact:\nMs. Shruti Jain\nConnectin Whizttech\n1st Floor Singapur Complex\nDiwanwadi Road, Chhatrapati Sambhajinagar (Aurangabad)\nâ˜Ž 9921990176")

        elif further_question != "yes":
            print(Back.MAGENTA + Fore.WHITE + "Please enter 'yes' or 'no'.")
            break

if __name__ == "__main__":
    admission_chatbot()
