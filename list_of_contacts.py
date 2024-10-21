import csv
import loading_json_file

def saving_contacts_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Order', 'Gender', 'First Name', 'Last Name', 'University ID'])
        for record in data:
            university_id = record.get('university', {}).get('id', 'N/A')
            contacts = record.get('contacts', [])
            for contact in contacts:
                writer.writerow([contact.get('order', 'N/A'),contact.get('gender', 'N/A'),contact.get('firstname', 'N/A'),contact.get('lastname', 'N/A'),university_id])


saving_contacts_to_csv(loading_json_file.data, 'contacts.csv')