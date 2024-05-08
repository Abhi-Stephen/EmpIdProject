from PIL import Image, ImageDraw, ImageFont
import csv
import os

def generate_employee_id(template_path, csv_path, photo_directory, output_path):
    # Load the ID template image
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # Load default font for text
    font = ImageFont.load_default(size=30)

    # Read employee data from CSV file
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Get employee information
            name = row['Name']
            position = row['Position']
            photo_filename = row['Photo_Filename']

            # Load employee photo
            photo_path = os.path.join(photo_directory, photo_filename)
            photo = Image.open(photo_path)

            # Resize photo to fit template
            photo = photo.resize((175, 175))  # Adjust dimensions as needed

            # Paste photo onto template
            template.paste(photo, (265, 10))  # Adjust position as needed

            # Draw text onto template
            draw.text((190, 225), name, fill=(0, 0, 0), font=font)


            # Save generated ID as PDF
            output_filename = f"{name.replace(' ', '_')}_ID.pdf"
            output_path = os.path.join(output_directory, output_filename)
            template.save(output_path, "PDF", resolution=100.0)
            
            # Reset template for next iteration
            template = Image.open(template_path)
            draw = ImageDraw.Draw(template)

if __name__ == "__main__":
    # Paths and directories
    template_path = r"C:\Users\basut\OneDrive\Desktop\emp_id_project\image.jpg"
    csv_path = r"C:\Users\basut\OneDrive\Desktop\emp_id_project\emp_details.csv"
    photo_directory = r"C:\Users\basut\OneDrive\Desktop\emp_id_project"
    output_directory = r"C:\Users\basut\OneDrive\Desktop\emp_id_project"

    # Generate employee IDs
    generate_employee_id(template_path, csv_path, photo_directory, output_directory)
