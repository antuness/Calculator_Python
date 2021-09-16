#!/usr/bin/env python
# coding: utf-8

# In[25]:


print("Selecione uma operação: ")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")


# In[26]:


operation = input()
if operation == "1":
    num1 = input("Informe o primeiro número: ")
    num2 = input("Informe o segundo número: ")
    print("A soma é: " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Informe o primeiro número: ")
    num2 = input("Informe o segundo número: ")
    print("A subtração é: " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Informe o primeiro número: ")
    num2 = input("Informe o segundo número: ")
    print("A multiplicação é: " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Informe o primeiro número: ")
    num2 = input("Informe o segundo número: ")
    print("A divisão é: " + str(int(num1) / int(num2)))
else:
    print("Número inválido")


# In[ ]:




