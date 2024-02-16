class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}    
        self.__show_list = []    
        self.__rows = rows
        self.__cols = cols    
        self.__hall_no = hall_no
    

    def entry_show(self, id, movie_name, time):
        self.__show_list.append( (id, movie_name, time) )
        
        self.__seats[id] = []
        for i in range(self.__rows):
            seat_list = []
            for j in range(self.__cols):
                seat_list.append('free')
            self.__seats[id].append(seat_list)


    def book_seats(self, id, seats_to_book):
        for row, col in seats_to_book:
            if self.__seats[id][row][col] == 'free':
                self.__seats[id][row][col] = 'booked'
                print(f'Seat {row, col} booked for show {id}')
            else:
                print(f'Seat {row, col} is already booked !')


    def view_show_list(self):
        print('--------------------')
        for show in self.__show_list:
            print(f'SHOW ID: {show[0]}   MOVIE NAME: {show[1]}  TIME: {show[2]}')
        print('--------------------')
    

    def view_available_seats(self, id):
        available_seats = []

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 'free':
                    available_seats.append((i, j))

        print('Available Seats:')
        for seats in available_seats:
            print(f'Seat {seats}')


class Star_Cinema:
    hall_list = []

    def __init__(self, rows, cols, hall_no):
        self.hall = Hall(rows, cols, hall_no)
        self.entry_hall()

    def entry_hall(self):
        self.hall_list.append(self.hall)


cinema = Star_Cinema(10, 10, 1)

while True:
    op = int(input('''1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. Exit\nENTER OPTION: '''))
    print('\n')

    if op == 1:
        for hall in cinema.hall_list:
            hall.entry_show(111, 'Avengers', '2024:02:16')
            hall.entry_show(222, 'Superman', '2024:02:16')
            hall.view_show_list()
    elif op == 2:
        id = int(input('ENTER SHOW ID: '))

        try:
            for hall in cinema.hall_list:
                hall.view_available_seats(id)
        except:
            print(f'No shows available with id: {id}')

    elif op == 3:
        id = int(input('ENTER SHOW ID: '))
        tickets = int(input('ENTER NUMBER OF TICKETS: '))
        
        seats_to_book = []      
        while tickets > 0:
            row = int(input('ENTER SEAT ROW: '))
            col = int(input('ENTER SEAT COL: '))

            try:
                seats_to_book.append((row, col))
                
                for hall in cinema.hall_list:
                    hall.book_seats(id, seats_to_book)
            except:
                print('\nInvalid seat')
                print('Try again!\n')
                continue

            tickets -= 1 

    elif op == 4:
        break
    
    print('\n')
    





