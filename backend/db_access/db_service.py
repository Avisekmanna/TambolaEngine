from db_access.models import db, TambolaTicket
import utils.ticket_generator as ticket 
from loguru import logger

@logger.catch
def generate_n_tambola_sets(n):
    try:
        tickets = {}
        for i in range(1, n+1):
            global_used_numbers = []
            for j in range(1, 6+1):
                new_ticket = ticket.get_ticket(global_used_numbers)
                while TambolaTicket.query.filter_by(ticket_data=new_ticket).first():
                    new_ticket = ticket.get_ticket(global_used_numbers)
                tickets[str(i)+str(j)] = new_ticket
                tambola_ticket = TambolaTicket(ticket_data=new_ticket)
                db.session.add(tambola_ticket)
                db.session.commit()

                for row in new_ticket:
                    for num in row:
                        if num != 0:
                            global_used_numbers.append(num)
        return tickets
    except Exception as e:
        logger.error(f"Error in generate tambola ticket: {e}")
        return None

@logger.catch
def fetch_tambola_tickets():
    try:
        tickets = TambolaTicket.query.all()
        tickets.reverse()
        all_tickets = {}
        result = {"tickets": {}}
        for i in range(1, (len(tickets)//6)+1):
            for j in range(1, 6+1):
                ticket_index = (i-1) * 6 + (j-1)
                if ticket_index < len(tickets):
                    all_tickets[str(i)+str(j)] = tickets[ticket_index].ticket_data
        return all_tickets
    except Exception as e:
        logger.error(f"Error in get all tickets: {e}")
        return None
