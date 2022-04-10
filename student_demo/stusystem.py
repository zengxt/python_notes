#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 22:37
# @Author  : zengxt
# @File    : stusystem.py

import os

# 保存学生信息的文件名
filename = 'student.dat'

def main():
    while True:
        menum()
        try:
            num = int(input('请选择：'))
            if num in [0, 1, 2, 3, 4, 5, 6, 7]:
                if num == 0:
                    answer = input('您确定要退出系统吗？ y/n：')
                    if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'YES':
                        print('谢谢您的使用！！！')
                        break
                elif num == 1:
                    insert()
                elif num == 2:
                    search()
                elif num == 3:
                    delete()
                elif num == 4:
                    modify()
                elif num == 5:
                    sort()
                elif num == 6:
                    total()
                elif num == 7:
                    show()
        except ValueError:
            print('请选择有效的菜单！')


def menum():
    print('学生信息管理系统')
    print('---功能菜单---')
    print('1，录入学生信息')
    print('2，查找学生信息')
    print('3，删除学生信息')
    print('4，修改学生信息')
    print('5，排序')
    print('6，统计学生总共人数')
    print('7，显示所有学生信息')
    print('0，退出')


def insert():
    student_list = []
    while True:
        id = input('请输入学生ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入的信息不是整数类型，请重新输入！')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加 y/n？：')
        if answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            break

    save(student_list)
    print('学生信息录入完成！')


def save(student_list):
    try:
        file = open(filename, 'a', encoding='utf-8')
    except:
        file = open(filename, 'w', encoding='utf-8')

    for item in student_list:
        file.write(str(item) + '\n')
    file.close()


def search():
    pass


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if not student_id:
            break

        if os.path.exists(filename):
            with open(filename, 'r',  encoding='utf-8') as file:
                student_list = file.readlines()
        else:
            student_list = []

        if student_list:
            flag = False
            with open(filename, 'w', encoding='utf-8') as file:
                for stu in student_list:
                    stu = dict(eval(stu))
                    if stu['id'] != student_id:
                        file.write(str(stu) + '\n')
                    else:
                        flag = True

                if flag:
                    print(f'ID为{student_id}的学生已删除。')
                else:
                    print(f'没有找到ID为{student_id}的学生。')
        else:
            print('没有学生记录！')
            break

        answer = input('是否继续删除 y/n？：')
        if answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            break


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    if os.path.exists(filename):
        print('学号\t姓名\t英语成绩\tpython成绩\tjava成绩')
        with open(filename, 'r', encoding='utf-8') as file:
            for item in file.readlines():
                item = dict(eval(item))
                print(item['id'] + '\t' + item['name'] + '\t' + str(item['english']) + '\t\t' + str(item['python']) + '\t\t\t' + str(item['java']))
    else:
        print('暂无学生信息！')


if __name__ == '__main__':
    main()
