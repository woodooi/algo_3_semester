# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Антонюк Павло Дмитрович (Група ІР-23)

### Лабораторна робота №1 (Варіант 1 Рівень 3)

Потрібно написати програму для обходу двовимірного масиву розміром NxM у форматі "зігзагу". Зігзаговий обхід означає, що спочатку ми рухаємось по діагоналях масиву, пчинаючи з лівої верхньої точки.  Другим елементом буде виведено елемент, який знаходиться справа, потім  знизу і ліворуч, далі ще крок вниз і рухаємось по діагоналі знову вправо. Для масиву розміром 3x3 обхід у форматі зігзагу виглядає так (де номер у клітинці відповідає порядку її відвідин):

1 2 6
3 5 7
4 8 9

Для масиву 3 х 5 це матиме вигляд:

1  2  6   7  12
3  5  8  11  13
4  9  10 14 15

Реалізуйте алгоритм, який отримає на вхід масив розміром m та n та поверне одномірний масив з значеннями елементів вхідного масиву при обході його у порядку, зазначеному вище у задачі

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` . Ваш тести мають перевірити роботу алгоритму при значеннях m == n == 5, m =2, n =4, n = 1, m = 6, n == m == 1

***
### Лабораторна робота №2 (Варіант 1 Рівень 3)

Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте, як
виявилося, вони мають цiкаву харчову поведiнку.
Для того, щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму
на день. Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть.
У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день за
кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними для кожного
хом’ячка.
Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати якомога бiльше, проте у вас
є всього S пакетiв їжi на день. Визначте максимальну кiлькiсть хом’ячкiв, яку ви
можете прогодувати.

Реалізуйте функцію, яка поверне число - максимальне число хо
Вхідні параметри функції:
S — ваш денний запас їжi. 0 ≤ S ≤ 109
C — загальна кiлькiсть хом’ячкiв, яка є в продажу, 1 ≤ C ≤ 105
Матриця `hamsters`, яка містить С рядків, перший стовчик якої містить денну норму корму, другий - рiвень жадiбностi кожного хом’ячка. Деннs нормb є цілими додатніми числами і гарантовано меншими за 109. Іноді у вас можуть бути не жадібні хом’ячки, але також можуть траплятись і надзвичайно жадібні, рівень жадібності може бути як нульовим, так і великим цілим числом

Приклад 1

S = 7
C = 3
hamsters = `[ [1 2], [2 2], [3 1]]``

Результат:
2

Пояснення: Можна взяти першого хом’ячка та будь-якого з iнших двох.

Приклад 2

S = 19
C = 4
hamsters = `[ [5 0], [2 2], [1 4], [5 1]]

Результат:
3
Пояснення: Третiй хом’ячок надто жадiбний. Можна взяти всiх iнших трьох, тодi
за день вони з’їдять (5 + 0 · 2) + (2 + 2 · 2) + (5 + 1 · 2) = 18 пакетiв

Приклад 3
hamstr .in
S = 2
C = 2
hamsters = `[[1 50000], [1 60000]]

Результат:
1
Пояснення: Обидва хом’ячки надто жадiбнi, щоб їсти разом.

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище

***
### Лабораторна робота №3 (Варіант 1 Рівень 3)

Для заданого бінарного дерева та конкретної вершини в цьому дереві реалізуйте функцію пошуку наступного елемента під час серединного проходу (in-order traversal). Наступник - це вузол, який має значення більше за заданий вузол і знаходиться найближче до нього при серединному обході.

Нехай у вас задане бінарне дерево такого вигляду:
```
    10
   /  \
  5    15
 / \     \
3   7    20
         /
        12

```
Для вершини зі значенням 7, наступник - це вузол зі значенням 10.

Функція отримує на вхід корінь бінарного дерева та вершину, для якої потрібно знайти наступника.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
```
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
```

Ваша функція має мати такий вигляд:

```
def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
```

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу `BinaryTree` наступним чином:

```
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
```

***
### Лабораторна робота №5 (Варіант 1 Рівень 3)

Важливим фактором для багатокористувацької онлайн-гри є низька мережева затримка
вiд користувача до сервера. При цьому, пристрої в Iнтернетi спiлкуються один з
одним, використовуючи мережевi маршрути, якi проходять через низку промiжних
вузлiв-маршрутизаторiв. Кожна ланка цього маршруту має власну ненульову затримку.

• Кожен вузол мережi може виконувати одну з трьох ролей: Client, Router або
Server.
• Server може бути лише один на всю мережу.
• Усi комунiкацiї двостороннi: якщо вузол A може спiлкуватися з вузлом B,
вузол B може спiлкуватися з вузлом A з такою ж затримкою.
• Якщо iснує кiлька шляхiв вiд клiєнта до сервера, клiєнт гарантовано пiде
шляхом з найменшою сумарною затримкою (навiть якщо цей шлях пролягає
через iншого клiєнта).
• Усi затримки — сталi додатнi числа.
Для прикладу вище, затримки до клiєнтiв становлять:
• Client 1: 10 + 80 + 50 = 140 ms
• Client 2: 100 + 50 = 150 ms
• Client 3: 20 ms
Максимальною затримкою в такому випадку є 150 ms. Однак, якщо ми помiняємо
ролями вузли “Router 2” i “Server”, затримки скоротяться до 90 ms, 100 ms i 70 ms
вiдповiдно, тодi максимальна затримка буде становити 100 ms.

Ви розробляєте онлайн-гру для користувачiв зi всiєї країни, i бажаєте розмiстити
центральний iгровий сервер таким чином, щоб максимальна затримка мiж сервером
i кожним клiєнтом була мiнiмальною. В якостi сервера можна вибрати будь-який
вузол мережi, який не є клiєнтом.
Маючи iнформацiю про топологiю мережi (якi вузли з’єднанi з якими, i яка затримка
кожного з’єднання), знайдiть таке розташування сервера, яке мiнiмiзує найбiльше
значення затримки до клiєнта. Виведiть це значення затримки.
Вхiднi данi
Вхiдний файл gamsrv .in складається з M + 2 рядкiв.
• Перший рядок мiстить N i M — кiлькiсть вузлiв та з’єднань вiдповiдно.
3 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
• Другий рядок мiстить перелiк цiлих чисел, роздiлених пробiлом — номери
вузлiв, якi є клiєнтами. Усi вузли в мережi нумеруються вiд 1 до N.
• Наступнi M рядкiв мiстять трiйки натуральних чисел startnode, endnode, latency
— номер початкового вузла, кiнцевого вузла та затримка для кожного з’єднання.
1 ≤ latency ≤ 109

Вихiднi данi
Вихiдний файл gamsrv .out повинен мiстити одне число — мiнiмальне значення найбiльшої
затримки до клiєнта (яке ми отримаємо при оптимальному розташуваннi сервера).

### Лабораторна робота №6  (Варіант 1 Рівень 3)

Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle" в стрічці "haystack" та повернути цей індекс, використовуючи  метод скінченних автоматів для пошуку підстрічки у стрічці