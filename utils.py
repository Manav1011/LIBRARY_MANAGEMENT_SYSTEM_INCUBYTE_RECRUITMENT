from rich.prompt import Prompt
from rich.text import Text
from rich.table import Table
from rich.panel import Panel

def show_menu(console) -> int:
    console.print("\n[bold cyan]Please select an option:[/bold cyan]")
    console.print("1 - Add a book")
    console.print("2 - View Books")
    console.print("3 - Borrow a book")
    console.print("4 - Return a book")
    console.print("5 - Exit")
    choice = Prompt.ask("\n[bold yellow]Enter your choice (1-5)[/bold yellow]", choices=["1", "2", "3", "4", "5"], default="1")
    return int(choice)

def return_book(console) -> None:
    console.print("\n[bold green]You selected: Return a book[/bold green]")
    # Return book logic here

def get_email(console) -> str:
    console.print(Text("Please enter your email address:", style="bold cyan"))
    email = input("Email: ")
    return email

def add_book(console,client) -> None:
    console.print(Panel("[bold green]Add a New Book[/bold green]", expand=False))
    while True:
        try:
            isbn = int(Prompt.ask("[bold yellow]Enter the ISBN (integer)[/bold yellow]"))
            break
        except ValueError:
            console.print("[bold red]Invalid input! ISBN must be an integer.[/bold red]")    
    title = Prompt.ask("[bold yellow]Enter the Title[/bold yellow]")    
    author = Prompt.ask("[bold yellow]Enter the Author[/bold yellow]")    
    while True:
        try:
            publication_year = int(Prompt.ask("[bold yellow]Enter the Publication Year (integer)[/bold yellow]"))
            break
        except Exception:
            console.print("[bold red]Invalid input! Publication year must be an integer.[/bold red]")        
    try:
        result = client.add_book(isbn,title,author,publication_year)
        if result:
            console.print(f"\n[bold green]Your Book Is Added Successfully!! [/bold green]")
    except Exception as e:
        print(e)
    finally:
        return
    
def view_books(console,client) -> None:
    books = client.get_books()
    table = Table(title="Book List")    
    table.add_column("ISBN", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Author", style="green")
    table.add_column("Publication Year", justify="right", style="yellow")    

    for book in books:
        isbn, title, author, publication_year = book
        table.add_row(str(isbn), title, author, str(publication_year))
    
    console.print(table)   

def borrow_book(console,client,user_id) -> None:
    console.print(Panel("[bold green]Borrow a Book[/bold green]", expand=False))
    while True:
        try:
            isbn = int(Prompt.ask("[bold yellow]Enter the ISBN (integer)[/bold yellow]"))
            break
        except ValueError:
            console.print("[bold red]Invalid input! ISBN must be an integer.[/bold red]")    
    try:
        result = client.borrow_book(isbn,user_id)
        if result:
            console.print(f"\n[bold green]Your Book Is Borrowd Successfully!! [/bold green]")
    except Exception as e:
        console.print(f"[bold red] {str(e)} [/bold red]")    
    finally:
        return

def return_book(console,client,user_id) -> None:
    console.print(Panel("[bold green]Return a Book[/bold green]", expand=False))
    while True:
        try:
            isbn = int(Prompt.ask("[bold yellow]Enter the ISBN (integer)[/bold yellow]"))
            break
        except ValueError:
            console.print("[bold red]Invalid input! ISBN must be an integer.[/bold red]")    
    try:
        result = client.return_book(isbn,user_id)
        if result:
            console.print(f"\n[bold green]Your Book Is Returned Successfully!! [/bold green]")
    except Exception as e:
        console.print(f"[bold red] {str(e)} [/bold red]")    
    finally:
        return 
