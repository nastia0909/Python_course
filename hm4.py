ticket_number = input()
checking = [int(ticket_number) for ticket_number in range(0, 1000000)]
if sum(checking[3:]) == sum(checking[:3]):
    print('lucky ')
else:
    print('unlucky')
