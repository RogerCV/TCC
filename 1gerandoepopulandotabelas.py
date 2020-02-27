from random import randrange, randint, choice

with open("test.txt", "a") as myfile:
    Item_Cosif = ['varchar(255)', 'tinytext']
    Base_anterior = ['double(8, 2)', 'float(8, 2)', 'decimal(8, 2)']
    Base_atual = ['double(8, 2)', 'float(8, 2)', 'decimal(8, 2)']
    Aliquota = ['double(3, 2)', 'float(3, 2)', 'decimal(3, 2)']
    Tributavel = ['boolean', 'char']
    Total_recolhido = ['double(8, 2)', 'float(8, 2)', 'decimal(8, 2)']
    count = 1
    for a in Item_Cosif:
        for b in Base_anterior:
            for c in Base_atual:
                for d in Aliquota:
                    for e in Tributavel:
                        for f in Total_recolhido:
                            myfile.write('create table if not exists iss_prefeitura_' + str('{0:03}'.format(count)) + ' ( Id int not null auto_increment, Item_Cosif ' + a + ', Base_anterior ' + b + ', Base_atual ' + c + ', Aliquota ' + d + ', Tributavel ' + e + ', Total_recolhido ' + f + ', primary key (id)); \n')
                            count += 1
    
    TributavelIsBoolean = False
    for table in range(1, 325):
        if ((table - 1) % 3 == 0):
            TributavelIsBoolean = not TributavelIsBoolean
        for registro in range(1000):
            Item_116 = '100' + str('{0:05}'.format(registro))
            Base_anterior = randrange(10000000)/100
            Base_atual = float("%.2f" % (Base_anterior * (1 + randint(1,5)/100)))
            Aliquota = float("%.2f" % randint(2,5))
            Total_recolhido = "%.2f" % ((Base_atual - Base_anterior) * (1 + Aliquota/100))
            if TributavelIsBoolean:
                Tributavel = choice(['TRUE', 'FALSE'])
                myfile.write("insert into iss_prefeitura_" + str('{0:03}'.format(table)) + " values (NULL, \'{}\', {}, {}, {}, {}, {});\n".format(Item_116, Base_anterior, Base_atual, Aliquota, Tributavel, Total_recolhido))
            else:
                Tributavel = choice(['S', 'N'])
                myfile.write("insert into iss_prefeitura_" + str('{0:03}'.format(table)) + " values (NULL, \'{}\', {}, {}, {}, \'{}\', {});\n".format(Item_116, Base_anterior, Base_atual, Aliquota, Tributavel, Total_recolhido))