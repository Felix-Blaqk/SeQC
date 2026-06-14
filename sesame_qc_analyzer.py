# Sesame QC Analyzer
# Copyright (c) 2026 Felix [Oba]
# All rights reserved.
import collections
from datetime import datetime
limits = {
    "NWSS": {
        "ffa": 2, #Free Fatty Acids
        "purity": 99,
        "moisture": 6,
        "s_aureus": 10, #Staphylococcus aureus
        "salmonella": 'absent',
        "e_coli": 10, #Escherichia coli
        "tpc": 1000, #Total Plate Count
        "yeast_and_moulds": 100, #Yeast and Moulds
        "etb": 10,  #Enterobacteriaceae
        "bacillus": 100,
    },
    "PSS": {
        "ffa": 2, #Free Fatty Acids
        "purity": 99.95,
        "moisture": 6,
        "s_aureus": 10, #Staphylococcus aureus
        "salmonella": 'absent',
        "e_coli": 10, #Escherichia coli
        "tpc": 1000, #Total Plate Count
        "yeast_and_moulds": 100, #Yeast and Moulds
        "etb": 10,  #Enterobacteriaceae 
        "bacillus": 100,
    },
    "HSS": {
        "ffa": 1, #Free Fatty Acids
        "purity": 99.98,
        "moisture": 5.5,
        "s_aureus": 10, #Staphylococcus aureus
        "salmonella": 'absent',
        "e_coli": 10, #Escherichia coli
        "tpc": 500, #Total Plate Count
        "yeast_and_moulds": 100, #Yeast and Moulds
        "etb": 10,  #Enterobacteriaceae
        "bacillus": 100,
    },
}

batches =[]

