
from PatternExtractor import extract_emails
from PatternExtractor import extract_phone
from PatternExtractor import read_text_file
from PatternExtractor import validate_data




def main():
	#Read text from file

	text=read_text_file('file.txt')

	#Extract Emails and Phones from the text

	emails=extract_emails(text)
	phone_numbers=extract_phone(text)

	print(emails)



	#Validate extracted data
	valid_emails=validate_data (emails)
	valid_phone_numbers=validate_data(phone_numbers)

	#print the extracted and validated data

	print("Valid Email Addresses:", valid_emails)
	#for email in valid_emails:
		#return email

	
	print("\nValid phone numbers:",valid_phone_numbers)
	#for phone_number in valid_phone_numbers:
		#return phone_number


if __name__=='__main__':
	main()