# n = 0;
# while n<5:
#     print('a');
#     n = n + 1;

# foods = ['a','b','c'];
# for food in foods:
#     print(food);

# numbers = [1,2,3,4,5,6]
# numberss = []
# for number in numbers:
#     # print(number *2);
#     numberss.append(number*2);

# print(numberss);
# print('-----------------------');
# print(num*nums, end=' ,');

a = [];
b = [];
num = 1;
for num in range(1,10):
    for nums in range(1,10):
        temp = num*nums
        if(temp%2 ==1):
            a.append(temp);
        else:
            b.append(temp);
print(a);