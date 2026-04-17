import csv

def get_books(filename):
    """Задание 1: Читает CSV файл"""
    books = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        
        for row in reader:
            if not row or len(row) < 5:
                continue
            if row[0] == 'isbn':
                continue
            
            isbn = row[0]
            title = row[1]
            author = row[2]
            quantity = int(row[3])
            price = float(row[4])
            
            books.append([isbn, title, author, quantity, price])
    
    return books

def filtered_books(books, search_term):
    """Задание 2: Фильтрует книги по названию"""
    filtered = []
    search_term_lower = search_term.lower()
    
    for book in books:
        isbn, title, author, quantity, price = book
        
        if search_term_lower in title.lower():
            # Объединяем название и автора
            combined = f"{title}, {author}"
            filtered.append([isbn, combined, quantity, price])
    
    return filtered

def calculate_total_values(filtered_books_list):
    """Задание 3: Считает общую стоимость"""
    result = []
    
    for book in filtered_books_list:
        isbn = book[0]
        quantity = book[2]
        price = book[3]
        total = quantity * price
        result.append((isbn, total))
    
    return result

if __name__ == "__main__":
    print("Задание 1: Загрузка книг...")
    books = get_books("books.csv")
    print(f"Загружено книг: {len(books)}")
    print(f"Первая книга: {books[0]}\n")
    
    print("Задание 2: Поиск книг с 'python'...")
    filtered = filtered_books(books, "python")
    print(f"Найдено книг: {len(filtered)}")
    for book in filtered:
        print(f"  {book}")
    print()
    
    print("Задание 3: Расчет общей стоимости...")
    totals = calculate_total_values(filtered)
    for isbn, total in totals:
        print(f"  ({isbn}, {total})")