class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}    
        self.__show_list = []    
        self.__rows = rows
        self.__cols = cols    
        self.__hall_no = hall_no

        self.entry_hall()
    

    def entry_show(self, id, movie_name, time):
        self.__show_list.append( (id, movie_name, time) )
        
        self.__seats[id] = []
        for i in range(self.__rows):
            seat_list = []
            for j in range(self.__cols):
                seat_list.append(0)
            self.__seats[id].append(seat_list)


    def book_seats(self, id, seats_to_book):
        for row, col in seats_to_book:
            if self.__seats[id][row][col] == 0:
                self.__seats[id][row][col] = 1
                print(f'Seat {row, col} booked for show {id}')
            elif row < 0 or col < 0 or row >= self.__row or col >= self.__col:
                print(f'Seat is unavailable')
            elif self.__seats[id][row][col] == 1:
                print(f'Seat {row, col} is already booked !')


    def view_show_list(self):
        print('--------------------')
        for show in self.__show_list:
            print(f'SHOW ID: {show[0]}   MOVIE NAME: {show[1]}  TIME: {show[2]}')
        print('--------------------')
    

    def view_available_seats(self, id):
        for i in range(self.__rows):
            print(self.__seats[id][i])



cinema = Hall(10, 10, 1)

while True:
    op = int(input('''1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. Exit\nENTER OPTION: '''))
    print('\n')

    if op == 1:
        cinema.entry_show(111, 'Avengers', '2024:02:16')
        cinema.entry_show(222, 'Superman', '2024:02:16')
        cinema.view_show_list()
            
    elif op == 2:
        id = int(input('ENTER SHOW ID: '))

        try:
            cinema.view_available_seats(id)
        except:
            print(f'No shows available with id: {id}')

    elif op == 3:
        id = int(input('ENTER SHOW ID: '))

        try:
            cinema._Hall__seats[id]
        except:
            print(f'No shows available with id: {id}')
            continue

        
        tickets = int(input('ENTER NUMBER OF TICKETS: '))
        
        seats_to_book = []      
        while tickets > 0:
            row = int(input('ENTER SEAT ROW: '))
            col = int(input('ENTER SEAT COL: '))

            try:
                seats_to_book.append((row, col))
                
                cinema.book_seats(id, seats_to_book)
                   
            except:
                print('\nInvalid Seat')
                print('Try again!\n')
                continue

            tickets -= 1 


    elif op == 4:
        break
    
    print('\n')
    





