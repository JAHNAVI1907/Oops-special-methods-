# Oops-special-methods-
__getitem__(self,key)-- fetch index value,__setitem__(self,key,value)-- set a value which is created

# Python OOP Concepts: Variables, Special Methods, and Constructors

This repository contains explanations and examples of key Python **Object-Oriented Programming (OOP) concepts**, including **variables, special methods, and constructors**.

---

## Table of Contents
- [1. Variables](#1-variables)
  - [1.1 Instance Variables](#11-instance-variables)
  - [1.2 Class Variables](#12-class-variables)
- [2. Constructors](#2-constructors)
- [3. Special Methods](#3-special-methods)
  - [3.1 `__str__`](#31-str)
  - [3.2 `__repr__`](#32-repr)
  - [3.3 `__len__`](#33-len)
  - [3.4 `__add__`](#34-add)
  - [3.5 Other Common Special Methods](#35-other-common-special-methods)
- [4. Example Combining All Concepts](#4-example-combining-all-concepts)
- [5. Summary Table](#5-summary-table)

---

## 1. Variables
Variables in Python classes are used to store data and can be **instance-level** or **class-level**.

### 1.1 Instance Variables
- Belong to a specific object.
- Defined inside a constructor (`__init__`) using `self`.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

print(s1.name)  # Alice
print(s2.age)   # 22
