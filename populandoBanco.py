import controllers

banco = controllers

banco.add_item('Notebook intel', 3, 'Notebook')
banco.add_item('Memória ram 4gb',  10, 'Memória')

print(banco.get_itens())