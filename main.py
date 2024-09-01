from library_management import LibraryManagement
from rich.console import Console
from utils import get_email,show_menu,add_book,view_books,borrow_book,return_book


console = Console()


def main(user_id):
    # Here i'm createing an instance of the LibraryManagement Class
    client = LibraryManagement()

    # Taking user's email to recognize him
    while True:
        email = get_email(console=console,)
        console.print(f"\nYou entered: [bold green]{email}[/bold green]")
        
        user = client.get_user(email)
        if user:
            console.print(f"\n[bold blue]You're Authenticated[/bold blue]")
            user_id = user[0][0]
            break
        else:
            console.print(f"\n[bold red]You're Not Authenticated[/bold red]")
            continue

    while True:
        choice = show_menu(console=console,)
        if choice == 1:
            add_book(console=console,client=client)
        elif choice == 2:
            view_books(console=console,client=client)
        elif choice == 3:
            borrow_book(console=console,client=client,user_id=user_id)
        elif choice == 4:
            return_book(console=console,client=client,user_id=user_id)
        elif choice == 5:
            console.print("\n[bold red]Exiting... Goodbye![/bold red]")
            break  # Exit the while loop



if __name__ == '__main__':
    main(user_id=None)
    
    
    
