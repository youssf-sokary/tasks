
records_input = input("Enter the books borrowed in the format 'Book Title - Days Borrowed', separated by commas: ")


records = records_input.split(',')

borrowed_books = {}

unique_titles = set()

for record in records:
    title, days = map(str.strip, record.split('-'))  
    days = int(days)  
    if title in borrowed_books:
        borrowed_books[title] += days
    else:
        borrowed_books[title] = days
    
    unique_titles.add(title)

most_borrowed = max(borrowed_books.items(), key=lambda item: item[1])
least_borrowed = min(borrowed_books.items(), key=lambda item: item[1])

total_days = sum(borrowed_books.values())
average_days = total_days / len(borrowed_books)


sorted_books = sorted(borrowed_books.items(), key=lambda item: item[1], reverse=True)

print("\nAnalysis Results:")
print(f"Most borrowed book: {most_borrowed[0]} ({most_borrowed[1]} days)")
print(f"Least borrowed book: {least_borrowed[0]} ({least_borrowed[1]} days)")
print(f"Average borrowing days: {average_days:.2f}")
print(f"Unique book titles: {unique_titles}")
print("Books sorted by borrowing days (descending):")
for title, days in sorted_books:
    print(f"{title}: {days} days")
