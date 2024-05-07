class Star_Cinema:
    hall_list = []
    
    def entry_hall(self,name):
        self.name = name
        self.hall_list.append(name)

    
class Hall():

    def __init__(self,rows,cols,hall_no) -> None:
        self.__hall_no = hall_no
        self.rows = rows
        self.cols = cols
        self.seats = {} 
        self.show_list = []
        
        
       
    def entry_show(self,id,movie_name,time):
        self.__id = id
        self.movie_name = movie_name
        self.time = time
        info = (id,movie_name,time)
        self.show_list.append(info)
        seat = [['free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seat


    def book_seats(self,id,rows,cols):
        self.__id = id
        self.rows = rows
        self.cols = cols
        if id in self.seats:
            
            if self.seats[id][self.rows-1][self.cols-1] == 'free':
                self.seats[id][self.rows-1][self.cols-1] = 'Booked'
                print(f'Seat ({self.rows},{self.cols}) booked successfully.')

            else:
                print("\nSeat is already booked !\n")

        else:
            print('\nInvalid Show ID\n')

    
    
    def view_show_list(self):
        if not self.show_list:
            print("No shows available")
        else:
            print("\n\t!!!Currently Available Shows!!!")
            for show in self.show_list:
                print(f"Show ID:{show[0]}  Movie:{show[1]}  Time:{show[2]}")


    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print("Available Seats:")
            for row in self.seats[show_id]:
                print(row)
        else :
            print("\nInvalid Show ID\n")


star_cinema = Star_Cinema()
Hall1 = Hall(10,10,1)
star_cinema.entry_hall(Hall1)


Hall1.entry_show(112,'Dune 2','10:00 am')
Hall1.entry_show(334,'Shawshank Redemption','7:00 pm')


while True:
    print("\n\t!!Welcome to Star Cinema!!")
    print("1.View all show today")
    print("2.View available seats")
    print("3.Book ticket")
    print("4.Exit")

    ch = int(input("Enter option: "))

    if ch == 1:
        Hall1.view_show_list()

    elif ch == 2:
        show_id = int(input("Enter Show id: "))
        Hall1.view_available_seats(show_id)

    elif ch == 3:
        show_id = int(input("Enter Show id: "))
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        if row<1 or row>10 and col<1 or col>10:
            print("\nInvalid Seat Number\n")
        else: 
            Hall1.book_seats(show_id,row,col)

    elif ch == 4:
        print("***Thanks for being with Star Cinema***")
        break

    else:
        print("\nInvalid choice\n")
