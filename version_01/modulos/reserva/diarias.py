from datetime import datetime


def calculaDiarias(checkin, checkout):

    formato = "%d/%m/%Y"

    checkin = datetime.strptime(checkin, formato)
    checkout = datetime.strptime(checkout, formato)

    diarias = (checkout - checkin).days
    return diarias

def verificaDiarias(checkin, checkout):

    formato = "%d/%m/%Y"

    checkin = datetime.strptime(checkin, formato)
    checkout = datetime.strptime(checkout, formato)

    if checkin < checkout:
        return True
    else:
        return False