def add_batch():
    #adds a new batch of sesame seeds to the system
    batch_id = input("Enter Batch ID: ").upper()
    while True:
        grade = input("Enter Grade (NWSS, PSS, HSS): ")
        if grade in ['NWSS', 'PSS', 'HSS']:
            break
        print("Invalid grade. Please enter NWSS, PSS, or HSS.")
    while True:
        try:
            date = datetime.strptime(input("Enter Date (DD-MM-YYYY): "), "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter a valid date.")
    while True:
        try:
            ffa = float(input("Enter Free Fatty Acids (FFA) percentage: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            purity = float(input("Enter Purity percentage: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            moisture = float(input("Enter Moisture percentage: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            s_aureus = int(input("Enter Staphylococcus aureus count: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        salmonella = input("Enter Salmonella status (present/absent): ")
        if salmonella in ['present', 'absent']:
            break
        print("Invalid status. Please enter 'present' or 'absent'.")
    while True:
        try:
            e_coli = int(input("Enter Escherichia coli count: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            tpc = int(input("Enter Total Plate Count: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            yeast_and_moulds = int(input("Enter Yeast and Moulds count: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            etb = int(input("Enter Enterobacteriaceae count: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            bacillus = int(input("Enter Bacillus count: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    batch = {
        "id": batch_id,
        "grade": grade,
        "date": date,
        "ffa": ffa,
        "purity": purity,
        "moisture": moisture,
        "s_aureus": s_aureus,
        "salmonella": salmonella,
        "e_coli": e_coli,
        "tpc": tpc,
        "yeast_and_moulds": yeast_and_moulds,
        "etb": etb,
        "bacillus": bacillus
    }
    batches.append(batch)

def analyze_batches(batch):
    #analyzes the quality of a batch of sesame seeds
    grade_limits = limits[batch['grade']]
    results = {}
    for key in grade_limits:
        if key in batch:
            if key == 'purity':
                results[key] = 'PASS' if batch[key] >= grade_limits[key] else 'FAIL'
            elif isinstance(grade_limits[key], (int, float)):
                results[key] = 'PASS' if batch[key] <= grade_limits[key] else 'FAIL'
            else:
                results[key] = 'PASS' if batch[key] == grade_limits[key] else 'FAIL'
    return results 

def print_batch_report(batch, results):
    heading = f"{'='*40}\nBATCH REPORT\n{'='*40}\n"
    print_result = f"{'Batch ID':<10}: {batch['id']}\n{'Grade':<10}: {batch['grade']}\n{'Date':<10}: {batch['date'].strftime('%d %B %Y')}\n{'-'*40}\n {'PARAMETER':<20} RESULT\n{'-'*40}\n"
    for key, result in results.items():
        print_result += f" {key.upper():<20} {result}\n"
    overall_result = 'FAIL' if 'FAIL' in results.values() else 'PASS'
    print_result += f"{'-'*40}\nOVERALL: {overall_result}\n{'='*40}\n"
    print(heading + print_result)

def filtered_batches():
    #filters batches based on a date range
    while True:
        try:
            start_date = datetime.strptime(input("From (DD-MM-YYYY): "), "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY format.")
    while True:
        try:
            end_date = datetime.strptime(input("To (DD-MM-YYYY): "), "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY format.")
    filtered = [batch for batch in batches if start_date <= batch['date'] <= end_date]
    if not filtered:
        print("No batches found in the specified date range.")
    return filtered,start_date,end_date

def print_summary_report(filtered,start_date,end_date):
    #prints a summary report of batches in a date range
    if not filtered:
        print("No batches to summarize.")
        return
    grade_counts = collections.Counter(batch['grade'] for batch in filtered)
    total_batches = len(filtered)
    total_pass = 0
    total_fail = 0
    failed_parameters = {}
    for batch in filtered:
        results = analyze_batches(batch)
        for key in {k for k, v in results.items() if v == 'FAIL'}:
                failed_parameters.setdefault(key, []).append(batch['id'])
        if 'FAIL' in results.values():
            total_fail += 1
        else:
            total_pass += 1
    pass_percentage = (total_pass / total_batches) * 100
    if failed_parameters:
        most_common = max(failed_parameters, key=lambda k: len(failed_parameters[k]))
    else:
        most_common = 'None'
    grade_breakdown = ""
    for grade, count in grade_counts.items():
        grade_breakdown += f"{grade:<20}: {count} batches\n"
    failure_breakdown = ""
    for param, batch_ids in failed_parameters.items():
        failure_breakdown += f"{param.upper():<20}: {len(batch_ids)} batches (IDs: {', '.join(batch_ids)})\n"
    print (f"{'='*40}\nSUMMARY REPORT\n"
           f"Reporting Period: {start_date.strftime('%d %B %Y')} to {end_date.strftime('%d %B %Y')}\n{'='*40}\n"
           f"{'Total Batches':<20}: {total_batches}\n"
           f"{'Total Pass':<20}: {total_pass}\n"
           f"{'Total Fail':<20}: {total_fail}\n"
           f"{'Pass Rate':<20}: {pass_percentage:.2f}%\n"
           f"{'-'*40}\nGRADE BREAKDOWN\n{'-'*40}\n{grade_breakdown}\n"
           f"{'-'*40}\nFAILURE BREAKDOWN\n{'-'*40}\n{failure_breakdown}\n"
           f"{'Most Common Failed Parameter':<20}: {most_common}\n"
           f"{'='*40}\n")
    
def search_batch():
    batch_id = input("Enter Batch ID to search: ").upper()
    for batch in batches:
        if batch['id'].upper() == batch_id:
            results = analyze_batches(batch)
            print_batch_report(batch, results)
            return
    print(f"Batch {batch_id} not found.")

def main():
    while True:
        print(f"{'='*40}\nSeQC\n{'='*40}\n"
              f"1. Add New Batch\n"
              f"2. Reports\n"
              f"3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_batch()
            analyze_batches(batches[-1])
            print(f"Batch {batches[-1]['id']} added and analyzed successfully.")
        elif choice == '2':
            print(f"{'='*40}\nREPORTS\n{'='*40}\n"
                  f"1. Batch Report\n"
                  f"2. Summary Report\n"
                  f"3. Back to Main Menu")
            report_choice = input("Enter your choice: ")
            if report_choice == '1':
                search_batch()
            elif report_choice == '2':
                filtered, start_date, end_date = filtered_batches()
                print_summary_report(filtered, start_date, end_date)
            elif report_choice == '3':
                continue
            else:
                print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting SeQC. Goodbye!")
            break
if __name__ == '__main__':
    main()