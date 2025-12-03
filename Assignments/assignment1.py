print("SKILLMENTOR AI – STUDENT PROFILE FORM")
print("----------------------------------------")

student_id = int(input("Enter Student ID (integer number): "))
student_name = input("Enter Full Name: ")
student_age = int(input("Enter Age (years): "))
cgpa = float(input("Enter Current CGPA (0-10): "))

skills_input = input("Enter Current Skills (separate skills with commas): ")
current_skills = skills_input.split(",")

target_roles_input = input("Enter Target Roles (separate roles with commas): ")
target_roles = target_roles_input.split(",")

experience_years = float(input("Enter Experience in Years (0 if none): "))

degree = input("Enter Education Degree (e.g., B.Tech CSE): ")
college_info = (degree, "Bachelor Level")

certificates_input = input("Enter Certifications Earned (separate certifications with comma): ")
certifications = set(certificates_input.split(","))

student_email = input("Enter Email Address: ")
student_phone = input("Enter Phone Number (optional): ")
linkedin_url = input("Enter LinkedIn Profile URL: ")

profile_data = {
    "name": student_name,
    "email": student_email,
    "phone": student_phone,
    "linkedin": linkedin_url
}

print("\nSKILLMENTOR AI – PROFILE SUMMARY")
print("----------------------------------------")
print("Student ID:", student_id)
print("Age: %d years | CGPA: %.2f" % (student_age, cgpa))
print("Education: Degree - {}, Level - {}".format(college_info[0], college_info[1]))
print(f"""
Name: {student_name}
Skills: {current_skills}
Target Roles: {target_roles}
Experience: {experience_years} years
Certifications Earned: {certifications}
Contact Details: {profile_data}
LinkedIn: {linkedin_url}
""")

print("----------------------------------------")