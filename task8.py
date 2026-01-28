import csv

try:
    with open("fight_club_summary.txt", "w") as txt_file:
        plot_data = (
            "The unnamed narrator is an insomniac dissatisfied with his job and lifestyle. "
            "As a form of therapy, he attends support groups... [Plot summary continues] ... "
            "Marla and the narrator hold hands and watch the skyline as the targeted buildings collapse."
        )
        txt_file.write(plot_data)
    print("Success: Text file created and summary written.")

    with open("fight_club_summary.txt", "a") as txt_file:
        txt_file.write("\n\n--- Metadata ---\n")
        txt_file.write("Content: Movie Plot Analysis\n")

    with open("fight_club_summary.txt", "r") as txt_file:
        print("\n--- Reading from Text File ---")
        print(txt_file.read())

    # 4. Create and Write multiple rows to a CSV file
    csv_headers = ["Character", "Role", "Trait"]
    csv_rows = [
        ["Narrator", "Protagonist", "Insomniac"],
        ["Tyler Durden", "Alter Ego", "Soap Salesman"],
        ["Marla Singer", "Support Group Impostor", "Cynical"]
    ]

    with open("character_database.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_headers)
        writer.writerows(csv_rows)
    print("\nSuccess: CSV character database created.")

    print("\n--- Character Database (CSV) ---")
    with open("character_database.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(f"{row[0]:<15} | {row[1]:<25} | {row[2]}")

# 6. Exception Handling for robust code
except FileNotFoundError:
    print("Error: Required file was not found in the directory.")
except PermissionError:
    print("Error: Permission denied. Ensure the file isn't open in another app.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\n" + "="*50)
    print("Status: All file streams closed and resources released.")
    print("="*50)