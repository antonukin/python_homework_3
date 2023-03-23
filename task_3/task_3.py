'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; K – 5 очков;
J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
'''

word = input('Введите слово: ').upper()
counter = 0

if 'A' <= word[0] <= 'Z':
    for i in range(len(word)):
        match word[i]:
            case ('A' | 'E' | 'I' | 'O' | 'U' | 'L' | 'N' | 'S' | 'T' | 'R'):
                counter += 1
            case ('D' | 'G'):
                counter += 2
            case ('B' | 'C' | 'M' | 'P'):
                counter += 3
            case ('F' | 'H' | 'V' | 'W' | 'Y'):
                counter += 4
            case 'K':
                counter += 5
            case ('J' | 'X'):
                counter += 8
            case ('Q' | 'Z'):
                counter += 10
            case default:
                break
elif 'А' <= word[0] <= 'Я':
    for i in range(len(word)):
        match word[i]:
            case ('А' | 'В' | 'Е' | 'И' | 'Н' | 'О' | 'Р' | 'С' | 'Т'):
                counter += 1
            case ('Д' | 'К' | 'Л' | 'М' | 'П' | 'У'):
                counter += 2
            case ('Б' | 'Г' | 'Ё' | 'Ь' | 'Я'):
                counter += 3
            case ('Й' | 'Ы'):
                counter += 4
            case ('Ж' | 'З'| 'Х' | 'Ц' | 'Ч'):
                counter += 5
            case ('Ш' | 'Э' | 'Ю'):
                counter += 8
            case ('Ф' | 'Щ' | 'Ъ'):
                counter += 10
            case default:
                break
else:
    print('Введено не поддерживаемое слово или не слово')
print(counter)

eng_dict = { 1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
rus_dict = { 1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
if 'A' <= word[0] <= 'Z':
    for i in word:
        for key, item in eng_dict.items():
            if i in item:
                counter += key
    print(counter)
elif 'А' <= word[0] <= 'Я':
    for i in word:
        for key, item in rus_dict.items():
            if i in item:
                counter += key
    print(counter)
else:
    print('Введено не поддерживаемое слово или не слово')

