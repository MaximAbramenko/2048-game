#!/usr/bin/env python
# coding: utf-8

import numpy as np
import random as rnd
from math import log2


def set_rand_cell(field):
    rand_сell = rnd.randint(0, field.shape[0]**2 - 1)
    while field[rand_сell // field.shape[0], rand_сell % field.shape[0]] != 0:
        rand_сell = rnd.randint(0, field.shape[0]**2 - 1)
    field[rand_сell // field.shape[0], rand_сell % field.shape[0]] = 2


def shift_left(field):
    global mov_fl
    mov_fl = 0
    for i in range(field.shape[0]):

        for j in range(field.shape[0]):
            if field[i, j] != 0:
                j_c = j
                while j_c != 0 and field[i,j_c-1] == 0:
                    field[i,j_c-1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c -= 1
                    mov_fl = 1

        for j in range(field.shape[0] - 1):
            if field[i,j] == field[i,j+1]:
                field[i,j] *= 2
                field[i,j+1] = 0

        for j in range(field.shape[0]):
            if field[i,j] != 0:
                j_c = j
                while j_c != 0 and field[i,j_c-1] == 0:
                    field[i,j_c-1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c -= 1
                    mov_fl = 1
    return mov_fl

def shift_right(field):
    global mov_fl
    for i in range(field.shape[0]):

        for j in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                j_c = j
                while j_c != field.shape[0] - 1 and field[i,j_c+1] == 0:
                    field[i,j_c+1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c += 1
                    mov_fl = 1

        for j in range(field.shape[0] - 1, -1, -1):
            if field[i,j] == field[i,j - 1]:
                field[i,j] *= 2
                field[i,j-1] = 0


        for j in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                j_c = j
                while j_c != field.shape[0] - 1  and field[i,j_c+1] == 0:
                    field[i,j_c+1] = field[i,j_c]
                    field[i,j_c] = 0
                    j_c += 1
                    mov_fl = 1

    return mov_fl

def shift_up(field):
    global mov_fl
    for j in range(field.shape[0]):

        for i in range(field.shape[0]):
            if field[i, j] != 0:
                i_c = i
                while i_c != 0 and field[i_c - 1,j] == 0:
                    field[i_c-1,j] = field[i_c,j]
                    field[i_c,j] = 0
                    i_c -= 1
                    mov_fl = 1

        for i in range(field.shape[0] - 1):
            if field[i,j] == field[i+1,j]:
                field[i,j] *= 2
                field[i+1,j] = 0

        for i in range(field.shape[0]):
            if field[i, j] != 0:
                i_c = i
                while i_c != 0 and field[i_c - 1, j] == 0:
                    field[i_c - 1, j] = field[i_c, j]
                    field[i_c, j] = 0
                    i_c -= 1
                    mov_fl = 1
    return mov_fl


def shift_down(field):
    global mov_fl
    for j in range(field.shape[0]):
        for i in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                i_c = i
                while i_c != field.shape[0] - 1  and field[i_c+1,j] == 0:
                    field[i_c+1,j] = field[i_c,j]
                    field[i_c,j] = 0
                    i_c += 1
                    mov_fl = 1

        for i in range(field.shape[0] - 1, -1, -1):
            if field[i,j] == field[i-1, j]:
                field[i,j] *= 2
                field[i-1,j] = 0


        for i in range(field.shape[0]-2,-1,-1):
            if field[i,j] != 0:
                i_c = i
                while i_c != field.shape[0] - 1  and field[i_c+1,j] == 0:
                    field[i_c+1,j] = field[i_c,j]
                    field[i_c,j] = 0
                    i_c += 1
                    mov_fl = 1

    return mov_fl

def check_free(field):
    cnt = 0
    for j in range(field.shape[0]):
        for i in range(field.shape[1]):
            if field[i, j] > 0:
                cnt += 1
    if cnt == field.shape[0] ** 2:
        return (False, 0)
    return True,field.shape[0] ** 2 - cnt


def check_if_lose(field):
    cur_field = np.copy(field)
    shift_down(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    shift_right(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    shift_left(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    shift_up(cur_field)
    if check_free(cur_field)[0] == True:
        return False
    return True



def ai_gamer(field):
    global mov_fl
    tmp_field = np.copy(field)
    shift_up(tmp_field)
    if mov_fl == 1:
        up_profit = check_free(tmp_field)[1]
    else:
        up_profit = -1
    mov_fl = 0
    
    tmp_field = np.copy(field)
    shift_left(tmp_field)
    if mov_fl == 1:
        left_profit = check_free(tmp_field)[1]
    else:
        left_profit = -1
    mov_fl = 0

    tmp_field = np.copy(field)
    shift_right(tmp_field)
    if mov_fl == 1:
        right_profit = check_free(tmp_field)[1]
    else:
        right_profit = -1
    mov_fl = 0

    tmp_field = np.copy(field)
    shift_down(tmp_field)
    if mov_fl == 1:
        down_profit = check_free(tmp_field)[1]
    else:
        down_profit = -1
    mov_fl = 0
    
    prof_list = [up_profit,left_profit,right_profit,down_profit]
    m_ind = prof_list.index(max(prof_list))
    kekule = 0 
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if (field[i,j] == 0):
                kekule += 1
    if (kekule == 1):
        shift_right(field)
        shift_up(field)
        shift_up(field)
    if m_ind == 0:
        shift_up(field)
    if m_ind == 1:
        shift_left(field)
    if m_ind == 2:
        shift_right(field)
    if m_ind == 3:
        shift_down(field)
mov_fl = 0


def scorei(field):
    sc = 0
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i, j] != 0:
                sc += field[i, j] * (log2(field[i, j])-1)
    return sc

def game():
    global mov_fl
    print('Enter field size')
    size = int(input())
    g_field = np.zeros((size, size))
    set_rand_cell(g_field)
    set_rand_cell(g_field)
    print(g_field)
    while True:
        ai_gamer(g_field)
        print(scorei(g_field))
        if mov_fl == 1:
            set_rand_cell(g_field)
        if check_free(g_field)[0] == False:
            if check_if_lose(g_field) == True:
                print('LOSE')
                print(scorei(g_field))
                print(g_field)
                break
        mov_fl = 0
        print(g_field)

game()

